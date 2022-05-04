class Board:

    def __init__(self, size, blocks):
        self.size = size
        self.blocks_empty_info = filling(blocks, size)

    def print_blocks_empty_info(self):
        print(self.blocks_empty_info)

#Judge to see if the board's info is valid
def is_board_valid(blocks, start, end, size):
    if is_blocks_valid(blocks,size) and is_start_end_valid(start, end,size):
        return True
    return False


def is_blocks_valid(blocks,size):
    for block in blocks:
        if block[1] >= size or block[2] >= size:
            return False
    return True

def is_start_end_valid(start, end, size):
    if start[0] >= size or end[0] >= size or start[1] >= size or end[1] >= size:
        return False
    return True

#fill out the map according to board's info
def filling(blocks, size):
    map = {}
    for i in range(0,size):
        for j in range(0, size):
            map.update({(i, j): "empty"})
            for block in blocks:
                if block[1] == i and block[2] == j:
                    map[(i,j)] = "b"
    return map

def iterative_print(lst):
    if lst[0] == "0":
        print(0)
    else:
        print(len(lst))
        for i in lst:
            if i == 0:
                break
            print(i)
