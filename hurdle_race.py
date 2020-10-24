def hurdleRace(k, height):
    potion = 0
    max_jump = max(height)
    if k < max_jump:
        potion = max_jump - k
    return potion
