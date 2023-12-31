from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from data import market
import handlers
from keyboards.reply import market_keyboard
import lines

router = Router(name=__name__)

@router.message(Command('start'))
async def start_command_handler(message: Message) -> None:
    # Insert user into database.
    market.insert_new_user_into_database_market(user_id=handlers.fetch_user_id(obj=message))

    await message.answer(text=lines.commands_lines['text_start_command'],
                         reply_markup=market_keyboard.create_market_keyboard(user_id=handlers.fetch_user_id(obj=message)))