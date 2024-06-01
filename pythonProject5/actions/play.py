import pyautogui

def _play_card(file, pos):
    pyautogui.press(pos)

def play_card(card, pos):
    if card == "knight":

    elif card == "archers":

    elif card == "goblins":

    elif card == "gaint":

    elif card == "pekka":

    elif card == "minions":

    elif card == "balloon":

    elif card == "witch":

    elif card == "barbarians":

    elif card == "golem":

    elif card == "skeleton":

    elif card == "valkyrie":

    elif card == "skeleton army":

    elif card == "bomber":

    elif card == "musketeer":

    elif card == "baby dragon":

    elif card == "prince":

    elif card == "wizard":

    elif card == "mini pekka":

    elif card == "spear goblins":

    elif card == "giant skeleton":

    elif card == "hog rider":

    elif card == "minion horde":

    elif card == "ice wizard":

    elif card == "royal gaint":

    elif card == "guards":

    elif card == "princess":

    elif card == "dark prince":

    elif card == "three musketeers":

    elif card == "lava hound":

    elif card == "ice spirit":

    elif card == "fire spirit":

    elif card == "miner":

    elif card == "sparky":

    elif card == "bowler":

    elif card == "lumberjack":

    elif card == "battle ram":

    elif card == "inferno dragon":

    elif card == "ice golem":

    elif card == "mega minion":

    elif card == "dart goblin":

    elif card == "goblin gang":

    elif card == "electro wizard":

    elif card == "elite barbarians":

    elif card == "hunter":

    elif card == "executioner":

    elif card == "bandit":

    elif card == "royal recruits":

    elif card == "night witch":

    elif card == "bats":

    elif card == "royal ghost":

    elif card == "ram rider":

    elif card == "zappies":

    elif card == "rascals":

    elif card == "cannon card":

    elif card == "mega knight":

    elif card == "skeleton barrel":

    elif card == "flying machine":

    elif card == "wall breakers":

    elif card == "royal hogs":

    elif card == "goblin giant":

    elif card == "fisherman":

    elif card == "magic archer":

    elif card == "electro dragon":

    elif card == "firecracker":

    elif card == "mighty miner":

    elif card == "elixir golem":

    elif card == "battle healer":

    elif card == "skeleton king":

    elif card == "archer queen":

    elif card == "golden knight":

    elif card == "monk":

    elif card == "skeleton dragons":

    elif card == "mother witch":

    elif card == "electro spirit":

    elif card == "electro giant":

    elif card == "phoenix":

    elif card == "little prince":
        
    elif card =="cannon":
        
    elif card =="goblin hut":
        
    elif card =="mortar":
        
    elif card =="inferno tower":
        
    elif card =="bomb tower":
        
    elif card =="barbarian hut":
        
    elif card =="tesla":
        
    elif card =="elixir pump":
        
    elif card =="x-bow":
        
    elif card =="tombstone":
        
    elif card =="furnace":
        
    elif card =="goblin cage":
        
    elif card =="goblin drill":
        
    elif card =="fireball":
        
    elif card =="arrows":
        
    elif card =="rage":
        
    elif card =="rocket":
        
    elif card =="goblin barrel":
        
    elif card =="freeze":
        
    elif card =="mirror":
        
    elif card =="lightning":
        
    elif card =="zap":
        
    elif card =="poison":
        
    elif card =="graveyard":
        
    elif card =="log":
        
    elif card =="tornado":
        
    elif card =="clone":
        
    elif card =="earthquake":
        
    elif card =="barbarian barrel":
        
    elif card =="heal spirit":
        
    elif card =="giant snowball":
        
    elif card =="royal delivery":
        
    elif card =="void":


# returns tuple of troop name and card
# returns None on failure to parse
def valid_play_command(content: str):
    c = content.lower().split(" ")
    if len(c) == 2 and validate_1_word_card(c[0]) and validate_position(c[1]):
        return c[0], c[1]
    elif len(c) == 3:
        return c[0] + " " + c[1], c[2]

    return None, None

