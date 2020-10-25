# to find the average of the items in set

if __name__ == '__main__':
    n = int(input())
    list1 = []
    sum = 0
    for i in(input().split()):
        list1.append(i)
    set1 = set(list1)
    for i in set1:
        sum += int(i)
    avg = sum / len(set1)
    print(avg)