employee_info = [
                 {"name": "Rishi", "experience":"3", "role": "data engineer", "salary_pa": "12"},
                 {"name": "Vamshi", "experience":"2", "role": "data analyst", "salary_pa": "10"},
                 {"name": "Ankitha", "experience":"1", "role": "data analyst", "salary_pa": "9.5"},
                 {"name": "Lakshmi", "experience":"5", "role": "data scientist", "salary_pa": "15"}]

def avg(salary):
    avg_sal = salary/len(employee_info)
    return avg_sal

sum = 0

for emp in employee_info:
    sum += float(emp['salary_pa'])
    
    
average_sal = avg(sum)    

for emp in employee_info:    
   if average_sal > float(emp['salary_pa']):
        print("--------Employee Data--------")
        print(f"Name               : {emp['name']}")
        print(f"Role               : {emp['role']}")
        print(f"Salary Per Annum   : {emp['salary_pa']}")
        print(f"Average Salary     :"+ str(average_sal))
        print()


    
    





