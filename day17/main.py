class User :
    def __init__(self,user_id,username):
        self.user_id = user_id
        self.username = username
        self.follower = 0
        self.following = 0
    def follow(self,user):
        user.follower +=1
        self.following +=1

user1 = User("001","Roshan")
user2 = User("002","Dalami")

user2.follow(user1)

print(user1.follower)
print(user1.following)
print(user2.follower)
print(user2.following)