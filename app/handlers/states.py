from aiogram.utils.helper import Helper, HelperMode, ListItem


class States(Helper):
    """
    машина состояний FSM
    теория и практика:
    https://mastergroosha.github.io/telegram-tutorial-2/fsm/
    https://surik00.gitbooks.io/aiogram-lessons/content/chapter3.html
    """
    mode = HelperMode.snake_case

    START = ListItem()
    BEGIN = ListItem()
    INFO = ListItem()
    HELP = ListItem()
    SEARCH_OR_OFFER = ListItem()
    SEARCH = ListItem()
    OFFER = ListItem()
