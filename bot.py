import telebot
from cfg import TOKEN
import model as m
from random import randint

bot = telebot.TeleBot(TOKEN)
candys = 117

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Игра в конфеты. На столе лежит 117 конфет. Можно забрать за раз не более 28 конфет. Победит тот, кто заберет последние конфеты.")
	bot.send_message(message.chat.id, "Первый ходит игрок. Введите число конфет, которое хотите забрать(0-28)")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	global candys
	if int(message.text) > 28 or int(message.text) < 1:
			
		bot.send_message(message.chat.id, "Нельзя забрать столько конфет!!!")
	else:
		candys = m.Subtraction(candys, int(message.text))
		if candys < 1:
			bot.send_message(message.chat.id, "Игра окончена. Победил Игрок")
			candys = 117
			bot.send_message(message.chat.id, "Игра перезапущена. На столе вновь 117 кофет. Ходит Игрок. Введите количество конфет, которое хотите забрать(0-28)")
		else:
			bot.send_message(message.chat.id, f'Вы забрали {message.text} конфет. Осталось {str(candys)} конфет.')
			botnumber = randint(1,28)
			candys = m.Subtraction(candys, botnumber)
			if candys < 1:
				bot.send_message(message.chat.id, "Игра окончена. Победил Бот")
				candys = 117
				bot.send_message(message.chat.id, "Игра перезапущена. На столе вновь 117 кофет. Ходит Игрок. Введите количество конфет, которое хотите забрать(0-28)")
			else:
				bot.send_message(message.chat.id, f'Бот забрал {str(botnumber)} конфет. Осталось {str(candys)} конфет.')
				bot.send_message(message.chat.id, "Введите число конфет, которое хотите забрать(0-28)")
	
bot.infinity_polling()