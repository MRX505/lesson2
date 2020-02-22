def ask_user():
    spr={"как дела": "хорошо!","что делаешь?":"программирую", "почему": "надо учиться"}
    x=input()

    
    if x in spr:
        print(spr[x])
    else:
        print('Я вас не понял')
    ask_user()

ask_user()