# print("Welcome to the tip calculator")
# total_bill = float(input("What was the total bill? $"))
# tip_amount = float(input("How much tip would you like to give? 10, 12, or 15? "))
# num_people = float(input("How many people to split the bill? "))

# total_amount = (total_bill * (1 + (tip_amount / 100))) / num_people

# print(f"Each person should pay: {round(total_amount, 2)}")

def minmax(nums):
    mn = nums[0]
    mx = nums[0]
    for x in nums[1:]:
        if x < mn:
            mn = x
        elif x > mx:
            mx = x

    return (mn, mx)
print(minmax([3, 3, 2, 5, 5, 1, 4]))

