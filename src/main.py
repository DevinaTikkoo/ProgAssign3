import sys

def OPT():
    #read input
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as filename:
            lines = [line.strip() for line in filename if line.strip()]
    else:
        lines = [line.strip() for line in sys.stdin if line.strip()]
    #parse input
    k = int(lines[0])
    character_values = {}
    #parse and store character values
    for i in range(1, k + 1):
        character, value = lines[i].split()
        character_values[character] = int(value)
    #parse strings; a = first string, b = second string
    a = lines[k + 1]
    n = len(a)
    b = lines[k + 2]
    m = len(b)
    #create 2D array to store optimal values
    arr = list()
    for i in range(n + 1):
        arr.append([0] * (m + 1))
    #fill in the array with cases 
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            #if character names match and gives better maximum, accept and add character_value to optimal value of previous characters; otherwise
            if a[i - 1] == b[j - 1]:
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1], arr[i - 1][j - 1] + character_values[a[i - 1]])
            #character names do not match, take the maximum of the two previous optimal values and skip
            else:
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
    #backtrack to find the optimal subsequence
    subsequence = list()
    i = n
    j = m
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1] and arr[i][j] == arr[i - 1][j - 1] + character_values[a[i - 1]]:
            #character names was added to optimal subsequence
            # add to list and move diagonally up left
            subsequence.append(a[i - 1])
            i -= 1
            j -= 1
        elif arr[i - 1][j] > arr[i][j - 1]:
            #optimal value came from above, move up
            #skip character in a
            i -= 1
        else:
            #optimal value came from left, move left
            #skip character in b
            j -= 1
    #outputs
    print(arr[n][m])
    print(''.join(reversed(subsequence)))

if __name__ == "__main__":
    OPT()