def fill(m):z=[(u+i)%2for i,x in enumerate(m)for u,a in enumerate(x)if a<1];return z.count(0)==z.count(1)and bool(z)