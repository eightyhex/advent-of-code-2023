def main():
    with open("/Users/yeelee/code/advent-of-code-2023/day8/input.txt", 'r') as file:
        file_contents = file.read().splitlines()
        
        direction, _, *mapping = file_contents
        parsed_mapping = {}
        for row in mapping:
            key = row.split("=")[0].strip()
            L,R = row.split("=")[1].strip().replace('(', "").replace(')', "").split(", ")
            # print(key)
            # print(f"left:{L} | right:{R}")
            # print(value)
            # print("\n-----------------------")
        
            parsed_mapping[key] = [L,R]

        current_value = "AAA"
        loop_counter = 0
        while current_value != "ZZZ":
            left_or_right = 0 if direction[loop_counter%len(direction)] == 'L' else 1
            current_value = parsed_mapping[current_value][left_or_right]
            loop_counter += 1
        print(loop_counter)
            

if __name__ == "__main__":
    main()