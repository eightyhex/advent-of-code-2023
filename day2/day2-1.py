
# 12 red, 13 green, 14 blue
RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

def main():
    with open("/Users/yeelee/code/advent-of-code-2023/day2/input.txt", 'r') as file:
        file_contents = file.read().splitlines()
        
        # split by game id, game 1; game 2; game 3
        score = 0
        for results in file_contents:
            skip = False
            game_id = int(results.split(":")[0].split(" ")[1])
            game_results = [results.split(":")[1].split(";")[x] for x in range(len(results.split(":")[1].split(";")))]
            for result in game_results:
                if skip == False:
                    color_values = result.split(",")
                    for cube in color_values:
                        value, color = int(cube.split(' ')[1]), cube.split(' ')[2]
                        if (color == 'red' and value > RED_MAX) or (color == 'green' and value > GREEN_MAX) or (color == 'blue' and value > BLUE_MAX):
                            skip = True
            if skip == False:
                score += game_id
        print(score)

            
if __name__ == "__main__":
    main()