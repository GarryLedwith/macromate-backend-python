from fastapi import FastAPI,HTTPException # Importing FastAPI and HTTPException for creating the app and handling errors
from pydantic import BaseModel # Importing BaseModel for data validation

app = FastAPI()

items = ['test', 'test2'] # List to store food items

# GET, POST, PUT, DELETE routes
@app.get("/") # app decorator and root endpoint
async def root():
    return {"message": "Hello from MacroMate!"}

########## PRACTICE ENDPOINTS ##########

# practice POST endpoint (used CURL to test)
@app.post("/items")
async def create_item(item: str):
    items.append(item)
    return {"item": item, "items": items}

# GET endpoint to retrieve all items
@app.get("/items")
async def read_items():
    return {"items": items}

# GET endpoint to retrieve a specific item by index
@app.get("/items/{item_id}")
async def get_item(item_id: int) -> str: # Endpoint to get an item by its index
    if item_id < len(items): 
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found") # Endpoint to handle item not found error
    
    
######### END OF PRACTICE ENDPOINTS ##########