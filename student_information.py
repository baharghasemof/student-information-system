system_name = "Student Information System"


def student_information(name,age=17,**kwargs):
    print(f"=== Welcome to the {system_name} ===")
    print("\n===== Student Information =====")
    print(f"Name        : {name}")
    print(f"Age         : {age}")

    for key, value in kwargs.items():
        print(f"{key.capitalize():12}: {value}")


name = input("Enter your name: ")

if name == "":
    print("Name cannot be empty!")

else:
    age = input("Enter your age (Press Enter for 17): ")

    try:
        if age == "":
            age = 17
        else:
            age = int(age)

        if age < 0:
            print("Age cannot be negative!")

        else:
            country = input("Enter your country: ")
            city = input("Enter your city: ")
            major = input("Enter your major: ")
            institution = input("Enter your school or university: ")

            if country == "":
                print("Country cannot be empty!")

            else:
                student_information(
                    name,
                    age,
                    country=country,
                    city=city,
                    major=major,
                    institution=institution
                )

    except:
        print("Invalid age! Please enter a number.")