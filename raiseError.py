a = int(input("Enter a number between 5 and 9: "))
if (a > 9 or a < 5):
    raise ValueError("Invalid input")