import asyncio
from aiogram import Bot, Dispatcher, types

API_TOKEN = "8722275863:AAFG0ezlgbUOdvCMatO0V5Y3qrTz3RqEFws"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


def format_application(text: str) -> str:
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    try:
        fio = lines[1]
        yen = lines[2].replace(" ", "").replace("JPY", "")
        rub = lines[3].replace(" ", "")
        code = lines[4]

        return (
            f"8 Акебоно {fio}\n"
            f"{yen} йен \n"
            f"{rub} руб \n\n"
            f"Акебоно Вн {code}"
        )
    except:
        return "❌ Ошибка формата. Проверь заявку."


@dp.message()
async def handle_message(message: types.Message):
    result = format_application(message.text)
    await message.answer(result)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
