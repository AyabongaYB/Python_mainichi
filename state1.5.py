score = input("enter score between 0.0 and 1.0: ")

try:
    score = float(score)
except:
    print("Error: Enter a decimal number between 0.0 and 1.0.")
    quit()

if score > 1.0:
    print("OUT OF RANGE, try again.")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score < 0.6:
    print("F")
else:
    print("OUT OF RANGE, try again.")