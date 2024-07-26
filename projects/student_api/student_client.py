import requests

# Define the base URL for the API endpoints
base_url = "http://127.0.0.1:8000/students/"

def create_student(student_data):
    """
    Function to create a new student record.
    - student_data: A dictionary with student details.
    - Sends a POST request to the API with the student data.
    - Returns the response from the API as a Python dictionary.
    """
    # Send POST request to create a student
    response = requests.post(base_url, json=student_data)
    # Convert the API response to JSON and return it
    return response.json()

def get_all_students():
    """
    Function to retrieve all student records.
    - Sends a GET request to the API to fetch all students.
    - Returns the response from the API as a Python dictionary.
    """
    # Send GET request to retrieve all students
    response = requests.get(base_url)
    # Convert the API response to JSON and return it
    return response.json()

def get_student(student_id):
    """
    Function to retrieve a specific student by their ID.
    - student_id: The ID of the student to retrieve.
    - Sends a GET request to the API with the student's ID.
    - Returns the response from the API as a Python dictionary.
    """
    # Send GET request to retrieve a specific student
    response = requests.get(f"{base_url}{student_id}")
    # Convert the API response to JSON and return it
    return response.json()

def update_student(student_id, student_data):
    """
    Function to update a student's record.
    - student_id: The ID of the student to update.
    - student_data: A dictionary with updated student details.
    - Sends a PUT request to the API with the updated student data.
    - Returns the response from the API as a Python dictionary.
    """
    # Send PUT request to update student data
    response = requests.put(f"{base_url}{student_id}", json=student_data)
    # Convert the API response to JSON and return it
    return response.json()

def delete_student(student_id):
    """
    Function to delete a student record by their ID.
    - student_id: The ID of the student to delete.
    - Sends a DELETE request to the API with the student's ID.
    - Returns the response from the API as a Python dictionary.
    """
    # Send DELETE request to delete the student
    response = requests.delete(f"{base_url}{student_id}")
    # Convert the API response to JSON and return it
    return response.json()

# Example usage of the functions:
# Define the details of a student to be created
student_data = {
    "id": "1", 
    "firstName": "John",
    "middleName": "Doe",
    "lastName": "Smith",
    # Date of birth in YYYY-MM-DD format
    "dateOfBirth": "2000-01-01",  
    "phoneNumber": "1234567890",
    "email": "john@example.com",
    "module": "math",
    "enrollmentDate": "2022-09-01"
}

# Create a new student
print("Creating student...")
# Print the response from the API after creating the student
print(create_student([student_data]))

# Get and print all student records
print("Getting all students...")
# Print the list of all students
print(get_all_students())

# Get and print the student with ID 1
print("Getting student with ID 1...")
# Print the details of the student with ID 1
print(get_student("1"))

# Update the student details
print("Updating student...")
# Make a copy of the student data
updated_data = student_data.copy()
# Change the first name to "Jane"
updated_data["firstName"] = "Jane"
# Print the response from the API after updating the student
print(update_student("1", updated_data))

# Delete the student with ID 1
print("Deleting student...")
# Print the response from the API after deleting the student
print(delete_student("1"))

# Get and print all student records after deletion
print("Getting all students after deletion...")
# Print the list of all students after deletion to show that the student was removed
print(get_all_students())
