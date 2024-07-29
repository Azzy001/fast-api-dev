# import necessary modules from FastAPI, SQLAlchemy, and other libraries
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from vehicleDB import VehicleDB, init_db, get_db
from vehicleModel import VehicleCreate, VehicleResponse
import uuid

# ==============================

# initialize the database connection and tables
# this function sets up the database and creates any necessary tables
init_db()

# create an instance of the FastAPI application
# this is the main object that will handle incoming requests and route them to the correct functions
app = FastAPI()

# ==============================

# define a route to add a new vehicle
# this function handles POST requests to create a new vehicle entry
@app.post("/vehicles", response_model=VehicleResponse)
async def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    # create a new vehicle record using the data provided in the request
    new_vehicle = VehicleDB(
        id=str(uuid.uuid4()),
        make=vehicle.make,
        model=vehicle.model,
        year=vehicle.year,
        licence_plate=vehicle.licence_plate,
        colour=vehicle.colour,
        mileage=vehicle.mileage,
        available=vehicle.available,
        quantity=vehicle.quantity
    )
    # add the new vehicle to the database session
    db.add(new_vehicle)
    # commit the changes to the database
    db.commit()
    # refresh the vehicle instance with the updated data
    db.refresh(new_vehicle)
    # return the newly created vehicle
    return new_vehicle

# ==============================

# define a route to get a list of all vehicles
# this function handles GET requests to retrieve all vehicle records
@app.get("/vehicles", response_model=list[VehicleResponse])
def get_vehicles(db: Session = Depends(get_db)):
    # query the database for all vehicles
    vehicles = db.query(VehicleDB).all()
    return vehicles  # return the list of vehicles

# ==============================

# define a route to get details of a specific vehicle by its ID
# this function handles GET requests to retrieve a vehicle by its unique ID
@app.get("/vehicles/{vehicle_id}", response_model=VehicleResponse)
def get_vehicle(vehicle_id: str, db: Session = Depends(get_db)):
    # query the database for the vehicle with the specified ID
    vehicle = db.query(VehicleDB).filter(VehicleDB.id == vehicle_id).first()
    if vehicle:
        return vehicle  # return the vehicle if found
    # raise an HTTP exception if the vehicle is not found
    raise HTTPException(status_code=404, detail="Vehicle not found.")

# ==============================

# define a route to update details of a specific vehicle by its ID
# this function handles PUT requests to update a vehicle's details
@app.put("/vehicles/{vehicle_id}", response_model=VehicleResponse)
def update_vehicle(vehicle_id: str, vehicle: VehicleCreate, db: Session = Depends(get_db)):
    # query the database for the vehicle with the specified ID
    db_vehicle = db.query(VehicleDB).filter(VehicleDB.id == vehicle_id).first()
    if db_vehicle:
        try:
            # create a dictionary of the fields to update, excluding unset fields
            update_data = vehicle.dict(exclude_unset=True)
            # update the vehicle record with the new data
            for key, value in update_data.items():
                setattr(db_vehicle, key, value)
            # commit the changes to the database
            db.commit()
            # refresh the vehicle instance with the updated data
            db.refresh(db_vehicle)
            # return the updated vehicle
            return db_vehicle
        except Exception as e:
            # raise an HTTP exception if there is a validation error
            raise HTTPException(status_code=422, detail=f"Validation Error: {str(e)}")
    # raise an HTTP exception if the vehicle is not found
    raise HTTPException(status_code=404, detail="Vehicle not found.")

# ==============================

# define a route to delete a specific vehicle by its ID
# this function handles DELETE requests to remove a vehicle from the database
@app.delete("/vehicles/{vehicle_id}", response_model=dict)
def delete_vehicle(vehicle_id: str, db: Session = Depends(get_db)):
    # query the database for the vehicle with the specified ID
    vehicle = db.query(VehicleDB).filter(VehicleDB.id == vehicle_id).first()
    if vehicle:
        # delete the vehicle from the database session
        db.delete(vehicle)
        # commit the changes to the database
        db.commit()
        # return a success message
        return {"message": f"Vehicle with id {vehicle_id} deleted."}
    # raise an HTTP exception if the vehicle is not found
    raise HTTPException(status_code=404, detail="Vehicle not found.")

# ==============================

# if this script is run directly (not imported as a module), start the FastAPI server
# this is the entry point of the application when running the script directly
if __name__ == "__main__":
    import uvicorn
    # run the FastAPI application on the local development server
    uvicorn.run(app, host="127.0.0.1", port=8000)
