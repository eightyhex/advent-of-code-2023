
HIGH = 1
PAIR = 2
TWO_PAIR = 3
THREE_OF_A_KIND = 4
FULL_HOUSE = 5
FOUR_OF_A_KIND = 6
FIVE_OF_A_KIND = 7

def score(cards):
    map_of_cards = {}
    for card in cards:
        map_of_cards.setdefault(card,0)
        map_of_cards[card] += 1
    return evaluate(map_of_cards)

def evaluate(map_of_cards):
    num_of_high = 0
    num_of_pair = 0
    num_of_three = 0
    num_of_fh = 0
    num_of_four = 0
    num_of_five = 0

    for count in map_of_cards.values():
        if count == 1:
            num_of_high += 1
        if count == 2:
            num_of_pair += 1
        if count == 3:
            num_of_three += 1
        if count == 4:
            num_of_four += 1
        if count == 5:
            num_of_five += 1

    if 'J' in map_of_cards:
        available_j = 0
        if map_of_cards['J'] == 1:
            num_of_high -= 1
            available_j += 1

        elif map_of_cards['J'] == 2:
            num_of_pair -= 1
            available_j += 2

        elif map_of_cards['J'] == 3:
            num_of_three -= 1
            available_j += 3

        elif map_of_cards['J'] == 4:
            num_of_four -= 1
            available_j += 4

        for j in range(available_j):
            if num_of_four == 1:
                num_of_five += 1
                num_of_four = 0
            elif num_of_three == 1:
                num_of_four += 1
                num_of_three = 0
            elif num_of_pair > 0:
                num_of_three += 1
                num_of_pair -= 1
            else:
                num_of_pair += 1
                num_of_high -= 1
    
    if num_of_pair and num_of_three:
        num_of_fh += 1
    
    if num_of_five:
        return FIVE_OF_A_KIND
    if num_of_four:
        return FOUR_OF_A_KIND
    if num_of_fh:
        return FULL_HOUSE
    if num_of_three:
        return THREE_OF_A_KIND
    if num_of_pair == 2:
        return TWO_PAIR
    if num_of_pair == 1:
        return PAIR
    else:
        return HIGH

char_weights = {
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, 
    '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 
    'J': 0, 'Q': 12, 'K': 13, 'A': 14
}


def sort(list_of_hands,tier):
    # sorted_list = sorted(list_of_hands, key=lambda x: char_weights.get(x[0][0],0),reverse=True)
    return sorted(list_of_hands,key=lambda lst: [char_weights.get(char, 0) for char in lst[0]], reverse=True)
    

def main():
    with open("/Users/yeelee/code/advent-of-code-2023/day7/input.txt", 'r') as file:
        file_contents = file.read().splitlines()
        hands_to_points =  [[hand.split(" ")[0],int(hand.split(" ")[1])] for hand in file_contents]
        groupings_of_hands_by_score = {HIGH:[], PAIR:[], TWO_PAIR:[], THREE_OF_A_KIND:[], FULL_HOUSE:[], FOUR_OF_A_KIND:[], FIVE_OF_A_KIND:[]}
        num_of_hands = len(hands_to_points)
        result = 0
        for i in range(num_of_hands):
            hand_score = score(hands_to_points[i][0])
            groupings_of_hands_by_score[hand_score].append(hands_to_points[i])
       
        for s in range(7,0,-1):
            sorted_values = sort(groupings_of_hands_by_score[s],s)
            for i in range(len(sorted_values)):
                result += sorted_values[i][1] * num_of_hands
                num_of_hands -= 1
        
        print(result)


if __name__ == "__main__":
    main()