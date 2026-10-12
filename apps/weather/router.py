from fastapi import APIRouter

from apps.weather.model import get_weather_model

router = APIRouter()


@router.post("/weather")
async def get_weather(city: str):
    # Placeholder for weather fetching logic
    return await get_weather_model(city)