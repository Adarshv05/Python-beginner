import random

def game():
    score=random.randint(1,100)
    print(f"Socre {score}")
    return score

score=game()
with open("81 game_score.txt", "r") as f:
    hscore=int(f.read())

if score>hscore:
    with open("81 game_score.txt", "w") as f:
        f.write(str(score))
