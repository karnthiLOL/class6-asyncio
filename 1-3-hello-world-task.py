import asyncio
import time

async def print_after(message, delay):
    """Print a message after the specified delay (in seconds)"""
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message}")

async def main():
    # Start coroutine twice (hopefully they start!)
    first_awaitable = asyncio.create_task(print_after("World!",2))
    second_awaitable = asyncio.create_task(print_after("Hello", 1))
    # Wait for coroutines to finish
    await first_awaitable
    await second_awaitable

asyncio.run(main())


## เป็น asyncio ที่ถูกต้องเพราะมีการสร้าง task

## Result
# PS E:\00Lab\IOT\asyncio_exercise> & C:/Users/karnt/AppData/Local/Programs/Python/Python310/python.exe e:/00Lab/IOT/asyncio_exercise/class6-asyncio/1-3-hello-world-task.py
# Wed Aug  9 13:20:28 2023 - Hello
# Wed Aug  9 13:20:29 2023 - World!
# PS E:\00Lab\IOT\asyncio_exercise> 