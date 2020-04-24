import telebot
from telebot import types
bot = telebot.TeleBot('922627039:AAFnSM9eTwr1kZyWD_vGWOFehz_iv6RNTL4')
key = types.InlineKeyboardMarkup()

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('команды', 'random')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Aya yo')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
keyboard3.row('Stop ayaya')
keyboard4 = telebot.types.ReplyKeyboardMarkup(True)
keyboard4.row('Да')
keyboard5 = telebot.types.ReplyKeyboardMarkup(True)
keyboard5.row('stop гэндальф')
keyboard6 = telebot.types.ReplyKeyboardMarkup(True)
keyboard6.row('Да', 'Нет')


@bot.message_handler(commands=['start'])
def start_message(message):
      bot.send_message(message.chat.id, 'Меню:', reply_markup=keyboard1)
@bot.message_handler(content_types=['text'])
@bot.message_handler(content_types=['sticker'])

# для просмотра id стикера
#def send_text5 (message):
#    print (message)
#    bot.send_message(message.chat.id,message);

def send_text (message):
     global t
     global b

     t = 0;
     b = 0;



     if message.text.lower() == 'команды':
        bot.send_message(message.chat.id, "Открыть список команд?", reply_markup=keyboard4);
        bot.register_next_step_handler(message, send_text6);




     if "красный диплом" in message.text.lower():
        bot.send_photo(message.chat.id,'https://mywishcard.com/s/i2/74/8/470x0_TNVi53JE693951PFq8eyMGkp9Zn5pnqn___jpg____4_aae855ea.jpg')


     if message.text.lower() == 'start':
        bot.send_message(message.chat.id, 'Меню:', reply_markup=keyboard1)
     if message.text.lower() == 'райан фото серёжа':
        bot.send_photo(message.chat.id,'https://im0-tub-ru.yandex.net/i?id=c2ad27bd9f4ad8a9c17ff5862dda42df-l&n=13')

     if message.text.lower() == 'pikachu':
        bot.send_message(message.chat.id, 'Pika!')
        bot.send_document(message.chat.id, 'https://zvezdochet.guru/images/pokemon/Pikachu.gif')



     if message.text.lower() == '...':
        bot.send_message(message.chat.id, 'произошла постирония')
        bot.send_photo(message.chat.id,'https://im0-tub-ru.yandex.net/i?id=509de419419eb3797b638f7b9f13dae1-l&n=13')



     #if message.text.lower() == 'команды':
      # bot.send_message(message.chat.id, 'Перед каждой командой пиши мое имя. Исключение: секундомер, потому что я не секундомер.\n -Привет \n -пока \n -а \n -кто такой андрей? \n -андрей это \n -ааа \n -ну да \n -держу в курсе \n -твой любимый фильм \n -ракета \n -а? \n -гослинг \n -фото андрей \n - фото серёжа  \n -ставь лайк \n -секундомер (для остановки пиши стоп \n ...\n -Yoko ')
     if message.text.lower() == 'райан привет':
        bot.send_message(message.chat.id, 'Привет')
     if message.text.lower() == 'райан пока':
        bot.send_message(message.chat.id, 'Увидимся в бэтманке')
     if message.text.lower() == 'райан а':
        bot.send_message(message.chat.id, 'А? ЧТО? М?')
     if message.text.lower() == 'райан кто такой андрей?':
        bot.send_message(message.chat.id, 'Самый лучший человек')
     if message.text.lower() == 'райан андрей это':
        bot.send_message(message.chat.id, 'солнышко')
     if message.text.lower() == 'райан ааа':
        bot.send_message(message.chat.id, 'ну тогда давай')
     if message.text.lower() == 'райан ну да':
        bot.send_message(message.chat.id, 'Ну да получается')
     if message.text.lower() == '/держу в курсе':
        bot.send_message(message.chat.id, '#держувкурсеплотнее')

     if message.text.lower() == ' твой любимый фильм':
        bot.send_message(message.chat.id, 'лалаленд')

     if 'ракета' in message.text.lower():
        bot.send_message(message.chat.id, '_________$__________\n________$_$________\n_______$___$_______\n______$_____$______\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n___$__$___$__$____\n__$__$_$_$_$__$__\n_$__$__$$$__$__$_\n_$$$____$____$$$_\n_$_______$_______$_\n$________$________$\n')
     if message.text.lower() == 'ракета':
        bot.send_message(message.chat.id, '_________$__________\n________$_$________\n_______$___$_______\n______$_____$______\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n___$__$___$__$____\n__$__$_$_$_$__$__\n_$__$__$$$__$__$_\n_$$$____$____$$$_\n_$_______$_______$_\n$________$________$\n')
     if message.text.lower() == 'лайк':
        bot.send_sticker(message.chat.id, 'CAADAgADJwQAApzW5wr4HQ0g1_0P6RYE');

     if message.text.lower() == 'yoko':
        bot.send_message(message.chat.id, "shinobu ni", reply_markup=keyboard2);
        bot.register_next_step_handler(message, send_text5);
     if message.text.lower() == 'stop ayaya':
        b  = 1;
     if message.text.lower() == 'stop гэндальф':
        t  = 1;
     if message.text.lower() == 'stop гэндальф':
         bot.send_photo(message.chat.id,'http://www.cap-that.com/lotr/fotr/images/LOTR-FOTR_0210.jpg',reply_markup=keyboard1)
     if message.text.lower() == 'stop ayaya':
         bot.send_message(message.chat.id, 'Ну да получается')
         bot.send_photo(message.chat.id,'https://cdn.discordapp.com/icons/645265594219757568/a_f8b99909ac505b5ca915bb4c78427d09.jpg?size=256',reply_markup=keyboard1)

     if message.text.lower() == 'матрица':
         bot.send_message(message.chat.id, '\033[96mТекст будет голубым\033[0m')

