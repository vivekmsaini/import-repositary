import manager


print("employee name : " , manager.employee_name)
print("employee id : " , manager.employee_id)
print("employee password : " , manager.employee_pass)
print("employee salary : " , manager.employee_salary)




import manager as mng

print("employee name : " , mng.employee_name)
print("employee id : " , mng.employee_id)
print("employee password : " , mng.employee_pass)
print("employee salary : " ,mng.employee_salary)

marks = [14,52,63,96,74,52,63,63,42,41,52,63]
mng.average_finder(ls=marks)

import manager    # all content recived from the another file


from manager import employee_id,employee_name,employee_pass,employee_salary
from manager  import manager_name,manager_id,manager_pass
print("employee name : " , employee_name)
print("employee id : " , employee_id)
print("employee password : " , employee_pass)
print("employee salary : " , employee_salary)

print()
print(manager_id)
print(manager_pass)
print(manager_name)
