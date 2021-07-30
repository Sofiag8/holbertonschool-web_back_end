#!/usr/bin/env python3
"""
You will spawn wait_random n times
with the specified max_delay.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values)"""
    delay_list: List[float] = []
    for i in range(n):
        delay_list.append(await wait_random(max_delay))
    return sorted(delay_list)