#######Рандом######################################################################################

     if (message.text.lower() == 'random' ) or ("random"  in message.text.lower()) or (message.text.lower() == 'рандом' )  or ("рандом"  in message.text.lower()):
         import random
         f = random.randint(1,17)
         if f == 1:
                bot.send_message(message.chat.id,' AYAYA')
         if f == 2:
                bot.send_message(message.chat.id,' В ловушке живем')
         if f == 3:
                bot.send_message(message.chat.id,' Ну да получается')

         if f == 4:

                bot.send_photo(message.chat.id,'https://memepedia.ru/wp-content/uploads/2019/10/lovushka.jpg')

         if f == 5:

                bot.send_photo(message.chat.id,'https://samoeinteresnoe.net/wp-content/uploads/2019/06/1-23.jpg')

         if f == 6:

                bot.send_photo(message.chat.id,'https://pbs.twimg.com/media/EDtjBCmWsAADNAx.jpg:large')

         if f == 7:

                            bot.send_photo(message.chat.id,'https://boards.420chan.org/w/src/1492208139254.jpg')


         if f == 8:

                            bot.send_photo(message.chat.id,'https://i.gifer.com/22Tp.gif')

         if f == 9:

                            bot.send_photo(message.chat.id,'https://yt3.ggpht.com/a/AGF-l7-M3Ib62aHylMXHtFX4kEotf4tLtVa-ShybUg=s900-c-k-c0xffffffff-no-rj-mo')

         if f == 10:

                            bot.send_photo(message.chat.id,'https://yt3.ggpht.com/a/AGF-l7-M3Ib62aHylMXHtFX4kEotf4tLtVa-ShybUg=s900-c-k-c0xffffffff-no-rj-mo')

         if f == 11:

                            bot.send_photo(message.chat.id,'https://media2.s-nbcnews.com/i/newscms/2016_50/1181140/ryan-reynolds-ryan-gosling-tease-today-161212_69556971c630cd803eff366623006eaa.jpg')

         if f == 12:

                            bot.send_photo(message.chat.id,'http://uzhgorod.in/var/plain_site/storage/images/media/images/novosti/2017/17264940_10206004728515539_8823208410894587362_n/2381204-1-rus-RU/17264940_10206004728515539_8823208410894587362_n_reference.jpg')

         if f == 13:

                            bot.send_photo(message.chat.id,'http://uzhgorod.in/var/plain_site/storage/images/media/images/novosti/2017/17264940_10206004728515539_8823208410894587362_n/2381204-1-rus-RU/17264940_10206004728515539_8823208410894587362_n_reference.jpg')

         if f == 14:

                            bot.send_message(message.chat.id,'АААААААААААААААААААААААААААААААААААААА')

         if f == 15:

                            bot.send_message(message.chat.id,'0_0')

         if f == 16:

                            bot.send_photo(message.chat.id,'https://s00.yaplakal.com/pics/pics_original/0/1/9/13144910.jpg')

         if f == 17:

                            bot.send_photo(message.chat.id,'https://im0-tub-ru.yandex.net/i?id=b9c38387e9dd3efe33f877a8f530ac9c&n=13')

