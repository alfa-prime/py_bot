from aiogram.dispatcher import FSMContext
from aiogram import types

from app.bot import dp


@dp.message_handler(commands=['start'], state='*')
async def command_start(message: types.Message, state: FSMContext):
    await state.finish()
    return await message.answer('Start successful')
