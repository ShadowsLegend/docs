def MinMax(nodes, ans, turn):
    if turn == 1:
        new = []
        for i in range(0, len(nodes), 2):
            if(i!=len(nodes)-1):
                new.append(max(nodes[i], nodes[i+1]))
            else:
                new.append(nodes[i])
        ans.insert(0, new)
        if(len(new) > 1):
            return MinMax(new, ans, 0)
        else:
            return ans
    else:
        new = []
        for i in range(0, len(nodes), 2):
            if(i!=len(nodes)-1):
                new.append(min(nodes[i], nodes[i+1]))
            else:
                new.append(nodes[i])
        ans.insert(0, new)
        if(len(new) > 1):
            return MinMax(new, ans, 1)
        else:
            return ans
leaf = [-1, 4, 2, 6, -3, -5, 0, 7, 9]
ans = MinMax(leaf, [], 1)
for i in ans:
    for j in i:
        print(f"{j}", end='\t')
    print()
for i in leaf:
    print(f'{i}', end='\t')
        
