employee_name = "rocky"
employee_id = "jio@gmail.com"
employee_pass = "jio@123"
employee_salary = 50000



if __name__ == "__main__":

    #will not be acessible by other file 
    manager_name="suresh chandra"
    manager_id = "hello@gmail.com"
    manager_pass = "helo@123"
    manager_salary = 80000


def average_finder(ls):
  total_sum=0
  count=0
  for item in ls:
    total_sum+=item
    count+=1
  average=total_sum / count
  print("your average is:",round(average,2))

  print("manager file is exicuted !")