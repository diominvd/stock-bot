from aiogram.fsm.state import StatesGroup, State

class MarketStates(StatesGroup):
    get_new_ticker = State()
    get_ticker_for_parsing = State()
    get_ticker_for_delete = State()