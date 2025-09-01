import asyncio
import time
from time import time as now


def brew_coffee():
    print("Brewing coffee...")
    time.sleep(2)
    print("Coffee is ready!")

def make_toast():
    print("Making toast...")
    time.sleep(3)
    print("Toast is ready!")








# async def brew_coffee_async():
#     print("Brewing coffee...")
#     await asyncio.sleep(2)
#     print("Coffee is ready!")

# async def make_toast_async():
#     print("Making toast...")
#     await asyncio.sleep(3)
#     print("Toast is ready!")






# if __name__ == "__main__":
#     start = now()
#     brew_coffee()
#     make_toast()
#     print(f"[Sync] Done in {now() - start:.2f}s")

#     async def run_async_tasks():
#         start = now()
#         await asyncio.gather(
#             brew_coffee_async(),
#             make_toast_async()
#         )
#         print(f"[Async] Done in {now() - start:.2f}s")

#     asyncio.run(run_async_tasks())