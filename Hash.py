d={'age':17}
d['name']="Sanjay"
print(d["name"])
print(d["age"])
for k in d.keys():
    print(d[k])
for k,v in d.items():
    print(str(k)+":"+str(v))
m={}
l=["a","b","c"]
n=[32,54,76]
m={k:v for k,v in zip(l,n)}
for k,v in m.items():
    print(str(k)+":"+str(v))

