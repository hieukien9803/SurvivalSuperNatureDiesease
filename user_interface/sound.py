import winsound


def play_sound(soundFile):
    """Plays a wav file."""
    winsound.PlaySound(soundFile, winsound.SND_FILENAME)


def rain_sound():
    soundFile = 'user_interface/sounds/rain.wav'
    play_sound(soundFile)


def night_sound():
    soundFile = 'user_interface/sounds/night.wav'
    play_sound(soundFile)


def noon_sound():
    soundFile = 'user_interface/sounds/noon.wav'
    play_sound(soundFile)


def button_sound():
    soundFile = 'user_interface/sounds/button.wav'
    play_sound(soundFile)


def page_sound():
    soundFile = 'user_interface/sounds/page_flip.wav'
    play_sound(soundFile)
