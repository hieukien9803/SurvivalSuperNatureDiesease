import winsound


def play_sound(soundFile):
    """Plays a wav file."""
    winsound.PlaySound(soundFile, winsound.SND_FILENAME)
def eat_sound():
    soundFile = 'user_interface/sounds/eat.wav'
    play_sound(soundFile)

def drink_sound():
    soundFile = 'user_interface/sounds/drink.wav'
    play_sound(soundFile)

def scary():
    soundFile = 'user_interface/sounds/scary.wav'
    play_sound(soundFile)

def playSound():
    soundFile = 'user_interface/sounds/play.wav'
    play_sound(soundFile)

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
