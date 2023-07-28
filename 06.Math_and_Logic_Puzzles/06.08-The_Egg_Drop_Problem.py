'''
06.08 The Egg Drop Problem: There is a building of 100 floors. If an egg drops from the Nth floor or
    above, it will break. If it's dropped from any floor below, it will not break. You're given two eggs. Find
    N, while minimizing the number of drops for the worst case.
'''

'''
Answer:
    To minimize the number of drops for the worst case, use the binary search approach. Start by dropping
    the first egg from the middle floor (floor 50) and then iteratively move up or down in halves until
    you find the critical floor "N." The maximum number of drops needed with this method is logarithmic
    in the number of floors, which is approximately 7 drops for 100 floors in the worst-case scenario.
'''