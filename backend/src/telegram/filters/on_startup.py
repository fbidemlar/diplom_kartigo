from diplom_kartigo.backend.src.telegram.bot import bot
from diplom_kartigo.backend.src.telegram.admin.admin_list import admin_list
from diplom_kartigo.backend.src.telegram.filters.menu import set_main_menu


async def on_startup(bot: bot):
    admin_ids = [admin['id'] for admin in admin_list.values()]
    for admin_id in admin_ids:
        await set_main_menu(bot, admin_id)