import random

#4.2
small = random.choice([True, False])
green = random.choice([True, False])

if small:
    if green:
         print("완두콩은 작고 녹색이다.")
    else:
         print("체리는 작고 녹색이 아니다.")
else:
    if green:
            print("수박은 크고 녹색이다.")
    else:
        print("호박은 크고 녹색이 아니다.")

#심심해서 추가
if green:
    if small:
         print("완두콩은 작고 녹색이다.")
    else:
         print("수박은 크고 녹색이다.")
else:
    if small:
            print("체리는 작고 녹색이 아니다.")
    else:
        print("호박은 크고 녹색이 아니다.")