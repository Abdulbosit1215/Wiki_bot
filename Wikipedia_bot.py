import logging
from aiogram import  Bot, Dispatcher, executor, types
import wikipedia as wk
import knopka as knk
API_TOKEN = '5495998861:AAHv8JQ70OSD0oxiSLd5IP_6r-BYLxDF034'


logging.basicConfig(level=logging.INFO)


bot=Bot(token=API_TOKEN)
db=Dispatcher(bot)


@db.message_handler(commands=['start'])
async def start(message: types.Message):
	await message.answer('Assalomu alaykum, {0.first_name}''.Botimizga xush kelibsiz!!!'.format(message.from_user), reply_markup=knk.Natija)
    




@db.message_handler()
async def function(message:types.Message):
    if message.text == '🇺🇿 Õzbek tili':
        wk.set_lang('uz')
        await bot.send_message(message.from_user.id,'siz òzbek tilini tanladingiz')
        
    if message.text == '🇷🇺 Русский язык':
        wk.set_lang('ru')
        await bot.send_message(message.from_user.id, 'Вы выбрали русский язык ' )
       
    if message.text == '🇺🇸 English':
        wk.set_lang('eng')
        await bot.send_message(message.from_user.id, 'You choosed english laungage' )

    try:
        mavzu = wk.summary(message.text)

        await message.answer(mavzu)
    except:
        await message.answer("Bu mavzuga oid maqola yòq")




if __name__=="__main__":
    executor.start_polling(db)









