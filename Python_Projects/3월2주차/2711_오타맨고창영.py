for i in range(int(input())):
    a, word = map(str, input().split())
    a = int(a)
    word1 = word[:a - 1]
    word2 = word[a:len(word)]

    print(word1 + word2)