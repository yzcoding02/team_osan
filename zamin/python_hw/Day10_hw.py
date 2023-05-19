fruits=[]
for i in range(1,11):
    fruits={'orange':500,'banana':301,'apple':460}
    fruitss=input('what do you want?:')
    if fruitss in fruits:
        print(f"우리는 가지고 잇어요{fruits},{fruits[fruitss]}남아있어요")
    else:
        print(f"우리는 지금 {fruits}를 가지고 있지 않아요")