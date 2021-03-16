from random import randint

Human = input("Enter the input: ")
System = ["Paper", "Rock", "Scissor"]
Random_System = System[randint(0, 2)]

if Human == Random_System:
    print(f"you have chosen {Human} and Computer have chosen {Random_System}")
    print("Tie")

elif Human == "Paper":
    if Random_System == "Scissor":
        print(f"you have chosen {Human} and Computer have chosen {Random_System} .Computer won the game!!!!")
    else:
        print(f"you have chosen {Human} and Computer have chosen {Random_System} .Haayyy!You won the game!!!!")


elif Human == "Scissor":
    if Random_System == "Rock":
        print(f"you have chosen {Human} and Computer have chosen {Random_System}.Haayyy!You won the game!!!!")
    else:
        print(f"you have chosen {Human} and Computer have chosen {Random_System}.Computor won the game!!!!")


elif Human == "Rock":
    if Random_System == "Paper":
        print(f"you have chosen {Human} and Computer have chosen {Random_System} .Computer won the game!!!!")
    else:
        print(f"you have chosen {Human} and Computer have chosen {Random_System}.Haayyy!You won the game!!!!")

else:
    pass














