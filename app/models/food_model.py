# Food Model for MacroMate
# This file defines the data model for food items in the MacroMate application.
from pydantic import BaseModel

class FoodModel(BaseModel): 
    label: str
    calories: float
    protein: float
    carbohydrates: float
    fat: float