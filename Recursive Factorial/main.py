
def fac(sayi):
    faktoriyel = 1
    if(sayi == 1):
        return 1
    else:
        return sayi * fac(sayi - 1)



sayi = input("Sayi : ")
result = fac(sayi)
print("Sonuc : {}".format(result))
    