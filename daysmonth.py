month=int(input("enter month"))
year=int(input("enter year"))
if (month==1) or (month==3) or (month==5) or (month==7) or (month==8) or (month==10) or (month==12):
    print("31 days")
elif (year%4==0 and month==2):
    print("29 days")
elif (year%4!=0 and month==2):
    print("28 days")
else:
    print("30 days")