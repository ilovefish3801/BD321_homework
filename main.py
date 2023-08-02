if __name__ == "__main__":
    import telebot
    from telebot import types
    import requests

    bot = telebot.TeleBot("6342244998:AAEfTjyeKwBQtadMfGfDYchZxSESt0Vs-tI")

    exchange = requests.get("http://data.fixer.io/api/latest?access_key=95a514490ca9c1254b7cabe1caf2bbb2&format=1")
    rates = exchange.json()
    def main_reply_menu():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.row(types.KeyboardButton("Побачити курс валют"))
        return markup


    @bot.message_handler(commands=["start"])
    def isWorking(msg):
        bot.reply_to(msg, "Я включився", reply_markup=main_reply_menu())


    @bot.message_handler(func=lambda message: True)
    def echo_all(msg):
        cid = msg.chat.id
        if msg.text == "Побачити курс валют":
            bot.reply_to(msg, f"1 USD - {round(rates['rates']['UAH'] / rates['rates']['USD']), 2} UAH \n1 EUR - {round(rates['rates']['UAH'] / rates['rates']['EUR']), 2} UAH")


    bot.infinity_polling()
