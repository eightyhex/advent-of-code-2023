
from enum import Enum

class Attribute(Enum):
    SOIL = 0
    FERTILIZER = 1
    WATER = 2
    LIGHT = 3
    TEMPERATURE = 4
    HUMIDITY = 5
    LOCATION = 6
    

class SeedInfo:
    def __init__(self, seed):
        self.seed = seed
        self.soil = None
        self.fertilizer = None
        self.water = None
        self.light = None
        self.temperature = None
        self.humidity = None
        self.location = None

    def __str__(self):
        return f"seed:{self.seed}\nsoil:{self.soil}\nfertilizer:{self.fertilizer}\nwater:{self.water}\nlight:{self.light}\ntemperature:{self.temperature}\nhumidity:{self.humidity}\nlocation:{self.location}"
    

def main():
    with open("/Users/yeelee/code/advent-of-code-2023/day5/input.txt", 'r') as file:
        file_contents = file.read()
        sections = file_contents.strip().split('\n\n')
        
        
        seeds = [int(x) for x in sections[0].split(':')[1].strip().split(' ')]
        parsed_seeds = [[seeds[i-1],seeds[i]] for i in range(1,len(seeds),2)]

        # list_of_seeds = []

        # for seed in seeds:
        #     list_of_seeds.append(SeedInfo(seed)) 

        mappings = [section.split('\n')[1:] for section in sections[1:]]
        parsed_mappings = [[[int(y) for y in x.split(' ')] for x in set_of_maps] for set_of_maps in mappings]
        current_keys = parsed_seeds.copy()

        for i in range(len(parsed_mappings)):
            new_keys = []
            for mapping in parsed_mappings[i]:
                d, s, r = mapping
                for range_start, range_end in current_keys:
                    # a-b
                    #  c-d
                    # a < d and b > c

                    #    a - b
                    #  c - d
                    # 
                    #  a - b
                    #  c - d
                    # 
                    #  a - b
                    #    c - d
                    #
                    #  a - b
                    #      c - d
                    # 
                    #    a - b
                    #  c   -   d
                    # 
                    #  a  -   b
                    #   c - d 
                    #
                    #       a - b
                    # c - d
                    #
                    # a - b
                    #       c - d
                    set_of_new_ranges = []
                    if s <= range_start+range_end and s+r >= range_start:
                        if range_start >= s:
                            sub_range_start = range_start
                            sub_range_end = min(range_start+range_end, s+r)
                            converted_start = range_start - s + d
                            converted_end = range_start - s + + d + min(range_end,r)
                            set_of_new_ranges.append([converted_start,converted_end])
                            
                            if sub_range_end == s+r:
                                sub_range_start = s+r+1
                                sub_range_end = range_start+range_end
                                # same as above because we are outside the range of the mapping
                                converted_start = s+r+1
                                converted_end = range_start+range_end
                                set_of_new_ranges.append([converted_start,converted_end])

                        else: # c is less than a but there's still an overlap
                            sub_range_start = range_start
                            sub_range_end = s - 1
                            converted_start = range_start
                            converted_end = s - 1
                            set_of_new_ranges.append([converted_start,converted_end])

                            sub_range_start = s
                            sub_range_end = min(s+r, range_start+range_end)
                            converted_start = range_start - s + d
                            converted_end = d + r if sub_range_end == s+r else range_start + range_end
                            set_of_new_ranges.append([converted_start,converted_end])
                            if sub_range_end == s+r:
                                sub_range_start = s+r+1
                                sub_range_end = range_start + range_end
                                converted_start = s+r+1
                                converted_end = range_start + range_end
                                set_of_new_ranges.append([converted_start,converted_end])

                    # else: # if they are not overlapping
                    #     set_of_new_ranges.append([range_start,range_end])
                    
                    new_keys.extend(set_of_new_ranges.copy())
            if new_keys:
                current_keys = new_keys.copy()
        
        minimum = float("inf")

        for min_value, _ in current_keys:
            if min_value < minimum:
                minimum = min_value

        print(minimum)

                
    # min = float("inf")

    # for seed in list_of_seeds:
    #     if seed.location < min:
    #         min = seed.location
    # print(min)



if __name__ == "__main__":
    main()