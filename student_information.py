system_name = "Student Information System"

def student_information(name,age=17,**kwargs):
    print(f"=== Welcome to the {system_name} ===")
    print("\n===== Student Information =====")
    print(f"Name        : {name}")
    print(f"Age         : {age}")
    
    for key, value in kwargs.items():
        print(f"{key.capitalize():12}: {value}")

name = input("Enter your name: ")
age = input("Enter your age (Press Enter for 17): ")
country = input("Enter your country:")
city = input("Enter your city: ")
major = input("Enter your major: ")
institution= input("Enter your school or university: ")

try:   
    if age == "":
        student_information(
            name,
            country=country,
            city=city,
            major=major,
            institution=institution
        )
    else:
        student_information(
            name,
            age=int(age),
            country=country,
            city=city,
            major=major,
            institution=institution
        )
        
except:
    print("Invalid age! Please enter a number.")