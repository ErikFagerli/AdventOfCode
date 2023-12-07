seeds, *blocks = open("example.txt").read().split("\n\n")

seeds = list(map(int, seeds.split(": ")[1].split()))

print(seeds)

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    for seed in seeds:
        for destination, source, range_len in ranges:
            if source <= seed < source + range_len:
                new.append(seed - source + destination)
                break
        else:
            new.append(seed)
    seeds = new
print(min(seeds))