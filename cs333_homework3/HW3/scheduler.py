import math

def bfs(graph,s,t):
    visited = [0 for i in range(len(graph))]
    parents = [-1 for i in range(len(graph))]
    visited[s] = 1
    q = []
    q.append(s)
    while len(q) != 0:
        v = q[0] 
        q.pop(0)
        for i in range(len(graph[v])):
            if(graph[v][i]>0 and visited[i]==0):
                q.append(i)
                visited[i] = 1
                parents[i] = v
    found = False
    path = [t]
    if visited[t] == 0:
        return (False,[-1])
    else :
        n = t
        while parents[n] != -1:
            path.append(parents[n])
            n = parents[n] 
        return (True,path)
    

def fordFulkerson(graph,s,t):
    residual_graph = [[graph[i][j] for j in range(len(graph))] for i in range(len(graph))]
    max_flow = 0
    while(bfs(residual_graph,s,t)[0]==True):
        path = bfs(residual_graph,s,t)[1]
        min_cost = math.inf
        for n in range(len(path)-1):
            u = path[n+1]
            v = path[n]
            if residual_graph[u][v] < min_cost:
                min_cost = residual_graph[u][v]
        for n in range(len(path)-1):
            u = path[n+1]
            v = path[n]
            residual_graph[u][v] -= min_cost
            residual_graph[v][u] += min_cost
        max_flow += min_cost
    return max_flow

def takeInput():
    
    file_path = input()
    file = open(file_path, 'r')
    lines = file.readlines()

    operations = []
    operation_shifts = []
    employee_shifts = []
    employee_professions = []
    for n in range(4):
        operation = lines[2*n].split(' ')
        operation_name = operation[0]
        operation_number = int(operation[1])
        shifts = lines[2*n+1].split(' ')
        for sh in range(len(shifts)):
            shifts[sh] = int(shifts[sh])
        operation_shifts.append(shifts)
        operations.append((operation_name,operation_number))
    n_employees = int(lines[8][10])
    for n in range(n_employees):
        professions = lines[9+2*n].split(' ')
        for p in range(len(professions)):
            professions[p] = professions[p][:-1]
        shifts = lines[10+2*n].split(' ')
        for sh in range(len(shifts)):
            shifts[sh] = int(shifts[sh])
        employee_professions.append(professions)
        employee_shifts.append(shifts)

    n_nondes = 4 + 4 + n_employees + 24 + 2 #start and terminal (2) + profession*2 + employees + n_shifts
    graph = [[0 for j in range(n_nondes)] for i in range(n_nondes)]
    for i in range(4):
        graph[0][i+1] = math.inf # 1 to 4 will represent the professions
    for e in range(len(employee_professions)):
        for p in range(len(employee_professions[e])): # 5 to n_employees + 4 (8 in this case) will represent the employees
            if employee_professions[e][p] == 'blend':
                graph[1][5+e] = math.inf
            elif employee_professions[e][p] == 'cook':
                graph[2][5+e] = math.inf
            elif employee_professions[e][p] == 'strain':
                graph[3][5+e] = math.inf
            elif employee_professions[e][p] == 'finish':
                graph[4][5+e] = math.inf
    for e in range(len(employee_shifts)): # 9 to 32 will represent shift hours
        for shift in range(len(employee_shifts[e])):
            graph[5+e][9+employee_shifts[e][shift]] = 1
    for p in range(len(operation_shifts)):
        for sh in range(len(operation_shifts[p])):
            graph[9+operation_shifts[p][sh]][33+p] += operations[p][1]
    for p in range(len(operations)):
        graph[33+p][37] = math.inf
    
    max_flow_expected = 0
    for p in range(len(operations)):
        max_flow_expected += (len(operation_shifts[p])*operations[p][1])
    return max_flow_expected == fordFulkerson(graph,0,37)

print(takeInput())