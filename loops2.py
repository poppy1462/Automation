class Songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)

lyrics2 = ['Oh the weather outside is frightful', 'But the fire is so delightful', 'And since weve no place to go', 'Let It SnowLet It Snow! Let It Snow!']
christmas_song = Songs(lyrics2)

christmas_song.sing_me_a_song()