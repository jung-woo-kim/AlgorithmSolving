import sys

class Node(object):
    def __init__(self,key,data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert(self,string):
        curr_node = self.head

        for s in string:
            if s not in curr_node.children:
                curr_node.children[s] = Node(s)
            curr_node = curr_node.children[s]
        
        curr_node.data = string
    
    def search(self, string):
        curr_node = self.head

        for s in string:
            curr_node = curr_node.children[s]

        if curr_node.children:
            return False

        else:
            return True

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    trie = Trie()
    nums = []

    for _ in range(n):
        num = sys.stdin.readline().rstrip()
        nums.append(num)
        trie.insert(num)
    
    flag = True

    for num in nums:
        if not trie.search(num):
            flag = False
            break
    
    if flag:
        print("YES")
    else:
        print("NO")