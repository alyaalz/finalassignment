class Employee:
    def __init__(self, name, emp_id, department, job_title, basic_salary, age, dob, passport_details):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.dob = dob
        self.passport_details = passport_details

class Manager(Employee):
    def __init__(self, name, emp_id, department, job_title, basic_salary, age, dob, passport_details, manages=None):
        super().__init__(name, emp_id, department, job_title, basic_salary, age, dob, passport_details)
        self.manages = manages if manages else []

class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

class Supplier:
    def __init__(self, supplier_id, name, address, contact_details):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

class Event:
    def __init__(self, event_id, type, theme, date, time, duration, venue_address, guest_list, catering_company=None, cleaning_company=None, decorations_company=None, entertainment_company=None, furniture_supply_company=None, invoice=None, client=None, guests=None, suppliers=None):
        self.event_id = event_id
        self.type = type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.guest_list = guest_list
        self.catering_company = catering_company
        self.cleaning_company = cleaning_company
        self.decorations_company = decorations_company
        self.entertainment_company = entertainment_company
        self.furniture_supply_company = furniture_supply_company
        self.invoice = invoice
        self.client = client
        self.guests = guests if guests else []
        self.suppliers = suppliers if suppliers else []

class Venue:
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

class Caterer:
    def __init__(self, caterer_id, name, address, contact_details, menu, min_guests, max_guests):
        self.caterer_id = caterer_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.menu = menu
        self.min_guests = min_guests
        self.max_guests = max_guests