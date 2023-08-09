import asyncio
import time

async def print_after(message, delay):
    """Print a message after the specified delay (in seconds)"""
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message}")

async def main():
    # Use asyncio.gather to run two coroutine concurrently:
    await asyncio.gather(
        print_after("World!",2),
        print_after("Hello", 1)
    )

asyncio.run(main())

## เป็น asyncio แต่ไม่ต้องสร้าง task 2 ครั้งเหมือน 1-3
# เพราะเอา asyncio.gather มาช่วย

## Result
# PS E:\00Lab\IOT\asyncio_exercise> & C:/Users/karnt/AppData/Local/Programs/Python/Python310/python.exe e:/00Lab/IOT/asyncio_exercise/class6-asyncio/1-4-hello-world-gather.py
# Wed Aug  9 13:23:08 2023 - Hello
# Wed Aug  9 13:23:09 2023 - World!