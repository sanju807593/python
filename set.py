# s=set()       #set oru empty set ann ()
# s={'a',1,2,3}
# s.add(1)
# print(s)


# s=set() 
# s={'a',1,2,3}

# p={'d',1,2,3,4,5,6,7,8,9}   
# s.add(1)
# print(s)
# s.update({2,3,4,5})
# print(s)
# s.clear()
# print(s)
# s.discard(2)      # discard means set oru value dlt cheyyan aan eg: discard(2)   {1,3,'a'}
# print(s)

# print(s.difference(p))
# print(s)

# s=set() 
# s={'a',1,2,3}

# p={'d',1,2,3,4,5,6,7,8,9} 
# # print(s.intersection(p))
# # print(s.isdisjoint(p))
# # print(s.issuperset(p))
# # print(s.issubset(p))
# # print(s.union(p)) 
# print(s.union(p))

# h={'s',3,4,5,6,7,8,9}
# print(h.intersection(h))
# print(h.isdisjoint(h))
# print(h.issuperset(h))
# print(h.union(h))
# print(h.issubset(h))

# s=set()
# print(s)
# s.add(12)
# print(s)
# s.add((1,2,3))
# print(s)
# s.update({1,2,3,4,5,})
# # print(s)
# s={34,73,54,78,92,92}
# s1={32,54,67,68,54,78}
# # print(s.difference(s1))....ith randilum illathath...
# # print(s.intersection(s1))....ith randilum ullath...
# # print(s.isdisjoint(s1)).....true or false...
# a={2,3,4,5,6}
# b={1,2,3,4,5,6,7,8}
# print(a.issuperset(b))
# print(a.issubset(b))
# print(a.union(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))...a and b yill ulathum koodathe b yill baaki ullathum.... 

# s={1,2,3,4,5,8,9}
# s1={1,2,3,4,5,6,7}
# print(s.difference_update(s1))
# print(s.intersection_update(s1))
# print(s.symmetric_difference_update(s1))


# d={2,3,4,5,6}
# print(d)
# d.add(35)
# print(d)
# d.remove(3)
# print(d)
# d.update({7,8,9,10})
# print(d)
# d.__len__()
# print(d)

z={1,2,3,4,5,6}
z1={1,3,4,6,8,9,10,11}
print(z.difference(z1))
print(z.intersection(z1))
print(z.issubset(z1))
print(z.issuperset(z1))
print(z.difference_update(z1))
print(z.intersection_update(z1))
print(z.symmetric_difference(z1))
print(z. symmetric_difference_update(z1))
print(z.isdisjoint(z1))
print(z.copy())
print()