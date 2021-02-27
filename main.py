# coding=utf-8
import collections
import datetime
import logging
import random
import re
import sys
import time
import db
from generate import generate

from scheduler import scheduler
from gtts import gTTS
from constants import SMALL, MEDIUM, LARGE, HISTORY, commands, andrew_stickers
import telebot

# add your file info.py with TOKEN and MY_ID variables or simply change it in bot initialization V
from info import TOKEN, MY_ID
bot = telebot.AsyncTeleBot(TOKEN)


def print_msg(msg, date, from_id):
    bot.send_message(from_id, msg)
    db.delete_remind(date, msg, from_id)


def print_dict(dictionary):
    for x in dictionary:
        print(x, dictionary[x])


def listener(messages):
    if isinstance(messages, collections.Iterable):
        for m in messages:
            if m.content_type == 'text' and "бот скажи" in m.text.lower():
                bot_say(m)
            elif m.content_type == 'text' and "/tts" in m.text.lower():
                text_to_speech(m)
            elif m.content_type == 'text' and 'напомни' in m.text.lower():
                remember(m)
            elif m.content_type == 'text' and (m.text.lower() == 'бот кинь кубик' or m.text.lower() == 'кинь кубик'):
                bot.send_dice(m.chat.id)
            elif m.content_type == 'text' and (m.text.lower() == 'бутерброд' or '🥪' in m.text.lower()):
                bot.send_sticker(m.chat.id,
                                 "CAACAgIAAx0CT5KqDQACKfZey-lqcAABF5W6DVtvX6jzk_FVD8wAAh0EAAJa44oXaJW1lB4mzXcZBA")
                bot.register_next_step_handler(m, buterbrod)
            elif m.content_type == 'text' and " или " in m.text.lower() and m.text.lower().startswith("бот"):
                choice(m)
            elif m.content_type == 'text' and (
                    "бот насколько " in m.text.lower() or "насколько" in m.text.lower() or "на сколько" in m.text.lower()):
                probability(m)
            elif m.content_type == 'text' and m.text[0] != '/':
                db.save_message(m)
            elif m.content_type == 'sticker':
                bot.send_message(MY_ID, m.sticker.file_id)
                file_history = open(HISTORY + str(m.chat.id) + ".txt", "a")
                file_history.close()
    elif messages.text == '🥪':
        probability(messages)


# help page
@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    logger.debug(f"'/help' from {cid}")
    help_text = "The following commands are available: \n"
    for key in commands:
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)


def remember(m):
    spl = m.text.split(' ')
    if len(spl) < 2:
        return
    if spl[0] != 'напомни':
        return
    if spl[1] == 'через' and spl[2] not in ('час', 'минуту', 'секунду', 'неделю', 'год'):
        return
    if spl[1] == 'завтра' or spl[1] == 'сегодня':
        dt = datetime.datetime.now().date()
        if spl[1] == 'завтра':
            dt = datetime.timedelta(days=1) + dt
        dt = datetime.timedelta(days=1) + dt
        # spl[2] = 'в'
        tm = datetime.datetime.strptime(spl[3], "%H:%M:%S").time()  # todo: пока с секундами
        date = datetime.datetime.combine(dt, tm)
        what = " ".join(spl[4:])
    elif spl[1] == 'через':
        if spl[2] == 'неделю':
            date = datetime.timedelta(weeks=1) + datetime.datetime.now()
        elif spl[2] == 'час':
            date = datetime.timedelta(hours=1) + datetime.datetime.now()
        elif spl[2] == 'минуту':
            date = datetime.timedelta(minutes=1) + datetime.datetime.now()
        elif spl[2] == 'секунду':
            date = datetime.timedelta(seconds=1) + datetime.datetime.now()
        elif spl[2] == 'год':
            date = datetime.timedelta(days=365) + datetime.datetime.now()  # todo: Придумать нормальный год
        what = " ".join(spl[3:])
    elif re.match(
            r'^([1-2][0-9]|[1-9]|(0[1-9])|[1-9])-(0[1-9]|1[0-2]|[1-9])-(\d{4}) ([0-1][0-9]|[1-9]|2[0-3])(:([0-5]\d)){2}$',
            spl[1] + ' ' + spl[2]):
        date = datetime.datetime.strptime(spl[1] + ' ' + spl[2], "%d-%m-%Y %H:%M:%S")
        what = " ".join(spl[3:])
    elif re.match(
            r'^([1-2][0-9]|[1-9]|(0[1-9])|[1-9])-(0[1-9]|[1-9]|1[0-2])-(\d{4}) ([0-1][1-9]|[1-9]|2[0-3]):([0-5]\d)$',
            spl[1] + ' ' + spl[2]):
        date = datetime.datetime.strptime(spl[1] + ' ' + spl[2], "%d-%m-%Y %H:%M")
        what = " ".join(spl[3:])
    else:
        return
    logger.debug(f'remember {date} -- {what}')
    db.save_remind(date, what, m.chat.id)
    bot.send_message()
    scheduler.add_job(print_msg, 'date', run_date=date, args=(f'Напоминаю: {what}', date, m.chat.id, ))


