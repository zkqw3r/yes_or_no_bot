import aiohttp
import asyncio

url = 'https://yesno.wtf/api'


async def yes_or_no():
    timeout = aiohttp.ClientTimeout(total=10)
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url=url) as request:
                response = await request.json()
                if response.get('answer') == 'yes':
                    answer = 'Да'
                elif response.get('answer') == 'no':
                    answer = 'Нет'
                elif response.get('answer') == 'maybe':
                    answer = 'Возможно'
                else:
                    answer = 'пиздец'
                gif = response.get('image')
                return gif, answer
    except (aiohttp.ClientError, asyncio.TimeoutError) as e:
        # Если API недоступен, возвращаем None
        return None, None
