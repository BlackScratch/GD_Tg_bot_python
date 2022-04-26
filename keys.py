from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton






btnMain = KeyboardButton('Главное меню')

#=============Главное меню=============
btnRandom = KeyboardButton('Случайное число')
secondbtn = KeyboardButton('Хочу узнать курс')
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandom,secondbtn,btnMain)

#=============Другое меню=============
btnInfo = KeyboardButton('Другая информация')
btnMoney = KeyboardButton('Информация о погоде')
secondmenu2 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo,btnMoney,btnMain)

#=============Меню для курса валют=============
btnBacks = KeyboardButton('Доллара')
backsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnBacks,btnMain)

#=============Меню выбора валют=============
btnYes = KeyboardButton('Да')
changeBucks = ReplyKeyboardMarkup(resize_keyboard=True).add(btnYes,btnMain)
