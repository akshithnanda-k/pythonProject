#Operators

Amount = int(input("Enter the amount: "))

Notes_100 = Amount//100
Remaining_100 = Amount - (Notes_100 * 100)

Notes_50 = Remaining_100//50
Remaining_50 = Remaining_100 - (Notes_50 * 50)

Notes_10 = Remaining_50//10
Remaining_Amount = Remaining_50 - (Notes_10 * 10)

print("100 Notes : ", Notes_100)
print("50 Notes: ", Notes_50)
print("10 Notes: ", Notes_10)
print("Change: ", Remaining_Amount)