
class User:
    user_list = []

    def __init__(self,username,password):
        self.username=username
        self.password=password

    def saving(self):
        User.user_list.append(self)
            
    def delete(self):
            
        User.user_list.remove(self)

    def displaying(cls):
        return cls.user_list
    
