from application.people import get_employees
from application.salary import calculate_salary
from datetime import datetime

today = datetime.now()

if __name__ == '__main__':
    calculate_salary()
    get_employees()

print(today)
