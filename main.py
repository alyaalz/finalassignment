import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import pickle
from models import Employee, Event, Client, Guest, Supplier, Venue

class EventManagementSystem(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Event Management System")
        self.geometry("600x400")

        # Load data from binary files
        self.load_data()

        # Create buttons for various functionalities
        self.create_buttons()

    def load_data(self):
        try:
            with open("employees.dat", "rb") as file:
                self.employees = pickle.load(file)
        except FileNotFoundError:
            self.employees = []
        try:
            with open("events.dat", "rb") as file:
                self.events = pickle.load(file)
        except FileNotFoundError:
            self.events = []
        try:
            with open("clients.dat", "rb") as file:
                self.clients = pickle.load(file)
        except FileNotFoundError:
            self.clients = []
        try:
            with open("guests.dat", "rb") as file:
                self.guests = pickle.load(file)
        except FileNotFoundError:
            self.guests = []
        try:
            with open("suppliers.dat", "rb") as file:
                self.suppliers = pickle.load(file)
        except FileNotFoundError:
            self.suppliers = []
        try:
            with open("venues.dat", "rb") as file:
                self.venues = pickle.load(file)
        except FileNotFoundError:
            self.venues = []

    def save_data(self):
        with open("employees.dat", "wb") as file:
            pickle.dump(self.employees, file)
        with open("events.dat", "wb") as file:
            pickle.dump(self.events, file)
        with open("clients.dat", "wb") as file:
            pickle.dump(self.clients, file)
        with open("guests.dat", "wb") as file:
            pickle.dump(self.guests, file)
        with open("suppliers.dat", "wb") as file:
            pickle.dump(self.suppliers, file)
        with open("venues.dat", "wb") as file:
            pickle.dump(self.venues, file)

    def create_buttons(self):
        add_employee_btn = tk.Button(self, text="Add Employee", command=self.add_employee)
        add_employee_btn.pack()

        add_event_btn = tk.Button(self, text="Add Event", command=self.add_event)
        add_event_btn.pack()

        add_event_btn = tk.Button(self, text="Add Client", command=self.add_client)
        add_event_btn.pack()

        add_event_btn = tk.Button(self, text="Add Guest", command=self.add_guest)
        add_event_btn.pack()

        add_event_btn = tk.Button(self, text="Add Supplier", command=self.add_supplier)
        add_event_btn.pack()

        button = tk.Button(self, text="Search Employee", command=self.show_employee_data)
        button.pack()
        button = tk.Button(self, text="Search Event", command=self.show_event_data)
        button.pack()
        button = tk.Button(self, text="Search Client", command=self.show_client_data)
        button.pack()
        button = tk.Button(self, text="Search Guest", command=self.show_guest_data)
        button.pack()

        

    def add_employee(self):
        name = simpledialog.askstring("Employee Details", "Enter employee name:")
        emp_id = simpledialog.askinteger("Employee Details", "Enter employee ID:")
        department = simpledialog.askstring("Employee Details", "Enter department:")
        job_title = simpledialog.askstring("Employee Details", "Enter job title:")
        basic_salary = simpledialog.askfloat("Employee Details", "Enter basic salary:")
        age = simpledialog.askinteger("Employee Details", "Enter age:")
        dob = simpledialog.askstring("Employee Details", "Enter date of birth (YYYY-MM-DD):")
        passport_details = simpledialog.askstring("Employee Details", "Enter passport details:")
        
        new_employee = Employee(name, emp_id, department, job_title, basic_salary, age, dob, passport_details)
        self.employees.append(new_employee)
        self.save_data()
        messagebox.showinfo("Success", "Employee added successfully!")

    def add_event(self):
        event_id = simpledialog.askinteger("Event Details", "Enter event ID:")
        type = simpledialog.askstring("Event Details", "Enter event type:")
        theme = simpledialog.askstring("Event Details", "Enter event theme:")
        date = simpledialog.askstring("Event Details", "Enter event date (YYYY-MM-DD):")
        time = simpledialog.askstring("Event Details", "Enter event time (HH:MM AM/PM):")
        duration = simpledialog.askstring("Event Details", "Enter event duration:")
        venue_address = simpledialog.askstring("Event Details", "Enter venue address:")
        guest_list = simpledialog.askstring("Event Details", "Enter guest list:")
        catering_company = simpledialog.askstring("Event Details", "Enter catering company:")
        cleaning_company = simpledialog.askstring("Event Details", "Enter cleaning company:")
        decorations_company = simpledialog.askstring("Event Details", "Enter decorations company:")
        entertainment_company = simpledialog.askstring("Event Details", "Enter entertainment company:")
        furniture_supply_company = simpledialog.askstring("Event Details", "Enter furniture supply company:")
        invoice = simpledialog.askstring("Event Details", "Enter invoice details:")
        client_id = simpledialog.askinteger("Event Details", "Enter client ID:")
        
        new_event = Event(event_id, type, theme, date, time, duration, venue_address, guest_list, catering_company,
                          cleaning_company, decorations_company, entertainment_company, furniture_supply_company,
                          invoice, client_id)
        self.events.append(new_event)
        self.save_data()
        messagebox.showinfo("Success", "Event added successfully!")

    def add_client(self):
            client_id = simpledialog.askinteger("Event Details", "Enter client ID:")
            clinet_name = simpledialog.askstring("Event Details", "Enter client name:")
            address = simpledialog.askstring("Event Details", "Enter Address")
            budget = simpledialog.askinteger("Event Details", "Enter Budget:")
            
            new_client = Client(client_id, clinet_name, address, budget)
            self.clients.append(new_client)
            self.save_data()
            messagebox.showinfo("Success", "Event added successfully!")

    def add_guest(self):
        client_id = simpledialog.askinteger("Event Details", "Enter Guest ID:")
        clinet_name = simpledialog.askstring("Event Details", "Enter Guest name:")
        address = simpledialog.askstring("Event Details", "Enter Address")
        contact_details = simpledialog.askinteger("Event Details", "Enter Contact Details:")
                
        new_guest = Guest(client_id, clinet_name, address, contact_details)
        self.clients.append(new_guest)
        self.save_data()
        messagebox.showinfo("Success", "Event added successfully!")

    def add_supplier(self):
        supplier_id = simpledialog.askinteger("Event Details", "Enter Supplier ID:")
        supplier_name = simpledialog.askstring("Event Details", "Enter Supplier name:")
        address = simpledialog.askstring("Event Details", "Enter Address")
        contact_details = simpledialog.askinteger("Event Details", "Enter contact details:")
            
        new_supplier= Supplier(supplier_id, supplier_name, address, contact_details)
        self.clients.append(new_supplier)
        self.save_data()
        messagebox.showinfo("Success", "Event added successfully!")


    def extract_data_from_pickle(self,file_name):
        try:
            with open(file_name, 'rb') as file:
                extracted_data = pickle.load(file)
                
            return extracted_data
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")

    def show_employee_data(self):
        file_name = "employees.dat"
        extracted_data = self.extract_data_from_pickle(file_name)
        if extracted_data:
            id_to_find = simpledialog.askinteger("Enter ID", "Enter the ID you want to search for:")
            if id_to_find is not None:
              
                count = 0
                for emp in extracted_data:
             
                    if id_to_find == emp.emp_id:
                        data = extracted_data[count]
                     
                        message = f"The following employee found \n Employee Name : {data.name} \n Employee Department{data.department} \n Employee Job Title: {data.job_title} \n Employee Basic Salary{data.basic_salary} \n Employee Age{data.age} "
                        messagebox.showinfo("Employee Data", message)
                        # self.show_table(data)
                    count +=1
                        # Display the message box
                    
                    # else:
                    #     messagebox.showerror("Error", "ID not found.")

    def show_event_data(self):
            file_name = "events.dat"
            extracted_data = self.extract_data_from_pickle(file_name)
            if extracted_data:
                id_to_find = simpledialog.askinteger("Enter ID", "Enter the ID you want to search for:")
                if id_to_find is not None:
                
                    count = 0
                    for emp in extracted_data:
                
                        if id_to_find == emp.event_id:
                            data = extracted_data[count]
                        
                            message = f"The following event details found \n Event Type : {data.type} \n Employee Theme{data.theme} \n Employee Duration: {data.duration} \n Event Venue{data.venue_address} \n Event Cleaning Company{data.cleaning_company} "
                            messagebox.showinfo("Employee Data", message)
                            # self.show_table(data)
                        count +=1
                          

    def show_client_data(self):
            file_name = "clients.dat"
            extracted_data = self.extract_data_from_pickle(file_name)
            if extracted_data:
                id_to_find = simpledialog.askinteger("Enter ID", "Enter the ID you want to search for:")
                if id_to_find is not None:
                
                    count = 0
                    for emp in extracted_data:
                
                        if id_to_find == emp.client_id:
                            data = extracted_data[count]
                        
                            message = f"The following employee found \n Client name : {data.name} \n Client Address {data.address} \n Client Contact: {data.budget} \n Client Budget{data.venue} "
                            messagebox.showinfo("Client Data", message)
                            # self.show_table(data)
                        count +=1


    def show_guest_data(self):
            file_name = "guests.dat"
            extracted_data = self.extract_data_from_pickle(file_name)
            if extracted_data:
                id_to_find = simpledialog.askinteger("Enter ID", "Enter the ID you want to search for:")
                if id_to_find is not None:
                
                    count = 0
                    for emp in extracted_data:
                
                        if id_to_find == emp.guest_id:
                            data = extracted_data[count]
                        
                            message = f"The following Guest found \n Guest name : {data.name} \n Guest Address {data.address} \n Guest Contact: {data.budget} \n Client Budget{data.venue} "
                            messagebox.showinfo("Guest Data", message)
                            # self.show_table(data)
                        count +=1

if __name__ == "__main__":
    app = EventManagementSystem()
    app.mainloop()
