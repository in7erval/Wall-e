"""
This is a detailed example using almost every command of the API
"""

import time
import random
import telebot
from telebot import types
from collections import deque
import os

TOKEN = "1085187414:AAGoY-iUZ43A1Ya8b4ortxbS2a_utuOZYz8"
MY_ID = 374545615
Z_ID = 919861051
A_ID = 948882144
S_ID = 229916429
SMALL = 5
MEDIUM = 15
LARGE = 40
COMMAND1 = "ls"
COMMAND = "curl -s -X POST https://api.telegram.org/bot" + TOKEN + "/sendMessage -d chat_id=" # $CHAT_ID -d text="$MESSAGE""
knownUsers = []     # todo: save these in a file,
userStep = {}       # so they won't reset every time the bot restarts

commands = {  # command description used in the "help" command
    'help'          : 'Gives you information about the available commands',
    'history'       : 'Shows all messages',
    'reset_history' : 'Delete all history messages',
    'my_id'         : 'return your id',
    'random_sentence': 'return random sentence',
	'large_random_sentence' : 'return random sentence of ' + str(LARGE) + ' words',
	'medium_random_sentence' : 'return random sentence of ' + str(MEDIUM) + ' words',
	'small_random_sentence' : 'return random sentence of ' + str(SMALL) + ' words'
}

andrew_stickers = [ "CAACAgIAAxkBAAIEDl6y6VHHWnQyREHAf6ciCC4g6sfWAAIMAAPPHFMW_xIObRSe8EQZBA",
					"CAACAgIAAxkBAAIEE16y6ieuLn_a1joCCWtf1ve2LWXSAAIBAAPPHFMWZCoAAV4VIN5WGQQ",
					"CAACAgIAAxkBAAIEFV6y6jTkYvMlQUKJR0UFLJj5QrRBAAIGAAPPHFMWD0lbtp6iuh4ZBA",
					"CAACAgIAAxkBAAIEF16y6kS2WQSRkle5LKknEZRMCoHgAAIHAAPPHFMWwDI8NPfq8RsZBA",
					"CAACAgIAAxkBAAIEGV6y6lRC8V4IXFFgDWw4Kai52lo4AAIIAAPPHFMWLY1eRtlHV7AZBA",
					"CAACAgIAAxkBAAIEG16y6m1byu2S_viRgz8uvtl1KFNFAAIJAAPPHFMWkpb7UbBT4fsZBA",
					"CAACAgIAAxkBAAIEHV6y6nbHiYksGG9asOuu2zmiGpOvAAIKAAPPHFMWOevX0ynrgOkZBA",
					"CAACAgIAAxkBAAIEH16y6oFeaJrYPiHcD7MAAbvpGVgSOwACCwADzxxTFifmEP1vWjb0GQQ",
					"CAACAgIAAxkBAAIEI16y6qKQWQ1fa1Ff47AeilLn3rQ_AAINAAPPHFMWmuFldpfiaVMZBA",
					"CAACAgIAAxkBAAIEJV6y6q0JcEGoEgEJ4vceWmuzqF3dAAIOAAPPHFMW_Hws-Aiv2TgZBA",
					"CAACAgIAAxkBAAIEJ16y6rd7qK4xd5WBy_WOdsAREHaNAAIPAAPPHFMWpiPA89HCncYZBA",
					"CAACAgIAAxkBAAIEKV6y6sHanYl7nidGYQ6IR9fKZggEAAIQAAPPHFMWCW9W5uGyrmgZBA",
					"CAACAgIAAxkBAAIEK16y6s0_2JFwagNQznsywHY288VMAAIRAAPPHFMW_qspvjA-hL0ZBA",
					"CAACAgIAAxkBAAIELV6y6tncqtRBIphzxjRhMfCyV93OAAISAAPPHFMWN6eASVHHi0sZBA",
					"CAACAgIAAxkBAAIEL16y6uOW1ulDiF3LsvfdQahyarS6AAITAAPPHFMWlvLmN498LmIZBA"					
				]		

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
            file_history = open("history" + str(m.chat.id) + ".txt", "a+")
            file_history.write(m.from_user.first_name + "[" + str(m.from_user.id) + "] : " + m.text + "\n")
            file_history.close()
        elif m.content_type == 'sticker':
            bot.send_message(MY_ID, m.sticker.file_id)
            file_history = open("history" + str(m.chat.id) + ".txt", "a")
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
	bot.send_message(m.chat.id, generate("history" + str(m.chat.id) + ".txt", random.randint(SMALL, LARGE)))


@bot.message_handler(commands=['large_random_sentence'])
def large_random_sentence(m):
	bot.send_chat_action(m.chat.id, 'typing')
	time.sleep(1)
	bot.send_message(m.chat.id, generate("history" + str(m.chat.id) + ".txt", LARGE))


@bot.message_handler(commands=['medium_random_sentence'])
def medium_random_sentence(m):
	bot.send_chat_action(m.chat.id, 'typing')
	time.sleep(1)
	bot.send_message(m.chat.id, generate("history" + str(m.chat.id) + ".txt", MEDIUM))


@bot.message_handler(commands=['small_random_sentence'])
def small_random_sentence(m):
	bot.send_chat_action(m.chat.id, 'typing')
	time.sleep(1)
	bot.send_message(m.chat.id, generate("history" + str(m.chat.id) + ".txt", SMALL))


@bot.message_handler(commands=['everybody'])
def	everybody(m):
	s = "idi nahui i zaidi v konfu plis"
	bot.send_message(m.chat.id, "@soooslooow @suslik13 go to nahui")
	bot.send_message(MY_ID, "Dimochka " + s)
	# bot.send_message(Z_ID, "Zenechka " + s)
	# bot.send_message(A_ID, "Andryusha " + s)
	# bot.send_message(S_ID, "Serezhecha " + s)
	os.system(COMMAND + str(A_ID) + ' -d text="Andryusha ' + s + '"')



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
    if m.chat.id != m.from_user.id and m.from_user.id == MY_ID:
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


@bot.message_handler(func=lambda message: "сука" in message.text.lower())
def sticker12324(m):
	bot.send_chat_action(m.chat.id, 'typing')
	bot.send_sticker(m.chat.id, random.choice(andrew_stickers))



BEGIN = "BEGIN"
END = "END"
LENGTH = 50

def generate(filename, length):
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
		if len(x) > 0:
			dictionary[BEGIN].add(x[0])
	for x in strings:
		if len(x) > 1:
			for i in range(len(x) - 1):
				if x[i] not in dictionary.keys():
					dictionary[x[i]] = set()
				dictionary[x[i]].add(x[i + 1])
		if len(x) > 0:
			dictionary[x[len(x) - 1]].add(END)
	generated = ""
	print_dict_file(dictionary)
	count = 0
	while len(generated.split(" ")) < length and count < 1000000:
		generated = find(dictionary).strip().capitalize()
		count += 1
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
