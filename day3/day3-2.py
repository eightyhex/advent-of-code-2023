def find_gear_ratio(matrix, x, y) -> int:
    value1 = 0
    value2 = 0
    num1 = check_and_get_upper_left(matrix, x, y)
    num2 = check_and_get_upper_mid(matrix, x, y)
    num3 = check_and_get_upper_right(matrix, x, y)
    num4 = check_and_get_mid_left(matrix, x, y)
    num5 = check_and_get_mid_right(matrix, x, y)
    num6 = check_and_get_lower_left(matrix, x, y)
    num7 = check_and_get_lower_mid(matrix, x, y)
    num8 = check_and_get_lower_right(matrix, x, y)

    if num1 == num3 and num1 != num2 and num1 > 0:
        value1 = num1
        value2 = num2
        
    elif num6 == num8 and num6 != num7 and num6 > 0:
        value1 = num6
        value2 = num8
    else:
        gears = set([num1, num2, num3, num4, num5, num6, num7, num8])
        gears.remove(0)
        if len(gears) == 1:
            return 0
        value1 = gears.pop()
        value2 = gears.pop()
    return value1*value2




def is_number(char) -> bool:
    return char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
 
def is_symbol(char) -> bool:
    return char not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.')

def find_entire_number(matrix,x,y) -> int:
    start = y

    while start >= 0 and is_number(matrix[x][start]):
        start -= 1
    start +=1 
    
    current_number = ""
    while start < len(matrix[0]) and is_number(matrix[x][start]):
        current_number += matrix[x][start]
        start+= 1
    
    return int(current_number)
    


def check_and_get_upper_left(matrix,x,y) -> int:
    number = 0
    if x > 0 and y > 0: 
        if is_number(matrix[x-1][y-1]):
            number = find_entire_number(matrix,x-1,y-1)
    return number

def check_and_get_upper_mid(matrix,x,y) -> int:
    number = 0
    if x != 0:
        if is_number(matrix[x-1][y]):
            number = find_entire_number(matrix,x-1,y)
    return number

def check_and_get_upper_right(matrix,x,y) -> int:
    number = 0
    if x != 0 and y < len(matrix[0]) - 1:
        if is_number(matrix[x-1][y+1]):
            number = find_entire_number(matrix,x-1,y+1)
    return number

def check_and_get_mid_left(matrix,x,y) -> int:
    number = 0
    if y != 0:
        if is_number(matrix[x][y-1]):
            number = find_entire_number(matrix,x,y-1)
    return number

def check_and_get_mid_right(matrix,x,y) -> int:
    number = 0
    if y != len(matrix[0]) - 1:
        if is_number(matrix[x][y+1]):
            number = find_entire_number(matrix,x,y+1)
    return number

def check_and_get_lower_left(matrix,x,y) -> int:
    number = 0
    if x < len(matrix) - 1 and y > 0:
        if is_number(matrix[x+1][y-1]):
            number = find_entire_number(matrix,x+1,y-1)
    return number

def check_and_get_lower_mid(matrix,x,y) -> int:
    number = 0
    if x < len(matrix) - 1:
        if is_number(matrix[x+1][y]):
            number = find_entire_number(matrix,x+1,y)
    return number

def check_and_get_lower_right(matrix,x,y) -> int:
    number = 0
    if x < len(matrix) - 1 and y < len(matrix[0]) - 1:
        if is_number(matrix[x+1][y+1]):
            number = find_entire_number(matrix,x+1,y+1)
    return number

def main():
    with open("/Users/yeelee/code/advent-of-code-2023/day3/input.txt", 'r') as file:
        # read the file into a variable by each row
        file_contents = file.read().splitlines()

        # split each row into individual characters so we have a matrix
        matrix = [[char for char in row] for row in file_contents]

        result = 0

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == '*':
                    product = find_gear_ratio(matrix,x,y)
                    result += product
        
        print(result)

if __name__ == "__main__":
    main()