

def main():
    with open("/Users/yeelee/code/advent-of-code-2023/day4/input.txt", 'r') as file:
        file_contents = file.read().splitlines()

        result = 0

        winning_numbers = [results.split('|')[0].split(':')[1].strip().replace('  ', ' ') for results in file_contents]
        scratch_results = [results.split('|')[1].strip().replace('  ', ' ') for results in file_contents]
        
        winning_numbers_parsed = [[int(number) for number in row.split(' ')] for row in winning_numbers]
        scratch_results_parsed = [[int(number) for number in row.split(' ')] for row in scratch_results]
        
        ticket_num = 0

        while ticket_num < len(winning_numbers_parsed):
            ticket_value = 0
            for num in range(len(scratch_results_parsed[0])):
                if scratch_results_parsed[ticket_num][num] in winning_numbers_parsed[ticket_num]:
                    ticket_value = 1 if ticket_value == 0 else ticket_value * 2
            result += ticket_value
            ticket_num += 1
        print(result)
if __name__ == "__main__":
    main()