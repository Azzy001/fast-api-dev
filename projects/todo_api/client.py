import requests

# Base URL for the API endpoints
# This is the address where the server is listening for requests.
base_url = "http://127.0.0.1:8000/todolist/"

def create_list(list_data):
    """
    Send a POST request to create a batch of to-do lists.
    """
    response = requests.post(base_url, json=list_data)
    return response.json()

def get_all_lists():
    """
    Send a GET request to retrieve all to-do lists.
    """
    response = requests.get(base_url)
    return response.json()

def get_list(lst_id):
    """
    Send a GET request to retrieve a specific to-do list by ID.
    """
    response = requests.get(f"{base_url}{lst_id}")
    return response.json()

def update_to_do_list(lst_id, list_data):
    """
    Send a PUT request to update a specific to-do list by ID.
    """
    response = requests.put(f"{base_url}{lst_id}", json=list_data)
    return response.json()

def delete_to_do_list(lst_id):
    """
    Send a DELETE request to remove a specific to-do list by ID.
    """
    response = requests.delete(f"{base_url}{lst_id}")
    return response.json()

# Example data for testing
example_list_data = [
    {
        "id": "1",
        "title": "Task 1",
        "description": "Description for Task 1",
        "due_date": "2024-07-24",
        "status": "pending",
        "priority": "medium",
        "creation_date": "2024-07-23"
    }
]

# Test API functions
# The following lines of code test the functions to ensure they are working as expected.

print("Creating list...")
# Calls the function to create a new to-do item and prints the response from the server.
print(create_list(example_list_data))

print("Getting all lists...")
print(get_all_lists())

print("Getting list with ID 1...")
print(get_list("1"))

# Make a copy of the first item in the example list
# This creates a duplicate of the to-do item so we can make changes without altering the original data.
updated_list_data = example_list_data[0].copy()

# Update the title of the copied to-do item
# This changes the title of the copied item to "Updated Task 1".
updated_list_data["title"] = "Updated Task 1"

print("Updating list...")
print(update_to_do_list("1", updated_list_data))

print("Deleting list...")
print(delete_to_do_list("1"))

print("Getting all lists after deletion...")
print(get_all_lists())


"""
# Test POST request
curl -X POST http://127.0.0.1:8000/todolist/ \
     -H "Content-Type: application/json" \
     -d '[{
           "id": "1",
           "title": "Task 1",
           "description": "Description for Task 1",
           "due_date": "2024-07-24",
           "status": "pending",
           "priority": "medium",
           "creation_date": "2024-07-23"
         }]'

# Test GET request
curl -X GET http://127.0.0.1:8000/todolist/ \
     -H "Content-Type: application/json"
"""