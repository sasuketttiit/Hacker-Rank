def pickingNumbers(a):
    # Write your code here
    max = 0
    for i in a:
        c = a.count(i)
        d = a.count(i-1)
        c += d
        if c > max:
            max = c
    return max
