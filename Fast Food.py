best = ["chick fil a", "zaxby's", "popeyes", "famous recipe"]
fast = ["mcdonalds", "DQ", "burger king", "five guys"]
sandwich = ["quiznos", "subway", "jersey mikes", "potbelly"]
all = [best, fast, sandwich]

#1
print()
print(all[1])

#2
print()
for x in range (len(all)):
    print()
    for a in range(3):
        print(all[x][a], end=" ")
best[3] = "KFC"
sandwich[3] = "penn station"

#3
print()
print()
for x in range(3):
    print(all[x][3])
