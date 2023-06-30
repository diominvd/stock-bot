from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

import handlers
from keyboards.reply import market_keyboard
from lines import commands_lines

router = Router(name=__name__)

@router.message(Command('help'))
async def start_command_handler(message: Message) -> None:
    await message.answer(text=commands_lines['text_help_command'],
                         reply_markup=market_keyboard.create_market_keyboard(user_id=handlers.fetch_user_id(obj=message)))