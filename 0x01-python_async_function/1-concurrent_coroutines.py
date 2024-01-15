#!/usr/bin/env python3

'''
Import wait_random from
 the previous python file
   and create an async method
     called wait_n that accepts
       two int arguments (in this order): n and max_delay.
         You will spawn wait_random n times with the max_delay you choose.

wait_n should provide a list of
 all delays (in floats).
 Because of concurrency, the list of delays should be in ascending order
   without using sort().
'''

import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''return the list of all the delays (float values)
    '''
    waits = await asyncio.gather(
        *list(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sorted(waits)
