# import necessary libraries
# requests is used to send HTTP requests to the API
# rich.console, rich.table, and rich.prompt are used for enhanced terminal output
# uuid is used for generating unique identifiers
import requests
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import uuid

# ==============================

# initialize the console for pretty printing
console = Console()

# ==============================

# function to generate a UUID string
# this generates a unique identifier for vehicles
def generate_uuid() -> str:
    return str(uuid.uuid4())

# ==============================

# base URL for the API endpoints
API_URL = "http://127.0.0.1:8000/vehicles"

# ==============================

# function to send HTTP requests to the API
# method: HTTP method (e.g., GET, POST, PUT, DELETE)
# endpoint: specific API endpoint (e.g., '/{vehicle_id}')
# data: payload for the request (e.g., vehicle details)
def send_request(method, endpoint="", data=None):
    url = f"{API_URL}{endpoint}"
    try:
                
        # send the HTTP request and get the response
        response = requests.request(method, url, json=data)
        response.raise_for_status()  # raise an error for unsuccessful requests
                
        # return the JSON content of the response
        return response.json()
    except requests.RequestException as e:
        # handle request errors
        console.print(f"[red]Request failed: {e}[/red]")
        console.print(f"[red]Response Content: {response.text if response else 'No response received'}[/red]")
        return None

# ==============================

# function to display a list of vehicles in a nicely formatted table
# vehicles: list of vehicle data to be displayed
def print_inventory(vehicles):
    # create a table with columns for vehicle attributes
    table = Table(title="Vehicle Inventory")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Make", style="magenta")
    table.add_column("Model", style="green")
    table.add_column("Year", style="yellow")
    table.add_column("Licence Plate", style="red")
    table.add_column("Colour", style="blue")
    table.add_column("Mileage", style="cyan")
    table.add_column("Available", style="magenta")
    table.add_column("Quantity", style="green")
    
    # add rows to the table for each vehicle
    for vehicle in vehicles:
        vehicle_id = vehicle.get('id', 'N/A')
        table.add_row(
            vehicle_id,
            vehicle.get('make', 'N/A'),
            vehicle.get('model', 'N/A'),
            str(vehicle.get('year', 'N/A')),
            vehicle.get('licence_plate', 'N/A'),
            vehicle.get('colour', 'N/A'),
            str(vehicle.get('mileage', 'N/A')),
            'Yes' if vehicle.get('available', False) else 'No',
            str(vehicle.get('quantity', 'N/A'))
        )
    
    # print the table to the console
    console.print(table)

# ==============================

# function to add a new vehicle
def add_vehicle():
    # prompt the user for vehicle details
    make = Prompt.ask("Enter make")
    model = Prompt.ask("Enter model")
    
    while True:
        try:
            year = int(Prompt.ask("Enter year", default="2023"))
            break
        except ValueError:
            console.print("[red]Invalid year, please enter a valid number.[/red]")

    licence_plate = Prompt.ask("Enter licence plate")
    colour = Prompt.ask("Enter colour")

    while True:
        try:
            mileage = int(Prompt.ask("Enter mileage", default="0"))
            break
        except ValueError:
            console.print("[red]Invalid mileage, please enter a valid number.[/red]")

    while True:
        try:
            quantity = int(Prompt.ask("Enter vehicle quantity", default="1"))
            break
        except ValueError:
            console.print("[red]Invalid quantity, please enter a valid number.[/red]")

    is_available = Prompt.ask("Is vehicle available? (yes/no)", choices=["yes", "no"]) == "yes"

    # prepare data for the POST request
    data = {
        "make": make,
        "model": model,
        "year": year,
        "licence_plate": licence_plate,
        "colour": colour,
        "mileage": mileage,
        "available": is_available,
        "quantity": quantity
    }

    # send the POST request to add the vehicle
    result = send_request('POST', '', data)

    if result and 'id' in result:
        console.print(f"[green]Vehicle with ID {result['id']} added successfully.[/green]")
    else:
        console.print("[red]Failed to add vehicle or response does not contain 'id'.[/red]")

# ==============================

