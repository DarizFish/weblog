import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

async def index(request):
    return web.Response(content_type='text/html', body=b'<h1>Blog</h1>')

async def init():
    app = web.Application()
    app.router.add_get('/', index)
    runner = web.AppRunner(app)
    await runner.setup()
#    srv = await loop.create_server(runner, '127.0.0.1', 9009)
    site = web.TCPSite(runner, '127.0.0.1', 9000)
    await site.start()
    logging.info('server start at localhost')
    return site

loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()