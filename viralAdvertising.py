def viralAdvertising(n):
    shares = 5
    likes = total = 0
    for day in range(1,n+1):
        likes = shares//2
        shares = likes * 3
        total += likes
    return total
