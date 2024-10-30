# "Асинхронные силачи"
import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for ball in range(1, 6):
        delay = 1 / power
        await asyncio.sleep(delay)
        print(f'Силач {name} поднял {ball} шар.')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    first = asyncio.create_task(start_strongman('Pasha', 3))
    second = asyncio.create_task(start_strongman('Denis', 4))
    third = asyncio.create_task(start_strongman('Apollon', 5))
    await first
    await second
    await third

asyncio.run(start_tournament())
