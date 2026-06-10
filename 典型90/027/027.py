N = int(input())
user_names = [input() for _ in range(N)]

registered = set()
accepted_days = []

for day, name in enumerate(user_names, start = 1):
    if name not in registered:
        registered.add(name)
        accepted_days.append(day)
print("\n".join(map(str, accepted_days)))