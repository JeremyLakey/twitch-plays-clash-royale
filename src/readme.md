# Twitch Plays Bot for CR

This twitch bot reads twitch chat and interprets them into clash royale moves.

This project requires a bit more set up than most.

# Setup
## Downloads

Get and install [python 3.9.0](https://www.python.org/downloads/release/python-390/). You can try any version of python, but I haven't tested on other versions.

Clone the repo `git clone https://github.com/JeremyLakey/twitch-plays-clash-royale.git`

In a terminal go inside the folder `/pythonProject5` and run `pip install -r requirements.txt`

You also need an emulator of some kind. I use Bluestacks 5. It just needs hot keys you can set up.

## Calibrate

To Calibrate, you have to run a series of different calibrate programs. 

Each calibrate program will have a list of spots to hover over in the ui. 

You can move onto the next spot after you hear the beep.

Go to `/pythonProject5/calibrate` folder to get started. 

Make sure to do each calibration 

### Chests Calibration

run `python chest.py`

Spot 1: Left Chest Slot

Spot 2: Second from Left Chest Slot

Spot 3: Second from Right Chest Slot

Spot 4: Right Chest Slot

Spot 5: Click on a check and Hover over the open button

### Edit Deck Calibration

run `python editDeck.py`

Spot 1: Top left card slot

Spot 2: Bottom right card slot

### Menu Calibration

run `python menuActions.py`

For this one, go back to the middle button each time.

Spot 1: Shop Button

Spot 2: Deck Button

Spot 3: Swords button


### Scroll Calibration

run `python scroll.py`

Spot 1: Middle of screen

Spot 2: Move up one quarter of the screen

### Safe Spot Calibration

run `python emotes.py`

Spot 1: click near bottom of swords button on menu

### Emote Calibration

run `python emotes.py`

Go into a battle

Spot 1: Emote button

Spot 2: Top left emote

Spot 3: Bottom right emote


## Setting up hot keys

WIP

