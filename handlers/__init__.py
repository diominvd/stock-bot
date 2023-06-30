import aiogram.types
import pydantic.main

from config import dispatcher


from handlers.commands import help, start
dispatcher.include_routers(
    help.router,
    start.router
)

from handlers.market.add_ticker import add_new_ticker, add_ticker_command
from handlers.market.delete_ticker import delete_ticker_command, get_ticker_for_delete
from handlers.market.my_tickers import get_ticker_for_parsing, my_ticker_command
dispatcher.include_routers(
    add_new_ticker.router,
    add_ticker_command.router,
    delete_ticker_command.router,
    get_ticker_for_delete.router,
    get_ticker_for_parsing.router,
    my_ticker_command.router
)

from handlers.other import incorrect_ticker, market_menu
dispatcher.include_routers(
    incorrect_ticker.router,
    market_menu.router
)

def fetch_user_id(obj: pydantic.main.ModelMetaclass) -> int:
    return int(obj.from_user.id)

def fetch_user_username(obj: pydantic.main.ModelMetaclass) -> str:
    return str(obj.from_user.username)


async def remove_callback_delay(callback_query: aiogram.types.CallbackQuery) -> None:
    await callback_query.answer(text=None,
                                show_alert=None)
    return None