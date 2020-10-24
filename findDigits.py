def findDigits(n):
    temp = n
    count = 0
    for digit in str(n):
        if int(digit) != 0:
            if temp % int(digit) == 0:
                count +=1
    return count
