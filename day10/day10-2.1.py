
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def check_bounds(x,y,map):
    if x < 0 or y >= len(map[0]) or x >= len(map) or y < 0:
        return False
    return True


def find_path_length(direction,x,y,map,seen):
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
                    seen.add((x_n,y_n))
                    next_value = map[x_n-1][y_n]
                    x_n -= 1
                    previous_direction = NORTH
                    counter +=1 
            elif next_value == 'F':
                if check_bounds(x_n,y_n+1,map):
                    seen.add((x_n,y_n))
                    next_value = map[x_n][y_n+1]
                    y_n += 1
                    previous_direction = EAST
                    counter +=1 
            elif next_value == '7':
                if check_bounds(x_n,y_n-1,map):
                    seen.add((x_n,y_n))
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
                    seen.add((x_n,y_n))
                    next_value = map[x_n+1][y_n]
                    x_n += 1
                    previous_direction = SOUTH
                    counter += 1
            elif next_value == 'L':
                if check_bounds(x_n,y+1,map):
                    seen.add((x_n,y_n))
                    next_value = map[x_n][y_n+1]
                    y_n += 1
                    previous_direction = EAST
                    counter += 1
            elif next_value == 'J':
                if check_bounds(x_n,y_n-1,map):
                    seen.add((x_n,y_n))
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
                    seen.add((x_n,y_n))
                    next_value = map[x_n][y_n-1]
                    y_n -= 1
                    previous_direction = WEST
                    counter += 1
            elif next_value == 'L':
                if check_bounds(x_n-1,y_n,map):
                    seen.add((x_n,y_n))
                    next_value = map[x_n-1][y_n]
                    x_n -= 1
                    previous_direction = NORTH
                    counter += 1
            elif next_value == 'F':
                if check_bounds(x_n+1,y_n,map):
                    seen.add((x_n,y_n))
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
                    seen.add((x_n,y_n))
                    next_value = map[x_n][y_n+1]
                    y_n += 1
                    previous_direction = EAST
                    counter += 1
            elif next_value == 'J':
                if check_bounds(x_n-1,y_n,map):
                    seen.add((x_n,y_n))
                    next_value = map[x_n-1][y_n]
                    x_n -= 1
                    previous_direction = NORTH
                    counter += 1
            elif next_value == '7':
                if check_bounds(x_n+1,y_n,map):
                    seen.add((x_n,y_n))
                    next_value = map[x_n+1][y_n]
                    x_n += 1
                    previous_direction = SOUTH
                    counter += 1
            else:
                next_value = None
    return counter
    
        
def is_inside_loop(x,y,data) -> bool:
    '''
    peform ray casting algorithm.
    if the number of times we hit a wall going left is odd then we are inside the loop otherwise even means we are outside
    since we have chosen to go left we will count how many times we hit: '|', 'L', 'F'

    one of these conditions has to be met to hit a wall when going left
    L 7
    F J
    L J
    F 7
    |
    '''
    counter = 0
    while y >= 0:
        if data[x][y] in ('|','J','L'):
            counter += 1
        y -= 1
    return counter % 2 == 1

def main():
    with open("/Users/yeelee/code/advent-of-code-2023/day10/input.txt",'r') as file:
        data = file.read().splitlines()

        result = 0
        found = False
        points_on_path = set()
        for x, row in enumerate(data):
            for y, value in enumerate(row):
                if value == 'S':
                    points_on_path.add((x,y))
                    north = 1 +find_path_length(SOUTH,x+1,y,data,points_on_path)
                    print(north//2)
                    found = True
                    data[x] = data[x].replace("S","|")
                    break
            if found:
                break

        data = ["".join(ch if (r,c) in points_on_path else "0" for c, ch in enumerate(row)) for r, row in enumerate(data)]
        
        for x, row in enumerate(data):
            for y, value in enumerate(row):
                if (x,y) not in points_on_path:
                    # do ray casting algorithm
                    if is_inside_loop(x,y,data):
                        result += 1
        print(result)
                    

if __name__ == "__main__":
    main()