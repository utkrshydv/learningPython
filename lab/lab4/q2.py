t1 = (1, 2, 3)
print(t1[1])

t2 = ('python', 3.10, True)
lang, version, is_dynamic = t2
print(lang, version, is_dynamic)

# t2[2] = 99  # tuple doesnt support item assignment

t3 = (42,) #if i do just (42) -> it returns int
print(type(t3))
