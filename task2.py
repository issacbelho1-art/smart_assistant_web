#Functions
def yearly_emi():
    monthly = int(input("Enter monthly EMI: "))
    print("Your yearly EMI is:", monthly *12)
def loan_check():
    loan = int(input("Enter loan amount:"))
    if loan > 1000000:
        print("High debt, need skill upgrade")
    else:
        print("Debt manageable")

# Main program loop
while True:
    print("\nWelcome to Smart Assistant")
    print("1. Calculate yearly EMI")
    print("2. Check loan status")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3):")
    if choice == "1":
        yearly_emi()
    elif choice == "2":
        loan_check()
    elif choice == "3":
        print("Thank you. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")