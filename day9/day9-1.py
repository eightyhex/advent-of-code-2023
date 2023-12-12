
def main():
    with open("C:/Users/Yee/code/advent-of-code-2023/day9/input.txt",'r') as file:
        data = file.read().splitlines()
        result = []
        for row in data:
            last_digits = []
            extrapolated_last_chars = []
            curent_row = [int(x) for x in row.split(' ')]
            while any(num != 0 for num in curent_row):
                next_row = []
                for i in range(len(curent_row)-1):
                    next_row.append(curent_row[i+1]-curent_row[i])
                last_digits.append(curent_row[i+1]) 
                curent_row = next_row
            for j in range(len(last_digits)-1,-1,-1):
                if len(extrapolated_last_chars) == 0:
                    extrapolated_last_chars.append(last_digits[j])
                else:
                    x = extrapolated_last_chars[-1] + last_digits[j]
                    extrapolated_last_chars.append(x)
            result.append(extrapolated_last_chars[-1])
        print(sum(result))

                 

        
if __name__ == "__main__":
    main()