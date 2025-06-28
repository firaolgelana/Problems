# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
    arr.sort(key=lambda a : a[1])
    minScore, secondMinScore = arr[0][1], 0
    for name, score in arr:
        if score != minScore:
            secondMinScore = score
            break
    secondMinScoreNames = []
    for name, score in arr:
        if score == secondMinScore:
            secondMinScoreNames.append(name)
    secondMinScoreNames.sort()
    for name in secondMinScoreNames:
        print(name)
