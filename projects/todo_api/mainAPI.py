from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
from enum import Enum
import datetime
import logging

# Initialize FastAPI application
# Create an instance of FastAPI which will be used to define routes and handle requests
app = FastAPI()

# Set up logging to capture information, errors, etc.
# Configure logging to display messages of INFO level and higher
logging.basicConfig(level=logging.INFO)

# Define an enumeration for status options
# This allows the status of a to-do list to be one of the predefined values
class StatusEnum(str, Enum):
    pending = "pending"
    completed = "completed"
    in_progress = "in_progress"

# Define an enumeration for priority levels
# This allows the priority of a to-do list to be one of the predefined values
class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

# =========================

# Define To-Do List model using Pydantic
# This model defines the structure of the data for a to-do list item
class ToDoList(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    due_date: datetime.date
    status: StatusEnum
    priority: Optional[PriorityEnum] = None
    creation_date: datetime.date
    last_updated_date: Optional[datetime.date] = None

# =========================

# In-memory storage for To-Do Lists
# A dictionary to store to-do lists temporarily
toDoList_db: Dict[str, ToDoList] = {}

# =========================

# Endpoint to create a batch of to-do lists
# This endpoint accepts a list of to-do lists and adds them to the in-memory database
@app.post("/todolist/", response_model=List[ToDoList])
def create_to_do_list(lists: List[ToDoList]):
    """
    Create a batch of to-do lists.
    """
    created_lists = []
    for lst in lists:
        if lst.id in toDoList_db:
            logging.error(f"ToDoList ID {lst.id} already exists.")
            raise HTTPException(status_code=400, detail=f"ToDoList ID {lst.id} already exists.")
        toDoList_db[lst.id] = lst
        created_lists.append(lst)
        logging.info(f"Created list with ID {lst.id}")
    return created_lists

# =========================

# Endpoint to get all to-do lists
# This endpoint returns all to-do lists stored in the in-memory database
@app.get("/todolist/", response_model=List[ToDoList])
def get_to_do_list():
    """
    Retrieve all to-do lists.
    """
    logging.info(f"Retrieving all to-do lists. Total count: {len(toDoList_db)}")
    return list(toDoList_db.values())

# =========================

# Endpoint to get a specific to-do list by ID
# This endpoint returns a single to-do list identified by its ID
@app.get("/todolist/{lst_id}", response_model=ToDoList)
def get_to_do_list_by_id(lst_id: str):
    """
    Retrieve a specific to-do list by its ID.
    """
    if lst_id in toDoList_db:
        return toDoList_db[lst_id]
    else:
        raise HTTPException(status_code=404, detail="ToDoList not found.")

# =========================

# Endpoint to update a specific to-do list by ID
# This endpoint updates a to-do list identified by its ID with new data
@app.put("/todolist/{lst_id}", response_model=ToDoList)
def update_to_do_list(lst_id: str, list_data: ToDoList):
    """
    Update a specific to-do list by its ID.
    """
    if lst_id in toDoList_db:
        toDoList_db[lst_id] = list_data
        return list_data
    else:
        raise HTTPException(status_code=404, detail="ToDoList not found.")

# =========================

# Endpoint to delete a specific to-do list by ID
# This endpoint removes a to-do list identified by its ID from the in-memory database
@app.delete("/todolist/{lst_id}", response_model=ToDoList)
def delete_to_do_list(lst_id: str):
    """
    Delete a specific to-do list by its ID.
    """
    if lst_id in toDoList_db:
        return toDoList_db.pop(lst_id)
    else:
        raise HTTPException(status_code=404, detail="ToDoList not found.")

# =========================

# Entry point to run the FastAPI application
# This block ensures the FastAPI application runs when this script is executed directly
if __name__ == "__main__":
    import uvicorn
    # Run the FastAPI application on localhost:8000
    uvicorn.run(app, host="127.0.0.1", port=8000)
