try:
    from enum import StrEnum
except ImportError:
    from enum import Enum

    class StrEnum(str, Enum):
        pass


class Colour(StrEnum):
    # colour pallet
    colour1 = "#B8D8D8"
    colour2 = "#7A9E9F"
    colour3 = "#4F6367"
    colour4 = "#EEF5DB"
    colour5 = "#FE5F55"
