'''
06.04 Ants on a Triangle: There are three ants on different vertices of a triangle. What is the probability of
    collision (between any two or all of them) if they start walking on the sides of the triangle? Assume
    that each ant randomly picks a direction, with either direction being equally likely to be chosen, and
    that they walk at the same speed.

    Similarly, find the probability of collision with n ants on an n-vertex polygon.
'''

'''
Answer:
    1)
    Three Ants on a Triangle:
        Each of the three ants on a triangle has two choices (clockwise or counterclockwise),
        resulting in 8 possible outcomes. Only two of these outcomes lead to a collision. Thus, the
        probability of collision is 1/4 (25%).

    2)
    n Ants on an n-Vertex Polygon:
        For n ants on an n-vertex polygon, each ant has two choices of direction. The probability of
    collision occurs when two ants move in opposite directions and meet at a vertex. The
    probability of this happening is 1/2 (50%).

    In conclusion, for three ants on a triangle, the probability of collision is 1/4 (25%),
    and for n ants on an n-vertex polygon, the probability of collision is 1/2 (50%).
'''