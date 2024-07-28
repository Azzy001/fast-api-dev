from pydantic import BaseModel

class VehicleCreate(BaseModel):
    make: str
    model: str
    year: int
    licence_plate: str
    colour: str
    mileage: int
    available: bool
    quantity: int

class VehicleResponse(VehicleCreate):
    id: str

    class Config:
        from_attributes = True
