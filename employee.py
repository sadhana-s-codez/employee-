import requests
url="https://api.slingacademy.com/v1/sample-data/files/employees.json"
try:
    response=requests.get(url,timeout=10)
    if response.status_code == 200:
         employees=response.json()
    
         for emp in employees:
            years=int(emp.get("years_of_experience",0))
            if years<3:
                emp["designation"]="System Engineer"
            elif years<5:
                emp["designation"]="Data Engineer"
            elif years<10:
                emp["designation"]="Senior Data Engineer"
            else:
                emp["designation"]="Lead"

            emp["full_name"]=(str(emp.get("first_name",""))+" "+str(emp.get("last_name","")))


            phone=str(emp.get("phone",""))
            if "x" in phone.lower():
                emp["phone"]="Invalid Number"


            emp["full_name"]=str(emp.get("full_name",""))
            emp["phone"]=str(emp.get("phone",""))
            emp["years_of_experience"]=int(emp.get("years_of_experience",0))   
            emp["email"]=str(emp.get("email",""))
            emp["gender"]=str(emp.get("gender",""))
            emp["job_title"]=str(emp.get("job_title",""))
            emp["department"]=str(emp.get("department",""))
            emp["age"]=int(emp.get("age",0))
            emp["salary"]=int(emp.get("salary",0))



            print("Employee ID:",emp.get("id"))
            print("Full Name:",emp["full_name"])
            print("Designation:",emp["designation"])
            print("Email:",emp.get("email"))
            print("Phone:",emp.get("phone"))
            print("Gender:",emp.get("gender"))
            print("Age:",emp.get("age"))
            print("Job Title:",emp.get("job_title"))
            print("Years of Experience:",emp.get("years_of_experience"))
            print("Salary:",emp.get("salary"))
            print("Department:",emp.get("department"))
            print("-"*30)
    else:
         print("Failed to fetch data:",response.status_code)
except requests.exceptions.RequestException as e:
<<<<<<< HEAD
     print("Request Failed:",e)
=======
     print("Request  Failed:",e)
>>>>>>> 3dd5fe507e86feec365416cd7b3976693c7e321a
