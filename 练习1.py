# print("hello world")

#a = "hello world"
#print(a)
#a = "hello everyone"
#print(a)

#字符串大小写
#name = "hello world"
#print(name.title())
#print(name.upper())
#print(name.lower())

#合并字符串
#first = "xing"
#second = "ming"
#all = first + " " + second
#print(all)
#print("li"+" "+"zhao")

#制表符与换行符
#print("Languages: \n\tPython \n\tC \n\tJavaScript")

#删除空白(暂时性)
#a = 'python '
#print(a)
#print(a.rstrip())

#练习
#name = "Eric"
#print("hello" + " " + name + "," + "would you like noodles")

#print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

#famous_person = "Albert Einstein"
#print(famous_person +" "+"once said, "+message)

#famous_person = "Albert Einstein"
#print("\t\t" +famous_person+"  \n")
#print(famous_person.strip())

#print(5+3)

#列表
#names = ['xiaoli','xiaohong','xiaomei','xiaoqiang']
#print(names[0].title())
#print(names[0].title() +","+"miss you")

#traffic = ['bike','car','Honda motorcycle']
#print("I would like to own a" +" "+traffic[1])

#修改列表
#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles) 
#motorcycles[0] = 'ducati' 
#print(motorcycles)
#motorcycles.append('ducati') 
#print(motorcycles)
#motorcycles.insert(2, 'ducati')
#print(motorcycles)

#删除列表元素
#（1）pop()
#popped_motorcycle = motorcycles.pop() 
#print(motorcycles) 
#print(popped_motorcycle)

#(2)del 列表名[]
#del motorcycles[1] 
#print(motorcycles)

#(3)remove(元素名)
#motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
#print(motorcycles) 
#motorcycles.remove('ducati') 
#print(motorcycles)


#练习
#people = ['xiaoli','xiaohong','xiaomei']
#print("欢迎 "+people[0]+" 的到来")
#print("欢迎 "+people[1]+" 的到来")
#print("欢迎 "+people[2]+" 的到来")

#bu_neng_lai = 'xiaomei'
#people.remove('xiaomei')
#people.insert(2,'xiaozhang') 
#print(bu_neng_lai +" 有事不能来")
#print(people)
#print("欢迎 "+people[0]+" 的到来")
#print("欢迎 "+people[1]+" 的到来")
#print("欢迎 "+people[2]+" 的到来")

#print("找到了更大的餐桌，因此再邀请三人")

#people.insert(0,'xiaoliu')
#people.insert(2,'xiaoai')
#people.append('xiaogao')
#print(people)

#a =people.pop(-1)
#print(people)
#b =people.pop(-2)
#print(people)
#del people[3]
#print(people)
#del people[2]
#print(people)

#组织列表
#cars = ['bmw', 'audi', 'toyota', 'subaru']
#cars.sort()
#print(cars)
#cars.sort(reverse=True)
#print(cars)
#print(sorted(cars))
#print(sorted((cars),reverse=True))
#cars.reverse() 
#print(cars)
#cars.reverse() 
#print(cars)

#确定列表长度
#a = len(cars)
#print(str(a) + '\n')

#练习
#trip = ['shouzhou','xinzhou','yuncheng','datong','linfen']
#print(trip)
#print(sorted(trip))
#print(trip)
#print(sorted(trip,reverse =True))
#trip.reverse()
#print(trip)
#trip.reverse()
#print(trip)
#trip.sort()
#print(trip)
#trip.sort(reverse=True)
#print(trip)
#print(len(people))

#for循环
#magicians = ['alice', 'david', 'carolina'] 
#for magician in magicians: 
#    print(magician)
#    print(magician.title() + ", that was a great trick!") 
#print("Thank you, everyone. That was a great magic show!")

#练习
#pizzas = ['one','teo','three']
#for pizza in pizzas:
#    print(pizza)
#    print(pizza.title()+', I like pepperoni pizza!')
#print('I really love pizza!')

#animals = ['cat','dog','lion']
#for animal in animals:
#    print("A "+animal+ ' would make a great pet')
#print('Any of these animals would make a great pet!')

#创建数字列表
#numbers = list(range(1,6)) 
#print(numbers)

#for a in range(1,6):
#    print(a)

