import random

#4.1
secret = random.randint(1, 10)
guess = random.randint(1, 10)
print(f'secret는 {secret} 입니다.')
print(f'guess는 {guess} 입니다.')

if secret > guess:
    print("too low")
elif secret == guess:
    print("just right")
else:
    print("too high")