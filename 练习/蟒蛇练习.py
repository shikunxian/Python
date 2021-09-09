
#a=list(range(1,21))
#print(a)


#x=list(range(1,10000001))
#print('最大数为:',max(x),'\n最小数为:',min(x),'\n和为：',sum(x))


#nub=list(range(3,30,3))
#for a in nub:
#    print(a,end=' ')


#l=[]
#for i in range(1,11):
#    s=i**3
#    print(s,end=' ')
#    l.append(s)
#print(l)


#使用列表解析生成一个列表，其中包含前10个整数的立方。

#squares=[value**3 for value in range(1,10)]
#print(squares)
#for i in squares:
#    print(i)
#    print(i,end=' ')

#57页 4-10切片
#playsrs=['charles','martina','michael','florence','eli']

#使用切片打印列表前三个元素
#print('The first three items in the list are:')
#print(playsrs[:3])

#使用切片打印列表的中间三个元素
#print('Three items from the middle of the list are:')
#print(playsrs[1:4])
#使用切片打印列表的末尾三个元素
#print('The last three items in the list are:')
#print(playsrs[2:])

#4-11:
#favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
#复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]）
#friend_pizzas = favorite_pizzas[:]

#favorite_pizzas.append("meat lover's")
#friend_pizzas.append('pesto')

#print("My favorite pizzas are:")
#for pizza in favorite_pizzas:
#    print(f"- {pizza}")
#print("\nMy friend's favorite pizzas are:")

#for pizza in friend_pizzas:
#    print(f"- {pizza}")

#4-12:
#my_foods = ['pizza','falafel','carrot cake']
#print("My favorite foods are:")
#for food in my_foods:
#    print(food)

#friend_foods = ['pizza','falafel','carrot cake','ice ccream']
#print("My friend's favorite foods are:")
#for foods in friend_foods:
#    print(foods)

#4-13:
#menu =(
#    'jiucai','jidan','duofu','xihongsi','pinggou'
#)

#print("you can choose from the following menu items:")
#for menus in menu:
#    print(menus)

#menu = (
#    'jiucai','jidan','duofu','xihongsi','pinggou','king crab legs',
#        )
#print("\nOur menu hes been updated.")
#print("you can now choose from the fillowing items:")
#for menus in menu:
#    print(f"-{menus}")


#5-3:

#alien_color = 'red'
#if alien_color=='green':
#    print("you just earned 5 points!")
#elif alien_color=="yellow":
#    print("you just earned 10 points!")
#else:
#    print("you just earned 15 points!")
























# 8-1:消息
#def display_messge(content):
#    """"显示一条消息，指出你在本章学的是什么。"""
#    learning_content = "本章学习了函数"
#    print(f"本章学习了:{content}")

#display_messge("函数")

# 8-2：喜欢的书。
def faxorite_book(title):

    print(f"{title} is one of my favorite books.")

faxorite_book('The Abstract wild')