# function to list all vehicles
def list_vehicles():
    # send a GET request to retrieve all vehicles
    vehicles = send_request("GET")
    if vehicles is not None:
        # print the list of vehicles in a table
        print_inventory(vehicles)
    else:
        console.print("[red]Failed to retrieve vehicles.[/red]")

# ==============================

# function to update an existing vehicle
def update_vehicle():
    # prompt the user for the vehicle ID
    vehicle_id = Prompt.ask("Enter the vehicle ID to update")

    if len(vehicle_id) != 36 or vehicle_id.count('-') != 4:
        console.print("[red]Invalid ID format. Please provide a valid UUID.[/red]")
        return

    data = {}

    # prompt for optional updates to vehicle attributes
    make = Prompt.ask("Enter new make (leave blank to keep current)")
    if make:
        data["make"] = make

    model = Prompt.ask("Enter new model (leave blank to keep current)")
    if model:
        data["model"] = model

    while True:
        year = Prompt.ask("Enter new year (leave blank to keep current)", default=None)
        if year:
            try:
                year = int(year)
                if year < 1900 or year > 2100:
                    raise ValueError("Year must be between 1900 and 2100.")
                data["year"] = year
                break
            except ValueError as e:
                console.print(f"[red]{e}[/red]")
        else:
            break

    licence_plate = Prompt.ask("Enter new licence plate (leave blank to keep current)")
    if licence_plate:
        data["licence_plate"] = licence_plate

    colour = Prompt.ask("Enter new colour (leave blank to keep current)")
    if colour:
        data["colour"] = colour

    while True:
        mileage = Prompt.ask("Enter new mileage (leave blank to keep current)", default=None)
        if mileage:
            try:
                mileage = int(mileage)
                if mileage < 0:
                    raise ValueError("Mileage must be a non-negative integer.")
                data["mileage"] = mileage
                break
            except ValueError as e:
                console.print(f"[red]{e}[/red]")
        else:
            break

    while True:
        quantity = Prompt.ask("Enter new quantity (leave blank to keep current)", default=None)
        if quantity:
            try:
                quantity = int(quantity)
                if quantity < 0:
                    raise ValueError("Quantity must be a non-negative integer.")
                data["quantity"] = quantity
                break
            except ValueError as e:
                console.print(f"[red]{e}[/red]")
        else:
            break

    is_available = Prompt.ask("Is vehicle available? (yes/no, leave blank to keep current)", choices=["yes", "no"], default=None)
    if is_available:
        data["available"] = is_available == "yes"

    # send the PUT request to update the vehicle
    result = send_request('PUT', f'/{vehicle_id}', data)

    if result:
        console.print(f"[green]Vehicle with ID {vehicle_id} updated successfully.[/green]")
    else:
        console.print("[red]Failed to update vehicle.[/red]")

# ==============================

# function to delete a vehicle
def delete_vehicle():
    # prompt the user for the vehicle ID to delete
    vehicle_id = Prompt.ask("Enter the vehicle ID to delete")
    
    if len(vehicle_id) != 36 or vehicle_id.count('-') != 4:
        console.print("[red]Invalid ID format. Please provide a valid UUID.[/red]")
        return

    # send the DELETE request to remove the vehicle
    result = send_request('DELETE', f'/{vehicle_id}')
    if result is None:
        console.print("[red]Failed to delete vehicle or vehicle not found.[/red]")
    else:
        console.print(f"[green]Vehicle with ID {vehicle_id} deleted successfully.[/green]")

# ==============================

# function to display the main menu and handle user choices
def main_menu():
    while True:
        # print the main menu options
        console.print("\n[bold]Vehicle Management System[/bold]")
        console.print("1. List vehicles")
        console.print("2. Add vehicle")
        console.print("3. Update vehicle")
        console.print("4. Delete vehicle")
        console.print("5. Exit")
        choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4", "5"])
        
        # handle user choice
        if choice == "1":
            list_vehicles()
        elif choice == "2":
            add_vehicle()
        elif choice == "3":
            update_vehicle()
        elif choice == "4":
            delete_vehicle()
        elif choice == "5":
            console.print("[bold green]Exiting the program.[/bold green]")
            break

# ==============================

# run the main menu function if this script is executed directly
if __name__ == "__main__":
    main_menu()