################################################################################################################################################################################################################

def send_text5 (message):
      if message.text.lower() == 'aya yo':
          bot.send_message(message.chat.id,' AYAYA',reply_markup=keyboard3)
          while b==0:
             import time;
             bot.send_message(message.chat.id,' AYAYA')
             time.sleep(1)
             if message.text.lower() == 'stop ayaya':
                    bot.send_photo(message.chat.id,'https://i.ytimg.com/vi/5LEUJdxJEJk/maxresdefault.jpg', reply_markup=keyboard1)
             if message.text.lower() == 'stop ayaya':
                    False

      else:
         bot.send_message(message.chat.id, 'I feel disappointed (');
         bot.register_next_step_handler(message, send_text)



def send_text7 (message):
      if message.text.lower() == 'да':
          bot.send_document(message.chat.id, 'https://i.gifer.com/7Q3S.gif', reply_markup=keyboard5)
          while t==0:
             import time;
             bot.send_document(message.chat.id, 'https://i.gifer.com/7Q3S.gif')
             time.sleep(1)
             if message.text.lower() == 'stop гэндальф':
                    bot.send_photo(message.chat.id,'https://i.ytimg.com/vi/5LEUJdxJEJk/maxresdefault.jpg', reply_markup=keyboard1)
             if message.text.lower() == 'stop гэндальф':
                    False

      else:
         bot.send_message(message.chat.id, 'I feel disappointed (', reply_markup=keyboard1);
         bot.register_next_step_handler(message, send_text)










def send_text6 (message):
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Ракета", callback_data="Ракета")
        but_2 = types.InlineKeyboardButton(text="Лайк", callback_data="Лайк")
        but_3 = types.InlineKeyboardButton(text="Yoko", callback_data="Yoko")
        but_4 = types.InlineKeyboardButton(text="pickachu", callback_data="pickachu")
        but_5 = types.InlineKeyboardButton(text="...", callback_data="...")
        but_6 = types.InlineKeyboardButton(text="гэндальф", callback_data="гэндальф")
        but_7 = types.InlineKeyboardButton(text="Не нажимай", callback_data="test")
        key.add(but_1, but_2, but_3, but_4, but_5, but_6, but_7)
        bot.send_message(message.chat.id, "Список команд", reply_markup=key)
        bot.send_message(message.chat.id, "oOOo ?·??·? oOOo", reply_markup=keyboard1)

