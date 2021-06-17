class User():    
    def add(self, username, enemy, num, ip):
        self.username=username
        self.num=num
        self.enemy=enemy
        self.ip=ip
    
    def print(self):
        return f"Name: {self.username}"
    
    def __str__(self):
        return "Player " + str(self.num) + ": " + self.username + " vs " + self.enemy

class Message():
    def add(self, sender, receiver):
        self.sender=sender
        self.receiver=receiver

