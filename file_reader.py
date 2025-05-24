#write here a code for task 

'''task 1'''
'''
count = 0 
with open('my_file.txt', 'r') as file:
    for string in file:
        string_list = string.split(' ')
        for symbol in string_list:
            if int(symbol) == 1:
                count = count+1
print(count) # ans = 26
'''

'''task 2'''
'''
with open('my_file.txt', 'r') as file:
    lines = file.readlines()
    second_line = lines[13].split(' ')
    item = int(second_line[7])
    print(item) # ans = 1
'''

'''task 3'''
'''
count = 0
with open('my_file.txt', 'r') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        string_list = lines[i].split(' ')
        for j in range(len(string_list)):
            count = count + int(string_list[j])
print(count) # ans = 1130
'''