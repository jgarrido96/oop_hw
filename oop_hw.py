
# 1. City Infrastructure Management System

# Task 1: Vehicle Registration System

class Vehicle:
    def __init__(self, reg_num, type, color, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
        self.color = color

    def show_everything(self):
        print(f"Registration number: {self.registration_number}")
        print(f"Vehicle type: {self.type}")
        print(f"Vehicle owner name: {self.owner}")

    def get_reg_num(self):
        return self.registration_number
    
    def set_reg_num(self, reg_num):
        self.registration_number = reg_num

    def get_type(self):
        return self.type

    def set_get_type(self, type):
        self.type = type

    def get_owner(self):
        return self.owner

    def update_owner(self, owner):
        self.owner = owner
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color


my_car = Vehicle("1234567890", "SUV", "Black on Black", "Some Guy")
print(f"Chevy Blazer information:\nRegistration Number: {my_car.get_reg_num()}\nVehicle Style: {my_car.get_type()}\nColor: {my_car.get_color()}\nOwner: {my_car.get_owner()}")
print('\n')
my_car.update_owner("Jose")

print(f"My car's new owner is: {my_car.get_owner()}")
print('\n')


# Task 2: Event Management System Enhancement

events = []

class Event:
    def __init__(self, name, date, count = 0):
        self.name = name
        self.date = date
        self.count = count

    def add_participant(self):
        print("\nPlease add participants!")
        while True:
            name_input = input("Name of participants (type 'done' when finished): ")
            if name_input == 'done':
                break
            else:
                self.count += 1
    
    def get_event(self):
        return self.name, self.date

    def get_participant_count(self):
        return self.count


event_1 = Event("Jose II's Birthday Party", "05/18/2024")
print(f"Event: {event_1.get_event()}")

event_1.add_participant()
print(f"The number of people attending {event_1.get_event()}: {event_1.get_participant_count()}")
