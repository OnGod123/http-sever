import asyncio

async def print_async(data="a"):  # Default argument for data
  """Prints data asynchronously. Defaults to 'a' if no argument provided."""
  await asyncio.sleep(0)  # No random delay
  print(data)

async def print_alphabet():
  """Prints lowercase alphabets asynchronously."""
  for char in chr(ord('a'))[:26]:
    await print_async(char)  # Pass each character to print_async

async def print_numbers():
  """Prints numbers from 1 to 26 asynchronously."""
  for num in range(1, 27):
    await print_async(num)

async def main():
  """Runs both printing functions asynchronously."""
  alphabet_task = asyncio.create_task(print_alphabet())
  numbers_task = asyncio.create_task(print_numbers())
  await asyncio.gather(alphabet_task, numbers_task)
  print("All data printed asynchronously.")

asyncio.run(main())
