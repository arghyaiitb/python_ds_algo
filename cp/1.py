'''

http://codeforces.com/contest/1005/problem/A
Input
7
1 2 3 1 2 3 4
Output
2
3 4
'''


def count_stairs(stair_data):

    total_stairs = 1
    current_stair = 0
    final_string = ''
    for a in stair_data.split(' '):
        previous_stair = current_stair
        current_stair = int(a)
        if current_stair <= previous_stair:
            total_stairs += 1
            final_string += str(previous_stair) + ' '
    final_string += stair_data[-1] + ' '
    print(total_stairs)
    print(final_string)

if __name__=="__main__":
    total_count = input()
    stair_data = input()
    # stair_data = '1 2 3 4 1 2 1 1 1 2 3'
    count_stairs(stair_data)