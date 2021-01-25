# Song Class - an Introductory Class

class Song(object):

    def __init__(self, lyrics):
        """Initializer with lyrics"""
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        """Sings the song lyrics"""
        print("")
        for line in self.lyrics:
            print(line)

    def sing_reverse(self):
        """Sings the song lyrics in reverse"""
        print("")
        song_length = len(self.lyrics) * -1
        starting = -1
        line = self.lyrics[starting]
        while line:
            print(line)
            starting += -1
            if starting < song_length:
                break
            line = self.lyrics[starting]

happy_bday_song = Song(["Happy birthday to you",
                        "I don't want to be sued",
                        "So I'll stop right here..."])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells."])

hot_cross_buns = Song(["Hot cross buns", "Hot cross buns", 
                            "One a penny, two a penny"])

mary_lyrics = ["Mary had a little lamb",
                        "litte lam, little lamb",
                        "Mary had a little lamb",
                        "Its fleece was white as snow."]
mary_little_lamb = Song(mary_lyrics)

happy_bday_song.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
hot_cross_buns.sing_me_a_song()
mary_little_lamb.sing_me_a_song()

hot_cross_buns.sing_reverse()