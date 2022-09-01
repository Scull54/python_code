def fizzBuzz(n):
    # create range
    for fizzbuzz in range(1, n):
        #divisible by certain number
        if fizzbuzz % 15 == 0:
            print("fizzbuzz")
            continue
        elif fizzbuzz % 3 == 0:
            print("fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("buzz")
            continue
        #print created list from n
        print(fizzbuzz)