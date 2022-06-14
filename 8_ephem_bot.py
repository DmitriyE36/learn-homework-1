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
import structlog
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date
import settings

logging.basicConfig(level=logging.INFO)
logger = structlog.getLogger()

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Здравствуй, пользователь!')

def my_planets(update, context):
    input_name = update.message.text.split()
    planet_name = input_name[1].lower().capitalize()
    print(planet_name)
    planet = getattr(ephem, planet_name)
    day = date.today()
    print(day)
    const_day = planet(day)
    const = ephem.constellation(planet(day))
    print(const)
    update.message.reply_text(f'Сегодня {day}, планета {planet_name} находится в созвездии {const}')
    
def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    lp_elfim_bot = Updater(settings.API_KEY, use_context=True)

    dp = lp_elfim_bot.dispatcher
    dp.add_handler(CommandHandler("planet", my_planets))
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, my_planets))

    logger.info("Бот стартовал")
    lp_elfim_bot.start_polling()
    lp_elfim_bot.idle()

if __name__ == "__main__":
    main()
