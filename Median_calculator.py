import time
def find_median():
    numbers = []
    while True:
        try:
            amount_nums = int(input("How many numbers would you like to enter?  "))
            if amount_nums >0:
                break
            else:
                print("You can't enter 0 or lower bud. Try again.")
                continue
        except ValueError:
            print("Not entering a number isn't helping me or you here pal. Enter a number.")

    for i in range(amount_nums):
        while True:
            try:
                temp_num = float(input("Enter a number here:  "))
                numbers.append(temp_num)
                break
            except ValueError:
                print("That isn't a number.")

    numbers.sort()
    div_length = amount_nums %2
    if div_length == 0:
        return (numbers[amount_nums//2] + numbers[(amount_nums//2)-1])/2
    elif amount_nums == 1:
        return numbers[0]
    else:
        return numbers[amount_nums//2]

continue_finding = True
while continue_finding == True:
    print("The median is:", find_median())
    answer = input("Would you like to find another median?  ").lower()
    if answer == "yes" or answer == "y":
        continue_finding = True
    else:
        print("You didn't enter yes or y. Therefore I will self destruct.")
        break
time.sleep(1)
quit()