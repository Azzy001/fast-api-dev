from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from vehicleDB import VehicleDB, init_db, get_db
from vehicleModel import VehicleCreate, VehicleResponse
import uuid

# Initialize the database
init_db()

# Define the FastAPI application
app = FastAPI()

@app.post("/vehicles", response_model=VehicleResponse)
async def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    new_vehicle = VehicleDB(
        id=str(uuid.uuid4()),  # Generate a unique ID for the vehicle
        make=vehicle.make,
        model=vehicle.model,
        year=vehicle.year,
        licence_plate=vehicle.licence_plate,
        colour=vehicle.colour,
        mileage=vehicle.mileage,
        available=vehicle.available,
        quantity=vehicle.quantity
    )
    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)
    return new_vehicle

@app.get("/vehicles", response_model=list[VehicleResponse])
def get_vehicles(db: Session = Depends(get_db)):
    vehicles = db.query(VehicleDB).all()
    return vehicles

@app.get("/vehicles/{vehicle_id}", response_model=VehicleResponse)
def get_vehicle(vehicle_id: str, db: Session = Depends(get_db)):
    vehicle = db.query(VehicleDB).filter(VehicleDB.id == vehicle_id).first()
    if vehicle:
        return vehicle
    raise HTTPException(status_code=404, detail="Vehicle not found.")

@app.put("/vehicles/{vehicle_id}", response_model=VehicleResponse)
def update_vehicle(vehicle_id: str, vehicle: VehicleCreate, db: Session = Depends(get_db)):
    db_vehicle = db.query(VehicleDB).filter(VehicleDB.id == vehicle_id).first()
    if db_vehicle:
        for key, value in vehicle.dict().items():
            if value is not None:
                setattr(db_vehicle, key, value)
        db.commit()
        db.refresh(db_vehicle)
        return db_vehicle
    raise HTTPException(status_code=404, detail="Vehicle not found.")

@app.delete("/vehicles/{vehicle_id}", response_model=dict)
def delete_vehicle(vehicle_id: str, db: Session = Depends(get_db)):
    vehicle = db.query(VehicleDB).filter(VehicleDB.id == vehicle_id).first()
    if vehicle:
        db.delete(vehicle)
        db.commit()
        return {"message": f"Vehicle with id {vehicle_id} deleted."}
    raise HTTPException(status_code=404, detail="Vehicle not found.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
