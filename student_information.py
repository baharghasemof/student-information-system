def student_information(name,age=17,**kwargs):
    print("====Welcome to the Student Information System====")
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

if age == "":
    student_information(name,country=country,city=city,major=major,institution=institution)
            
else:
    student_information(name,age=int(age),country=country,city=city,major=major,institution=institution)