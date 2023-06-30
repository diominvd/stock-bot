from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.types import Message, ReplyKeyboardRemove

import config

from keyboards.reply import market_keyboard, add_ticker_keyboard, user_tickers_keyboard


# market_keyboard: Dynamic keyboard. For use import def in file.
# user_tickers_keyboard: Dynamic keyboard. For use import def in file.
add_ticker_kb: ReplyKeyboardMarkup = add_ticker_keyboard.create_add_ticker_keyboard()


async def delete_reply_keyboard(message: Message, bot=config.bot) -> None:
    await message.answer(text='Загрузка...',
                         reply_markup=ReplyKeyboardRemove())

    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id + 1)