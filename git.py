import random
points = {"comp":0,"player":0}
while True:
    a = random.randint(1,9)
    b = random.randint(1,9)
    op = random.choice(("+","-"))
    if op == "+":
        ans=a+b
        user=input(f"{a}+{b}=")
    else:
        ans=a-b
        user=input(f"{a}-{b}=")
    if user == str(ans):
        print("верно")
        points["player"] +=1
    else:
        print('ты ошибся, попробуй ещё раз')
        points["comp"]+=1
    print(f'Счёт: {points["player"]}:{points["comp"]}')













