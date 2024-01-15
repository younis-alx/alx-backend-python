#!/usr/bin/env python3
'''
Take the code from wait_n and modify it to create the new function
 task_wait_n. Except for the use of task_wait_random,
   the code is virtually identical to wait_n.

'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes task_wait_random n times.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
