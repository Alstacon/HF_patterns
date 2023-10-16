from chapter_7 import home_theater


class HomeTheaterFacade:
    amplifier = home_theater.Amplifier()
    tuner = home_theater.Tuner()
    streaming_player = home_theater.StreamingPlayer()
    projector = home_theater.Projector()
    theater_lights = home_theater.TheaterLights()
    screen = home_theater.Screen()
    popcorn_popper = home_theater.PopcornPopper()

    def watch_movie(self, movie):
        print(f'''Get ready to watch a movie {movie}''')
        self.popcorn_popper.on()
        self.popcorn_popper.pop()
        self.theater_lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amplifier.on()
        self.amplifier.set_streaming_player(self.streaming_player)
        self.amplifier.set_surround_sound()
        self.amplifier.set_volume(5)
        self.streaming_player.on()
        self.streaming_player.play(movie)

    def end_movie(self):
        print(f'''Shutting movie theater down''')
        self.popcorn_popper.off()
        self.theater_lights.on()
        self.screen.up()
        self.projector.off()
        self.amplifier.off()
        self.streaming_player.stop()
        self.streaming_player.off()
