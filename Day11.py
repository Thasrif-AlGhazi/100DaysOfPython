print("Welcome to Day11")
scores=[]
#Using lisit to do a scores project.
for i in range(5):
    score = int(input(f"Enter Score {i+1}: "))
    scores.append(score)
print(f"Highest Score: {max(scores)}")
print(f"Lowest Score: {min(scores)}")
print(f"Average Score: {sum(scores) / len(scores)}")

scores.sort()
print(f"Sorted Order: {scores}")

scores.remove(min(scores))
print(f"Without lowest Score: {scores}")