from traceback import print_exc
from nonebot.message import MessageSegment
from aiocqhttp.event import Event
from os import path
from hoshino.log import new_logger
import re
import random
import aiohttp
import filetype
import os

logger = new_logger('shebot')

async def download_async(url: str, save_path: str, save_name: str) -> None:
    timeout = aiohttp.ClientTimeout(total=30)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(url) as resp:
            content = await resp.read()
            try:
                suffix = filetype.guess_mime(content).split('/')[1]
            except:
                raise ValueError('不是有效文件类型')
            abs_path = path.join(save_path, f'{save_name}.{suffix}')
            with open(abs_path, 'wb') as f:
                f.write(content)
                return abs_path

class Res:
    res_dir = path.join(path.dirname(__file__), 'modules', 'shebot', 'res')
    image_dir = path.join(res_dir, 'image')
    record_dir = path.join(res_dir, 'record')
    @classmethod
    def image(cls, pic_path: str) -> 'MessageSegment':
        return MessageSegment.image(path.join(cls.image_dir, pic_path))

    @classmethod
    def record(cls, rec_path) -> 'MessageSegment':
        return MessageSegment.record(path.join(cls.record_dir, rec_path))

    @classmethod
    async def save_image(cls, event: Event) -> None:
        for i, m in enumerate(event.message):
            match = re.match('\[CQ:image.+?\]', str(m))
            if match:
                try:
                    url = re.findall(r'http.*?term=\d', str(m))[0]
                    save_name = re.findall(r'(?<=-)[^-]*?(?=/)',url)[0]
                    image_path = await download_async(url, cls.image_dir, save_name)
                    event.message[i] = MessageSegment.image(image_path)
                except Exception as ex:
                    logger.warning(f'保存图片时发生错误{ex}')
        event.raw_message = str(event.message)

def get_random_file(path) -> str:
    files = os.listdir(path)
    rfile = random.choice(files)
    return rfile