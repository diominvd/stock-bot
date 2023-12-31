from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

import handlers
from keyboards.reply import market_keyboard
import lines
from states import MarketStates

router = Router(name=__name__)

@router.message(MarketStates.get_new_ticker, Text('Главное меню'))
async def back_to_chapter_market_from_add_new_ticker(message: Message, state: FSMContext):
    await message.answer(text=lines.market_lines['text_back_to_menu'],
                         reply_markup=market_keyboard.create_market_keyboard(user_id=handlers.fetch_user_id(obj=message)))

    await state.clear()


@router.message(MarketStates.get_ticker_for_parsing, Text('Главное меню'))
async def back_to_chapter_market_from_tickers_list(message: Message, state: FSMContext):
    await message.answer(text=lines.market_lines['text_back_to_menu'],
                         reply_markup=market_keyboard.create_market_keyboard(user_id=handlers.fetch_user_id(obj=message)))

    await state.clear()


@router.message(MarketStates.get_ticker_for_delete, Text('Главное меню'))
async def back_to_chapter_market_from_tickers_list(message: Message, state: FSMContext):
    await message.answer(text=lines.market_lines['text_back_to_menu'],
                         reply_markup=market_keyboard.create_market_keyboard(user_id=handlers.fetch_user_id(obj=message)))

    await state.clear()