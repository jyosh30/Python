# Number = (input("Enter the Marks :"))

def Grades(Number):
    Grades = {"Grade A": "Meet Professor Gokul ", "Grde B": "Meet Professor Gayathri ",
              "Grade C": "Meet Professor Radhika ",
              "Grade D": " Meet Professor Ramya", "Grade E": "Meet Principal"}

    if Number >= int(90) and Number <= int(100):
        print(Grades["Grade A"])

    elif Number >= int(80) and Number <= int(89):
        print(Grades["Grade B"])

    elif Number >= int(70) and Number <= int(79):
        print(Grades["Grade C"])

    elif Number >= int(60) and Number <= int(69):
        print(Grades["Grade D"])

    elif Number >= int(35) and Number <= int(59):
        print(Grades["Grade E"])

    else:
        print("Failed in all subjects")
    print(Grades)


Grades(67)
