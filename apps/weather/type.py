from pydantic import BaseModel


class WeatherData(BaseModel):
    city: str
    temperature_celsius: float
    condition: str              # जैसे: "Sunny", "Rainy"
    humidity_percentage: int
    summary: str
    crime_rate: float