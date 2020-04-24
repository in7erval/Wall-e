"""
This is a detailed example using almost every command of the API
"""

import time
import random
import telebot
from telebot import types
from collections import deque

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


def print_dict(dictionary):
	for x in dictionary:
		print(x, dictionary[x])


def print_dict_file(dictionary):
	f = open("dictionary.txt", "w")
	for x in dictionary:
		f.write(x + " " + str(dictionary[x]) + "\n")
	f.close()

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
	bot.send_chat_action(m.chat.id, 'typing')
	time.sleep(1)
	bot.send_message(m.chat.id, generate("history" + str(m.chat.id) + ".txt"))


# bot.send_chat_action(cid, 'typing')  # show the bot "typing" (max. 5 secs)


@bot.message_handler(commands=['history'])
def command_history(m):
	bot.send_chat_action(m.chat.id, 'typing')
	stri = "History: (last 10 messages)\n"
	with open("history" + str(m.chat.id) + ".txt") as f:
		for row in deque(f, 10):
			stri += row
	bot.send_message(m.chat.id, stri)

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



@bot.message_handler(func=lambda message: message.text == "ну ты и сука")
def sticker12324(m):
	bot.send_chat_action(m.chat.id, 'typing')
	bot.send_sticker(m.chat.id, "CAACAgIAAx0CT5KqDQACJBReoopG6ZHc2eYbeX5Pu69-FJLQxwACAQADzxxTFmQqAAFeFSDeVhkE")


BEGIN = "BEGIN"
END = "END"
LENGTH = 50

def generate(filename):
	file = open(filename, "r")
	strings = file.readlines()
	strs = set()
	for x in strings:
		pr = x.split(" : ", 2)
		if len(pr) > 1:
			strs.add(pr[1].replace("\n", " ").lower())
	strings = list()
	for x in strs:
		strings.append(x.replace(",", " ").replace("?", " ").replace("!", " ").replace(".", " ").split())
	dictionary = {BEGIN: set(), END: set()}
	for i in range(len(strings)):
		x = strings[i]
		for j in range(len(x)):
			if x[j] not in dictionary.keys(): 
				dictionary[x[j]] = set()
	for x in strings:
		dictionary[BEGIN].add(x[0])
	for x in strings:
		if len(x) > 1:
			for i in range(len(x) - 1):
				if x[i] not in dictionary.keys():
					dictionary[x[i]] = set()
				dictionary[x[i]].add(x[i + 1])
		dictionary[x[len(x) - 1]].add(END)
	generated = ""
	print_dict_file(dictionary)
	while len(generated.split(" ")) < LENGTH:
		generated += find(dictionary).strip().capitalize() + ". "
	return generated


def find(dictionary, generated=""):
	words = list(dictionary.get(BEGIN))
	while True:
		word = random.choice(words)
		if word == END:
			break
		generated += (word + " ")
		words = list(dictionary.get(word))
	return generated


bot.polling()
