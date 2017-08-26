from sys import stdin
T = int(stdin.next())
for t in range(T):
  C = int(stdin.next())
  I = int(stdin.next())
  P = map(int, stdin.next().split())
for i, p in enumerate(P):
    if C-p in P[i+1:]:
     break

print('Case #%d: %d %d' % (t+1, i+1, i+1 + P[i+1:].index(C-p)+1))
