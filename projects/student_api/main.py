from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Dict
import datetime
import logging

# Initialize the FastAPI application
# This creates a new FastAPI application instance
app = FastAPI()

# -------------------------

# Configure logging
# Set up logging to capture information, errors, etc.
logging.basicConfig(level=logging.INFO)

# -------------------------

# Define the Student model using Pydantic
class Student(BaseModel):
    id: str
    firstName: str
    middleName: str  
    lastName: str
    # Date of birth in YYYY-MM-DD format
    dateOfBirth: datetime.date
    phoneNumber: str
    email: EmailStr
    module: str
    enrollmentDate: datetime.date

# -------------------------

# In-memory storage for student records
# This dictionary will store student records. The key is the student ID.
students_db: Dict[str, Student] = {}  

# -------------------------

# Endpoint to create a batch of students
@app.post("/students/", response_model=List[Student])
def create_students_batch(students: List[Student]):
    """
    Create a batch of new students.
    - Accepts a list of students.
    - Checks if each student's ID already exists.
    - If not, adds the student to the in-memory database.
    - Returns the list of created students.
    """
    # List to keep track of students successfully created
    created_students = []  
    for student in students:
        if student.id in students_db:
            # Log an error if ID already exists
            logging.error(f"Student ID {student.id} already exists.")
            # Return error response
            raise HTTPException(status_code=400, detail=f"Student ID {student.id} already exists.")
        # Add student to in-memory database
        students_db[student.id] = student
        # Add to the list of created students
        created_students.append(student)
        # Log successful creation
        logging.info(f"Created student with ID {student.id}")
    # Return the list of created students
    return created_students

# -------------------------

# Endpoint to get all students
@app.get("/students/", response_model=List[Student])
def get_students():
    """
    Retrieve all students from the in-memory database.
    - Returns a list of all students.
    """
    # Log the number of students being retrieved
    logging.info(f"Retrieving all students. Total count: {len(students_db)}")
    # Return all students as a list
    return list(students_db.values())

# -------------------------

# Endpoint to get a specific student by ID
@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: str):
    """
    Retrieve a specific student by their ID.
    - Returns the student with the matching ID.
    - If the student ID does not exist, returns a 404 error.
    """
    # Log the request to retrieve a student
    logging.info(f"Retrieving student with ID {student_id}")
    if student_id in students_db:
        # Return the student if found
        return students_db[student_id]
    else:
        # Log an error if the student is not found
        logging.error(f"Student with ID {student_id} not found.")
        # Return a 404 error response
        raise HTTPException(status_code=404, detail="Student not found.")

# -------------------------

# Endpoint to update an existing student's information
@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: str, student: Student):
    """
    Update an existing student's information.
    - If the student ID exists, update the student's details.
    - Returns the updated student information.
    - If the student ID does not exist, returns a 404 error.
    """
    # Log the request to update a student
    logging.info(f"Updating student with ID {student_id}")
    if student_id in students_db:
        # Update the student record
        students_db[student_id] = student
        # Return the updated student
        return student
    else:
        # Log an error if the student is not found
        logging.error(f"Student with ID {student_id} not found.")
        # Return a 404 error response
        raise HTTPException(status_code=404, detail="Student not found.")

# -------------------------

# Endpoint to delete a student from the database
@app.delete("/students/{student_id}", response_model=Student)
def delete_student(student_id: str):
    """
    Delete a student by their ID.
    - Removes the student with the matching ID from the database.
    - Returns the deleted student's information.
    - If the student ID does not exist, returns a 404 error.
    """
    # Log the request to delete a student
    logging.info(f"Deleting student with ID {student_id}")
    if student_id in students_db:
        # Remove and return the student if found
        return students_db.pop(student_id)
    else:
        # Log an error if the student is not found
        logging.error(f"Student with ID {student_id} not found.")
        # Return a 404 error response
        raise HTTPException(status_code=404, detail="Student not found.")

# -------------------------

# Entry point to run the FastAPI application
if __name__ == "__main__":
    # Uvicorn is an ASGI server for running FastAPI applications
    import uvicorn
    # Run the FastAPI application on localhost:8000
    uvicorn.run(app, host="127.0.0.1", port=8000)
