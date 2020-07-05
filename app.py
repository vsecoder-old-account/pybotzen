import telebot, random
bot = telebot.TeleBot('1227702845:AAEZJMDHRxmuKSurVrT5nwCFM7rdbZ7nZCU')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        phrases = [
            'Нужна помощь? У меня её нет =)',
            'Сожалею, но не помогу...',
            'Хахахахахахахаха... Зачем тебе моя помощь?'
        ]
        bot.send_message(message.from_user.id, phrases[random.randint(0, len(phrases)-1)])
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, я повторяю всё за тобой, \nменя написал Всеволод html!")
        histi = open('assets/hi.tgs', 'rb')
        bot.send_sticker(message.chat.id, histi)
    elif message.text == "/settings":
        bot.send_message(message.from_user.id, "Меня нельзя настроить ☺")
    elif message.text == "html":
        bot.send_message(message.from_user.id, "Подпишись на мой кнала!\nhttps://zen.yandex.ru/id/5e7c78ee99d560276a9df6e4")
    else:
        bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True, interval=0)