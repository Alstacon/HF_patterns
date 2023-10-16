class Tuner:
    def on(self) -> None:
        print('Tuner on')

    def off(self) -> None:
        print('Tuner off')

    def set_am(self) -> None:
        print('Tuner set_am')

    def set_fm(self) -> None:
        print('Tuner set_fm')

    def set_frequency(self) -> None:
        print('Tuner set_frequency')

    def __repr__(self) -> str:
        return 'Tuner'


class Screen:
    def up(self) -> None:
        print('Screen up')

    def down(self) -> None:
        print('Screen down')

    def __repr__(self) -> str:
        return 'Screen'


class PopcornPopper:
    def on(self) -> None:
        print('Popcorn popper on')

    def off(self) -> None:
        print('Popcorn popper off')

    def pop(self) -> None:
        print('Popcorn popper pop')

    def __repr__(self) -> str:
        return 'Popcorn popper'


class TheaterLights:
    def on(self) -> None:
        print('Theater lights on')

    def off(self) -> None:
        print('Theater lights off')

    def dim(self, value: int) -> None:
        print(f'Theater lights dim {value}')

    def __repr__(self) -> str:
        return 'Theater lights'


class Projector:
    def on(self) -> None:
        print('Projector on')

    def off(self) -> None:
        print('Projector off')

    def tv_mode(self) -> None:
        print('Projector tv_mode')

    def wide_screen_mode(self) -> None:
        print('Projector wide_screen_mode')

    def __repr__(self) -> str:
        return 'Projector'


class StreamingPlayer:
    def on(self) -> None:
        print('Streaming player on')

    def off(self) -> None:
        print('Streaming player off')

    def pause(self) -> None:
        print('Streaming player pause')

    def play(self, movie: str) -> None:
        print(f'Streaming player play {movie}')

    def set_surround_audio(self) -> None:
        print('Streaming player set_surround_audio')

    def set_two_channel_audio(self) -> None:
        print('Streaming player set_two_channel_audio')

    def stop(self) -> None:
        print('Streaming player stop')

    def __repr__(self) -> str:
        return 'Streaming player'


class Amplifier:
    def on(self) -> None:
        print('Amplifier on')

    def off(self) -> None:
        print('Amplifier off')

    def set_streaming_player(self, player: StreamingPlayer) -> None:
        print(f'Amplifier set_streaming_player {player}')

    def set_stereo_sound(self) -> None:
        print('Amplifier set_stereo_sound')

    def set_surround_sound(self) -> None:
        print('Amplifier set_surround_sound')

    def set_tuner(self) -> None:
        print('Amplifier set_tuner')

    def set_volume(self, value: int) -> None:
        print(f'Amplifier set_volume {value}')

    def __repr__(self) -> str:
        return 'Stream amplifiering player'
