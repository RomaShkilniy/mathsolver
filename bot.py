import telebot
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, f'Welcome {message.chat.first_name} 😘')
	bot.send_message(message.chat.id, 'Enter two numbers separated by commas' )

@bot.message_handler(commands=['help'])
def helper(message):
	bot.send_message(message.chat.id, 'Help message')


@bot.message_handler(content_types=['text'])
def send(message):
	try:
		m = message.text.split(',')
		result = float(m[0]) ** float(m[1])
	except ValueError:
		result = 'Enter a number, not a letter'
	except:
		result = 'Something went wrong...'

	bot.reply_to(message, int(result) if result==int(result) else result)


if __name__ == '__main__':
	bot.polling(none_stop = True, interval = 0)