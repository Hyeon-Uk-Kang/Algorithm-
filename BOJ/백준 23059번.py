import sys;

ssr = sys.stdin.readline

N = int(ssr())
child_dic = {}
for _ in range(N):
    s1, s2 = ssr().split()
    try:
        child_dic[s1].append(s2)
    except:
        child_dic[s1] = [s2]
    try:
        child_dic[s2]
    except:
        child_dic[s2] = []

indeg_dic = {}
for i in child_dic:
    indeg_dic[i] = 0

for i in child_dic:
    for j in child_dic[i]:
        indeg_dic[j] += 1

stack = []
for i in child_dic:
    if indeg_dic[i] == 0:
        stack.append(i)

ans = []

t_stack = []
stack.sort(reverse=True)
while stack:
    s = stack.pop()
    ans.append(s)
    for i in child_dic[s]:
        indeg_dic[i] -= 1
        if indeg_dic[i] == 0: t_stack.append(i)
    if not stack:
        t_stack.sort(reverse=True)
        stack.extend(t_stack)
        t_stack.clear()

if list(indeg_dic.values()).count(0) == len(indeg_dic):
    for s in ans:
        print(s)
else:
    print(-1)