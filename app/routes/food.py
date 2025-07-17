from fastapi import APIRouter, HTTPException # Importing APIRouter for creating a router and HTTPException for error handling
from app.models.food_model import FoodModel # Importing FoodModel for data validation
from app.services.food_service import log_food

router = APIRouter() # Creating a new router instance

@router.post("/foods")
async def create_food_entry(food: FoodModel):
    """
    Endpoint to log a food entry.
    """
    try:
        response = await log_food(food)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
