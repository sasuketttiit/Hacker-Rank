def dayReverse(num):
    sum = rem = 0
    while num > 0:
        rem = num % 10
        sum = sum*10 + rem
        num = num//10
    return sum

def beautifulDays(i, j, k):
    count = reverse = 0
    for day in range(i,j+1):
        reverse = dayReverse(day)
        if abs(day-reverse)%k == 0:
            count += 1
    return count
