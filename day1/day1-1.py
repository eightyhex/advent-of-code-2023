
def main():
    total_sum = 0

    with open("/Users/yeelee/code/advent-of-code-2023/day1/input3.txt", 'r') as file:
        for line in file:
            first_digit = None
            second_digit = None
            for letter in line:
                if letter.isdigit():
                    if first_digit is None:
                        first_digit = int(letter)
                    second_digit = int(letter)
            line_number = (first_digit * 10) + second_digit
            total_sum += line_number
    print(total_sum)



if __name__ == "__main__":
    main()