#squares = [] 
#for value in range(1,11): 
#  square = value**2 
#  squares.append(square) 
#print(squares)

#print(min(squares)) 
#print(max(squares))
#print(sum(squares))

#列表解析
#squares = [value**2 for value in range(1,11)] 
#print(squares)

#练习
#for value in range(1,21):
#    print(value)

#numbers = []
#for number in range(1,1000001):
#    numbers.append(number)
#print(numbers)
#print(max(numbers))
#print(min(numbers))
#print(sum(numbers))

#jishu_s =[]
#for jishu in range(1,20,2):
#    jishu_s.append(jishu)
#print(jishu_s)

#a = []
#for a_ in range(1,11):
#    a_a =a_**3
#    a.append(a_a)
#print(a)

#b =[]
#for value in range(3,31,3):
#    b.append(value)
#for value in b:
#    print(value)

#c = [value**3 for value in range(1,11)]  
#print(c)

#切片
#players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
#print(players[0:3])
#print(players[:4])
#print(players[2:])
#print(players[-3:-1])
#for player in players[:3]: 
#  print(player.title()) 

#复制列表
#my_foods = ['pizza', 'falafel', 'carrot cake'] 
#friend_foods = my_foods[0:2]
#print(friend_foods)

#练习
#numbers = ['1','2','3','4','5','6','7','8','9']
#print('The first three items in the list are:')
#print(numbers[0:3])
#print('Three items from the middle of the list are:')
#print(numbers[3:6])
#print('The last three items in the list are:')
#print(numbers[-3:])

#my_pizzas = ['one','two','three']
#friend_pizza = my_pizzas[:]
#my_pizzas.append('four')
#friend_pizza.append("six")
#print('My favorite pizzas are:')
#for pizzas in my_pizzas:
#    print(pizzas)
#print("My friend's favorite pizzas are:")
#for pizza in friend_pizza:
#    print(pizza)

#元组
#dimensions = (200, 50) 
#print(dimensions[0]) 
#print(dimensions[1])

#练习
#foods =('mifan','miantiao','tang','jiaozi','hundun')
#for food in foods:
#   print(food)
#foods[0]='dami'
#print(foods)
#print("\n")
#foods =('dami','miantiao','tang','jiaozi','yuntun')
#for food in foods:
#    print(food)


#if 语句
#requested_toppings = ['mushrooms', 'onions', 'pineapple'] 
#user = 'mushrooms'
#if user not in requested_toppings:
#    print("false") 
#else :
#    print("true")

#测试
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.") 
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.") 
#print(car == 'audi')

#colors = ['red','blue','green','pick','yellow','black']
#color = 'Red'
#if color.lower() in colors:
#    print("yes")
#else:
#    print("no")

#a = 3 
#b = 5
#if (a-b)>0 or (a+b)==8:
#    print('yes')
#else:
#    print("no")


#测试
#alien_color = 'green'
#alien_color1 = 'red'
#alien_color2 = 'yellow'
#if alien_color2 =='green':
#    print("您获得5个点")
#elif alien_color2 =='yellow':
#    print("您获得10个点")
#elif alien_color2 =='red':
#    print("您获得15个点")

#age =15
#if age < 2:
#    print("他是婴儿")
#elif age >=2 and age <4:
#    print("他是蹒跚学步")
#elif age>=4 and age<13:
#    print("他是儿童")
#elif age>=13 and age<20:
#    print("他是青少年")
#elif age>=20 and age<65:
#    print("他是成年人")
#else:
#    print("他是老年人")

#检查特殊元素
#requested_toppings = ['mushrooms', 'green peppers', 'extra cheese'] 
#for requested_topping in requested_toppings: 
#    if requested_topping == 'green peppers': 
#       print("Sorry, we are out of green peppers right now.") 
#    else: 
#       print("Adding " + requested_topping + ".") 
#       print("\nFinished making your pizza!")

#requested_toppings = [] 
#if requested_toppings: 
# for requested_topping in requested_toppings: 
#    print("Adding " + requested_topping + ".") 
#    print("\nFinished making your pizza!") 
#else: 
#    print("Are you sure you want a plain pizza?")

