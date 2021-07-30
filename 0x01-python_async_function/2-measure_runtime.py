#!/usr/bin/env python3
"""
measures the total execution time for wait_n(n, max_delay)
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    returns total_time / n
    """
    initial_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    total_time = end_time - initial_time
    return (total_time) / n
