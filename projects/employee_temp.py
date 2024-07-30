from tkinter import *

class EmployeeApp:
    def __init__(self, master):
        """
        initialize the main window and configure its layout.
        
        parameters:
        master (Tk): the root Tkinter window instance.
        """
        # initialize the main window
        self.master = master
        master.geometry("1400x750")
        master.resizable(0, 0)  # make the window non-resizable
        master.title("Employee Database")
        master.attributes("-topmost", True)  # keep the window on top

        # configure grid layout for the master window
        master.columnconfigure(2, weight=1)
        master.rowconfigure(3, weight=1)

        # define light grey color for borders
        light_grey = "#C0C0C0"

        # create and configure frames for various sections of the form
        self.create_personal_info_frame(light_grey)
        self.create_contact_info_frame(light_grey)
        self.create_job_info_frame(light_grey)
        self.create_emergency_contact_frame(light_grey)
        self.create_buttons_frame(light_grey)

        # configure grid layout for the frames to expand properly
        self.configure_frame_grid()

        # adjust window size based on the content
        self.adjust_window_size()
        
        # ====================

    def create_personal_info_frame(self, border_color):
        """
        create and place the personal information frame.

        parameters:
        border_color (str): the color to use for the frame's border.
        """
        # create and place the personal information frame
        self.personal_frame = self.create_frame(border_color, 0)
        self.create_label(self.personal_frame, "Employee Information", 0, 0, 2)

        # create and place personal information fields
        self.create_label_entry(self.personal_frame, "First Name:", 1)
        self.create_label_entry(self.personal_frame, "Last Name:", 2)
        self.create_label_entry(self.personal_frame, "Date of Birth:", 3)
        self.create_label_entry(self.personal_frame, "Gender:", 4)

        # ====================

    def create_contact_info_frame(self, border_color):
        """
        create and place the contact information frame.

        parameters:
        border_color (str): the color to use for the frame's border.
        """
        # create and place the contact information frame
        self.contact_frame = self.create_frame(border_color, 1)
        self.create_label(self.contact_frame, "Contact Information", 0, 0, 2)

        # create and place contact information fields
        self.create_label_entry(self.contact_frame, "Email Address:", 1)
        self.create_label_entry(self.contact_frame, "Phone Number:", 2)
        self.create_label_entry(self.contact_frame, "Home Address:", 3)
        self.create_label_entry(self.contact_frame, "Zip Code:", 4)
        
        # ====================

    def create_job_info_frame(self, border_color):
        """
        create and place the job information frame.

        parameters:
        border_color (str): the color to use for the frame's border.
        """
        # create and place the job information frame
        self.job_frame = self.create_frame(border_color, 2)
        self.create_label(self.job_frame, "Job Information", 0, 0, 2)

        # create and place job information fields
        self.create_label_entry(self.job_frame, "Job Title:", 1)
        self.create_label_entry(self.job_frame, "Department:", 2)
        self.create_label_entry(self.job_frame, "Hire Date:", 3)
        self.create_label_entry(self.job_frame, "Salary:", 4)

        # ====================
        
    def create_emergency_contact_frame(self, border_color):
        """
        create and place the emergency contact frame.

        parameters:
        border_color (str): the color to use for the frame's border.
        """
        # create and place the emergency contact frame
        self.emergency_contact_frame = self.create_frame(border_color, 3)
        self.create_label(self.emergency_contact_frame, "Emergency Information", 0, 0, 2)

        # create and place emergency contact fields
        self.create_label_entry(self.emergency_contact_frame, "First Name:", 1)
        self.create_label_entry(self.emergency_contact_frame, "Last Name:", 2)
        self.create_label_entry(self.emergency_contact_frame, "Relationship:", 3)
        self.create_label_entry(self.emergency_contact_frame, "Phone Number:", 4)

        # ====================
        
    def create_buttons_frame(self, border_color):
        """
        Create and configure the buttons frame.

        parameters:
            border_color (str): the color to use for the frame's border.
        """
        # Create a frame for buttons with specified border color
        self.buttons_frame = Frame(self.master, relief="solid", highlightbackground=border_color, highlightthickness=1)
        # Place the frame in the grid at the bottom, right of the emergency_contact_frame
        self.buttons_frame.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        # Add labels or buttons to the frame
        self.create_label(self.buttons_frame, "Options", 0, 0, 1)
        # create button within the frame
        self.create_button()
        
        # ====================
        
    def create_button(self):
        """
        Create a button and place it in the buttons frame.
        """
        # create button and add it to buttons frame
        add_button = Button(self.buttons_frame, text="Add", width=10, height=2)
        add_button.grid(row=1, column=0, padx=5, pady=5)
        
        delete_button = Button(self.buttons_frame, text="Delete", width=10, height=2)
        delete_button.grid(row=2, column=0, padx=5, pady=5)
        
        view_button = Button(self.buttons_frame, text="View", width=10, height=2)
        view_button.grid(row=1, column=1, padx=5, pady=5)
        
        export_button = Button(self.buttons_frame, text="Export", width=10, height=2)
        export_button.grid(row=2, column=1, padx=5, pady=5)
        
        # ====================
        
    def create_frame(self, border_color, row):
        """
        create a frame with a specified border color and row placement.

        parameters:
        border_color (str): the color to use for the frame's border.
        row (int): the row index where the frame will be placed in the grid.

        returns:
        Frame: the created Tkinter frame.
        """
        # create a frame with a specified border color and row placement
        frame = Frame(self.master, relief="solid", highlightbackground=border_color, highlightthickness=1, highlightcolor="#C0C0C0")
        frame.grid(row=row, column=0, padx=10, pady=10, sticky="nsew")
        return frame
    
        # ====================

    def create_label(self, parent, text, row, column, columnspan=1):
        """
        create and place a label in a specified parent widget.

        parameters:
        parent (Frame): the parent widget where the label will be placed.
        text (str): the text to display on the label.
        row (int): the row index where the label will be placed in the grid.
        column (int): the column index where the label will be placed in the grid.
        columnspan (int, optional): the number of columns the label should span. default is 1.
        """
        # create and place a label in a specified parent widget
        label = Label(parent, text=text, font=("Arial", 10))
        label.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5, sticky="w")

        # ====================
        
    def create_label_entry(self, parent, text, row):
        """
        create and place a label and entry widget pair.

        parameters:
        parent (Frame): the parent widget where the label and entry will be placed.
        text (str): the text to display on the label.
        row (int): the row index where the label and entry will be placed in the grid.

        returns:
        Entry: the created Tkinter entry widget.
        """
        # create and place a label and entry widget pair
        label = Label(parent, text=text, font=("Arial", 10))
        label.grid(row=row, column=0, padx=5, pady=5, sticky="w")
        entry = Entry(parent, font=("Arial", 10))
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="e")
        return entry

        # ====================
        
    def configure_frame_grid(self):
        """
        configure grid layout for all frames to expand properly.
        """
        # configure grid layout for all frames to expand properly
        self.personal_frame.columnconfigure(1, weight=1)
        self.contact_frame.columnconfigure(1, weight=1)
        self.job_frame.columnconfigure(1, weight=1)
        self.emergency_contact_frame.columnconfigure(1, weight=1)

        # ====================
        
    def adjust_window_size(self):
        """
        update the window layout to calculate the total height and adjust the window size.
        """
        # update the window layout to calculate the total height
        self.master.update_idletasks()

        # calculate the total height needed for all frames
        total_height = (
            self.personal_frame.winfo_height() +
            self.contact_frame.winfo_height() +
            self.job_frame.winfo_height() +
            self.emergency_contact_frame.winfo_height() +
            50  # additional padding between frames
        )

        # set the window height to fit all frames
        self.master.geometry(f"1400x{total_height}")

        # ====================
        
def main():
    """
    initialize the tkinter window application.
    """
    # create the main window
    window = Tk()
    # create an instance of the EmployeeApp class
    app = EmployeeApp(window)
    # start the tkinter event loop
    window.mainloop()

# ====================
    
if __name__ == "__main__":
    # run the main function if the script is executed directly
    main()

