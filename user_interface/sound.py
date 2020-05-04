import winsound

class Sound(object):

    def play_sound(self, soundFile):
        """Plays a wav file."""
        winsound.PlaySound(soundFile, winsound.SND_ASNC)


    def test_sound(self):
        """Check to see if the sound file works."""
        #
        # The sound files should be in a subfolder right below where your
        # program is. They have to be WAV files and end in .wav"
        #
        soundFile = './sounds/sound.wav'
        Sound.play_sound(soundFile)