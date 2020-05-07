# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self,name, description,**kw):
        self.name = name
        self.description = description
        super().__init__(**kw)

    def __str__(self):
        return f" {self.name},{self.description}"

    def move(self):
        while True:
            print(f'testing move, {self.name}')
            m= input(f"What do you do next:")
            if m=="hi":
                    break