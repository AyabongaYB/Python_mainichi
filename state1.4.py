hrs = input("Enter Hours: ")
h = float(hrs)
rts = input("Enter Rates: ")
r = float(rts)

if h <= 40:
    grossPay = h * r
elif h > 40:
    nhrs = 40
    xhrs = h - nhrs
    temp = h * r
    temp2 = xhrs * 1.5

    grossPay = (40*r) + xhrs * (1.5*r)

print(grossPay)