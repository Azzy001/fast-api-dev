import tkinter as tk
from tkinter import ttk
import requests

# Base URL for the API endpoint
base_url = "http://127.0.0.1:8000/vehicles"

# Create the main application window
window = tk.Tk()
# Set the window title
window.title("Vehicle Management System")

# Create a frame to hold the Treeview widget and scrollbars
# Padding around the frame
frame = ttk.Frame(window, padding="10")
# Place frame in the grid and make it expand in all directions
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# ----- fetch vehicles --------------->

# Function to fetch and display vehicles from the API
def fetch_vehicles():
    # Make a GET request to fetch data from the API
    response = requests.get(base_url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON into a Python list
        vehicles = response.json()
        # Iterate through each vehicle record
        for vehicle in vehicles:
            # Insert each vehicle's data into the Treeview
            tree.insert('', 'end', values=(
                vehicle['id'], vehicle['make'], vehicle['model'],
                vehicle['year'], vehicle['license_plate'],
                vehicle['color'], vehicle['mileage'], vehicle['status']
            ))

# ----- load system ---------------->

def load_vehicles():
    """"""
    # clear existing items in the Treeview
    for item in tree.get_children():
        tree.delete(item)
    
    vehicles = fetch_vehicles()
    if not vehicles:
        print("No vehicles data to display.")
    for vehicle in vehicles:
        tree.insert('', 'end', values=(
                vehicle['id'], vehicle['make'], vehicle['model'],
                vehicle['year'], vehicle['license_plate'],
                vehicle['color'], vehicle['mileage'], vehicle['status']
            ))


# Define the columns for the Treeview widget
columns = ("ID", "Make", "Model", "Year", "License Plate", "Color", "Mileage", "Status")

# Create a Treeview widget to display the list of vehicles
tree = ttk.Treeview(frame, columns=columns, show="headings")

# Set column headings and widths
# Define the width for each column to ensure they are visible
column_widths = {
    "ID": 100,
    "Make": 120,
    "Model": 120,
    "Year": 80,
    "License Plate": 150,
    "Color": 100,
    "Mileage": 100,
    "Status": 100
}

# Iterate through each column to configure the headings and widths
for col in columns:
    # Set the heading text for the column
    tree.heading(col, text=col)
    # Set the width and alignment for the column
    tree.column(col, width=column_widths[col], anchor=tk.CENTER)

# Add a vertical scrollbar to the frame
# Create scrollbar for vertical scrolling
vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
# Link scrollbar with Treeview's yview
tree.configure(yscrollcommand=vsb.set)
# Place the scrollbar in the grid
vsb.grid(row=0, column=1, sticky=(tk.N, tk.S))

# Add a horizontal scrollbar to the frame
# Create scrollbar for horizontal scrolling
hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
# Link scrollbar with Treeview's xview
tree.configure(xscrollcommand=hsb.set)
# Place the scrollbar in the grid
hsb.grid(row=1, column=0, sticky=(tk.W, tk.E))

# Position the Treeview widget in the frame
# Place Treeview in the grid and make it expand in all directions
tree.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))

# Configure the frame to expand with the window
# Allow the row containing the Treeview to expand
frame.grid_rowconfigure(0, weight=1)
# Allow the column containing the Treeview to expand
frame.grid_columnconfigure(0, weight=1)



# Fetch vehicles when the application starts
# fetch_vehicles()

# Run the Tkinter event loop to keep the application running
window.mainloop()
