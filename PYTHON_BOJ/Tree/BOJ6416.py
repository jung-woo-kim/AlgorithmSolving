import sys

Tree_in = dict()
Tree_out = dict()
node = []
case = 1
edge = 0
answer = []
while True:
    
    line = sys.stdin.readline().rstrip()
    # -1 -1이 입력된 경우 입력종료
    if line == '-1 -1': 
        break
    # 빈 줄이 입력된 경우 무시
    elif line == '': 
        continue
    caseEnd = False
    inputLine = list(map(int,line.split()))
    # 입력으로 0 0이 들어올 때까지 간선 내용 저장
    for i in range(0,len(inputLine),2): 
        
        if inputLine[i] == 0 and inputLine[i+1] == 0: 
            caseEnd = True
            break
        try:
            Tree_out[inputLine[i]].append(inputLine[i+1])
        except:
            Tree_out[inputLine[i]] = [inputLine[i+1]]
        try:
            Tree_in[inputLine[i+1]].append(inputLine[i])
        except:
            Tree_in[inputLine[i+1]] = [inputLine[i]]
        edge+=1
        node.append(inputLine[i])
        node.append(inputLine[i+1])
    
    if caseEnd:
        node = set(node)
        root = -1
        is_cycle = False
        check_Tree = True

        for n in node:
            ##루트노드 하나
            in_node_li = []
            try:
                in_node_li = Tree_in[n]
            except:
                in_node_li = []

            if len(in_node_li) == 0:
                if root != -1:
                    check_Tree = False
                root = n
            ##들어오는 개수가 2개이상이면 False
            if len(in_node_li) >=2:
                check_Tree = False
        
        if root == -1:
            check_Tree = False

        if edge + 1 != len(node):
            check_Tree = False

        # visit = dict()       
        # ##사이클 체크 왜 없어도 되는거지..
        # def dfs(node):
        #     global is_cycle

        #     out_node = []
        #     try:
        #         out_node = Tree_out[node]
        #     except:
        #         out_node = []
            
        #     #print(out_node)
        #     for n in out_node:
        #         try:
        #             visit[n] += 1
        #             is_cycle = True
        #             return
        #         except:
        #             visit[n] = 1
        #         dfs(n)
        #         if is_cycle:
        #             return
                    
        # dfs(root)

        # if is_cycle:
        #     check_Tree = False
        
        # visit[root] = 1
        # for n in node:
        #     try:
        #         visit[n] += 1
        #     except:
        #         check_Tree = False
        
        if check_Tree or len(node) == 0:
            answer.append("Case "+str(case)+" is a tree.")
            
        else:
            answer.append("Case "+str(case)+" is not a tree.")
        
        case += 1
        edge = 0
        node = []
        Tree_in = dict()
        Tree_out = dict()

for a in answer:
    print(a)