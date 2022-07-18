import telebot
import parser_yandex
from prettytable import PrettyTable
TOKEN = "5435944408:AAHDWsDqQN9hUZRuS5kRXgVwF87Io0h7IH0"
bot = telebot.TeleBot(TOKEN)



def telegram_bot(TOKEN):
    #print("1")

    @bot.message_handler(commands=['start'])
    def welcome(message):
        bot.send_message(message.chat.id, "Практика 3 курс, парсер с яндекс погоды по г. Брянск")

    @bot.message_handler(commands=['pogoda'])
    def pogoda(message):
        list_temp = parser_yandex.parse_from_yandex_temp()
        condition = parser_yandex.parse_from_yandex_condition()
        pressure = parser_yandex.parse_from_yandex_pressure()
        humidity = parser_yandex.parse_from_yandex_humidity()
        mytable = PrettyTable()
        mytable.field_names = ["t","Давление, мм рт. ст.", "Влажность", "Ветер, м/с"]
        mytable.add_row([f"Утром: {list_temp[0]}", condition[0], pressure[0],humidity[0]])
        mytable.add_row([f"Днем: {list_temp[1]}", condition[1], pressure[1], humidity[1]])
        mytable.add_row([f"Вечером: {list_temp[2]}", condition[2], pressure[2], humidity[2]])
        mytable.add_row([f"Ночью: {list_temp[3]}", condition[3], pressure[3], humidity[3]])
        bot.send_message(message.chat.id, mytable)
        print(mytable)
        # bot.send_message(message.chat.id, )
        print("22")



if __name__ == "__main__":
    try:
        telegram_bot(TOKEN)
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)