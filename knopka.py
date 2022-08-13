from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

tugma1 = InlineKeyboardButton('🇺🇿 Õzbek tili', callback_data="uz")
tugma2 = InlineKeyboardButton('🇷🇺 Русский язык', callback_data="ru")
tugma3 = InlineKeyboardButton('🇺🇸 English', callback_data="eng")


#
Natija = InlineKeyboardMarkup().row(tugma1, tugma2, tugma3)

#.add(tel,lok)

tel = KeyboardButton(text='Tel raqamini  yuborish', request_contact=True)
lok = KeyboardButton(text='Lokatsiyani yuborish', request_location=True)
men = KeyboardButton(text='Tilni òzgartirish')
Natija_uz = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(tel, lok).row(men)

tel = KeyboardButton(text='Send phone number', request_contact=True)
lok = KeyboardButton(text='Send location', request_location=True)
men = KeyboardButton(text='Change laungage')
Natija_eng = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(tel, lok).row(men)


tel = KeyboardButton(text='Отправить номер телефона', request_contact=True)
lok = KeyboardButton(text='Отправить местоположение', request_location=True)
men = KeyboardButton(text='Изменить язык')
Natija_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(tel, lok).row(men)





if __name__=="__main__"











































































