import random

print("Welcome!!! Guess the Secret Number," \
" You will get 5 chances")
while True:
    secret = random.randint(1,100)
    attempts = 5
    won = False
    while attempts > 0:
        guess = int(input("Enter guess:"))

        if guess == secret:
            print("You Win!")
            won = True
            break
        elif guess > secret:
            print("Too High")
        elif guess < secret:
            print("Too Low")

        attempts -= 1 
        print(f"{attempts} attempts left")
    
    if won == False:
        print("Game Over! The number was", secret)
 
    again = input("Play again? (Yes/No): ")
    if again.lower() in ["no", "n"]:
        print("Thanks for playing!")
        break