

def main():
    total_sum = 0

    with open("/Users/yeelee/code/advent-of-code-2023/day1/input.txt", 'r') as file:
        for line in file:
            first_digit = None
            second_digit = None

            ptr_1 = 0
            while ptr_1 < len(line.strip()):
                char_value = line[ptr_1]
                if char_value.isdigit():
                    if first_digit is None:
                        first_digit = int(char_value)
                    second_digit = int(char_value)

                elif ptr_1 <= len(line.strip()) - 4 and char_value == 'z' and line[ptr_1+1] == 'e' and line[ptr_1+2] == 'r' and line[ptr_1+3] == 'o':
                    if first_digit is None:
                        first_digit = 0
                    second_digit = 0

                elif ptr_1 <= len(line.strip()) - 3 and char_value == 'o' and line[ptr_1+1] == 'n' and line[ptr_1+2] == 'e':
                    if first_digit is None:
                        first_digit = 1
                    second_digit = 1

                elif ptr_1 <= len(line.strip()) - 3 and char_value == 't' and line[ptr_1+1] == 'w' and line[ptr_1+2] == 'o':
                    if first_digit is None:
                        first_digit = 2
                    second_digit = 2

                elif ptr_1 <= len(line.strip()) - 5 and char_value == 't' and line[ptr_1+1] == 'h' and line[ptr_1+2] == 'r' and line[ptr_1+3] == 'e' and line[ptr_1+4] == 'e':
                    if first_digit is None:
                        first_digit = 3
                    second_digit = 3

                elif ptr_1 <= len(line.strip()) - 4 and char_value == 'f' and line[ptr_1+1] == 'o' and line[ptr_1+2] == 'u' and line[ptr_1+3] == 'r':
                    if first_digit is None:
                        first_digit = 4
                    second_digit = 4

                elif ptr_1 <= len(line.strip()) - 4 and char_value == 'f' and line[ptr_1+1] == 'i' and line[ptr_1+2] == 'v' and line[ptr_1+3] == 'e':
                    if first_digit is None:
                        first_digit = 5
                    second_digit = 5

                elif ptr_1 <= len(line.strip()) - 3 and char_value == 's' and line[ptr_1+1] == 'i' and line[ptr_1+2] == 'x':
                    if first_digit is None:
                        first_digit = 6
                    second_digit = 6

                elif ptr_1 <= len(line.strip()) - 5 and char_value == 's' and line[ptr_1+1] == 'e' and line[ptr_1+2] == 'v' and line[ptr_1+3] == 'e' and line[ptr_1+4] == 'n':
                    if first_digit is None:
                        first_digit = 7
                    second_digit = 7

                elif ptr_1 <= len(line.strip()) - 5 and char_value == 'e' and line[ptr_1+1] == 'i' and line[ptr_1+2] == 'g' and line[ptr_1+3] == 'h' and line[ptr_1+4] == 't':
                    if first_digit is None:
                        first_digit = 8
                    second_digit = 8

                elif ptr_1 <= len(line.strip()) - 4 and char_value == 'n' and line[ptr_1+1] == 'i' and line[ptr_1+2] == 'n' and line[ptr_1+3] == 'e':
                    if first_digit is None:
                        first_digit = 9
                    second_digit = 9

                ptr_1 += 1

            line_number = (first_digit * 10) + second_digit
            total_sum += line_number
    print(total_sum)

if __name__ == "__main__":
    main()