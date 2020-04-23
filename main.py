"""
This is a detailed example using almost every command of the API
"""

import time
import random
import telebot
from telebot import types

TOKEN = "1085187414:AAGoY-iUZ43A1Ya8b4ortxbS2a_utuOZYz8"
MY_ID = 374545615
knownUsers = []     # todo: save these in a file,
userStep = {}       # so they won't reset every time the bot restarts

commands = {  # command description used in the "help" command
    'help'          : 'Gives you information about the available commands',
    'history'       : 'Shows all messages',
    'reset_history' : 'Delete all history messages',
    'my_id'         : 'return your id',
    'random_sentence': 'return random sentence'
}

# imageSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)  # create the image selection keyboard
# imageSelect.add('Mickey', 'Minnie')
# hideBoard = types.ReplyKeyboardRemove()  # if sent as reply_markup, will hide the keyboard


# only used for console output now
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text' and m.text[0] != '/':
            file_history = open("history" + str(m.chat.id) + ".txt", "a")
            file_history.write(m.from_user.first_name + "[" + str(m.from_user.id) + "] : " + m.text + "\n")
            file_history.close()
        elif m.content_type == 'sticker':
            bot.send_message(m.chat.id, m.sticker.file_id)
            file_history = open("history" + str(m.chat.id) + ".txt", "a")
            file_history.write(m.from_user.first_name + "[" + str(m.from_user.id) + "] : " + m.sticker.file_id + "\n")
            file_history.close()


bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)  # register listener

"""
# handle the "/start" command
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers:  # if user hasn't used the "/start" command yet:
        knownUsers.append(cid)  # save user id, so you could brodcast messages to all users of this bot later
        userStep[cid] = 0  # save user id and his current "command level", so he can use the "/getImage" command
        bot.send_message(cid, "Hello, stranger, let me scan you...")
        bot.send_message(cid, "Scanning complete, I know you now")
        command_help(m)  # show the new user the help page
    else:
        bot.send_message(cid, "I already know you, no need for me to scan you again!")

"""
# help page
@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "The following commands are available: \n"
    for key in commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  # send the generated help page


@bot.message_handler(commands=['random_sentence'])
def random_sentence(m):
    bot.send_message(m.chat.id, generate("history" + str(m.chat.id) + ".txt"))


"""

# chat_action example (not a good one...)
@bot.message_handler(commands=['sendLongText'])
def command_long_text(m):
    cid = m.chat.id
    bot.send_message(cid, "If you think so...")
    bot.send_chat_action(cid, 'typing')  # show the bot "typing" (max. 5 secs)
    time.sleep(3)
    bot.send_message(cid, ".")


# user can chose an image (multi-stage command example)
@bot.message_handler(commands=['getImage'])
def command_image(m):
    cid = m.chat.id
    bot.send_message(cid, "Please choose your image now", reply_markup=imageSelect)  # show the keyboard
    userStep[cid] = 1  # set the user to the next step (expecting a reply in the listener now)


# if the user has issued the "/getImage" command, process the answer
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 1)
def msg_image_select(m):
    cid = m.chat.id
    text = m.text

    # for some reason the 'upload_photo' status isn't quite working (doesn't show at all)
    bot.send_chat_action(cid, 'typing')

    if text == 'Mickey':  # send the appropriate image based on the reply to the "/getImage" command
        bot.send_photo(cid, open('rooster.jpg', 'rb'),
                       reply_markup=hideBoard)  # send file and hide keyboard, after image is sent
        userStep[cid] = 0  # reset the users step back to 0
    elif text == 'Minnie':
        bot.send_photo(cid, open('kitten.jpg', 'rb'), reply_markup=hideBoard)
        userStep[cid] = 0
    else:
        bot.send_message(cid, "Please, use the predefined keyboard!")
        bot.send_message(cid, "Please try again")


# filter on a specific message
@bot.message_handler(func=lambda message: message.text == "hi")
def command_text_hi(m):
    bot.send_message(m.chat.id, "I love you too!")


# default handler for every other text
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    # this is the standard reply to a normal message
    bot.send_message(m.chat.id, "I don't understand \"" + m.text + "\"\nMaybe try the help page at /help")
"""
@bot.message_handler(commands=['history'])
def command_history(m):
    file = open("history" + str(m.chat.id) + ".txt", "r")
    lines = file.readlines()
    stri = "History:\n"
    for x in lines:
        stri += x
    bot.send_message(m.chat.id, stri)
    file.close()

@bot.message_handler(commands=['reset_history'])
def reset_history(m):
    if m.from_user.id == MY_ID:
        file = open("history" + str(m.chat.id) + ".txt", "r")
        to_f = open("backup" + str(m.chat.id) + ".txt", "w")
        lines = file.readlines()
        for x in lines:
            to_f.write(x)
        file.close()
        to_f.close()
        file = open("history" + str(m.chat.id) + ".txt", "w")
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

"""
@bot.message_handler(content_types=['text'])
def save_to_history(m):
    bot.send_message(m.chat.id, "Suka")
    history_file = open("history.txt", "a")
    history_file.write(m.from_user.first_name + "[" + str(m.from_user.id) + "] : " + m.text + "\n")
    history_file.close()
"""
BEGIN = "BEGIN"
END = "END"
LENGTH = 100

def generate(filename):
    file = open(filename, "r")
    strings = file.readlines()
    strs = set()
    for x in strings:
        strs.add(x.split(" : ", 2)[1].replace("\n", ""))
    strings = list()
    for x in strs:
        strings.append(x.split(" "))
    dictionary = {BEGIN: set(), END: set()}
    for i in range(len(strings)):
        x = strings[i]
        for j in range(len(x)):
            dictionary[x[j]] = set()

    for x in strings:
        dictionary[BEGIN].add(x[0])

    for x in strings:
        if len(x) > 1:
            for i in range(len(x) - 1):
                dictionary[x[i]] = set()
                dictionary[x[i]].add(x[i + 1])
        dictionary[x[len(x) - 1]].add(END)
    generated = ""
    while len(generated.split(" ")) < LENGTH:
        generated += find(dictionary)
    return generated


def find(dictionary, generated=""):
    words = list(dictionary.get(BEGIN))
    while True:
        word = random.choice(words)
        i = 0
        while len(list(dictionary.get(word))) < 5 and i < 100:
            i += 1
            word = random.choice(words)
        if word == END:
            break
        generated += word + " "
        i = 0
        words = list(dictionary.get(word))
    return generated


bot.polling()
