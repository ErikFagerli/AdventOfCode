
from collections import defaultdict
import re

def parseBlueprint(file, i):
    
    with open(file, "r") as f:
        blueprints = f.readlines()
        blueprint = blueprints[i]
        blueprint_values = re.findall(r'\d+', blueprint)
        cost = {"ore":      int(blueprint_values[1]),
                "clay":     int(blueprint_values[2]),
                "obsidian": list(map(int,blueprint_values[3:5])),
                "geode":    list(map(int,blueprint_values[5:]))}

    return cost

        

def maximizeGeodes(cost, minutes):


    resources = {"ore":         0,
                 "clay":        0,
                 "obsidian":    0,
                 "geode":       0}
    
    robots = {"ore":        1,
              "clay":       0,
              "obsidian":   0,
              "geode":      0}

    for minute in range(1, minutes+1):

        resources["ore"] += robots["ore"]
        resources["clay"] += robots["clay"]
        resources["obsidian"] += robots["obsidian"]

        if cost["geode"][0] <= resources["ore"] and cost["geode"][1] <= resources["obsidian"]:
            robots["geode"] += 1
            resources["ore"] -= cost["geode"][0]
            resources["obsidian"] -= cost["geode"][1]
        elif cost["obsidian"][0] <= resources["ore"] and cost["obsidian"][1] <= resources["clay"]:
            robots["obsidian"] += 1
            resources["ore"] -= cost["obsidian"][0]
            resources["clay"] -= cost["obsidian"][1]
        elif cost["clay"] <= resources["ore"]:
            robots["clay"] += 1
            resources["ore"] -= cost["clay"]
        elif cost["ore"] <= resources["ore"]:
            robots["ore"] += 1
            resources["ore"] -= cost["ore"]

        print("resources = ", resources)
        print("robots = ", robots)
        print("\n\n")

    return robots["geode"]

def main(minutes):
    total_quality_level = 0
    for i in range(0,30):
        cost = parseBlueprint("text.txt", i)

        geode = maximizeGeodes(cost, minutes)
        quality_level = geode * (i+1)
        total_quality_level += quality_level

    return total_quality_level

if __name__ == "__main__":
    results = main(24)
    print(results)
