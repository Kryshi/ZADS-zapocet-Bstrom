# Zápočtová úloha ZADS
# Kryštof Stejskal

class Node:
    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.n = 0
        self.leaf = leaf


class Tree:
    def __init__(self, t):
        self.root = Node(True)
        self.t = t

    def split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = Node(y.leaf)
        z.leaf = y.leaf
        z.n = t - 1
        y.n = t - 1
        for j in range(t-1):
            z.keys.append(y.keys[j + t]) 
        if not y.leaf:
            for j in range(t):
                z.children.append(y.children[j + t])
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        x.n = x.n + 1

    def tree_insert(self, k):
        root = self.root
        if root.n == (2 * self.t) - 1:
            temp = Node()
            self.root = temp
            temp.children.insert(0,root)
            self.split_child(temp, 0)
            self.tree_insert_nonfull(temp, k)
        else:
            self.tree_insert_nonfull(root, k)

    def tree_insert_nonfull(self, x, k):
        i = x.n - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i = i - 1
            x.keys[i + 1] = k
            x.n = x.n + 1
        else:
            while i >= 0 and k < x.keys[i]:
                i = i - 1
            i = i + 1
            if x.children[i].n == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i = i + 1
            self.tree_insert_nonfull(x.children[i], k)   

    def search_key(self, k, x=None):
        if x is None:
            return self.search_key(k, self.root)
        else:
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1
            if i < len(x.keys) and k == x.keys[i]:
                print("Number", k, "found")
                
            elif x.leaf:
                print("Number", k, "not found")
            else:
                return self.search_key(k, x.children[i])
            

    def print_node(self, x, ir):
        #funkce na konečné vypsání obsahu stromu, pro každý node napíše jeho hloubku
        print("Level:", ir)
        for i in range (x.n):
            print(x.keys[i])
        if not x.leaf:
            print(" ")
            for j in range(x.n + 1):
                ir+=1
                self.print_node(x.children[j],ir)
                ir-=1  
        print(" ")

    def print_tree(self):
        self.print_node(self.root, 0)



B = Tree(2)

B.tree_insert(1)
B.tree_insert(2)
B.tree_insert(4)
B.tree_insert(8)
B.tree_insert(5)
B.tree_insert(9)
B.tree_insert(10)
B.tree_insert(11)
B.tree_insert(12)
B.tree_insert(13)

B.print_tree()

B.search_key(1)
B.search_key(7)
B.search_key(9)
B.search_key(14)


