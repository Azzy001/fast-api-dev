import requests
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import uuid
import base64

# Initialize the console
console = Console()

# Base64 utility functions
def encode_id(vehicle_id: str) -> str:
    id_bytes = uuid.UUID(vehicle_id).bytes
    encoded_id = base64.urlsafe_b64encode(id_bytes).decode('utf-8').rstrip('=')
    return encoded_id

def decode_id(encoded_id: str) -> str:
    padded_encoded_id = encoded_id + '=' * (-len(encoded_id) % 4)
    id_bytes = base64.urlsafe_b64decode(padded_encoded_id)
    decoded_id = str(uuid.UUID(bytes=id_bytes))
    return decoded_id

# API base URL
API_URL = "http://127.0.0.1:8000/vehicles"

def send_request(method, endpoint="", data=None):
    url = f"{API_URL}{endpoint}"
    response = requests.request(method, url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def print_inventory(vehicles):
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
    
    for vehicle in vehicles:
        encoded_id = encode_id(vehicle.get('id', 'N/A'))
        table.add_row(
            encoded_id,
            vehicle.get('make', 'N/A'),
            vehicle.get('model', 'N/A'),
            str(vehicle.get('year', 'N/A')),
            vehicle.get('licence_plate', 'N/A'),
            vehicle.get('colour', 'N/A'),
            str(vehicle.get('mileage', 'N/A')),
            'Yes' if vehicle.get('available', False) else 'No',
            str(vehicle.get('quantity', 'N/A'))
        )
    
    console.print(table)

def add_vehicle():
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

    result = send_request('POST', '', data)
    console.print(f"[blue]API Response: {result}[/blue]")

    if result and 'id' in result:
        encoded_id = encode_id(result['id'])
        console.print(f"[green]Vehicle with ID {encoded_id} added successfully.[/green]")
    else:
        console.print("[red]Failed to add vehicle or response does not contain 'id'.[/red]")

# List vehicles
def list_vehicles():
    vehicles = send_request("GET")
    if vehicles is not None:
        print_inventory(vehicles)
    else:
        console.print("[red]Failed to retrieve vehicles.[/red]")


def update_vehicle():
    vehicle_id = Prompt.ask("Enter the vehicle ID to update")
    decoded_id = decode_id(vehicle_id)
    
    make = Prompt.ask("Enter new make (leave blank to keep current)")
    model = Prompt.ask("Enter new model (leave blank to keep current)")
    
    while True:
        try:
            year = Prompt.ask("Enter new year (leave blank to keep current)", default=None)
            year = int(year) if year else None
            break
        except ValueError:
            console.print("[red]Invalid year, please enter a valid number.[/red]")

    licence_plate = Prompt.ask("Enter new licence plate (leave blank to keep current)")
    colour = Prompt.ask("Enter new colour (leave blank to keep current)")

    while True:
        try:
            mileage = Prompt.ask("Enter new mileage (leave blank to keep current)", default=None)
            mileage = int(mileage) if mileage else None
            break
        except ValueError:
            console.print("[red]Invalid mileage, please enter a valid number.[/red]")

    while True:
        try:
            quantity = Prompt.ask("Enter new quantity (leave blank to keep current)", default=None)
            quantity = int(quantity) if quantity else None
            break
        except ValueError:
            console.print("[red]Invalid quantity, please enter a valid number.[/red]")

    is_available = Prompt.ask("Is vehicle available? (yes/no, leave blank to keep current)", choices=["yes", "no"], default=None)
    is_available = is_available == "yes" if is_available else None

    data = {
        "make": make if make else None,
        "model": model if model else None,
        "year": year,
        "licence_plate": licence_plate if licence_plate else None,
        "colour": colour if colour else None,
        "mileage": mileage,
        "available": is_available,
        "quantity": quantity
    }

    result = send_request('PUT', f'/{decoded_id}', data)
    console.print(f"[blue]API Response: {result}[/blue]")

    if result:
        encoded_id = encode_id(result['id'])
        console.print(f"[green]Vehicle with ID {encoded_id} updated successfully.[/green]")
    else:
        console.print("[red]Failed to update vehicle.[/red]")

def delete_vehicle():
    vehicle_id = Prompt.ask("Enter the vehicle ID to delete")
    decoded_id = decode_id(vehicle_id)

    result = send_request('DELETE', f'/{decoded_id}')
    console.print(f"[blue]API Response: {result}[/blue]")

    if result is None:
        console.print("[red]Failed to delete vehicle or vehicle not found.[/red]")
    else:
        console.print(f"[green]Vehicle with ID {encode_id(decoded_id)} deleted successfully.[/green]")

def main_menu():
    while True:
        console.print("\n[bold]Vehicle Management System[/bold]")
        console.print("1. List vehicles")
        console.print("2. Add vehicle")
        console.print("3. Update vehicle")
        console.print("4. Delete vehicle")
        console.print("5. Exit")
        choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4", "5"])
        
        if choice == "1":
            list_vehicles()
        elif choice == "2":
            add_vehicle()
        elif choice == "3":
            update_vehicle()
        elif choice == "4":
            delete_vehicle()
        elif choice == "5":
            console.print("[bold green]Exiting...[/bold green]")
            break

if __name__ == "__main__":
    try:
        print("Starting Vehicle Management UI...")
        main_menu()
    except Exception as e:
        print(f"An error occurred: {e}")
