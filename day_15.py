s = "13,16,0,12,15,1"
ns = [int(n) for n in s.split(",")]
d = dict(zip(ns, range(1, len(ns))))
last = ns[-1]
for i in range(len(ns), 30_000_000):
    new = i - d.get(last, i)
    d[last] = i
    last = new
print(new)
