
from enum import Enum

DESTINATION = 0
SOURCE = 1
RANGE = 2

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

        list_of_seeds = []

        for seed in seeds:
            list_of_seeds.append(SeedInfo(seed)) 

        mappings = [section.split('\n')[1:] for section in sections[1:]]
        parsed_mappings = [[[int(y) for y in x.split(' ')] for x in set_of_maps] for set_of_maps in mappings]

        current_keys = seeds.copy()
        for i in range(len(parsed_mappings)):
            new_keys = []
            for mapping in parsed_mappings[i]:
                d, s, r = mapping
                for key in current_keys:
                    if s <= key <= s+r:
                        offset = key - s
                        value = d + offset
                        if i == Attribute.SOIL.value:
                            for seed in list_of_seeds:
                                if seed.seed == key:
                                    seed.soil = value

                        if i == Attribute.FERTILIZER.value:
                            for seed in list_of_seeds:
                                if seed.soil == key:
                                    seed.fertilizer = value

                        if i == Attribute.WATER.value:
                            for seed in list_of_seeds:
                                if seed.fertilizer == key:
                                    seed.water = value

                        if i == Attribute.LIGHT.value:
                            for seed in list_of_seeds:
                                if seed.water == key:
                                    seed.light = value

                        if i == Attribute.TEMPERATURE.value:
                            for seed in list_of_seeds:
                                if seed.light == key:
                                    seed.temperature = value

                        if i == Attribute.HUMIDITY.value:
                            for seed in list_of_seeds:
                                if seed.temperature == key:
                                    seed.humidity = value

                        if i == Attribute.LOCATION.value:
                            for seed in list_of_seeds:
                                if seed.humidity == key:
                                    seed.location = value
                        new_keys.append(value)
            for seed in list_of_seeds:
                if i == Attribute.SOIL.value:
                    if seed.soil is None:
                        seed.soil = seed.seed
                        new_keys.append(seed.soil)

                if i == Attribute.FERTILIZER.value:
                    if seed.fertilizer is None:
                        seed.fertilizer = seed.soil
                        new_keys.append(seed.fertilizer)

                if i == Attribute.WATER.value:
                    if seed.water is None:
                        seed.water = seed.fertilizer
                        new_keys.append(seed.water)

                if i == Attribute.LIGHT.value:
                    if seed.light is None:
                        seed.light = seed.water
                        new_keys.append(seed.light)

                if i == Attribute.TEMPERATURE.value:
                    if seed.temperature is None:
                        seed.temperature = seed.light
                        new_keys.append(seed.temperature)

                if i == Attribute.HUMIDITY.value:
                    if seed.humidity is None:
                        seed.humidity = seed.temperature
                        new_keys.append(seed.humidity)

                if i == Attribute.LOCATION.value:
                    if seed.location is None:
                        seed.location = seed.humidity
                        new_keys.append(seed.location)
            current_keys = new_keys.copy()
            new_keys = []
        
    # for seed in list_of_seeds:
    #     print(seed)
    #     print("\n ------------------------")

    min = float("inf")

    for seed in list_of_seeds:
        if seed.location < min:
            min = seed.location
    print(min)



if __name__ == "__main__":
    main()