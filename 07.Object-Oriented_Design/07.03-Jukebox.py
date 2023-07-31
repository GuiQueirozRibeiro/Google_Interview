'''
07.03 Jukebox: Design a musical jukebox using object-oriented principles.
'''

class Jukebox:
    def __init__(self, cdPlayer, user, cdCollection, ts):
        self.cdPlayer = cdPlayer
        self.user = user
        self.cdCollection = cdCollection
        self.ts = ts

    def getCurrentSong(self):
        return self.ts.getCurrentSong()

    def setUser(self, u):
        self.user = u
        
class CDPlayer:
    def __init__(self, c, p=None):
        self.p = p
        self.c = c

    def playSong(self, s):
        # Implementation for playing a song goes here
        pass

    def getPlaylist(self):
        return self.p

    def setPlaylist(self, p):
        self.p = p

    def getCD(self):
        return self.c

    def setCD(self, c):
        self.c = c
        
class Playlist:
    def __init__(self, song, queue=None):
        self.song = song
        self.queue = queue if queue is not None else []

    def getNextSToPlayQ(self):
        return self.queue[0] if self.queue else None

    def queueUpSong(self, s):
        self.queue.append(s)

class CD:
    # Data for id, artist, songs, etc goes here
    pass


class Song:
    # Data for id, CD (could be null), title, length, etc goes here
    pass


class User:
    def __init__(self, name, iD):
        self.name = name
        self.ID = iD

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getID(self):
        return self.ID

    def setID(self, iD):
        self.ID = iD

    @staticmethod
    def addUser(name, iD):
        return User(name, iD)