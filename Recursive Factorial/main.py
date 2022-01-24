
def fac(num):
    faktoriyel = 1
    if(num == 1):
        return 1
    else:
        return num * fac(num - 1)



num = input("Number : ")
result = fac(num)
print("Result : {}".format(result))
    