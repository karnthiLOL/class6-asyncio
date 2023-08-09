# When do coroutines start running?
import asyncio
import time

async def print_after(message, delay):
    """Print a message after the specified delay (in seconds)"""
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message}")

async def main():
    # Start coroutine twice (hopefully they start!)
    first_awaitable = print_after("World!",2)
    second_awaitable = print_after("Hello", 1)
    # Wait for coroutines to finish
    await first_awaitable
    await second_awaitable

asyncio.run(main())


## ไม่ใช่โปรแกรม asyncio 
## เพราะ print_after(message, delay):เป็น co-lutine function
## การทำงานจึงไม่ใช่แบบ asyncio

## Result
# PS E:\00Lab\IOT\asyncio_exercise> & C:/Users/karnt/AppData/Local/Programs/Python/Python310/python.exe e:/00Lab/IOT/asyncio_exercise/class6-asyncio/1-1-hello-world-wrong.py      
# Wed Aug  9 13:13:23 2023 - World!
# Wed Aug  9 13:13:24 2023 - Hello
# PS E:\00Lab\IOT\asyncio_exercise> 