
def second_max_num_in_arr(arr):
    max = -9999
    sec_max = -9999
    for i in arr:
        print(i)
        if max < i:
            max = i
    for i in arr:
        if i != max and i > sec_max:
            sec_max = i
    print(sec_max)


def second_max_num_in_list(list):
    list.sort(reverse=True)
    max = list[0]
    sec_max = -1
    for i in range(1, n):
        if list[i] < max:
            sec_max = list[i]
            break
    print(sec_max)


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list = list(arr)
    print("arr:", arr)
    print("list:", list)
    second_max_num_in_arr(list)
    second_max_num_in_list(list)
