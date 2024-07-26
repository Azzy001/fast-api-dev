import rich
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import random

# --------------------

# create a Console object for rich output
console = Console()

# define the Vehicle class
class Vehicle:
    # initialize the Vehicle object with attributes
    def __init__(self, id, make, model, year, licence_plate, colour, mileage, isAvailable, quantity):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.licence_plate = licence_plate
        self.colour = colour
        self.mileage = mileage
        self.isAvailable = isAvailable
        self.quantity = quantity

    # method to convert the Vehicle object to a dictionary
    def to_dict(self):
        return {
            "id": self.id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "licence_plate": self.licence_plate,
            "colour": self.colour,
            "mileage": self.mileage,
            "isAvailable": self.isAvailable,
            "quantity": self.quantity,
        }

# --------------------

# function to print the inventory of vehicles
def print_inventory(vehicles):
    # create a Table object for structured display
    table = Table(show_header=True, header_style="bold magenta", show_lines=True)

    # add columns to the table with appropriate justification
    table.add_column("ID", justify="left")
    table.add_column("Make", justify="left")
    table.add_column("Model", justify="left")
    table.add_column("Year", justify="right")
    table.add_column("Licence Plate", justify="left")
    table.add_column("Colour", justify="left")
    table.add_column("Mileage", justify="right")
    table.add_column("Available", justify="center")
    table.add_column("Quantity", justify="right")

    # iterate through the list of vehicles
    for vehicle in vehicles:
        # convert the vehicle object to a dictionary
        vehicle_dict = vehicle.to_dict()
        # add a row to the table with vehicle data
        table.add_row(
            str(vehicle_dict["id"]),
            str(vehicle_dict["make"]),
            str(vehicle_dict["model"]),
            str(vehicle_dict["year"]),
            str(vehicle_dict["licence_plate"]),
            str(vehicle_dict["colour"]),
            str(vehicle_dict["mileage"]),
            "Yes" if vehicle_dict["isAvailable"] else "No",
            str(vehicle_dict["quantity"]),
        )
    # print the table to the console
    console.print(table)

# --------------------

# function to display the menu and get user choice
def display_menu():
    # display the menu options
    console.print("\n----- [bold cyan]Vehicle Inventory System[/bold cyan] -----", style="bold green")
    console.print("Please choose an option:", style="bold yellow")
    console.print("1. View Inventory")
    console.print("2. Add to Inventory")
    console.print("3. Edit Inventory")
    console.print("4. Delete from Inventory")
    console.print("5. Exit System")
    
    try:
        # get user choice with validation
        choice = Prompt.ask("\nSelect an option:", choices=["1", "2", "3", "4", "5"], default="1")
        return int(choice)
    except ValueError:
        # handle invalid input
        console.print("[red]Invalid choice, please enter a number between 1 and 5.[/red]")
        return None

# --------------------

def add_vehicle(vehicles):
    # generate a unique ID for the new vehicle
    id = str(random.randint(10000, 99999))
    make = Prompt.ask("Enter make")
    model = Prompt.ask("Enter model")
    
    # validate year input
    while True:
        try:
            year = int(Prompt.ask("Enter year", default="2023"))
            break
        except ValueError:
            console.print("[red]Invalid year, please enter a valid number.[/red]")

    licence_plate = Prompt.ask("Enter licence plate")
    colour = Prompt.ask("Enter colour")

    # validate mileage input
    while True:
        try:
            mileage = int(Prompt.ask("Enter mileage", default="0"))
            break
        except ValueError:
            console.print("[red]Invalid mileage, please enter a valid number.[/red]")

    # validate quantity input
    while True:
        try:
            quantity = int(Prompt.ask("Enter vehicle quantity", default="1"))
            break
        except ValueError:
            console.print("[red]Invalid quantity, please enter a valid number.[/red]")

    # handle availability input
    isAvailable = Prompt.ask("Is vehicle available? (yes/no)", choices=["yes", "no"]) == "yes"

    # create a new vehicle object and add it to the list
    new_vehicle = Vehicle(id, make, model, year, licence_plate, colour, mileage, isAvailable, quantity)
    vehicles.append(new_vehicle)
    console.print(f"[green]Vehicle with ID {id} added successfully.[/green]")

# --------------------

