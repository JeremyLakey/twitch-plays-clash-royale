VALID_CARD_NAMES = [
"knight",
"archers",
"goblins",
"giant",
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
"royal giant",
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
    if card == "knight" or card == "night":
        return "knight"

    elif card == "archers":
        return "archers"

    elif card == "goblins":
        return "goblins"

    elif card == "giant":
        return "giant"

    elif card == "pekka":
        return "pekka"

    elif card == "minions":
        return "minions"

    elif card == "balloon" or card == "ballon" or card == "baloon":
        return "balloon"

    elif card == "witch":
        return "witch"

    elif card == "barbarians" or card == "barb" or card == "barbs":
        return "barbarians"

    elif card == "golem":
        return "golem"

    elif card == "skeletons" or card == "skeleton" or card == "larry":
        return "skeletons"

    elif card == "valkyrie" or card == "valk":
        return "valkyrie"

    elif card == "skeleton army" or card == "skarmy":
        return "skeleton army"

    elif card == "bomber" or card == "barry":
        return "bomber"

    elif card == "musketeer":
        return "musketeer"

    elif card == "baby dragon":
        return "baby dragon"

    elif card == "prince":
        return "prince"

    elif card == "wizard":
        return "wizard"

    elif card == "mini pekka":
        return "mini pekka"

    elif card == "spear goblins":
        return "spear goblins"

    elif card == "giant skeleton":
        return "giant skeleton"

    elif card == "hog rider":
        return "hog rider"

    elif card == "minion horde" or card == "horde":
        return "minion horde"

    elif card == "ice wizard":
        return "ice wizard"

    elif card == "royal giant":
        return "royal giant"

    elif card == "guards":
        return "guards"

    elif card == "princess":
        return "princess"

    elif card == "dark prince":
        return "dark prince"

    elif card == "three musketeers":
        return "three musketeers"

    elif card == "lava hound" or card == "hound":
        return "lava hound"

    elif card == "ice spirit":
        return "ice spirit"

    elif card == "fire spirit":
        return "fire spirit"

    elif card == "miner" or card == "minor":
        return "miner"

    elif card == "sparky":
        return "sparky"

    elif card == "bowler":
        return "bowler"

    elif card == "lumberjack" or card == "lumber jack":
        return "lumberjack"

    elif card == "battle ram":
        return "battle ram"

    elif card == "inferno dragon":
        return "inferno dragon"

    elif card == "ice golem":
        return "ice golem"

    elif card == "mega minion" or card == "meta minion":
        return "mega minion"

    elif card == "dart goblin":
        return "dart goblin"

    elif card == "goblin gang":
        return "goblin gang"

    elif card == "electro wizard" or card == "e wizard" or card == "ewizard":
        return "electro wizard"

    elif card == "elite barbarians" or card == "e barbs" or card == "ebarbs":
        return "elite barbarians"

    elif card == "hunter":
        return "hunter"

    elif card == "executioner":
        return "executioner"

    elif card == "bandit":
        return "bandit"

    elif card == "royal recruits" or card == "recruits":
        return "royal recruits"

    elif card == "night witch":
        return "night witch"

    elif card == "bats":
        return "bats"

    elif card == "royal ghost" or card == "ghost":
        return "royal ghost"

    elif card == "ram rider":
        return "ram rider"

    elif card == "zappies":
        return "zappies"

    elif card == "rascals":
        return "rascals"

    elif card == "cannon card":
        return "cannon card"

    elif card == "mega knight":
        return "mega knight"

    elif card == "skeleton barrel":
        return "skeleton barrel"

    elif card == "flying machine":
        return "flying machine"

    elif card == "wall breakers":
        return "wall breakers"

    elif card == "royal hogs":
        return "royal hogs"

    elif card == "goblin giant":
        return "goblin giant"

    elif card == "fisherman" or card == "fisher man":
        return "fisherman"

    elif card == "magic archer":
        return "magic archer"

    elif card == "electro dragon" or card == "edragon" or card == "edrag" or card == "e dragon" or card == "e drag":
        return "electro dragon"

    elif card == "firecracker" or card == "fire cracker":
        return "firecracker"

    elif card == "mighty miner" or card == "mighty minor":
        return "mighty miner"

    elif card == "elixir golem" or card == "egolem" or card == "e golem":
        return "elixir golem"

    elif card == "battle healer" or card == "healer":
        return "battle healer"

    elif card == "skeleton king":
        return "skeleton king"

    elif card == "archer queen" or card == "queen":
        return "archer queen"

    elif card == "golden knight":
        return "golden knight"

    elif card == "monk":
        return "monk"

    elif card == "skeleton dragons":
        return "skeleton dragons"

    elif card == "mother witch" or card == "mother":
        return "mother witch"

    elif card == "electro spirit":
        return "electro spirit"

    elif card == "electro giant":
        return "electro giant"

    elif card == "phoenix":
        return "phoenix"

    elif card == "little prince":
        return "little prince"

    elif card == "cannon":
        return "cannon"

    elif card == "goblin hut":
        return "goblin hut"

    elif card == "mortar" or card == "morter" or card == "mortor":
        return "mortar"

    elif card == "inferno tower":
        return "inferno tower"

    elif card == "bomb tower":
        return "bomb tower"

    elif card == "barbarian hut":
        return "barbarian hut"

    elif card == "tesla" or card == "hidden telsa":
        return "tesla"

    elif card == "elixir pump" or card == "pump":
        return "elixir pump"

    elif card == "x-bow" or card == "xbow":
        return "x-bow"

    elif card == "tombstone" or card == "tomb stone":
        return "tombstone"

    elif card == "furnace":
        return "furnace"

    elif card == "goblin cage" or card == "cage":
        return "goblin cage"

    elif card == "goblin drill" or card == "drill":
        return "goblin drill"

    elif card == "fireball":
        return "fireball"

    elif card == "arrows" or card == "arrow":
        return "arrows"

    elif card == "rage":
        return "rage"

    elif card == "rocket":
        return "rocket"

    elif card == "goblin barrel":
        return "goblin barrel"

    elif card == "freeze":
        return "freeze"

    elif card == "mirror":
        return "mirror"

    elif card == "lightning":
        return "lightning"

    elif card == "zap":
        return "zap"

    elif card == "poison":
        return "poison"

    elif card == "graveyard" or card == "grave yard":
        return "graveyard"

    elif card == "log":
        return "log"

    elif card == "tornado":
        return "tornado"

    elif card == "clone":
        return "clone"

    elif card == "earthquake" or card == "earth quake":
        return "earthquake"

    elif card == "barbarian barrel":
        return "barbarian barrel"

    elif card == "heal spirit":
        return "heal spirit"

    elif card == "giant snowball" or card == "snowball":
        return "giant snowball"

    elif card == "royal delivery" or card == "delivery":
        return "royal delivery"

    elif card == "void":
        return "void"