#available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese'] 
#requested_toppings = ['mushrooms', 'french fries', 'extra cheese'] 
#for requested_topping in requested_toppings: 
#  if requested_topping in available_toppings: 
#     print("Adding " + requested_topping + ".") 
#  else: 
#     print("Sorry, we don't have " + requested_topping + ".")

#测试
#user_names= ['admin','li','hong','lan','zhang']
#for user_name in user_names:
#    if user_name =='admin':
#        print("Hello admin, would you like to see a status report?")
#    else:
#        print("Hello "+user_name+" thank you for logging in again")

#name = []
#if name:
#    print("hello")
#else:
#    print("We need to find some users!")

#current_users = ['admin','li','hong','lan','zhang']
#news_users = ['mei','mark','hong','amy','zhang']
#for news_user in news_users:
#    if news_user.lower() in current_users:
#        print("用户名已被使用,需要输入其他用户名")
#    else :
#        print("该用户未被使用")

# 字典
#alien_0 = {'color': 'green', 'points': 5,} 
#print(alien_0) 
#alien_0['x_position'] = 0 
#alien_0['y_position'] = 25 
#print(alien_0)
#alien_0['x_position'] = 3 
#print(alien_0)
#del alien_0['points'] 
#print(alien_0)

#测试
#people = {'first_name':'li','last_name':'zhao','age':15,'city':'shanxi'}
#print(people)
#for key ,value in people:
#   print(key+' : '+str(value))
#for key  in people:
#    print(key)
#for value in people.values():
#    print(str(value))

#遍历字典
#按顺序
#favorite_languages = { 
# 'jen': 'python', 
# 'sarah': 'c', 
# 'edward': 'ruby', 
# 'phil': 'python', 
# } 
#for name in sorted(favorite_languages.keys()): 
#   print(name.title() + ", thank you for taking the poll.")

#集合set
#for language in set(favorite_languages.values()):
#   print(language)
    
#测试
#zuhe ={
#    'nile': 'egypt',
#    'huanghe':'china',
#    'laiyinhe':'faguo',
#    }
#for key ,value in zuhe.items():
#    print('The '+ key +' runs through ' +value)
#for key in zuhe:
#    print(key)
#for value in zuhe.values():
#    print(value)

#favorite_languages = { 
#    'jen': 'python',
#    'sarah': 'c', 
#    'edward': 'ruby', 
#    'phil': 'python', 
#} 
#people = ['jen', 'sarah', 'mei', 'li']
#for key in people:
#    if key in favorite_languages:
#        print(f"感谢 {key} 参与调查！")
#    else:
#        print(f"你好 {key}，请参与我们的调查！")

#嵌套
#字典列表
#alien_0 = {'color': 'green', 'points': 5} 
#alien_1 = {'color': 'yellow', 'points': 10} 
#alien_2 = {'color': 'red', 'points': 15} 
#aliens = [alien_0, alien_1, alien_2] 
#for alien in aliens: 
#   print(alien)

#aliens = [] 
# 创建30个绿色的外星人
#for alien_number in range(30): 
#    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} 
#    aliens.append(new_alien) 
# 
# 显示前五个外星人
#for alien in aliens[:5]: 
#   print(alien) 
# 显示创建了多少个外星人
#print("Total number of aliens: " + str(len(aliens)))

#用字典存储列表
#pizza = { 
#   'crust': 'thick', 
#   'toppings': ['mushrooms', 'extra cheese'], 
#    }
#for topping in pizza['toppings']: 
#   print("\t" + topping)

#在字典中存储字典
#users = { 
# 'aeinstein': { 
# 'first': 'albert', 
# 'last': 'einstein', 
# 'location': 'princeton', 
# }, 
# 'mcurie': { 
# 'first': 'marie', 
# 'last': 'curie', 
# 'location': 'paris', 
# }, 
# } 
#for username, user_info in users.items(): 
#  print("\nUsername: " + username) 
#  full_name = user_info['first'] + " " + user_info['last'] 
#  location = user_info['location'] 
#  print("\tFull name: " + full_name.title()) 
#  print("\tLocation: " + location.title())

#测试
#favourite ={
#    'xiaohong':['xiamen','guangxi','yantai'],
#    'xiaozhang':['xianggang','aomen','taiwan'],
#    'xiaomei':['shanxi','hunan','yunnan'],
#}





