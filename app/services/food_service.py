from app.db import db  # Importing the database connection
from app.models.food_model import FoodModel # Importing FoodModel for data validation

async def log_food(food: FoodModel):
    food_dict = food.dict()
    await db["foodLogs"].insert_one(food_dict)
    return {"message": "Food logged successfully"}