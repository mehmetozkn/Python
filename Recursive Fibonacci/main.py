def fib(stepNum):
    # 1 1 2 3 5 8 13
    faktoriyel = 1 
    if(stepNum == 1 or stepNum == 2):
        return 1
    elif stepNum < 1:
        return 0    
    else:
        return fib(stepNum - 1) + fib(stepNum - 2)

try:
    stepNum = input("Number : ")
    result = fib(stepNum)
    

except NameError:
    print("Yanlis Girdi")

except SyntaxError:
    print("Yanlis Girdi")

finally:
    print("Result : {}".format(result))
    