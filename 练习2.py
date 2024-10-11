#用户的输入
#input()
#message = input("Tell me something, and I will repeat it back to you: ") 
#print(message)

#name = input("Please enter your name: ") 
#print("Hello, " + name + "!")

#prompt = "If you tell us who you are, we can personalize the messages you see." 
#prompt += "\nWhat is your first name? " 
#name = input(prompt) 
#print("\nHello, " + name + "!")

#注意str()和int()

#age = input("How old are you? ") 
#if age>=str(18):
#    print("true")

#求模 %
#number = input("Enter a number, and I'll tell you if it's even or odd: ") 
#number = int(number) 
#if number % 2 == 0: 
# print("\nThe number " + str(number) + " is even.") 
#else: 
# print("\nThe number " + str(number) + " is odd.")

#测试
#message = input("你想要什么车?")
#print("Let me see if I can find you a  "+message)

#people = input("有多少人用餐？")
#people =int(people)
#if people >8:
#    print("没有空桌")
#else:
#    print("有空桌")

#number = input("请输入一个数字")
#number = int(number)
#if number%10 ==0:
#    print("是10的整数倍")
#else:
#    print("不是10的整数倍")

#while循环
#prompt = "\nTell me something, and I will repeat it back to you:" 
#prompt += "\nEnter 'quit' to end the program. "
#active = True 
#while active: 
#  message = input(prompt) 
#  if message == 'quit': 
#     active = False 
#  else: 
#     print(message)

#break
#prompt = "\nPlease enter the name of a city you have visited:" 
#prompt += "\n(Enter 'quit' when you are finished.) "
#while True: 
# city = input(prompt)  
# if city == 'quit': 
#    break
# else: 
#    print("I'd love to go to " + city.title() + "!")

#continue
#current_number = 0 
#while current_number < 10: 
#  current_number += 1 
#  if current_number % 2 == 0: 
#    continue 
#  print(current_number)

#测试
#message = "请输入披萨配料 "
#message += "\n输入quit结束"
#while True:
#    prompt = input(message)
#    if prompt == 'quit':
#        print("结束")
#        break
#    else:
#        print(prompt)
        
#message =input("用户年龄：")
#message = int(message)
#if message<=3:
#    print("票价免费")
#elif message>3 and message <12:
#    print("票价12美元")
#else:
#    print("票价15美元")


#在列表中移动元素
#unconfirmed_users = ['alice', 'brian', 'candace'] 
#confirmed_users = [] 
#while unconfirmed_users: 
#   current_user = unconfirmed_users.pop() 
#   print("Verifying user: " + current_user.title()) 
#   confirmed_users.append(current_user) 
#print("\nThe following users have been confirmed:") 
#for confirmed_user in confirmed_users: 
# print(confirmed_user.title())
#print(unconfirmed_users)
#print(confirmed_users)

#删除包含特定值的所有列表元素
#pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'] 
#print(pets) 
#while 'cat' in pets: 
# pets.remove('cat') 
#print(pets)

#测试
#sandwich_orders =['caomei','pastrami','fanqie','pastrami','liulian','pastrami']
#finished_sandwiches =[]
#print("熟食店的五香烟熏牛肉卖完了")
#while 'pastrami' in sandwich_orders:
#   sandwich_orders.remove('pastrami')
#while sandwich_orders:
#    finished = sandwich_orders.pop()
#    print("I made your "+finished+" sandwich")
#    finished_sandwiches.append(finished)
#print(finished_sandwiches)
#print(sandwich_orders)

#wish ={}
#active =True
#while active:
#    name = input("请输入你的名字： ")
#    response = input("你想去的地方是： ")
#    wish[name] = response
#    repeat = input("还有人想回答吗?(yes or no)")
#    if repeat == 'no':
#        active =False
#for key,value in wish.items():
#    print(key)
#    print(value)


#函数
"""def greet_user(username): 
 print("Hello, " + username.title() + "!") 
greet_user('jesse')"""
#位置实参
"""def describe_pet( pet_name,animal_type='dog'):
     print("\nI have a " + animal_type + ".") 
     print("My " + animal_type + "'s name is " + pet_name.title() + ".") 
describe_pet('hamster', 'harry')
describe_pet( 'willie')"""

#测试
"""def make_shirt(name,yangshi="I love you"):
    print(name+" 想要一件有" +yangshi+"的T恤")
make_shirt("小张")
make_shirt(name="小妹")
make_shirt("xiaohong","海洋")"""

#返回值
"""def get_formatted_name(first_name, last_name): 
   full_name = first_name + ' ' + last_name 
   return full_name.title() 
musician = get_formatted_name('jimi', 'hendrix') 
print(musician)"""

"""def get_formatted_name(first_name, last_name, middle_name=''): 
  if middle_name: 
    full_name = first_name + ' ' + middle_name + ' ' + last_name 
  else: 
    full_name = first_name + ' ' + last_name 
  return full_name.title() 
musician = get_formatted_name('jimi', 'hendrix') 
print(musician) 
musician = get_formatted_name('john', 'hooker', 'lee') 
print(musician)"""

#测试
'''def make_album(name,sing_name,number=' '):
    heji= {'name':name,'sing':sing_name,'number':number}
    return heji
a = make_album('zhangjie','nizhan')
print(a)
b =make_album('xiaohong','blue',3)
print(b)'''

'''def make_album(name,sing_name):
    heji= {'name':name,'sing':sing_name}
    return heji
while True:
    print("\nPlease tell me name:") 
    print("(enter 'q' to quit)")
    name1 =input("name: ")
    if name1=='q':
      break
    sing_name1=input("sing_name: ")
    heji_ =make_album(name1,sing_name1)
    print(heji_)'''

#传递列表
'''def greet_users(names): 
 for name in names: 
   msg = "Hello, " + name.title() + "!" 
   print(msg) 
usernames = ['hannah', 'ty', 'margot'] 
greet_users(usernames)'''

#修改列表
'''def print_models(unprinted_designs, completed_models): 
 while unprinted_designs: 
   current_design = unprinted_designs.pop() 
   print("Printing model: " + current_design) 
   completed_models.append(current_design)
def show_completed_models(completed_models): 
 print("\nThe following models have been printed:") 
 for completed_model in completed_models: 
   print(completed_model) 
 
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
completed_models = [] 
print_models(unprinted_designs, completed_models) 
show_completed_models(completed_models)'''

#测试
'''magicians =['hong','lan','bai']
def show_magicians(names):
    for name in names:
        print(name)
def make_great(names):  
    great_names = []  # 创建一个空列表来存储修改后的名字  
    for name in names:  
        great_name = f"The Great {name}"  # 修改名字  
        great_names.append(great_name)  # 将修改后的名字添加到新列表中  
    return great_names  # 返回包含所有修改后名字的列表  
  
# 调用函数并打印结果  
finish = make_great(magicians)  # 获取修改后的名字列表  
print(finish)  # 打印修改后的名字列表  
show_magicians(finish)  # 显示修改后的名字'''

'''def make_pizza(size, *toppings): 
 """概述要制作的比萨""" 
 print("\nMaking a " + str(size) + 
 "-inch pizza with the following toppings:") 
 for topping in toppings: 
   print("- " + topping)'''