VALID_CARD_NAMES = [
"knight",
"archers",
"goblins",
"gaint",
"pekka",
"minions",
"balloon",
"witch",
"barbarians",
"golem",
"skeleton",
"valkyrie",
"skeleton army",
"bomber",
"musketeer",
"baby dragon",
"prince",
"wizard",
"mini pekka",
"spear goblins",
"giant skeleton",
"hog rider"
"minion horde",
"ice wizard",
"royal gaint",
"guards",
"princess",
"dark prince",
"three musketeers",
"lava hound",
"ice spirit",
"fire spirit",
"miner",
"sparky",
"bowler",
"lumberjack",
"battle ram",
"inferno dragon",
"ice golem"
"mega minion",
"dart goblin",
"goblin gang",
"electro wizard",
"elite barbarians",
"hunter",
"executioner",
"bandit",
"royal recruits",
"night witch",
"bats",
"royal ghost",
"ram rider",
"zappies",
"rascals",
"cannon card",
"mega knight",
"skeleton barrel",
"flying machine",
"wall breakers",
"royal hogs",
"goblin giant",
"fisherman",
"magic archer",
"electro dragon",
"firecracker",
"mighty miner",
"elixir golem",
"battle healer"
"skeleton king",
"archer queen",
"golden knight",
"monk",
"skeleton dragons",
"mother witch",
"electro spirit",
"electro giant",
"phoenix",
"little prince",
"cannon",
"goblin hut",
"mortar",
"inferno tower",
"bomb tower",
"barbarian hut",
"tesla",
"elixir pump",
"x-bow",
"tombstone",
"furnace",
"goblin cage",
"goblin drill",
"fireball",
"arrows",
"rage",
"rocket",
"goblin barrel",
"freeze",
"mirror",
"lightning",
"zap",
"poison",
"graveyard",
"log",
"tornado",
"clone",
"earthquake",
"barbarian barrel",
"heal spirit",
"giant snowball",
"royal delivery",
"void",
]
def validate_card_name(card):
    if card == "knight" or "night":

    elif card == "archers":

    elif card == "goblins":

    elif card == "giant":

    elif card == "pekka":

    elif card == "minions":

    elif card == "balloon" or "ballon" or "baloon":

    elif card == "witch":

    elif card == "barbarians" or "barb" or "barbs":

    elif card == "golem":

    elif card == "skeletons" or "larry":

    elif card == "valkyrie" or "valk":

    elif card == "skeleton army":

    elif card == "bomber" or "barry":

    elif card == "musketeer":

    elif card == "baby dragon":

    elif card == "prince":

    elif card == "wizard":

    elif card == "mini pekka":

    elif card == "spear goblins":

    elif card == "giant skeleton":

    elif card == "hog rider":

    elif card == "minion horde" or "horde":

    elif card == "ice wizard":

    elif card == "royal giant":

    elif card == "guards":

    elif card == "princess":

    elif card == "dark prince":

    elif card == "three musketeers":

    elif card == "lava hound" or "hound":

    elif card == "ice spirit":

    elif card == "fire spirit":

    elif card == "miner" or "minor":

    elif card == "sparky":

    elif card == "bowler":

    elif card == "lumberjack" or "lumber jack":

    elif card == "battle ram":

    elif card == "inferno dragon":

    elif card == "ice golem":

    elif card == "mega minion":

    elif card == "dart goblin":

    elif card == "goblin gang":

    elif card == "electro wizard":

    elif card == "elite barbarians":

    elif card == "hunter":

    elif card == "executioner":

    elif card == "bandit":

    elif card == "royal recruits":

    elif card == "night witch":

    elif card == "bats":

    elif card == "royal ghost":

    elif card == "ram rider":

    elif card == "zappies":

    elif card == "rascals":

    elif card == "cannon card":

    elif card == "mega knight":

    elif card == "skeleton barrel":

    elif card == "flying machine":

    elif card == "wall breakers":

    elif card == "royal hogs":

    elif card == "goblin giant":

    elif card == "fisherman" or "fisher man":

    elif card == "magic archer":

    elif card == "electro dragon":

    elif card == "firecracker" or "fire cracker":

    elif card == "mighty miner":

    elif card == "elixir golem":

    elif card == "battle healer":

    elif card == "skeleton king":

    elif card == "archer queen":

    elif card == "golden knight":

    elif card == "monk":

    elif card == "skeleton dragons":

    elif card == "mother witch":

    elif card == "electro spirit":

    elif card == "electro giant":

    elif card == "phoenix":

    elif card == "little prince":

    elif card == "cannon":

    elif card == "goblin hut":

    elif card == "mortar":

    elif card == "inferno tower":

    elif card == "bomb tower":

    elif card == "barbarian hut":

    elif card == "tesla" or "hidden telsa":

    elif card == "elixir pump":

    elif card == "x-bow" or "xbow":

    elif card == "tombstone":

    elif card == "furnace":

    elif card == "goblin cage":

    elif card == "goblin drill":

    elif card == "fireball":

    elif card == "arrows" or "arrow":

    elif card == "rage":

    elif card == "rocket":

    elif card == "goblin barrel":

    elif card == "freeze":

    elif card == "mirror":

    elif card == "lightning":

    elif card == "zap":

    elif card == "poison":

    elif card == "graveyard" or "grave yard":

    elif card == "log":

    elif card == "tornado":

    elif card == "clone":

    elif card == "earthquake" or "earth quake":

    elif card == "barbarian barrel":

    elif card == "heal spirit":

    elif card == "giant snowball" or "snowball":

    elif card == "royal delivery":

    elif card == "void":
    


VALID_POSITIONS = [
    "a","b","c","d","e","f","u","v","g","y","h","i","j","k","z","l","w","x","m","n","o","p","q","r","s","t","3","0","4","1","5","6","2","7","8","9"
]
def validate_position(pos):
    if pos in VALID_POSITIONS:
        return True