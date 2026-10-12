from fastapi import FastAPI

from apps.weather.router import router as weather_router

app = FastAPI()
app.include_router(weather_router)


@app.on_event("startup")
async def startup_event():
    print("Weather API is starting up...")