def catAndMouse(x, y, z):
    dist_A = dist_B = 0
    dist_A = abs(x-z)
    dist_B = abs(y-z)
    if dist_A == dist_B:
        return 'Mouse C'
    elif dist_A < dist_B:
        return 'Cat A'
    else:
        return 'Cat B'
