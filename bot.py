from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem


logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s',
 	                 level = logging.INFO,
 	                 filename = "bot.log")


def greet_user(bot, update):
	text = "Вызван /start"
	logging.info(text)
	update.message.reply_text(text)


def talk_to_me(bot, update):
	user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
	logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
		         update.message.chat.id, update.message.text)
	update.message.reply_text(user_text)


def horoscope(bot, update):
	user_planet = update.message.text.split()
	if user_planet[1] == 'Mars':
		planet = ephem.Mars('2019/03/02')
		update.message.reply_text(ephem.constellation(planet))
	elif user_planet[1] == 'Pluto':
		planet = ephem.Pluto('2019/03/02')
		update.message.reply_text(ephem.constellation(planet))
	elif user_planet[1] == 'Saturn':
		planet = ephem.Saturn('2019/03/02')
		update.message.reply_text(ephem.constellation(planet))
	elif user_planet[1] == 'Venus':
		planet = ephem.Venus('2019/03/02')
		update.message.reply_text(ephem.constellation(planet))
	elif user_planet[1] == 'Jupiter':
		planet = ephem.Jupiter('2019/03/02')
		update.message.reply_text(ephem.constellation(planet))
	elif user_planet[1] == 'Neptun':
		planet = ephem.Neptun('2019/03/02')
		update.message.reply_text(ephem.constellation(planet))
	elif user_planet[1] == 'Mercury':
		planet = ephem.Mercury('2019/03/02')
		update.message.reply_text(ephem.constellation(planet))
	elif user_planet[1] == 'Uranus':
		planet = ephem.Uranus('2019/03/02')
		update.message.reply_text(ephem.constellation(planet))


def main():
	mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY)

	logging.info("Бот запускается")

	dp = mybot.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))
	dp.add_handler(CommandHandler("planet", horoscope))

	mybot.start_polling()
	mybot.idle()

main()
