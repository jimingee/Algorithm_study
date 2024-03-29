def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == p1[i % 5]: result[0] += 1
        if answers[i] == p2[i % 8]: result[1] += 1
        if answers[i] == p3[i % 10]: result[2] += 1

    answer = [i + 1 for i,v in enumerate(result) if max(result) == v]

    return answer