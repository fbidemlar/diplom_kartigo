from aiogram.filters import Command, CommandStart

from diplom_kartigo.backend.src.db.db import Base, engine
from diplom_kartigo.backend.src.telegram.bot import bot, dp

from diplom_kartigo.backend.src.telegram.handlers.start import start, get_phone
from diplom_kartigo.backend.src.telegram.filters.on_startup import on_startup

from diplom_kartigo.backend.src.telegram.states import States

if __name__ == '__main__':
    # Инициализация базы данных
    Base.metadata.create_all(bind=engine)
    print("База инициализирована")
    # Регистрация кнопки меню в чате
    dp.startup.register(on_startup)

    dp.message.register(start, CommandStart())
    dp.message.register(get_phone, States.phone)

    print("Бот запущен")
    dp.run_polling(bot)