def edit_vehicle(vehicles):
    # prompt user to enter the ID of the vehicle to be edited
    choice = Prompt.ask("Enter vehicle ID to edit")

    # initialize vehicle_to_edit to None
    vehicle_to_edit = None

    # search for the vehicle in the list
    for vehicle in vehicles:
        if choice == vehicle.id:
            vehicle_to_edit = vehicle
            break
    
    if vehicle_to_edit:
        # vehicle found, display its current details
        console.print("\n[bold cyan]Current Vehicle Details:[/bold cyan]", style="bold green")
        console.print(f"ID: {vehicle_to_edit.id}")
        console.print(f"Make: {vehicle_to_edit.make}")
        console.print(f"Model: {vehicle_to_edit.model}")
        console.print(f"Year: {vehicle_to_edit.year}")
        console.print(f"Licence Plate: {vehicle_to_edit.licence_plate}")
        console.print(f"Colour: {vehicle_to_edit.colour}")
        console.print(f"Mileage: {vehicle_to_edit.mileage}")
        console.print(f"Available: {'Yes' if vehicle_to_edit.isAvailable else 'No'}")
        console.print(f"Quantity: {vehicle_to_edit.quantity}")

        # prompt user for new details
        console.print("\n[bold cyan]Enter new details (leave blank to keep current value):[/bold cyan]")

        # get new values for each attribute, or keep the old value if left blank
        make = Prompt.ask("Enter make", default=vehicle_to_edit.make)
        model = Prompt.ask("Enter model", default=vehicle_to_edit.model)

        while True:
            try:
                year = Prompt.ask("Enter year", default=str(vehicle_to_edit.year))
                year = int(year)
                break
            except ValueError:
                console.print("[red]Invalid year, please enter a valid number.[/red]")

        licence_plate = Prompt.ask("Enter licence plate", default=vehicle_to_edit.licence_plate)
        colour = Prompt.ask("Enter colour", default=vehicle_to_edit.colour)

        while True:
            try:
                mileage = Prompt.ask("Enter mileage", default=str(vehicle_to_edit.mileage))
                mileage = int(mileage)
                break
            except ValueError:
                console.print("[red]Invalid mileage, please enter a valid number.[/red]")

        while True:
            try:
                quantity = Prompt.ask("Enter vehicle quantity", default=str(vehicle_to_edit.quantity))
                quantity = int(quantity)
                break
            except ValueError:
                console.print("[red]Invalid quantity, please enter a valid number.[/red]")

        isAvailable = Prompt.ask("Is vehicle available? (yes/no)", choices=["yes", "no"], default="yes") == "yes"

        # update the vehicle's attributes
        vehicle_to_edit.make = make
        vehicle_to_edit.model = model
        vehicle_to_edit.year = year
        vehicle_to_edit.licence_plate = licence_plate
        vehicle_to_edit.colour = colour
        vehicle_to_edit.mileage = mileage
        vehicle_to_edit.isAvailable = isAvailable
        vehicle_to_edit.quantity = quantity

        console.print(f"[green]Vehicle with ID {choice} has been updated successfully.[/green]")
    else:
        # vehicle not found
        console.print("[red]Vehicle with the given ID not found.[/red]")

# --------------------     

def delete_vehicle(vehicles):
    # prompt the user to enter the id of the vehicle to be removed
    choice = Prompt.ask("Enter vehicle id to remove")
    # search for the vehicle in the list
    vehicle_to_remove = None
    for vehicle in vehicles:
        if choice == vehicle.id:
            vehicle_to_remove = vehicle
    
    if vehicle_to_remove:
        # vehicle found, display its details
        console.print("\n[bold cyan]Vehicle found:[/bold cyan]", style="bold green")
        console.print(f"ID: {vehicle_to_remove.id}")
        console.print(f"Make: {vehicle_to_remove.make}")
        console.print(f"Model: {vehicle_to_remove.model}")
        console.print(f"Year: {vehicle_to_remove.year}")
        console.print(f"Licence Plate: {vehicle_to_remove.licence_plate}")
        console.print(f"Colour: {vehicle_to_remove.colour}")
        console.print(f"Mileage: {vehicle_to_remove.mileage}")
        console.print(f"Available: {'Yes' if vehicle_to_remove.isAvailable else 'No'}")
        console.print(f"Quantity: {vehicle_to_remove.quantity}")

        # ask user for confirmation to delete
        confirm = Prompt.ask("Do you want to delete this vehicle? (yes/no)", choices=["yes", "no"])
        if confirm == "yes":
            vehicles.remove(vehicle_to_remove)
            console.print(f"[green]Vehicle with ID {choice} has been removed successfully.[/green]")
        else:
            console.print("[yellow]Deletion cancelled.[/yellow]")
    else:
        # vehicle not found
        console.print("[red]Vehicle with the given ID not found.[/red]")

# --------------------

# entry point of the script
if __name__ == "__main__":
    # initialize an empty list of vehicle objects
    vehicles = []

    # main loop to display the menu and handle user choices
    while True:
        choice = display_menu()
        if choice == 1:
            # view the current inventory
            print_inventory(vehicles)
        elif choice == 2:
            # add a new vehicle to the inventory
            add_vehicle(vehicles)
        elif choice == 3:
            # edit existing vehicles
            edit_vehicle(vehicles)
        elif choice == 4:
            # delete a vehicle from the inventory
            delete_vehicle(vehicles)
        elif choice == 5:
            # exit the system
            console.print("[bold green]Exiting system.[/bold green]")
            break
        else:
            # handle invalid choice
            console.print("[red]Invalid choice, try again.[/red]")
