MAX = 51
parent = [[[i, j] for j in range(MAX)] for i in range(MAX)]
graph = [['EMPTY' for _ in range(MAX)] for _ in range(MAX)]

def find_parent(x, y):
    if parent[x][y] == [x, y]:
        return parent[x][y]
    parent[x][y] = find_parent(parent[x][y][0], parent[x][y][1])
    return parent[x][y]


def union(r1, c1, r2, c2):

    r1, c1 = find_parent(r1, c1)
    r2, c2 = find_parent(r2, c2)

    if r1 == r2 and c1 == c2:
        return

    if graph[r1][c1] == 'EMPTY':
        parent[r1][c1] = [r2, c2]
    else:
        parent[r2][c2] = [r1, c1]

def solution(commands):
    answer = []
    for i in range(len(commands)):
        apply = commands[i].split(" ") # 명령어들 분리
        if apply[0] == 'UPDATE' and len(apply) == 4:
            row, col = find_parent(int(apply[1]), int(apply[2]))
            graph[row][col] = apply[3]

        elif apply[0] == 'UPDATE':
            for i in range(MAX):
                for j in range(MAX):
                    row, col = find_parent(i, j)
                    if graph[row][col] == apply[1]:
                        graph[row][col] = apply[2]

        elif apply[0] == 'MERGE':
            union(int(apply[1]), int(apply[2]), int(apply[3]), int(apply[4]))

        elif apply[0] == 'UNMERGE':
            row, col = find_parent(int(apply[1]), int(apply[2]))
            hello = graph[row][col]
            newline = []
            for i in range(MAX):
                for j in range(MAX):
                    if i == int(apply[1]) and j == int(apply[2]):
                        continue
                    if [row, col] == find_parent(i, j):
                        newline.append([i, j])
            for x, y in newline:
                parent[x][y] = [x, y]
                graph[x][y] = 'EMPTY' # merge 된 부분을 모두 초기화 한다

            parent[int(apply[1])][int(apply[2])] = [int(apply[1]), int(apply[2])] # 자기 자신을 부모로 바꾼다
            graph[int(apply[1])][int(apply[2])] = hello # merge되었을 때 값으로 초기화 한다

        elif apply[0] == 'PRINT':
            row, col = find_parent(int(apply[1]), int(apply[2]))
            answer.append(graph[row][col])

    return answer
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    commands = ["UPDATE 1 1 A", "UPDATE 1 2 B", "UPDATE 1 3 C", "MERGE 1 1 1 2", "MERGE 1 1 1 3", "MERGE 1 2 1 3", "UNMERGE 1 1", "PRINT 1 1", "PRINT 1 2", "PRINT 1 3"]
    print(solution(commands))
