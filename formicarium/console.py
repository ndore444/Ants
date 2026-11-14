from .config import PALETTE

#turns markup into a list of (char, color) pairs.
def parse_markup(s, fg):
    out = []
    color = fg
    i = 0
    while i < len(s):
        c = s[i]
        if c == "&" and i + 1 < len(s):
            nxt = s[i + 1]
            if nxt == "&":                  # && - one real &
                out.append(("&", color))
                i += 2
                continue
            if nxt in PALETTE:              # &R - switch color, draw nothing
                color = PALETTE[nxt]
                i += 2
                continue
        out.append((c, color))          # reg char
        i += 1
    return out
