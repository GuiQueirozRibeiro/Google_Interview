'''
06.06 Blue-Eyed Island: A bunch of people are living on an island, when a visitor comes with a strange
    order: all blue-eyed people must leave the island as soon as possible. There will be a flight out at
    8:00 pm every evening. Each person can see everyone else's eye color, but they do not know their
    own (nor is anyone allowed to tell them). Additionally, they do not know how many people have
    blue eyes, although they do know that at least one person does. How many days will it take the
    blue-eyed people to leave?
'''

'''
Answer:
      The blue-eyed people know that there is at least one blue-eyed person on the island since
    the visitor's order explicitly states so.
      On the first evening after the announcement, each blue-eyed person sees "n-1" other
    blue-eyed people (where "n" is the total number of blue-eyed people on the island).
      Each blue-eyed person reasons that if there were only "n-1" blue-eyed people, those people
    would leave on the first evening because they would all see "n-2" other blue-eyed people.
      Since no one leaves on the first evening, it means that there must be "n" blue-eyed
    people, including themselves.
      Now that they know they are blue-eyed and there are "n" of them, on the second evening,
    all "n" blue-eyed people will leave the island together at 8:00 pm.

    Therefore, it takes one day for all the blue-eyed people to leave the island.
'''