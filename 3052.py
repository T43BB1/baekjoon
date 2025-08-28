unique_mods = set() 

for _ in range(10):
    X = int(input())
    mod = X % 42
    unique_mods.add(mod)
print(len(unique_mods))