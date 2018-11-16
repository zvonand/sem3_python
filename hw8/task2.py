def turtle (coord, direction):
    dirs = [[1, 0], [0,1], [-1, 0], [0, -1]]
    currchg = dirs[direction]
    coord = list (coord)
    nxt = yield coord
    while nxt:
        if nxt == 'l':
            direction = (direction + 1) % 4
        elif nxt == 'r':
            direction = (direction + 3) % 4
        elif nxt == 'f':
            currchg = dirs[direction]
            coord[0] += currchg[0]
            coord[1] += currchg[1]
        nxt = yield coord
