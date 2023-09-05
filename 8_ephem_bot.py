"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
from datetime import datetime
import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


# PROXY = {
#     'proxy_url': 'socks5://t1.learn.python.ru:1080',
#     'urllib3_proxy_kwargs': {
#         'username': 'learn',
#         'password': 'python'
#     }
# }


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def planet(update,context):
    planet_lst={"Mars": ephem.Mars(),
                 "Venus":ephem.Venus(),
                 "Mercury":ephem.Mercury(),
                 "Jupiter":ephem.Jupiter() ,
                 "Saturn": ephem.Saturn(),
                 "Pluto": ephem.Pluto(),
                 "Uranus":ephem.Uranus(),
                 "Neptune":ephem.Neptune()}
    user_respons=update.message.text.split()
    for name in user_respons:
        if name in planet_lst:
            planet_name=planet_lst.get(name)
            planet_name.compute(f"{datetime.now().strftime('%Y/%m/%d')}")
            answer=ephem.constellation(planet_name)[1]
    update.message.reply_text(answer)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    # dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(MessageHandler(Filters.text,planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
