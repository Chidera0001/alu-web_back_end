#!/usr/bin/env python3
"""
Asynchronous coroutine that spawns wait_randomn
times with the specified max_delay
"""
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with specified max_delay
    Args:
        n: number of times to spawn wait_random
        max_delay: maximum delay between spawns
    Returns:
        List of delays in ascending order without using sort()
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
