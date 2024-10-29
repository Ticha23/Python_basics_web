#list

scores = [90, 45, 87, 35, 50]

#acces a value
print(scores[0])
print(scores[-1])

#add
scores.append(62)
print(scores)

#remove
scores.pop(3)
print(scores)

scores.sort(reverse=True)
print(scores)