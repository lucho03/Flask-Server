class User():    
    def add(self, username, enemy, num):
        self.username=username
        self.num=num
        self.enemy=enemy
    
    def print(self):
        return f"Name: {self.username}"
    
    def __str__(self):
        return "Player " + str(self.num) + ": " + self.username + " vs " + self.enemy