def text_to_speech(m):
    strs = m.text.split(" ", 1)
    if len(strs) < 2:
        return
    tts = gTTS(strs[1], lang='ru')
    tts.save('audio_files/audio.ogg')
    audio = open('audio_files/audio.ogg', 'rb')
    bot.send_voice(m.chat.id, audio)


def bot_say(m):
    strs = m.text.split("бот скажи", 1)
    if len(strs) < 2:
        return
    tts = gTTS(strs[1], lang='ru')
    tts.save('audio_files/audio.ogg')
    audio = open('audio_files/audio.ogg', 'rb')
    bot.send_voice(m.chat.id, audio)


@bot.message_handler(commands=['send_history'])
def command_help(m):
    rows = db.get_history(m.chat.id)
    temp = open("history.txt", 'w+')
    for row in rows:
        temp.write(f"{row[0]}[{row[1]}]: {row[2]}\n")
    temp = open('temp.txt', 'rb')
    bot.send_document(m.chat.id, temp)


@bot.message_handler(commands=['send_dictionary'])
def command_help(m):
    f = open("dictionary.txt", 'rb')
    bot.send_document(m.chat.id, f)
    f.close()


def buterbrod(m):
    bot.send_sticker(m.chat.id, "CAACAgIAAx0CT5KqDQACKfdey-ls5ffNFol-9PjTjr9qCEc_0QACFgQAAlrjihftOsVOK2ZRqRkE")
    bot.register_next_step_handler(m, listener)


def choice(m):
    strs = m.text.lower().split("бот ")
    strs = strs[1].split(" или ")
    for x in strs:
        if " я " in x:
            x = x.replace(" я ", " ты ")
        elif x.startswith("я"):
            x = x.replace("я", "ты", 1)
        elif " ты " in x:
            x = x.replace(" ты ", " я ")
        elif x.startswith("ты"):
            x = x.replace("ты", "я", 1)
    bot.send_message(m.chat.id, "Определённо " + random.choice(strs))


def probability(m):
    if "насколько" in m.text.lower():
        strs = m.text.lower().split("насколько", 2)
    elif "на сколько" in m.text.lower():
        strs = m.text.lower().split("на сколько", 2)
    if len(strs) > 1:
        prob = random.randint(0, 101)
        if " я " in strs[1]:
            strs[1] = strs[1].replace(" я ", " ты ")
        elif " ты " in strs[1]:
            strs[1] = strs[1].replace(" ты ", " я ")
        bot.send_message(m.chat.id, "Я думаю, что" + strs[1] + " на " + str(prob) + "%")


