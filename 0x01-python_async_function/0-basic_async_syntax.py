#!/usr/bin/env python3
'''Task 0: Async fundamentals
Create an asynchronous coroutine that takes an integer parameter
('max_delay,' with a default value of 10)
 and returns a value called

'wait_random' is a function
that waits for a random delay
between 0 and'max_delay' (included and float value)
seconds before returning it.
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''waits for a random number of seconds
    '''
    wait_seconds: float = random.random() * max_delay
    await asyncio.sleep(wait_seconds)
    return wait_seconds
