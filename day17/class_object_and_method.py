# # PascalCase
# # snake_case
# # camelCase


# # class User:
# #     pass    
    
# # user_1 = User()
# # user_1.id= "001"
# # user_1.name= "Bikash"

# # print(user_1.name)


# # user_2 = User()
# # user_2.id= "002"
# # user_2.name= "Dhami"
# # print(user_2.name)


# # class User:
#     # def __init__(self):             #Constructor
#     #     print("New user is being created")
    
        
# # user_1 = User()
# # user_1.id= "001"
# # user_1.username= "Bikash"

# # print(user_1.username)


# # user_2 = User()
# # user_2.id= "002"
# # user_2.username= "Dhami"
# # print(user_2.username)



# class User:
#     def __init__(self,user_id,username):
#         self.id=user_id
#         self.username=username
#         self.follower=0
    
# user_1=User("001","Bikash")
# print(user_1.id)
# print(user_1.username)
# print(user_1.follower)

# user_2=User("002","Dhami")
# print(user_2.id)
# print(user_2.username)


class User:
    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        self.followers=0
        self.following=0
        
    def follow(self,user):
        user.followers += 1
        self.following += 1
 
user_1=User("001","Bikash")       
user_2=User("002","Dhami")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)