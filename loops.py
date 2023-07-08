def main():
    count = 3
    
    # define a while loop
    while count < 8:
        print(count)
        count = count + 1

    # define a for loop
    for number in range(8, 15):
        print(number)
    
    # use a for loop over a collection
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for day in days:
        print(day)
  
    # use the break and continue statements
    for number in range(8, 15):
        # if number == 12:
        #     break
        # if number % 2 == 0:
        #     continue
        print(number)
  
    # using the enumerate() function to get index 
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for index, day in enumerate(days):
        print(index, day)
  
if __name__ == "__main__":
    main()
