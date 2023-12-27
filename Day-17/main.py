class User:
    def __init__(self, username):
        self.username = username
        self.followers = 0
        self.following = 0

    def print_user_name(self):
        print(self.username)

    def follow_user(self, user):
        self.following += 1
        user.followers += 1


user_1 = User(username="dag")

user_2 = User(username="yoh")

user_1.follow_user(user_2)


