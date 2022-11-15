from pkg_resources import resource_filename
from simpleaudio import WaveObject

bell = WaveObject.from_wave_file(resource_filename(__name__, "resources/bell.wav"))
