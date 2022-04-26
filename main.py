import time
from _ast import Add

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import logging

import keys as nav
from aiogram import Bot, Dispatcher, types, executor
import requests
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bs4 import BeautifulSoup
import lxml

url = 'https://www.cbr.ru/'

all_page = requests.get(url).text

soup = BeautifulSoup(all_page, 'lxml')

TOKEN = '5256088665:AAGztg5GCL3jwzR4VB77zpIga8zpB-yd3AQ'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class States(StatesGroup):
    how_much = State()

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здоровы были {0.first_name}'.format(message.from_user),
                           reply_markup=nav.mainmenu)



@dp.message_handler()
async def bot_message(message: types.Message, state: FSMContext):
    if message.text == 'Хочу узнать курс':
        await bot.send_message(message.from_user.id, 'Какой курс валют ты хочешь узнать?', reply_markup=nav.backsMenu)
    elif message.text == 'Доллара':
        usd_buy = soup.find('div', class_='col-md-2 col-xs-9 _right mono-num').text
        dollar = float(usd_buy.replace(' ₽', '').replace('\n', '').replace('\r', '').replace('\t', '').replace(',', '.'))
        buy_now = 73 * dollar
        await message.answer(f'курс доллара сейчас {dollar}')

async def bot_message2(message: types.Message, state: FSMContext):
    await message.reply('Сколько ты готов обменять? Вводи давай... свои мульоны!')
    await state.set_state(States.how_much)
    await message.answer('Вы ввели число' + message.text)


        #
        # await bot.send_message(message.from_user.id, 'Курс доллара сейчас , хочешь посчитать, сколько баксов на свои деревянные ты можешь купить?', reply_markup=nav.mainmenu)
        # # time.sleep(30)
        # # async def how_much(message: types.Message, state: FSMContext):
        # await States.how_much.set()
        # await message.answer('Вы ввели число' + message.text)
        # await state.set_state(States.how_much)



executor.start_polling(dp, skip_updates=True)
