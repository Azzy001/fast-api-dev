# import necessary modules from typing and pydantic libraries
# Optional is used to define fields that are not required
# BaseModel is used to create data models with validation
from typing import Optional
from pydantic import BaseModel

# ==============================

# define a class for creating a vehicle
# this class is used to specify the data needed to create or update a vehicle
class VehicleCreate(BaseModel):
    # define the fields for the vehicle, all fields are optional
    # this means that any of these fields can be left out when creating or updating a vehicle
    make: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    licence_plate: Optional[str] = None
    colour: Optional[str] = None
    mileage: Optional[int] = None
    available: Optional[bool] = None
    quantity: Optional[int] = None

# ==============================

# define a class for the response when fetching vehicle data
# this class extends VehicleCreate by adding an ID field for the vehicle
# this is used when returning vehicle data to include the unique identifier
class VehicleResponse(VehicleCreate):
    # unique identifier for the vehicle
    id: str

    # configuration class for Pydantic model
    class Config:
        # this setting allows the model to be created from database attributes
        from_attributes = True
