



def is_number(char) -> bool:
    return char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
 
def is_symbol(char) -> bool:
    return char not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.')

def check_adjacent(matrix,x,y) -> bool:
    '''
    A A A -> (0,0) (0,1) (0,2) 
    A B A -> (1,0) (1,1) (1,2)
    A A A -> (2,0) (2,1) (2,2)

    checks the adjacent and diagnol values of B for symbols
    '''

    # check upper left
    if x > 0 and y > 0: 
        has_adjecent_symbol = is_symbol(matrix[x-1][y-1])
        if has_adjecent_symbol:
            return True

    # check upper mid
    if x != 0:
        has_adjecent_symbol = is_symbol(matrix[x-1][y])
        if has_adjecent_symbol:
            return True

    # chck upper right
    if x != 0 and y < len(matrix[0]) - 1:
        has_adjecent_symbol = is_symbol(matrix[x-1][y+1])
        if has_adjecent_symbol:
            return True

    # check mid left
    if y != 0:
        has_adjecent_symbol = is_symbol(matrix[x][y-1])
        if has_adjecent_symbol:
            return True

    # check mid right
    if y != len(matrix[0]) - 1:
        has_adjecent_symbol = is_symbol(matrix[x][y+1])
        if has_adjecent_symbol:
            return True

    # check lower left
    if x < len(matrix) - 1 and y > 0:
        has_adjecent_symbol = is_symbol(matrix[x+1][y-1])
        if has_adjecent_symbol:
            return True

    # check lower mid
    if x < len(matrix) - 1:
        has_adjecent_symbol = is_symbol(matrix[x+1][y])
        if has_adjecent_symbol:
            return True

    # check lower right 
    if x < len(matrix) - 1 and y < len(matrix[0]) - 1:
        has_adjecent_symbol = is_symbol(matrix[x+1][y+1]) 
        if has_adjecent_symbol:
            return True
    
    return False


def main():
    with open("/Users/yeelee/code/advent-of-code-2023/day3/input.txt", 'r') as file:
        # read the file into a variable by each row
        file_contents = file.read().splitlines()

        # split each row into individual characters so we have a matrix
        matrix = [[char for char in row] for row in file_contents]

        result = 0

        for x in range(len(matrix)):
            y = 0
            current_number = ""
            has_adjecent_symbol = False
            while y < len(matrix[0]):
                if is_number(matrix[x][y]):
                    current_number += matrix[x][y]
                    if check_adjacent(matrix,x,y):
                        has_adjecent_symbol = True
                else:
                    if current_number and has_adjecent_symbol:
                        result += int(current_number)
                    current_number = ""
                    has_adjecent_symbol = False
                y += 1
            if current_number and has_adjecent_symbol:
                result += int(current_number)
            current_number = ""
            has_adjecent_symbol = False
        print(result)


if __name__ == "__main__":
    main()