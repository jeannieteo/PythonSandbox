rooms = [[[False for r in range(2)] for f in range(5)] for t in range(3)]

for t in range(3):
    print("building: ", t)
    for f in range(5):
        print(rooms[t][f])