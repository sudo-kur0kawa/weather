import python_weather

import asyncio
import os

user_city = input(print("enter your city:"))

async def main() -> None:
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(user_city)
        print(weather.temperature, weather.kind)
        
        for daily in weather:
            print(f"Good day, {user_city} citizen!\n here's the forecast for today and nexts!\n{daily}")
            if daily == weather.temperature >> 30:
                print("\U0001F975")
            elif daily == "temperature=31":
                print("\U0001F975")
            elif daily == "temperature=32":
                print("\U0001F975")
            elif daily == "temperature=33":
                print("\U0001F975")
            else:
                print("\U0001F976")
print("have a good day!")
                

if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(main())