

def main():
    with open("/Users/yeelee/code/advent-of-code-2023/day6/input.txt", 'r') as file:
        file_contents = file.read().splitlines()
        time = list(map(int, file_contents[0].split(':')[1].strip().split(" ")))
        winning_distances = list(map(int, file_contents[1].split(":")[1].strip().split(" ")))
        race_and_result = list(zip(time,winning_distances))

        result = 1

        # d = (T - t_h) * t_h
        for race_time, winning_distance in race_and_result:
            num_of_ways_to_win = 0
            for i in range(race_time):
                if winning_distance < (race_time - i) * i:
                    num_of_ways_to_win += 1
            result *= num_of_ways_to_win if num_of_ways_to_win != 0 else 1
        print(result)
            


if __name__ == "__main__":
    main()