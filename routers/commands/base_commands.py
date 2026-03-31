from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.utils.formatting import Text, Bold
from aiogram.enums import ChatAction
from aiogram.utils.chat_action import ChatActionSender

router = Router(name=__name__)


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    action_sender = ChatActionSender(bot=message.bot,
                                     chat_id=message.chat.id,
                                     action=ChatAction.TYPING)
    async with action_sender:
        content = Text(
            "Привет, ", Bold(message.from_user.full_name),
            ', я бот который поможет тебе с твоим тяжелым выбором простым и понятным ответом - да/нет\n'
            '(если вопрос слишком сложный то я могу ответить - возможно)\n\n'
            '💬 В личке: просто отправь мне вопрос\n'
            '👥 В группе: используй команду /ask перед вопросом\n\n'
            'помни что я всего лишь бот и окончательное решение все равно лежит на тебе и лучше все обдумать несколько раз, а не спрашивать совета у бота'
        )
        await message.answer(
            **content.as_kwargs()
        )
