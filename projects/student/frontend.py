import tkinter as tk
from tkinter import ttk
import requests

# Define the base URL for the API endpoints
base_url = "http://127.0.0.1:8000/students/"

def fetch_students():
    """
    Fetch all students from the FastAPI backend.
    - Sends a GET request to the /students/ endpoint.
    - Returns the list of students in JSON format.
    """
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Students fetched successfully")
        return response.json()  # Return the list of students
    except requests.RequestException as e:
        print(f"Error fetching students: {e}")
        return []

# Create the main application window
root = tk.Tk()
root.title("Student Management System")

# Create a frame for displaying students
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create a Treeview widget for displaying the list of students
tree = ttk.Treeview(frame, columns=("ID", "First Name", "Last Name", "Email"), show='headings')
tree.heading("ID", text="ID")
tree.heading("First Name", text="First Name")
tree.heading("Last Name", text="Last Name")
tree.heading("Email", text="Email")
tree.grid(row=0, column=0, sticky=(tk.W, tk.E))

def load_students():
    """
    Load students from the FastAPI backend and display them in the Treeview.
    """
    # Clear existing items in the Treeview
    for item in tree.get_children():
        tree.delete(item)
    
    students = fetch_students()
    if not students:
        print("No students data to display.")
    for student in students:
        tree.insert("", tk.END, values=(student["id"], student["firstName"], student["lastName"], student["email"]))

# Load students on application start
load_students()

# Create a button to refresh the student list
refresh_button = ttk.Button(frame, text="Refresh", command=load_students)
refresh_button.grid(row=1, column=0, pady="10")

# Run the Tkinter event loop
root.mainloop()
