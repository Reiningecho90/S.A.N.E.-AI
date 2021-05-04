import python_weather
import datetime
from asyncio import get_event_loop

client = python_weather.Client(format=python_weather.IMPERIAL)


async def weather():
    weather = await client.find("Washington DC")
    print('The temperature is currently: ', weather.current.temperature, 'fahrenheit or about', int((weather.current.temperature-32)/1.8), 'celcius')
    await client.close()


get_event_loop().run_until_complete(weather())