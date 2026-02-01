# Creating a Game Level System 
Player_level = int(input("Player Level: "))
has_training = input("Completed the Training(Yes or No): ").lower().strip()
user_input = has_training in ["yes","y","true"]
Level_Message = "None"

if 1 <= Player_level <= 5 :
    Level_Message = "Basic Weapons Unlocked"
elif 6 <= Player_level <= 15 :
    if user_input:
        Level_Message = "Advanced Weapons Unlocked"
    else:
        Level_Message = "Require Training"
elif 16 <= Player_level :
    Level_Message = "Unlocked All Weapons"
else:
    Level_Message = "Invalid Level"

print(Level_Message)