

with open("calories.txt", "r") as f:
    test = f.read()
    calories_lst = test.split("\n")
    calories_lst = " ".join(calories_lst)
    calories_lst = calories_lst.split("  ")

    lst = []

    for i in range(len(calories_lst)):
        lst_temp = calories_lst[i].split(" ")
        lst_temp = list(map(int, lst_temp))
        sum_calorie_elf = sum(lst_temp)
        lst.append(sum_calorie_elf)
    max_calories_elf = max(lst)
    
def Nmaxelements(list1, N):
    final_list = []
 
    for i in range(0, N):
        max1 = 0
         
        for j in range(len(list1)):    
            if list1[j] > max1:
                max1 = list1[j];
                 
        list1.remove(max1);
        final_list.append(max1)
         
    return(final_list) 

top3 = Nmaxelements(lst, 3)

print(sum(top3))