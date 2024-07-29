# import necessary functions and classes from SQLAlchemy
# SQLAlchemy is used to interact with databases in Python
from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ==============================

# URL for connecting to the database
# we're using SQLite, a lightweight database, for simplicity
DATABASE_URL = "sqlite:///./vehicle.db"

# create an engine that connects to the SQLite database
# the engine is the starting point for any SQLAlchemy application
engine = create_engine(DATABASE_URL)

# create a session maker to handle database transactions
# this session maker will be used to create new database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create a base class for declarative class definitions
# this base class maintains a catalog of classes and tables relative to that base
Base = declarative_base()

# ==============================

# define a class representing the 'vehicles' table in the database
# this class will be used to map the 'vehicles' table in the database
class VehicleDB(Base):
    # specify the table name in the database
    __tablename__ = "vehicles"
    
    # define columns in the 'vehicles' table
    # each attribute in this class represents a column in the table
    id = Column(String, primary_key=True, index=True)
    make = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer, index=True)
    licence_plate = Column(String, index=True)
    colour = Column(String, index=True)
    mileage = Column(Integer, index=True)
    available = Column(Boolean, default=True)
    quantity = Column(Integer, default=1)

# ==============================

# function to initialize the database
# this function creates all tables defined in the Base metadata
def init_db():
    Base.metadata.create_all(bind=engine)

# ==============================

# function to get a database session
# this function provides a new database session to interact with the database
def get_db():
    # create a new database session
    db = SessionLocal()
    try:
        # yield the session to be used by other functions
        # 'yield' allows the session to be used in a context manager
        yield db
    finally:
        # close the session when done
        # this ensures that the session is properly closed and resources are released
        db.close()
