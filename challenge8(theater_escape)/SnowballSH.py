def whichExit(m):b=[(i,l,l.index(0)) for i,l in enumerate(m) if 0 in l][0];L=sum(b[1][:b[2]])+b[1][:b[2]].count(-1);R=sum(b[1][b[2]+1:])+b[1][b[2]+1:].count(-1);return "same" if L==R else "left" if min(L,R)==L else "right"