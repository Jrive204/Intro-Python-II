# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self,name, description,**kw):
        self.name = name
        self.description = description
        super().__init__(**kw)

    def __str__(self):
        return f" {self.name},{self.description}"

    def move(self,player):
        print(f'{player.status(self.name)}')
        done = False
        while not  done:
            if(self.name == "Foyer"):
                while True:
                    print('Glad to see you have made it this FAR!!')
                    ma= input(f"in Foyer whats next: type-[status] for current player status:\n")
                    if ma=="out":
                            done=True
                            break
                            
            if(self.name == "Outside"):    
                m= input(f"What do you do next: type-[status] for current player status:\n")
                if m.lower() == "status":
                    print(f'{player.status(self.name)}')    
                if m=="hi":
                     done = True
                     break