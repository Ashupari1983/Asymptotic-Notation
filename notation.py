names = ['Aarav','Riya','Raj','Priya','Ram']
scores = [90, 80, 73, 77, 82]
n = len(scores)
print('Score Tracker for n = 5 players')
for i in range (n):
    print(i+1 , ". " , names[i] , " : " , scores[i])

print('Score at index [0]: ', scores[0], 'Theta(1) - Tight Bound')


steps = 0
for i in range(n):
    steps +=1
    if names[i] == 'Aarav':
        break
print('Search for Aarav: ',"steps: ",steps,"Omega(1) - Best Case Lower Bound")

target = "Ram"
steps = 0
for i in range(n):
    steps +=1
    if names[i] == target:
        break
print('Search for Aarav: '"O(n) = ",steps," - Worst Case Upper Bound")

print("Pairs with sum 150:")

target_sum = 150
steps = 0

for i in range (n):
    for j in range(i+1,n):
        steps +=1
        if scores[i] + scores[j] == target_sum:
            print(names[i] + names[j] == target_sum)

print('Total comparisons: ', steps, "O(n**2) - only keeps dominant term")   