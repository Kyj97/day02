import random

secret = random.randint(1, 10)
guess = random.randint(1, 10)
print(secret)
print(guess)

if secret > guess:
    print("too low")
elif secret == guess:
    print("just right")
else:
    print("too high")