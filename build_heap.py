# python3

def heapify(swaps, data, n, i):
        smallest = i
        l = 2*i+1
        r = 2*i+2

        if l < n and data[i] > data[l]:
            smallest = l
        if r < n and data[smallest] > data[r]:
            smallest = r
        if smallest != i:
            data[i], data[smallest] = data[smallest], data[i]
            swaps.append([i, smallest])
            heapify(swaps, data, n, smallest)

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range(n//2-1,-1,-1):
        heapify(swaps, data, n, i)


    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    choice = input()
    if "I" in choice:
        n = int(input())
        data = list(map(int, input().split()))
    if "F" in choice:
        lines = open("./tests/"+str(input()),"r").readlines()
        n = int(lines[0])
        data = list(map(int, lines[1].split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()


