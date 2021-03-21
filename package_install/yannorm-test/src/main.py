from yannorm import Condition, F

from src.models import Employee


employees = Employee.objects.select('*')
print(employees)