@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
     if c.data == 'Ракета':
        bot.send_message(c.message.chat.id, '_________$__________\n________$_$________\n_______$___$_______\n______$_____$______\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n_____$_______$_____\n___$__$___$__$____\n__$__$_$_$_$__$__\n_$__$__$$$__$__$_\n_$$$____$____$$$_\n_$_______$_______$_\n$________$________$\n', reply_markup=keyboard1)
     if c.data == 'Лайк':
        bot.send_sticker(c.message.chat.id, 'CAADAgADJwQAApzW5wr4HQ0g1_0P6RYE', reply_markup=keyboard1)
     if c.data == 'Yoko':
        bot.send_message(c.message.chat.id, "shinobu ni", reply_markup=keyboard2);
        bot.register_next_step_handler(c.message, send_text5);
     if c.data == 'pickachu':
        bot.send_message(c.message.chat.id, 'Pika!')
        bot.send_document(c.message.chat.id, 'https://zvezdochet.guru/images/pokemon/Pikachu.gif', reply_markup=keyboard1)
     if c.data == '...':
        bot.send_message(c.message.chat.id, 'произошла постирония')
        bot.send_photo(c.message.chat.id,'https://im0-tub-ru.yandex.net/i?id=509de419419eb3797b638f7b9f13dae1-l&n=13', reply_markup=keyboard1)
     if c.data == 'гэндальф':
        bot.send_message(c.message.chat.id, "время кивать? ??", reply_markup=keyboard6);
        bot.register_next_step_handler(c.message, send_text7);
     if c.data == "test":
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text="????????????")
        bot.answer_callback_query(callback_query_id=c.id, show_alert=False, text="Я же просил тебя не жать ??")










def send_text8 (message):
     import random
     f = random.randint(1,17)
     if f == 1:
            bot.send_message(message.chat.id,' AYAYA')
     if f == 2:
            bot.send_message(message.chat.id,' В ловушке живем')
     if f == 3:
            bot.send_message(message.chat.id,' Ну да получается')

     if f == 4:

            bot.send_photo(message.chat.id,'https://memepedia.ru/wp-content/uploads/2019/10/lovushka.jpg')

     if f == 5:

            bot.send_photo(message.chat.id,'https://samoeinteresnoe.net/wp-content/uploads/2019/06/1-23.jpg')

     if f == 6:

            bot.send_photo(message.chat.id,'https://pbs.twimg.com/media/EDtjBCmWsAADNAx.jpg:large')

     if f == 7:

                        bot.send_photo(message.chat.id,'https://boards.420chan.org/w/src/1492208139254.jpg')


     if f == 8:

                        bot.send_photo(message.chat.id,'https://i.gifer.com/22Tp.gif')

     if f == 9:

                        bot.send_photo(message.chat.id,'https://yt3.ggpht.com/a/AGF-l7-M3Ib62aHylMXHtFX4kEotf4tLtVa-ShybUg=s900-c-k-c0xffffffff-no-rj-mo')

     if f == 10:

                        bot.send_photo(message.chat.id,'https://yt3.ggpht.com/a/AGF-l7-M3Ib62aHylMXHtFX4kEotf4tLtVa-ShybUg=s900-c-k-c0xffffffff-no-rj-mo')

     if f == 11:

                        bot.send_photo(message.chat.id,'https://media2.s-nbcnews.com/i/newscms/2016_50/1181140/ryan-reynolds-ryan-gosling-tease-today-161212_69556971c630cd803eff366623006eaa.jpg')

     if f == 12:

                        bot.send_photo(message.chat.id,'http://uzhgorod.in/var/plain_site/storage/images/media/images/novosti/2017/17264940_10206004728515539_8823208410894587362_n/2381204-1-rus-RU/17264940_10206004728515539_8823208410894587362_n_reference.jpg')

     if f == 13:

                        bot.send_photo(message.chat.id,'http://uzhgorod.in/var/plain_site/storage/images/media/images/novosti/2017/17264940_10206004728515539_8823208410894587362_n/2381204-1-rus-RU/17264940_10206004728515539_8823208410894587362_n_reference.jpg')

     if f == 14:

                        bot.send_message(message.chat.id,'АААААААААААААААААААААААААААААААААААААА')

     if f == 15:

                        bot.send_message(message.chat.id,'0_0')

     if f == 16:

                        bot.send_photo(message.chat.id,'https://s00.yaplakal.com/pics/pics_original/0/1/9/13144910.jpg')

     if f == 17:

                        bot.send_photo(message.chat.id,'https://im0-tub-ru.yandex.net/i?id=b9c38387e9dd3efe33f877a8f530ac9c&n=13')







bot.polling(none_stop=True, interval=0)
