from pkg_resources import resource_filename
from simpleaudio import WaveObject


class Bell:
    def __init__(self) -> None:
        self.wave_obj = WaveObject.from_wave_file(
            resource_filename(__name__, "resources/bell.wav")
        )

    def play_sync(self) -> None:
        play_obj = self.wave_obj.play()
        play_obj.wait_done()
