from faker import Faker
from datetime import datetime, timedelta
from faker.providers import date_time
from collections import defaultdict

def generate_list(): #функція для генерації списку співробітників з використанням faker
    fake = Faker()
    name = fake.first_name()
    dob = fake.date_of_birth()
    return name, dob

names_list = [generate_list() for _ in range (100)]

employees = {"Amanda": datetime(2023, 7, 4),  #вручну написаний словник для перевірки 
"Britt": datetime(2023, 7, 10),
"Michael": datetime(2023, 7, 5),
"Larry": datetime(2023, 8, 3),
"Rodney": datetime(2023, 7, 5),
"Adam": datetime(2023, 7, 4)
}

employees1 = {}
for name, birthdate in names_list: 
    employees1[name] = birthdate  #генерація списку з використанням функції generate_list()
    
# for name, birthdate in employees.items():
#      print ({name}, {birthdate})

def get_period() -> tuple[datetime.date, datetime.date]: 
    current_date = datetime.now()
    start_period = current_date + timedelta(days=5-current_date.weekday())
    return start_period.date(), (start_period + timedelta(6)).date()
        
def check_empl(list_of_emp: dict) -> None:
    
    result = defaultdict(list)

    weekdays = { #робив словник днів тижня для альтернативного способу (нижче закоментований)
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Monday": 5,
    "Monday": 6   
}
    current_year = datetime.now().year
    for name, date in list_of_emp.items():
        
        bd = date
        bd = bd.replace(year=current_year)
        
        start, end = get_period()
        if start <= bd <= end:
            # wd = bd.weekday()
            if bd.weekday() in (5,6):
                result[bd].append(name)
            else: 
                result[bd].append(name)
                
    return result 
        
            # bd_day = None    - // альтеранативний спосіб, начебто теж працював. 
            # for key, value in weekdays.items():
            #     if value == wd:
            #         bd_day = key
                    
            #         print (f"{name} : {bd_day}")
            #         break
         
if __name__ == "__main__": 
    for key, value in check_empl(employees1).items(): 
        print (f"{key.strftime('%A')} : {value}")
        
    
