inputs, *blocks = open("text_file.txt").read().split("\n\n")

inputs = list(map(int, inputs.split(": ")[1].split()))

seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i+1]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new_pos = []
    while seeds:
        start, end = seeds.pop()
        for destination, source, range_len in ranges:
            overlap_start = max(start, source)
            overlap_end = min(end, source + range_len)
            if overlap_start < overlap_end:
                new_pos.append((overlap_start - source + destination, overlap_end - source + destination))
                if overlap_start > start:
                    seeds.append((start, overlap_start))
                if overlap_end < end:
                    seeds.append((overlap_end, end))
                break
        else: 
            new_pos.append((start, end))
    seeds = new_pos
print(min(seeds)[0])