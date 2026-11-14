import os
import sys

#Python finds the pckg in the folder above this one
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from formicarium.config import PALETTE
from formicarium.console import parse_markup

grey, red = PALETTE["y"], PALETTE["R"]

assert parse_markup("&Rhi&y!", grey) == [("h", red), ("i", red), ("!", grey)]
assert parse_markup("A&&B", grey) == [("A", grey), ("&", grey), ("B", grey)]
assert parse_markup("50&", grey)[-1] == ("&", grey)    # a lone & at the end is kept
assert parse_markup("&Zoo", grey)[0] == ("&", grey)    # & + a non-colour letter is kept
print("parse_markup: all good")