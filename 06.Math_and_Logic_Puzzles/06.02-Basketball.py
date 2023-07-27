'''
06.02 Basketball: You have a basketball hoop and someone says that you can play one of two games.

    Game 1: You get one shot to make the hoop.
    Game 2: You get three shots and you have to make two of three shots.

    If p is the probability of making a particular shot, for which values of p should you pick one game
    or the other?
'''

'''
Answer:

Game 1: One Shot
    Probability of winning = p (the probability of making the shot)
    
Game 2: Three Shots, Make Two
    Probability of winning = 2 * p^2 * (1 - p)
    
Choose Game 1 if p > 2 * p^2 * (1 - p), otherwise choose Game 2
In other words, if your probability of making a shot (p) is greater than twice the probability of making two out of three shots (2 * p^2 * (1 - p)), then pick Game 1. Otherwise, pick Game 2.
'''