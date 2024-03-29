from enum import Enum


class CocoSampleClassMapping(Enum):
    BACKGROUND = 0
    PERSON = 1
    BICYCLE = 2
    CAR = 3
    MOTORCYCLE = 4
    AIRPLANE = 5
    BUS = 6
    TRAIN = 7
    TRUCK = 8
    BOAT = 9
    TRAFFIC_LIGHT = 10
    FIRE_HYDRANT = 11
    STOP_SIGN = 13
    PARKING_METER = 14
    BENCH = 15
    BIRD = 16
    CAT = 17
    DOG = 18
    HORSE = 19
    SHEEP = 20
    COW = 21
    ELEPHANT = 22
    BEAR = 23
    ZEBRA = 24
    GIRAFFE = 25
    BACKPACK = 27
    UMBRELLA = 28
    HANDBAG = 31
    TIE = 32
    SUITCASE = 33
    FRISBEE = 34
    SKIS = 35
    SNOWBOARD = 36
    SPORTS_BALL = 37
    KITE = 38
    BASEBALL_BAT = 39
    BASEBALL_GLOVE = 40
    SKATEBOARD = 41
    SURFBOARD = 42
    TENNIS_RACKET = 43
    BOTTLE = 44
    WINE_GLASS = 46
    CUP = 47
    FORK = 48
    KNIFE = 49
    SPOON = 50
    BOWL = 51
    BANANA = 52
    APPLE = 53
    SANDWICH = 54
    ORANGE = 55
    BROCCOLI = 56
    CARROT = 57
    HOT_DOG = 58
    PIZZA = 59
    DONUT = 60
    CAKE = 61
    CHAIR = 62
    COUCH = 63
    POTTED_PLANT = 64
    BED = 65
    DINING_TABLE = 67
    TOILET = 70
    TV = 72
    LAPTOP = 73
    MOUSE = 74
    REMOTE = 75
    KEYBOARD = 76
    CELL_PHONE = 77
    MICROWAVE = 78
    OVEN = 79
    TOASTER = 80
    SINK = 81
    REFRIGERATOR = 82
    BOOK = 84
    CLOCK = 85
    VASE = 86
    SCISSORS = 87
    TEDDY_BEAR = 88
    HAIR_DRIER = 89
    TOOTHBRUSH = 90

    @staticmethod
    def get_class_id(name):
        return CocoSampleClassMapping.__members__.get(name.upper()).value
    