# -*- coding: utf8 -*-
#!/usr/bin/python

wf = open('output.txt', 'w')

class Node:
    def __init__(self, value, point):
        self.value = value
        self.point = point
        self.parent = None
        self.H = 0
        self.G = 0
   # def can_move(self):
    #    return True if self.value == 0 else False
    def g_score(self):
        return 0 if self.value == 1 else 1
    def h_score(self, other):
        return abs(self.point[0] - other.point[0]) + abs(self.point[1] - other.point[1])
    @property
    def get_point(self):
        return self.point
    @property
    def get_value(self):
        return self.value

def children(point, greedy, col):
    x, y = point.point
    links = []
    if x < len(greedy)-1:
        #print((x+1, y))
        links.append(greedy[x+1][y])
    if y < col - 1:
        links.append(greedy[x][y + 1])
    if x > 0:
        links.append(greedy[x-1][y])
    if y > 0:
        links.append(greedy[x][y-1])

    '''
    for link in links:
        if link.get_value != 1:
            print(link.get_value)
    '''
    a = [i for i in links if i.value != 1]
    '''
    for i in a:
        x = i.get_point
        print(x)
    '''
    return a

def aStar(start, goal, greedy, col):
    #탐색 안한 open set
    openSet = set()
    #탐색 한 closed set
    closedSet = set()
    current = start
    openSet.add(current)
    while openSet:
        current = min(openSet, key=lambda x : x.H + x.G)
        string = str(current.get_point)
        string = string.replace("(","")
        string = string.replace(")", "")
        string = string.replace(",", "")
        wf.write(string)
        wf.write("\n")
        #목적지에 도착했을 때
        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            #print(current.get_point)
            return path[::-1]
        openSet.remove(current)
        closedSet.add(current)

        #current의 자식 노드들 탐색
        for node in children(current, greedy, col):
            if node in closedSet:
                continue
            if node in openSet:
                children_G = current.G + current.g_score()
                if node.G > children_G:
                    node.G = children_G
                    node.parent = current
            else:
                node.G = current.G + current.g_score()
                node.H = node.h_score(goal)
                node.parent = current
                openSet.add(node)
    raise ValueError('No PATH')

def move(start, goal, matrix, row, col):
    greedy = [[0]*col for i in range(row)]
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            greedy[x][y] = Node(matrix[x][y], (x, y))
    '''
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            a = grid[x][y].get_point
            print(a)
    '''
    path = aStar(greedy[start[0]][start[1]], greedy[goal[0]][goal[1]], greedy, col)
    for node in path:
        result = node.get_point
        data = "("+ str(result[0]) + "," + str(result[1]) +")"
        wf.write(data)
    wf.write('\n')


with open('input.txt', 'r') as rf:
    content = rf.readlines()
    content = [x.strip() for x in content]
    repeat_time = int(content[0])
    del content[0]
    while repeat_time > 0:
        del content[0]
        row, col = map(int, content[0].split())
        matrix = [[0] * col for i in range(row)]
        del content[0]
        for j in range(row):
            matrix[j] = [int(x) for x in content[0].split(',')]
            del content[0]
        wf.write("\n")
        move((0,0), (row-1, col-1), matrix, row, col)
        #print("FInished!")
        repeat_time -= 1
rf.close()
wf.close()