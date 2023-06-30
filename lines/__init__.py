from data import market

keyboards_lines: dict = {
    'add_ticker_keyboard': {
        'menu': 'Главное меню'
    },
    'market_keyboard': {
        'add_ticker': 'Добавить тикер',
        'my_tickers': 'Мои тикеры',
        'delete_ticker': 'Удалить тикер',
    },
    'user_tickers_keyboard': {
        'menu': 'Главное меню'
    },
}

commands_lines: dict = {
    'text_help_command': 'Coming soon...',
    'text_start_command': 'Добро пожаловать в Stock Bot 📈\n\nЭтот бот поможет отслеживать котировки акций в реальном времени.\n\n'
                          'Для того, чтобы добавить желаемую компанию в свой список отслеживаемых нажмите кнопку "Добавить тикер".\n\n'
                          'Чтобы посмотреть добавленные тикеры нажмите кнопку "Мои тикеры".\n\n'
                          'P.S. <b>Тикер</b> - Краткое название в биржевой информации котируемых инструментов. '
                          'Например тикер компании Сбербанк: $SBER.',
}


def ticker_added(ticker: str) -> str:
    return f'Тикер ${ticker} успешно добавлен.'


def ticker_value(ticker: str) -> str:
    return f'📊 ${ticker}: {market.parse_ticker(ticker=ticker)}'


market_lines: dict = {
    'def_text_ticker_added': ticker_added,
    'def_text_ticker_value': ticker_value,

    'error_text_incorrect_ticker': 'Некорректное имя тикера. Повторите попытку.',
    'error_text_nonexistent_ticker': 'Данный тикер не существует. Повторите попытку.',
    'error_text_tickers_empty': 'У вас не добавлено ни одного тикера. '
                                'Добавьте хотя бы один тикер и повторите попытку.',
    'error_text_ticker_exists': 'Тикер с таким названием уже существует.',
    'error_text_tickers_limit': 'Достигнуто максимальное количество тикеров.',
    'error_text_ticker_not_added': 'У вас нет тикера с таким названием. Повторите попытку.',

    'text_add_ticker': 'Отправьте тикер, например: $SBER.\n\n'
                       'Будьте внимательны, так как неверные тикеры не будут добавлены.',
    'text_back_to_menu': 'Возвращаюсь в главное меню.',
    'text_ticker_deleted': 'Тикер успешно удалён. Для удаления еще одного тикера, нажмите на соответсвующую кнопку на клавиатуре.',
    'text_ticker_deleted_tickers_list_empty': 'Тикер успешно удалён. У вас ни осталось ни одного тикера.',
    'text_user_tickers': 'На клавиатуре представлен список ваших тикеров. Чтобы получить '
                         'текущую котировку нажмите на желаемый тикер.',
    'text_user_tickers_for_delete': 'На клавиатуре представлен список ваших тикеров. Чтобы удалить '
                                    'тикер выберите его на клавиатуре.',
}