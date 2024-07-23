import requests

# Define the base URL for the API endpoints
# This URL is where the FastAPI application is running
base_url = "http://127.0.0.1:8000/todolist/"

# --------------------

def create_list(list_data):
    """
    Send a POST request to create a batch of to-do lists.
    
    Args:
    - list_data: A list of dictionaries containing to-do list data.
    
    Returns:
    - The JSON response from the server, which typically contains the created to-do lists.
    """
    # Send a POST request to the base URL with the provided list_data as JSON
    response = requests.post(base_url, json=list_data)
    # Return the JSON content of the response
    return response.json()

# --------------------

def get_all_lists():
    """
    Send a GET request to retrieve all to-do lists.
    
    Returns:
    - The JSON response from the server, which typically contains all the to-do lists.
    """
    # Send a GET request to the base URL
    response = requests.get(base_url)
    # Return the JSON content of the response
    return response.json()

# --------------------

def get_list(lst_id):
    """
    Send a GET request to retrieve a specific to-do list by ID.
    
    Args:
    - lst_id: The ID of the to-do list to retrieve.
    
    Returns:
    - The JSON response from the server, which typically contains the specified to-do list.
    """
    # Send a GET request to the URL with the specific list ID
    response = requests.get(f"{base_url}{lst_id}")
    # Return the JSON content of the response
    return response.json()

# --------------------

def update_to_do_list(lst_id, list_data):
    """
    Send a PUT request to update a specific to-do list by ID.
    
    Args:
    - lst_id: The ID of the to-do list to update.
    - list_data: A dictionary containing the updated to-do list data.
    
    Returns:
    - The JSON response from the server, which typically contains the updated to-do list.
    """
    # Send a PUT request to the URL with the specific list ID and the updated data as JSON
    response = requests.put(f"{base_url}{lst_id}", json=list_data)
    # Return the JSON content of the response
    return response.json()

# --------------------

def delete_to_do_list(lst_id):
    """
    Send a DELETE request to remove a specific to-do list by ID.
    
    Args:
    - lst_id: The ID of the to-do list to delete.
    
    Returns:
    - The JSON response from the server, which typically contains the deleted to-do list.
    """
    # Send a DELETE request to the URL with the specific list ID
    response = requests.delete(f"{base_url}{lst_id}")
    # Return the JSON content of the response
    return response.json()

# --------------------

# Example data for testing
# This is a sample list of to-do list data used for testing the API endpoints
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

# --------------------

# Create a new to-do list
# Call the create_list function with example_list_data and print the response
print("Creating list...")
print(create_list(example_list_data))

# Retrieve all to-do lists
# Call the get_all_lists function and print the response
print("Getting all lists...")
print(get_all_lists())

# Retrieve a specific to-do list by ID
# Call the get_list function with the ID "1" and print the response
print("Getting list with ID 1...")
print(get_list("1"))

# Update a to-do list
# Create updated data by modifying the title and call the update_to_do_list function
updated_list_data = example_list_data[0].copy()
updated_list_data["title"] = "Updated Task 1"
print("Updating list...")
print(update_to_do_list("1", updated_list_data))

# Delete a to-do list
# Call the delete_to_do_list function with the ID "1" and print the response
print("Deleting list...")
print(delete_to_do_list("1"))

# Retrieve all to-do lists after deletion
# Call the get_all_lists function again to confirm deletion and print the response
print("Getting all lists after deletion...")
print(get_all_lists())
