from aiogram import Router, types, F
from aiogram.enums import ChatAction, ChatType
from aiogram.filters import Command
from aiogram.utils.chat_action import ChatActionSender
import main.main as main_func


router = Router(name=__name__)


async def send_answer(message: types.Message):
    """Отправляет ответ да/нет с гифкой"""
    if not message.bot:
        return
    
    action_sender = ChatActionSender(bot=message.bot,
                                     chat_id=message.chat.id,
                                     interval=2,
                                     action=ChatAction.UPLOAD_VIDEO)
    async with action_sender:
        gif, answer = await main_func.yes_or_no()
        if gif and answer:
            await message.answer_animation(animation=gif, caption=answer)
        else:
            await message.answer("Извини, API временно недоступен. Попробуй позже.")


# В группах работает только по команде /ask
@router.message(Command("ask"), F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP}))
async def ask_in_group(message: types.Message):
    await send_answer(message)


# В личке работает на любое сообщение (кроме команд)
@router.message(F.chat.type == ChatType.PRIVATE)
async def question_private(message: types.Message):
    await send_answer(message)
