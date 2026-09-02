try:
    grade: float = float(input("Enter your grade: "))
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    match grade:
        case g if 85 <= g <= 100:
            print("HD")
        case g if 75 <= g < 85:
            print("D")
        case g if 65 <= g < 75:
            print("C")
        case g if 50 <= g < 65:
            print("P")
        case g if 0 <= g < 50:
            print("F")
        case _:
            print("Invalid grade. Please enter a number from 0 to 100.")
