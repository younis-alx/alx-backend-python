#!/usr/bin/env python3
'''
Import the wait_random function from 0-basic_async_syntax.

Create a function (do not use async functions;
 instead, use ordinary function syntax).
task_wait_random returns an asyncio after taking an integer max_delay.Task.

'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates an asynchronous task for wait_random.
    '''
    return asyncio.create_task(wait_random(max_delay))
