if __name__ == "__main__":
    numbers = [1,2,3,4,5]
    listlen = len(numbers)
    print(f"The list is {numbers}")
    print(f"The length of the list is {listlen}")
    sum_numbers = 0
    # for i in range(listlen):
    #     print (f"i is {i}")
    #     print(f"Adding {numbers[i]} to the sum")
    #     sum_numbers += numbers[i]
    i= 0
    while i < listlen:
        print (f"i is {i}")
        print(f"Adding {numbers[i]} to the sum")
        sum_numbers += numbers[i]
        i+=1
    print(f"The sum of the numbers is {sum_numbers}")