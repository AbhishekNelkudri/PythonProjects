import telebot

Token = "6301299456:AAG9lz-PmUo-BDuqhYhZAtIFFwSMUUJpToc"

bot = telebot.TeleBot(Token)


@bot.message_handler(["start"])
def start(message):
  bot.reply_to(message, "hello welcome to calculator bot")


@bot.message_handler(["help"])
def help(message):
  bot.reply_to(
      message, """ /start->greeting
                 /help->will help you for the command/
                 /creator->wil display the creator name/
                 /hi->welcome message
                 /joke->displays a joke
                 if you want to use this as a calculator feel free """)


@bot.message_handler(['hi'])
def hi(message):
  bot.reply_to(message, "welcome to the calculator bot")


@bot.message_handler(['joke'])
def joke(message):
  bot.reply_to(message,
               "we always live in a hallucinaton that we live forever")


@bot.message_handler(['creator'])
def creator(message):
  bot.reply_to(message, 'this bot was created by AbhishekAishwarya')




@bot.message_handler()
def custom(message):
  try:
    msg = eval(message.text.strip())
  except Exception as e:
    msg = "this cannot be evaluated"
  bot.reply_to(message, msg)


bot.polling()
