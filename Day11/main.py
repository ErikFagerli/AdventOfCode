# Starting items for each monkey
M0 = [57]
M1 = [58, 93, 88, 81, 72, 73, 65]
M2 = [65, 95]
M3 = [58, 80, 81, 83]
M4 = [58, 89, 90, 96, 55]
M5 = [66, 73, 87, 58, 62, 67]
M6 = [85, 55, 89]
M7 = [73, 80, 54, 94, 90, 52, 69, 58]

all_monkeys = [M0, M1, M2, M3, M4, M5, M6, M7]

# Count number of times a monkey inspects an item
M0_count = 0
M1_count = 0
M2_count = 0
M3_count = 0
M4_count = 0
M5_count = 0
M6_count = 0
M7_count = 0


# Loop through 20 times

for i in range(10000):

    # Loop through each item in monkey
    for monkey in range(len(all_monkeys)):
        if len(all_monkeys[monkey]) == 0:
            continue
        #print(all_monkeys[monkey])
        for item in all_monkeys[monkey]:
            # Check which monkey is holding item
            if monkey == 0:
                M0_count += 1
                item_temp = int(item) * 13
                #item_temp = item_temp // 3
                if item_temp % 11 == 0:
                    all_monkeys[3].append(item_temp)
                    
                else:
                    all_monkeys[2].append(item_temp)
                    

            if monkey == 1:
                M1_count += 1
                item_temp = int(item) + 2
                #item_temp = item_temp // 3
                if item_temp % 7 == 0:
                    all_monkeys[6].append(item_temp)
                    
                else:
                    all_monkeys[7].append(item_temp)
                    

            elif monkey == 2:
                M2_count += 1
                item_temp = int(item) + 6
                #item_temp = item_temp // 3
                if item_temp % 13 == 0:
                    all_monkeys[3].append(item_temp)
                    
                else:
                    all_monkeys[5].append(item_temp)
                    

            elif monkey == 3:
                M3_count += 1
                item_temp = int(item) **2
                #item_temp = item_temp // 3
                if item_temp % 5 == 0:
                    all_monkeys[4].append(item_temp)
                    
                else:
                    all_monkeys[5].append(item_temp)
                    

            elif monkey == 4:
                M4_count += 1
                item_temp = int(item) + 3
                #item_temp = item_temp // 3
                if item_temp % 3 == 0:
                    all_monkeys[1].append(item_temp)
                    
                else:
                    all_monkeys[7].append(item_temp)
                    

            elif monkey == 5:
                M5_count += 1
                item_temp = int(item) * 7
                #item_temp = item_temp // 3
                if item_temp % 17 == 0:
                    all_monkeys[4].append(item_temp)
                    
                else:
                    all_monkeys[1].append(item_temp)
                    

            elif monkey == 6:
                M6_count += 1
                item_temp = int(item) + 4
                #item_temp = item_temp // 3
                if item_temp % 2 == 0:
                    all_monkeys[2].append(item_temp)
                    
                else:
                    all_monkeys[0].append(item_temp)
                    

            elif monkey == 7:
                M7_count += 1
                item_temp = int(item) + 7
                #item_temp = item_temp // 3
                if item_temp % 19 == 0:
                    all_monkeys[6].append(item_temp)
                    
                else:
                    all_monkeys[0].append(item_temp)
        all_monkeys[monkey] = []

# 121450 is the answer to part 1

count = [M0_count, M1_count, M2_count, M3_count, M4_count, M5_count, M6_count, M7_count]

count.sort()
monkey_business = count[-2] * count[-1]
print(monkey_business)