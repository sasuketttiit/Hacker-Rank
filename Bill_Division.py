def bonAppetit(bill, k, b):
    b_actual = 0
    sum = 0
    del(bill[k])
    for item in bill:
        sum += item
    b_actual = int(sum/2)
    if b_actual == b:
        print("Bon Appetit")
    else:
        print(abs(b - b_actual))
