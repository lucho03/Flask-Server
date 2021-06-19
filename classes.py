class User():    
    def __init__(self):
        self.enemy="There is no enemy "
    
    def add(self, username, enemy, num, ip):
        self.username=username
        self.num=num
        if len(enemy) > 0:
            self.enemy=enemy
        self.ip=ip
    
    def print(self):
        return f"Name: {self.username}"
    
    def __str__(self):
        return "Player " + str(self.num) + ": " + self.username + '\r' + "Enemy: " + self.enemy

class Message():
    def add(self, sender, receiver):
        self.sender=sender
        self.receiver=receiver

