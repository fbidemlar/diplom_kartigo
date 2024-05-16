from aiogram import Bot
from aiogram.types import BotCommand

from diplom_kartigo.backend.src.telegram.filters.lexicon import menu_commands, admin_menu_commands
from diplom_kartigo.config import settings
from diplom_kartigo.backend.src.telegram.admin.admin_list import admin_list

bot = Bot(token=settings.TOKEN, parse_mode='HTML')


# Кнопка меню, которая упаравляет основным функционалом
async def set_main_menu(bot: Bot, admin_id: int):
    if admin_id in [admin['id'] for admin in admin_list.values()]:
        admin_main_menu_commands = [
            BotCommand(
                command=command,
                description=description
            ) for command, description in admin_menu_commands.items()
        ]
        await bot.set_my_commands(admin_main_menu_commands)
    else:
        main_menu_commands = [
            BotCommand(
                command=command,
                description=description
            ) for command, description in menu_commands.items()
        ]
        await bot.set_my_commands(main_menu_commands)