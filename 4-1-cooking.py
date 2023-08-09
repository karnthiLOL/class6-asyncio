import asyncio
import time

class Coffee:
    pass
class Egg:
    pass
class Toast:
    pass

def PourCoffee():
    print(f"{time.ctime()} - Pouring coffee")
    return Coffee()

async def ApplyButter():
    print(f"{time.ctime()} - Spreading butter on toast")
    await asyncio.sleep(1)
  
async def FryEggsAsync(howMany):
    print(f"{time.ctime()} - Heat pan to fry eggs")
    await asyncio.sleep(3)
    print(f"{time.ctime()} - Frying",howMany,"eggs")
    await asyncio.sleep(3)
    print(f"{time.ctime()} - Eggs are ready")
    return Egg()

async def ToastAsync(slices):
    for slice in range(slices):
        print(f"{time.ctime()} - Toasting bread", slice + 1)
        await asyncio.sleep(3)
        print(f"{time.ctime()} - Bread", slice + 1, "toasted")
        await ApplyButter()
        print(f"{time.ctime()} - Toast", slice + 1, "ready")
    return Toast()

async def main():
    cup = PourCoffee()
    print(f"{time.ctime()} - Coffee is ready")
    await asyncio.gather(
        FryEggsAsync(2),
        ToastAsync(2)
    )
    
if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{time.ctime()} - Breakfast cooked in",elapsed,"seconds.")


## Result

# Wed Aug  9 14:56:04 2023 - Pouring coffee
# Wed Aug  9 14:56:04 2023 - Coffee is ready
# Wed Aug  9 14:56:04 2023 - Heat pan to fry eggs
# Wed Aug  9 14:56:04 2023 - Toasting bread 1
# Wed Aug  9 14:56:07 2023 - Frying 2 eggs
# Wed Aug  9 14:56:07 2023 - Bread 1 toasted
# Wed Aug  9 14:56:07 2023 - Spreading butter on toast
# Wed Aug  9 14:56:08 2023 - Toast 1 ready
# Wed Aug  9 14:56:08 2023 - Toasting bread 2
# Wed Aug  9 14:56:10 2023 - Eggs are ready
# Wed Aug  9 14:56:11 2023 - Bread 2 toasted
# Wed Aug  9 14:56:11 2023 - Spreading butter on toast
# Wed Aug  9 14:56:12 2023 - Toast 2 ready
# Wed Aug  9 14:56:12 2023 - Breakfast cooked in 8.040168400038965 seconds.