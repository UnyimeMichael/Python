# counter = 0
# while(counter < 10):
#     print("Godfrey" , end = " " )
#     counter+=1
# print("\n", counter)
#
# for letter in "victoria":
#     print(letter)
#
# for number in range(10):
#     print(number)
#
# for number in range(5,11):
#     print(number)
#
# for number in range(0,11,2):
#     print(number)
#
# for number in range(1 , 11 , 2):
#     print(number)


# def investment(amount: float, year : int):
#     profit = (amount * 5) / 100
#     # return amount + profit
#     for count in range (1, year):
#     amount = int(input("Enter amount : "))
#     year = int(input("Enter number of years : "))
#     print(f"Year {year} return on investment is {investment(amount): ,.2f}")
#
#
# principal_amount = float(input("Enter amount to invest: "))
# years = int(input("Enter number of years: "))
# rate = 0.05
# for year in range(1, years + 1):
#     roi = principal_amount * rate
#     future_amount = principal_amount + roi
#     principal_amount = future_amount
#     print(f" Year {year} return on investment is {roi}, your principal is now {future_amount: ,.2f}")

def investment(principal_amount, years):
    rate = 0.05
    try:
        for year in range(1, years + 1):
            roi = principal_amount * rate
            future_amount = principal_amount + roi
            principal_amount = future_amount
            print(f" Year {year} return on investment is {roi}, your principal is now {future_amount: ,.2f}")
    except TypeError:
        return "The amount cannot be a String"
    except ValueError:
        return "The value cannot be negative"


# recalling the function without rewriting the above codes;
principal_amount = float(input("Enter amount to invest: "))
years = int(input("Enter number of years: "))
print(investment(principal_amount, years))

# or recalling the function without rewriting the above codes;
