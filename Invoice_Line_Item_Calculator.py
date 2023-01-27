Go = "yes"


print("Invoice Line Item Calculator\n\n")

while Go == "yes":

    def quality():
        Price = input("Please type in a price: ")
        while True:
            try:
                Price = float(Price)
                return Price

            except ValueError:
                Price = input("\nPlease type a price in digits: ")


    def quantity(Price):
        Amount = input("\nPlease type in the amount: ")
        while True:
            try:
                Amount = int(Amount)
                print("\nYour price:", Price)
                print("Your amount:", Amount)
                return Amount
            
            except ValueError:
                Price = input("\nPlease type an amount in digits: ")

    Price = quality()
    Amount = quantity(Price)

    #if Price == float(Price):
     #   print("True")
    #else:
     #   print("False")

    print("\nTotal Price:", Price * Amount)

    Answer = input("\nContinue? ")

    while Answer.lower() != "y" and  Answer.lower() != "n":
        Answer = input("\nContinue? type in only y or n ")

    if Answer.lower() == "y":
        Go = "yes"

    else:
        Go = "no"

print("\nGoodbye!")

