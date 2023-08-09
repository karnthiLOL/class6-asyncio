import asyncio
import time

async def example(message):
    print(f"{time.ctime()} - start of : ", message)
    await asyncio.sleep(1)
    print(f"{time.ctime()} - end of : ", message)

async def main():
    # Start coroutine twice (hopefully they start!)
    first_awaitable = example("Frist call")
    second_awaitable = example("Second call")
    # Wait for coroutines to finish
    await first_awaitable
    await second_awaitable

asyncio.run(main())


## ยังไม่ใช่ asyncio เพราะยังไม่ได้สร้าง task ขึ้นมา
# *ต้องสร้าง task ถึงจะเป็น asyncio

## Result
# Programs/Python/Python310/python.exe e:/00Lab/IOT/asyncio_exercise/class6-asyncio/1-2-hello-world-time.py
# Wed Aug  9 13:17:44 2023 - start of :  Frist call
# Wed Aug  9 13:17:45 2023 - end of :  Frist call
# Wed Aug  9 13:17:45 2023 - start of :  Second call
# Wed Aug  9 13:17:46 2023 - end of :  Second call
# PS E:\00Lab\IOT\asyncio_exercise> 