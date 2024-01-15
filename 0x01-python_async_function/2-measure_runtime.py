#!/usr/bin/env python3
'''
Import wait_n from the previous file into 2-measure_runtime.py.

Create a measure_time function with the inputs n and max_delay that
 returns total_time / n and measures the total
   execution time for wait_n(n, max_delay).
     Your function's output should be a float.

To calculate an approximate elapsed time, use the time module.

'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Computes the average runtime of wait_n.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
