
def find_nearest_z(key,map,direction):
    current_value = key 
    loop_counter = 0
    while current_value[2] != "Z":
        left_or_right = 0 if direction[loop_counter%len(direction)] == 'L' else 1
        current_value = map[current_value][left_or_right]
        loop_counter += 1
    return loop_counter
    
def main():
    with open("/Users/yeelee/code/advent-of-code-2023/day8/input.txt", 'r') as file:
        file_contents = file.read().splitlines()
        
        direction, _, *mapping = file_contents
        parsed_mapping = {}
        for row in mapping:
            key = row.split("=")[0].strip()
            L,R = row.split("=")[1].strip().replace('(', "").replace(')', "").split(", ")
            parsed_mapping[key] = [L,R]

        for key, value in parsed_mapping.items():
            iterations_to_next_z = find_nearest_z(key, parsed_mapping, direction)
            value.append(iterations_to_next_z)


        print(parsed_mapping.items())

if __name__ == "__main__":
    main()