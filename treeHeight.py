def utopianTree(n):
    height = 0
    if n == 0:
        return 1
    else:
        for period in range(n+1):
            if period % 2 == 0:
                height += 1
            elif period % 2 != 0:
                height = height *2
        return height
