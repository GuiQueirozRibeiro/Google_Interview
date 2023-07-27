'''
06.01 The Heavy Pill: You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has pills of weight
    1.1 grams. Given a scale that provides an exact measurement, how would you find the heavy bottle?
    You can only use the scale once.
'''

'''
Answer:

1 - Label the bottles from 1 to 20 for identification.
2 - Take one pill from bottle 1, two pills from bottle 2, three pills from bottle 3, and so on, until you take 20 pills from bottle 20, making a total of 210 pills.
3 - Weigh all the collected pills together on the scale.
4 - If the total weight is 210 grams, all bottles contain 1.0 gram pills.
5 - If the total weight is more than 210 grams, the bottle number corresponds to the extra weight in grams (e.g., 210.1 grams would mean bottle 10 has 1.1 gram pills).
'''