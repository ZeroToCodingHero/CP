class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pocket full of shells"])

another_song = Song(["This is another song ..."])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

another_song.sing_me_a_song()


'''
import mystuff # get apple from dict

mystuff.apple() # get apple from the module
print(mystuff.tangerine) # same thing, it's just a variable

'''