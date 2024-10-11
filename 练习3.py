#传递任意数量的实参
'''def make_pizza(*toppings): 
 print(toppings) 
 for topping in toppings: 
  print("- " + topping)
make_pizza('pepperoni') 
make_pizza('mushrooms', 'green peppers', 'extra cheese')'''

'''def build_profile(first, last, **user_info):  
 profile = {} 
 profile['first_name'] = first 
 profile['last_name'] = last 
 for key, value in user_info.items():
   profile[key] = value 
 return profile 
user_profile = build_profile('albert', 'einstein', 
 location='princeton', 
 field='physics') 
print(user_profile)'''

#测试
'''def san(*foods):
    print(foods)
san('rou')
san('bread','fanqie','zhishi')'''

'''def build_profile(first,last,**message):
    profile={}
    profile['first']=first
    profile['last']=last
    for key,values in message.items():
        profile[key]=values
    return profile
a=build_profile('amy','john',age='15',tall='165')
print (a)'''

#导入整个模块
'''from untitled  import make_pizza
make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')'''



#类
'''class Dog(): 
 """一次模拟小狗的简单尝试""" 
 def __init__(self, name, age): 
  """初始化属性name和age""" 
  self.name = name 
  self.age = age 
 def sit(self): 
  """模拟小狗被命令时蹲下""" 
  print(self.name.title() + " is now sitting.") 
 def roll_over(self): 
  """模拟小狗被命令时打滚""" 
  print(self.name.title() + " rolled over!")
my_dog = Dog('willie', 6) 
print("My dog's name is " + my_dog.name.title() + ".") 
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.roll_over()'''

#测试
'''class Restaurant:
  def __init__(self,restaurant_name , cuisine_type):
    self.restaurant_name =restaurant_name
    self.cuisine_type = cuisine_type
    self.number = 0
  def describe_restaurant(self):
    print(self.restaurant_name )
    print(self.cuisine_type)
  def open_restaurant(self):
    print('餐馆正在营业')
  def increment_number_served(self,number):
    self.number  +=number
    print(self.number)'''
'''restaurant=Restaurant('old_dad','中餐')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number =12
print(restaurant.number)
print(restaurant.restaurant_name+" "+restaurant.cuisine_type)
restaurant=Restaurant('old_dad','中餐')
restaurant.increment_number_served(300)
restaurant.increment_number_served(300)'''


'''class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name  =last_name
        self.login_attempts =0
    def describe_user(self):
        print(self.first_name+" "+self.last_name)
    def greet_user(self):
        print("how are you")
    def increment_login_attempts(self):
        self.login_attempts +=1
        print(self.login_attempts)
    def reset_login_attempts(self):
        self.login_attempts =0
        print(self.login_attempts)
user1 = User('zhang','jie')'''
'''user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()'''
'''user1.describe_user()
user1.greet_user()
user2 = User('li','xing')
print(user2.first_name)'''


#继承
'''class Car():
 """一次模拟汽车的简单尝试"""
 def __init__(self, make, model, year):
   self.make = make
   self.model = model
   self.year = year
   self.odometer_reading = 0
 
 def get_descriptive_name(self):
  long_name = str(self.year) + ' ' + self.make + ' ' + self.model
  return long_name.title()
 
 def read_odometer(self):
  print("This car has " + str(self.odometer_reading) + " miles on it.")
 
 def update_odometer(self, mileage):
  if mileage >= self.odometer_reading:
   self.odometer_reading = mileage
  else:
   print("You can't roll back an odometer!")
 
 def increment_odometer(self, miles):
  self.odometer_reading += miles
class ElectricCar(Car): 
 """电动汽车的独特之处""" 
 def __init__(self, make, model, year): 
  """初始化父类的属性""" 
  super().__init__(make, model, year) 
 
my_tesla = ElectricCar('tesla', 'model s', 2016) 
print(my_tesla.get_descriptive_name())'''


#测试
'''class IceCreamStand(Restaurant):
  def __init__(self, restaurant_name, cuisine_type):
    super().__init__(restaurant_name, cuisine_type)
    self.types= ['xiangcao','caomei','hamigua','xiangyu']
  def describe(self):
    for type in self.types:
      print(type)
iceCreamStand = IceCreamStand('young','dinner')
iceCreamStand.describe()'''

'''class Privilege:  
    def __init__(self, privileges=None):  
        if privileges is None:  
            privileges = ['can add post', 'can delete post', 'can ban user']  
        self.privileges = privileges  
        print(self.privileges)  

class Admin(User):  
    def __init__(self, first_name, last_name):  
        super().__init__(first_name, last_name)  
        self.privileges = Privilege() 
    
admin= Admin('zhang','jie')'''


