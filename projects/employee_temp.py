from tkinter import *
from tkinter import messagebox

class EmployeeApp:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        master.geometry("1400x800")
        # make the window non-resizable
        master.resizable(0, 0)
        # set the title of the window
        master.title("Employee Database")
        # keep the window on top
        master.attributes("-topmost", True)

        # configure grid layout for the master window
        master.columnconfigure(2, weight=1)
        master.rowconfigure(3, weight=1)

        # define light grey color for borders
        light_grey = "#C0C0C0"

        # ====================

        # personal information frame
        self.personal_frame = Frame(master, relief="solid", highlightbackground=light_grey, highlightthickness=1)
        self.personal_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # personal frame title
        self.personal_title_label = Label(self.personal_frame, text="Employee Information", font=("Arial", 10))
        self.personal_title_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        # first Name
        self.first_name_label = Label(self.personal_frame, text="First Name:", font=("Arial", 10))
        self.first_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.first_name_entry = Entry(self.personal_frame, font=("Arial", 10))
        self.first_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="e")

        # last Name
        self.last_name_label = Label(self.personal_frame, text="Last Name:", font=("Arial", 10))
        self.last_name_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.last_name_entry = Entry(self.personal_frame, font=("Arial", 10))
        self.last_name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="e")

        # date of Birth
        self.dob_label = Label(self.personal_frame, text="Date of Birth:", font=("Arial", 10))
        self.dob_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.dob_entry = Entry(self.personal_frame, font=("Arial", 10))
        self.dob_entry.grid(row=3, column=1, padx=10, pady=5, sticky="e")

        # gender
        self.gender_label = Label(self.personal_frame, text="Gender:", font=("Arial", 10))
        self.gender_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.gender_entry = Entry(self.personal_frame, font=("Arial", 10))
        self.gender_entry.grid(row=4, column=1, padx=10, pady=5, sticky="e")

        # ====================

        # contact information frame
        self.contact_frame = Frame(master, relief="solid", highlightbackground=light_grey, highlightthickness=1)
        self.contact_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # contact frame title
        self.contact_title_label = Label(self.contact_frame, text="Contact Information", font=("Arial", 10))
        self.contact_title_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        # email Address
        self.email_label = Label(self.contact_frame, text="Email Address:", font=("Arial", 10))
        self.email_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.email_entry = Entry(self.contact_frame, font=("Arial", 10))
        self.email_entry.grid(row=1, column=1, padx=10, pady=5, sticky="e")

        # phone number
        self.phone_number_label = Label(self.contact_frame, text="Phone Number:", font=("Arial", 10))
        self.phone_number_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.phone_number_entry = Entry(self.contact_frame, font=("Arial", 10))
        self.phone_number_entry.grid(row=2, column=1, padx=10, pady=5, sticky="e")

        # home address
        self.address_label = Label(self.contact_frame, text="Home Address:", font=("Arial", 10))
        self.address_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.address_entry = Entry(self.contact_frame, font=("Arial", 10))
        self.address_entry.grid(row=3, column=1, padx=10, pady=5, sticky="e")

        # zip code
        self.zip_code_label = Label(self.contact_frame, text="Zip Code:", font=("Arial", 10))
        self.zip_code_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.zip_code_entry = Entry(self.contact_frame, font=("Arial", 10))
        self.zip_code_entry.grid(row=4, column=1, padx=10, pady=5, sticky="e")

        # ====================

        # job information frame
        self.job_frame = Frame(master, relief="solid", highlightbackground=light_grey, highlightthickness=1)
        self.job_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # job information title
        self.job_frame_title = Label(self.job_frame, text="Job Information", font=("Arial", 10))
        self.job_frame_title.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        # job title
        self.job_title_label = Label(self.job_frame, text="Job Title:", font=("Arial", 10))
        self.job_title_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.job_title_entry = Entry(self.job_frame, font=("Arial", 10))
        self.job_title_entry.grid(row=1, column=1, padx=10, pady=5, sticky="e")

        # department
        self.department_label = Label(self.job_frame, text="Department:", font=("Arial", 10))
        self.department_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.department_entry = Entry(self.job_frame, font=("Arial", 10))
        self.department_entry.grid(row=2, column=1, padx=10, pady=5, sticky="e")

        # date of hire
        self.hire_date_label = Label(self.job_frame, text="Hire Date:", font=("Arial", 10))
        self.hire_date_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.hire_date_entry = Entry(self.job_frame, font=("Arial", 10))
        self.hire_date_entry.grid(row=3, column=1, padx=10, pady=5, sticky="e")

        # salary
        self.salary_label = Label(self.job_frame, text="Salary:", font=("Arial", 10))
        self.salary_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.salary_entry = Entry(self.job_frame, font=("Arial", 10))
        self.salary_entry.grid(row=4, column=1, padx=10, pady=5, sticky="e")

        # ====================

        # emergency contact frame
        self.emergency_contact_frame = Frame(master, relief="solid", highlightbackground=light_grey, highlightthickness=1)
        self.emergency_contact_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        # emergency information title
        self.emergency_contact_title = Label(self.emergency_contact_frame, text="Emergency Information", font=("Arial", 10))
        self.emergency_contact_title.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        # emergency contact first name
        self.e_fname_label = Label(self.emergency_contact_frame, text="First Name:", font=("Arial", 10))
        self.e_fname_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.e_fname_entry = Entry(self.emergency_contact_frame, font=("Arial", 10))
        self.e_fname_entry.grid(row=1, column=1, padx=10, pady=5, sticky="e")

        # emergency contact last name
        self.elname_label = Label(self.emergency_contact_frame, text="Last Name:", font=("Arial", 10))
        self.elname_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.elname_entry = Entry(self.emergency_contact_frame, font=("Arial", 10))
        self.elname_entry.grid(row=2, column=1, padx=10, pady=5, sticky="e")

        # emergency contact relationship
        self.e_relationship_label = Label(self.emergency_contact_frame, text="Relationship:", font=("Arial", 10))
        self.e_relationship_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.e_relationship_entry = Entry(self.emergency_contact_frame, font=("Arial", 10))
        self.e_relationship_entry.grid(row=3, column=1, padx=10, pady=5, sticky="e")

        # emergency contact number
        self.e_phone_number_label = Label(self.emergency_contact_frame, text="Phone Number:", font=("Arial", 10))
        self.e_phone_number_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.e_phone_number_entry = Entry(self.emergency_contact_frame, font=("Arial", 10))
        self.e_phone_number_entry.grid(row=4, column=1, padx=10, pady=5, sticky="e")

        # configure grid layout for the frames to expand properly
        self.personal_frame.columnconfigure(1, weight=1)
        self.contact_frame.columnconfigure(1, weight=1)
        self.job_frame.columnconfigure(1, weight=1)
        self.emergency_contact_frame.columnconfigure(1, weight=1)

        # ====================

        # Adjust window size based on the content
        self.adjust_window_size()

    def adjust_window_size(self):
        # Update the window layout to calculate the total height
        self.master.update_idletasks()

        # Calculate the total height needed for all frames
        total_height = (
            self.personal_frame.winfo_height() +
            self.contact_frame.winfo_height() +
            self.job_frame.winfo_height() +
            self.emergency_contact_frame.winfo_height() +
            50  # additional padding between frames
        )

        # Set the window height to fit all frames
        self.master.geometry(f"1400x{total_height}")

def main():
    """Initialize the Tkinter window application."""
    # create the main window
    window = Tk()
    # create an instance of the EmployeeApp class
    app = EmployeeApp(window)
    # start the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    # run the main function if the script is executed directly
    main()
