'''
Function Description

Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.

countApplesAndOranges has the following parameter(s):

    s: integer, starting point of Sam's house location.
    t: integer, ending location of Sam's house location.
    a: integer, location of the Apple tree.
    b: integer, location of the Orange tree.
    apples: integer array, distances at which each apple falls from the tree.
    oranges: integer array, distances at which each orange falls from the tree.

Input Format

The first line contains two space-separated integers denoting the respective values of
and .
The second line contains two space-separated integers denoting the respective values of and .
The third line contains two space-separated integers denoting the respective values of and .
The fourth line contains space-separated integers denoting the respective distances that each apple falls from point .
The fifth line contains space-separated integers denoting the respective distances that each orange falls from point .
'''
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_ctr = 0
    orange_ctr = 0
    pos_apple = 0
    pos_orange = 0
    for apple in apples:
        pos_apple = a + apple
        if pos_apple >= s and pos_apple <= t:
            apple_ctr += 1
    
    for orange in oranges:
        pos_orange = b + orange
        if pos_orange >= s and pos_orange <= t:
            orange_ctr += 1
    print(apple_ctr)
    print(orange_ctr)
