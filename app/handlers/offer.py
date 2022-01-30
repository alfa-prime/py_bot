from aiogram.dispatcher import FSMContext
from aiogram import types


from app.bot import dp
from app.messages import replies
from app.keyboards import kb_generator

from .states import States


@dp.callback_query_handler(text="offer", state='*')
async def ask_term_for_search(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.OFFER[0])
    await call.message.edit_text(replies.ask_term_to_offer)
    await call.answer()


@dp.message_handler(state=States.OFFER)
async def output_term_offer_result(message: types.Message, state: FSMContext):
    # todo: подумать надо ли проверять введеный термин или нет, если да, то как?
    # todo: дальнейшая логика -> отправка предложенного термина на модерацию
    offer_input_value = message.text
    keyboard = await kb_generator(["offer_again", "start_again"], row_width=2)
    await message.answer(replies.taken_term_to_offer.format(term=offer_input_value), reply_markup=keyboard)
