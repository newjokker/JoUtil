# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
asyncio.run(main())