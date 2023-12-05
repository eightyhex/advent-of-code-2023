

def main():
    with open("/Users/yeelee/code/advent-of-code-2023/day4/input.txt", 'r') as file:
        file_contents = file.read().splitlines()

        result = 0

        winning_numbers = [results.split('|')[0].split(':')[1].strip().replace('  ', ' ') for results in file_contents]
        scratch_results = [results.split('|')[1].strip().replace('  ', ' ') for results in file_contents]
        
        winning_numbers_parsed = [[int(number) for number in row.split(' ')] for row in winning_numbers]
        scratch_results_parsed = [[int(number) for number in row.split(' ')] for row in scratch_results]

        # key = ticket_num :
        #           [
        #               matches,
        #               copies   
        #                       
        #           ]
        map_of_winnings = {}

        ticket_num = 0

        while ticket_num < len(winning_numbers_parsed):
            matches = 0
            for num in range(len(scratch_results_parsed[0])):
                if scratch_results_parsed[ticket_num][num] in winning_numbers_parsed[ticket_num]:
                    matches += 1
            if matches == 0:
                if ticket_num in map_of_winnings:
                    map_of_winnings[ticket_num] = [map_of_winnings[ticket_num][0], map_of_winnings[ticket_num][1] + 1]
                else:
                    map_of_winnings[ticket_num] = [0,1]
            else:
                if ticket_num in map_of_winnings:
                    map_of_winnings[ticket_num] = [matches, map_of_winnings[ticket_num][1] + 1]
                else:
                    map_of_winnings[ticket_num] = [matches,1]

            ticket_num += 1
        
        for ticket_num, value in map_of_winnings.items():
            matches,copies = value
            for j in range(copies):
                for i in range(ticket_num, ticket_num + matches + 1):
                    if i >= len(map_of_winnings):
                        break
                    if i != ticket_num:
                        map_of_winnings[i][1] += 1
            
            
        
        for key, value in map_of_winnings.items():
            matches, copies = value
            result += copies

        print(result)

if __name__ == "__main__":
    main()