@bot.message_handler(commands=['say_random'])
def random_sentence(m):
    text = generate(db.get_history(m.chat.id), SMALL)
    tts = gTTS(text, lang='ru')
    tts.save('audio_files/random.ogg')
    audio = open('audio_files/random.ogg', 'rb')
    bot.send_voice(m.chat.id, audio)


@bot.message_handler(commands=['say_random_large'])
def random_sentence(m):
    text = generate(db.get_history(m.chat.id), LARGE)
    tts = gTTS(text, lang='ru')
    tts.save('audio_files/random_large.ogg')
    audio = open('audio_files/random_large.ogg', 'rb')
    bot.send_voice(m.chat.id, audio)


@bot.message_handler(commands=['random_sentence'])
def random_sentence(m):
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(m.chat.id, generate(db.get_history(m.chat.id), random.randint(SMALL, LARGE)))


@bot.message_handler(commands=['large_random_sentence'])
def large_random_sentence(m):
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(m.chat.id, generate(db.get_history(m.chat.id), LARGE))


@bot.message_handler(commands=['medium_random_sentence'])
def medium_random_sentence(m):
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(m.chat.id, generate(db.get_history(m.chat.id), MEDIUM))


@bot.message_handler(commands=['small_random_sentence'])
def small_random_sentence(m):
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(m.chat.id, generate(db.get_history(m.chat.id), SMALL))


@bot.message_handler(commands=['history'])
def command_history(m):
    bot.send_chat_action(m.chat.id, 'typing')
    stri = "History: (last 10 messages)\n"
    rows = db.get_history(m.chat.id)
    rows.reverse()
    count = 0
    for row in rows:
        if count >= 10:
            break
        stri += f'{row[0]}[{row[1]}]: {row[2]}\n'
        count += 1
    bot.send_message(m.chat.id, stri)


@bot.message_handler(commands=['reset_history'])
def reset_history(m):
    if m.chat.id != m.from_user.id and m.from_user.id == MY_ID:
        file = open("history" + str(m.chat.id) + ".txt", "r")
        to_f = open("backup" + str(m.chat.id) + ".txt", "w")
        lines = file.readlines()
        for x in lines:
            to_f.write(x)
        file.close()
        to_f.close()
        file = open(HISTORY + str(m.chat.id) + ".txt", "w")
        file.close()
        bot.send_chat_action(m.chat.id, 'typing')
        bot.reply_to(m, "Done.\n 'backup" + str(m.chat.id) + ".txt' was created")
        command_history(m)
    else:
        bot.send_message(MY_ID, m.from_user.first_name + " wanted to delete history!")
        bot.reply_to(m, "You don't have permissions for this command")


@bot.message_handler(commands=['my_id'])
def get_id(m):
    bot.send_message(m.chat.id, m.from_user.id)


@bot.message_handler(func=lambda message: "сука" in message.text.lower())
def sticker12324(m):
    bot.send_chat_action(m.chat.id, 'typing')
    bot.send_sticker(m.chat.id, random.choice(andrew_stickers))


if __name__ == '__main__':
    bot.set_update_listener(listener)  # register listener
    db.init()

    logger = logging.getLogger('Wall•e')
    formatter = logging.Formatter('%(asctime)s (%(filename)s:%(lineno)d %(threadName)s) %(levelname)s - %(name)s: "%(message)s"')
    console_output_handler = logging.StreamHandler(sys.stderr)
    console_output_handler.setFormatter(formatter)
    logger.addHandler(console_output_handler)
    logger.setLevel(logging.ERROR)
    scheduler.add_job(logger.debug, 'interval', seconds=10, args=(' ',))

    rows = db.execute_read_query(f"SELECT (datetime, text, from_id) FROM reminder")
    if rows:
        for row in rows:
            print(f'{row[0]} {row[1]} {row[2]}')
            scheduler.add_job(print_msg, 'date', run_date=row[0], args=(f'Напоминаю: {row[1]}', row[0], row[2], ))

    scheduler.start()
    bot.polling(none_stop=True, timeout=20)
