import winsound


# Play the available sound for the game
def play_sound(soundFile):
    """Plays a wav file."""
    winsound.PlaySound(soundFile, winsound.SND_FILENAME)


def eat_sound():
    soundFile = 'user_interface/sounds/eat.wav'
    play_sound(soundFile)


def drink_sound():
    soundFile = 'user_interface/sounds/drink.wav'
    play_sound(soundFile)


def playSound():
    soundFile = 'user_interface/sounds/play.wav'
    play_sound(soundFile)


def button_sound():
    soundFile = 'user_interface/sounds/button.wav'
    play_sound(soundFile)


def page_sound():
    soundFile = 'user_interface/sounds/page_flip.wav'
    play_sound(soundFile)
