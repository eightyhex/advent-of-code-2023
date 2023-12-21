
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


def find_path_length(direction,x,y,map):
    if x < 0 or y >= len(map[0]) or x >= len(map) or y < 0 or map[x][y] in ['.','S']:
        return 0

    next_value = map[x][y]

    if direction == NORTH:
        '''
        |
        F
        7
        '''
        if next_value == '|':
            return 1 + find_path_length(NORTH,x-1,y,map)
        elif next_value == 'F':
            return 1+ find_path_length(EAST,x,y+1,map)
        elif next_value == '7':
            return 1 + find_path_length(WEST,x,y-1,map)
        return 0

    if direction == SOUTH:
        '''
        |
        L
        J
        '''
        if next_value == '|':
            return 1 + find_path_length(SOUTH,x+1,y,map)
        elif next_value == 'L':
            return 1 + find_path_length(EAST,x,y+1,map)
        elif next_value == 'J':
            return 1 + find_path_length(WEST,x,y-1,map)
        return 0

    if direction == WEST:
        '''
        -
        L
        F
        '''
        if next_value == '-':
            return 1 + find_path_length(WEST,x,y-1,map)
        elif next_value == 'L':
            return 1 + find_path_length(NORTH,x-1,y,map)
        elif next_value == 'F':
            return 1 + find_path_length(SOUTH,x+1,y,map)
        return 0

    if direction == EAST:
        '''
        -
        J
        7
        '''
        if next_value == '-':
            return 1 + find_path_length(EAST,x,y+1,map)
        elif next_value == 'J':
            return 1 + find_path_length(NORTH,x-1,y,map)
        elif next_value == '7':
            return 1 + find_path_length(SOUTH,x+1,y,map)
        return 0
    
    return 0

def main():
    with open("/Users/yeelee/code/advent-of-code-2023/day10/input.txt",'r') as file:
        data = file.read().splitlines()

        for x, row in enumerate(data):
            for y, value in enumerate(row):
                if value == 'S':
                    north = 1 +find_path_length(NORTH,x-1,y,data)
                    south = 1 +find_path_length(SOUTH,x+1,y,data)
                    east = 1 +find_path_length(EAST,x,y+1,data)
                    west = 1 +find_path_length(WEST,x,y-1,data)
                    print(max(north,south,east,west)//2)
if __name__ == "__main__":
    main()