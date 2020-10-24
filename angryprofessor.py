def angryProfessor(k, a):
    count_ontime = 0
    for time in a:
        if time <= 0:
            count_ontime += 1
    if count_ontime >= k:
        return 'NO'
    else:
        return 'YES'
