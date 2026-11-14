TITLE = "Formicarium"


#Screen Layout
#screen is a grid of cells that contain objects/characters. 
#---------------------------------------------------------------------------------------------------------------------------------------
CELL_W, CELL_H = 12,18      #pixels per cell - 2 wide, 3 tall (following Cave's of Qud Style)
COLS, ROWS = 100,45         #Whole window, in cells.
FPS = 30
FONT_FILE = "assets/DejaVuSansMono.ttf"

#Color Palette 
#Theme inspired by Caves of Qud
#lower = dark, upper = bright.
#---------------------------------------------------------------------------------------------------------------------------------------
PALETTE = {
"k": (15, 59, 58),    "K": (21, 83, 82),
"r": (166, 74, 46),   "R": (215, 66, 0),
"o": (241, 95, 34),   "O": (233, 159, 16),
"w": (152, 135, 95),  "W": (207, 192, 65),
"g": (0, 148, 3),     "G": (0, 196, 32),
"b": (0, 72, 189),    "B": (0, 150, 255),
"c": (64, 164, 185),  "C": (119, 191, 207),
"m": (177, 84, 207),  "M": (218, 91, 214),
"y": (177, 201, 195), "Y": (255, 255, 255),
}

BG = (8, 27, 28)    #Background teal
FRAME = (21,83,82)  #UI frame lines


