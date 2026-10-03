import re

def findPlacements(pattern, edge = 5,constraint = []):
    if constraint is None:
        constraint = set()
    else:
        constraint = set(constraint)

    # the pattern is a tuple list
    min_row = min(tile[0] for tile in pattern)
    min_col = min(tile[1] for tile in pattern)

    max_row = max (tile[0] for tile in pattern)
    max_col = max (tile[1] for tile in pattern)

    height = max_row - min_row + 1
    width = max_col - min_col + 1

    start_pattern = [(tile[0]-min_row, tile[1]-min_col) for tile in pattern]

    placements = []

    
    for i in range(0,edge-height+1):
        for j in range(0,edge-width+1):

            shifted = frozenset((tile[0]+i,tile[1]+j) for tile in start_pattern)
            if shifted.isdisjoint(constraint):
                placements.append(shifted)

    
    return frozenset(placements)

def parse_coord(raw: str, max=float('inf')): #this is called a type hint, tells us that raw is expected to be a string

    digits = re.findall(r"\d+",raw)
    if len(digits) == 2:
        r,c = int(digits[0]), int(digits[1])
        if r <= max and c <= max and r > 0 and c > 0:
            return (r,c)
    return None


