def plusMinus(arr):
    
    #defining the length of array
    n = len(arr)
    
    #output of arr / n
    positiveCount = 0;
    negativeCount = 0;
    zeroCount = 0;

    #set arr => i
    for i in range(n):
        if i > 0:
            positiveCount += 1
        elif i < 0:
            negativeCount += 1
        elif i == 0:
            zeroCount +=1
    
    # \/ example of how to get decimals
    print ("{:.6f}".format(positiveCount / n))
    print((negativeCount / n))
    print((zeroCount / n))
    print()
    

#module name is stored in name
#main is “Top-level code” is the first user-specified Python module that starts running. It’s “top-level” or "entry point"
if __name__ == '__main__':
    n = int(input().strip())

    #the array to be used
    arr = list(map(int, input().rstrip().split()))


    print("Start if __name__ == '__main__'")
    print('call plusMinus(arr)')
    plusMinus(arr)