# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# import asyncio
#
# async def count():
#     print("One")
#     await asyncio.sleep(1)
#     print("Two")
#
# async def main():
#     await asyncio.gather(count(), count(), count())
#
# asyncio.run(main())
#
#


import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    # await page.goto('http://example.com')
    await page.goto('http://jandan.net/pic')
    await page.screenshot({'path': 'example.png'})
    await browser.close()


asyncio.run(main())