'''
http://codeforces.com/contest/1005/problem/B


'''

input_1 = input()
input_2 = input()
total_attempts = 0
while True:
    if len(input_1) == len(input_2):
        if input_1 == input_2:
            print(total_attempts)
            break


    if len(input_2)> len(input_1):
        input_2 = input_2[1:]
    else:
        input_1 = input_1[1:]
    total_attempts += 1
