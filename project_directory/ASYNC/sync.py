import asyncio

async def print_numbers(name):
    for i in range(5):
        print(f"{name}: {i}")
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(
        print_numbers("Task 1"),
        print_numbers("Task 2")
    )

if __name__ == "__main__":
    asyncio.run(main())
