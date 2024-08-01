from tkinter import *

class EmployeeApp:
    def __init__(self, master):
        """
        Initialize the main window and configure its layout.
        
        Parameters:
        master (Tk): The root Tkinter window instance.
        """
        self.master = master
        self.setup_main_window()
        self.create_frames()
        self.create_form_fields()
        self.create_buttons_frame("#C0C0C0")
        self.configure_frame_grid()
        self.adjust_window_size()

    def setup_main_window(self):
        """
        Configure the main window properties.
        """
        self.master.geometry("1400x770")
        self.master.resizable(False, False)
        self.master.title("Employee Database")
        self.master.attributes("-topmost", True)
        self.master.columnconfigure(2, weight=1)
        self.master.rowconfigure(3, weight=1)

    def create_frames(self):
        """
        Create the frames for the various sections of the form.
        """
        border_color = "#C0C0C0"
        self.personal_frame = self.create_frame(border_color, 0)
        self.contact_frame = self.create_frame(border_color, 1)
        self.job_frame = self.create_frame(border_color, 2)
        self.emergency_contact_frame = self.create_frame(border_color, 3)

    def create_form_fields(self):
        """
        Create form fields within the respective frames.
        """
        self.create_personal_info_frame()
        self.create_contact_info_frame()
        self.create_job_info_frame()
        self.create_emergency_contact_frame()

    def create_personal_info_frame(self):
        """
        Create and place the personal information frame.
        """
        self.create_label(self.personal_frame, "Employee Information", 0, 0, 2)
        self.create_label_entry(self.personal_frame, "First Name:", 1)
        self.create_label_entry(self.personal_frame, "Last Name:", 2)
        self.create_label_entry(self.personal_frame, "Date of Birth:", 3)
        self.create_label_entry(self.personal_frame, "Gender:", 4)

    def create_contact_info_frame(self):
        """
        Create and place the contact information frame.
        """
        self.create_label(self.contact_frame, "Contact Information", 0, 0, 2)
        self.create_label_entry(self.contact_frame, "Email Address:", 1)
        self.create_label_entry(self.contact_frame, "Phone Number:", 2)
        self.create_label_entry(self.contact_frame, "Home Address:", 3)
        self.create_label_entry(self.contact_frame, "Zip Code:", 4)

    def create_job_info_frame(self):
        """
        Create and place the job information frame.
        """
        self.create_label(self.job_frame, "Job Information", 0, 0, 2)
        self.create_label_entry(self.job_frame, "Job Title:", 1)
        self.create_label_entry(self.job_frame, "Department:", 2)
        self.create_label_entry(self.job_frame, "Hire Date:", 3)
        self.create_label_entry(self.job_frame, "Salary:", 4)

    def create_emergency_contact_frame(self):
        """
        Create and place the emergency contact frame.
        """
        self.create_label(self.emergency_contact_frame, "Emergency Information", 0, 0, 2)
        self.create_label_entry(self.emergency_contact_frame, "First Name:", 1)
        self.create_label_entry(self.emergency_contact_frame, "Last Name:", 2)
        self.create_label_entry(self.emergency_contact_frame, "Relationship:", 3)
        self.create_label_entry(self.emergency_contact_frame, "Phone Number:", 4)

    def create_buttons_frame(self, border_color):
        """
        Create and configure the buttons frame.
        """
        self.buttons_frame = Frame(self.master, relief="solid", highlightbackground=border_color, highlightthickness=1)
        self.buttons_frame.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        self.create_label(self.buttons_frame, "Options", 0, 0, 1)
        self.create_buttons()

    def create_buttons(self):
        """
        Create buttons and place them in the buttons frame.
        """
        buttons = [("Add", 1, 0), ("Delete", 2, 0)]
        for (text, row, col) in buttons:
            button = Button(self.buttons_frame, text=text, width=10, height=2)
            button.grid(row=row, column=col, padx=5, pady=5)

    def create_frame(self, border_color, row):
        """
        Create a frame with a specified border color and row placement.

        Parameters:
        border_color (str): The color to use for the frame's border.
        row (int): The row index where the frame will be placed in the grid.

        Returns:
        Frame: The created Tkinter frame.
        """
        frame = Frame(self.master, relief="solid", highlightbackground=border_color, highlightthickness=1, highlightcolor=border_color)
        frame.grid(row=row, column=0, padx=10, pady=10, sticky="nsew")
        return frame

    def create_label(self, parent, text, row, column, columnspan=1):
        """
        Create and place a label in a specified parent widget.

        Parameters:
        parent (Frame): The parent widget where the label will be placed.
        text (str): The text to display on the label.
        row (int): The row index where the label will be placed in the grid.
        column (int): The column index where the label will be placed in the grid.
        columnspan (int, optional): The number of columns the label should span. Default is 1.
        """
        label = Label(parent, text=text, font=("Arial", 10))
        label.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5, sticky="w")

    def create_label_entry(self, parent, text, row):
        """
        Create and place a label and entry widget pair.

        Parameters:
        parent (Frame): The parent widget where the label and entry will be placed.
        text (str): The text to display on the label.
        row (int): The row index where the label and entry will be placed in the grid.

        Returns:
        Entry: The created Tkinter entry widget.
        """
        label = Label(parent, text=text, font=("Arial", 10))
        label.grid(row=row, column=0, padx=5, pady=5, sticky="w")
        entry = Entry(parent, font=("Arial", 10))
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="e")
        return entry

    def configure_frame_grid(self):
        """
        Configure grid layout for all frames to expand properly.
        """
        frames = [self.personal_frame, self.contact_frame, self.job_frame, self.emergency_contact_frame]
        for frame in frames:
            frame.columnconfigure(1, weight=1)

    def adjust_window_size(self):
        """
        Update the window layout to calculate the total height and adjust the window size.
        """
        self.master.update_idletasks()
        total_height = sum(frame.winfo_height() for frame in [
            self.personal_frame, self.contact_frame, self.job_frame, self.emergency_contact_frame
        ]) + 50  # Additional padding between frames
        self.master.geometry(f"1400x{total_height}")

def main():
    """
    Initialize the Tkinter window application.
    """
    window = Tk()
    app = EmployeeApp(window)
    window.mainloop()

if __name__ == "__main__":
    main()
