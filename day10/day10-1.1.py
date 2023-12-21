
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def check_bounds(x,y,map):
    if x < 0 or y >= len(map[0]) or x >= len(map) or y < 0:
        return False
    return True


def find_path_length(direction,x,y,map):
    if x < 0 or y >= len(map[0]) or x >= len(map) or y < 0 or map[x][y] in ['.','S']:
        return 0

    x_n, y_n = x,y
    next_value = map[x][y]
    counter = 0
    previous_direction = direction
    while next_value is not None:
        if previous_direction == NORTH:
            '''
            |
            F
            7
            '''
            if next_value == '|':
                if check_bounds(x_n-1,y_n,map):
                    next_value = map[x_n-1][y_n]
                    x_n -= 1
                    previous_direction = NORTH
                    counter +=1 
            elif next_value == 'F':
                if check_bounds(x_n,y_n+1,map):
                    next_value = map[x_n][y_n+1]
                    y_n += 1
                    previous_direction = EAST
                    counter +=1 
            elif next_value == '7':
                if check_bounds(x_n,y_n-1,map):
                    next_value = map[x_n][y_n-1]
                    y_n -= 1
                    previous_direction = WEST
                    counter +=1
            else:
                next_value = None

        if previous_direction == SOUTH:
            '''
            |
            L
            J
            '''
            if next_value == '|':
                if check_bounds(x_n+1,y,map):
                    next_value = map[x_n+1][y_n]
                    x_n += 1
                    previous_direction = SOUTH
                    counter += 1
            elif next_value == 'L':
                if check_bounds(x_n,y+1,map):
                    next_value = map[x_n][y_n+1]
                    y_n += 1
                    previous_direction = EAST
                    counter += 1
            elif next_value == 'J':
                if check_bounds(x_n,y_n-1,map):
                    next_value = map[x_n][y_n-1]
                    y_n -= 1
                    previous_direction = WEST
                    counter += 1
            else:
                next_value = None

        if previous_direction == WEST:
            '''
            -
            L
            F
            '''
            if next_value == '-':
                if check_bounds(x_n,y_n+1,map):
                    next_value = map[x_n][y_n-1]
                    y_n -= 1
                    previous_direction = WEST
                    counter += 1
            elif next_value == 'L':
                if check_bounds(x_n-1,y_n,map):
                    next_value = map[x_n-1][y_n]
                    x_n -= 1
                    previous_direction = NORTH
                    counter += 1
            elif next_value == 'F':
                if check_bounds(x_n+1,y_n,map):
                    next_value = map[x_n+1][y_n]
                    x_n += 1
                    previous_direction = SOUTH
                    counter += 1
            else:
                next_value = None

        if previous_direction == EAST:
            '''
            -
            J
            7
            '''
            if next_value == '-':
                if check_bounds(x_n,y_n+1,map):
                    next_value = map[x_n][y_n+1]
                    y_n += 1
                    previous_direction = EAST
                    counter += 1
            elif next_value == 'J':
                if check_bounds(x_n-1,y_n,map):
                    next_value = map[x_n-1][y_n]
                    x_n -= 1
                    previous_direction = NORTH
                    counter += 1
            elif next_value == '7':
                if check_bounds(x_n+1,y_n,map):
                    next_value = map[x_n+1][y_n]
                    x_n += 1
                    previous_direction = SOUTH
                    counter += 1
            else:
                next_value = None
    return counter
    
        
def main():
    with open("/Users/yeelee/code/advent-of-code-2023/day10/input.txt",'r') as file:
        data = file.read().splitlines()

        for x, row in enumerate(data):
            for y, value in enumerate(row):
                if value == 'S':
                    north = 1 +find_path_length(NORTH,x-1,y,data)
                    print(north//2)
if __name__ == "__main__":
    main()