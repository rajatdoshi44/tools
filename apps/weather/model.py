import os

import httpx

from apps.weather.type import WeatherData


async def get_weather_model(city: str) -> WeatherData:
    weather_api_key = os.getenv("GOOGLE_API_KEY")
    weather_api_url = "https://api.openweathermap.org/data/2.5/weather"

    if not weather_api_key:
        return WeatherData(
            city=city,
            temperature_celsius=0.0,
            condition="Unavailable",
            humidity_percentage=0,
            summary="Weather API key is not configured.",
            crime_rate=0.0,
        )

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                weather_api_url,
                params={"q": city, "appid": weather_api_key, "units": "metric"},
            )
            response.raise_for_status()
            data = response.json()
            weather = (data.get("weather") or [{}])[0]
            main = data.get("main") or {}

            return WeatherData(
                city=data.get("name", city),
                temperature_celsius=float(main.get("temp", 0.0)),
                condition=weather.get("main", "Unknown"),
                humidity_percentage=int(main.get("humidity", 0)),
                summary=f"{weather.get('description', 'Weather').capitalize()} in {city}.",
                crime_rate=0.0,
            )
    except (httpx.HTTPError, KeyError, TypeError, ValueError):
        return WeatherData(
            city=city,
            temperature_celsius=0.0,
            condition="Unavailable",
            humidity_percentage=0,
            summary="Unable to fetch live weather data.",
            crime_rate=0.0,
        )


# def get_weather_model(city: str):
#     model = get_llm_content(
#         model_name=None,
#         prompt=city,
#         config={
#             "max_output_tokens": 100,
#             "response_mime_type": "application/json",
#             "response_schema": WeatherData,
#             "tools": [weather_tool],
#             "system_instruction": "You are a smart travel advisor. Always fetch live weather using the tool before giving advice.",
#         },
#     )
#     return {"response": model}