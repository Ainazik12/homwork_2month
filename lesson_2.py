# class User:
#     def __init__(self, name, email, phone):
#         print(name)
        
#     def info(self):
#         print(self.name)
        
        
# user = User("Нурболот", "email@gmail.com", "8943893")
# user.info()

# class User:
#     def __init__(self, name, email, phone):
#         self.name   = name 
#         self.email   = email
#         self.phone = phone
        
#     def info(self):
#         print(self.name)

# user = User("Нурболот", "email@gmail.com", "8943893")
# user.info()


# class Dad:
#     def info_dad(self):
#         print("Я отец")
        
        
# dad = Dad()
# dad.info_dad()


# class son(Dad):
#     def info_son(self):
#         print("Я сын")
        
        
# son = Son()
# son.info_son()    
# son.info_dad()    



# class Dog:
#     def info_dog(self):
#         print("ГАФ ГАФ")
  
# dog = Dog()
# dog.info_dog()  
  
       
# class Cat(Dog):
#     def info_cat(self):
#         print("МИЯу МИЯу")
        
        
# cat = Cat()
# cat.info_cat()    
# cat.info_dog()   
        
        
# class Mother:
#     def info_mom(self):
#         print("Я мама. Я родительский класс Mother")    
      
# class Father:
#     def info_dad(self):
#         print("Я папа. Я родительский класс Father")   
        
# class Son(Mother, Father):
#     def info_son(self):
#         print("Я сын. Я дочерный класс Son, Я наследуюсь от класс Mother и Father")
        
# son = Son()
# son.info_mom()     
# son.info_dad()
# son.info_son()         



# class Phone:
#     def info_phone(self):
#         print("Я звоню маме")    
      
# class Camera:
#     def info_camera(self):
#         print("Я фоткаю отца")   
        
# class SmartPhone(Phone, Camera):
#     def info_smartphone(self):
#         print("Я фоткаю и так же звоню")
        
# smartphone = SmartPhone()
# smartphone.info_phone()     
# smartphone.info_camera()
# smartphone.info_smartphone() 