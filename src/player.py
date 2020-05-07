# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,name,**kw):
        self.pname=name
        super().__init__(**kw)

    def __str__(self):
        return f'Player: {self.pname}\n'

    def inventory(self):
        pass
    def status(self,desc):
        return f'** player: {self.pname} , Current Location: {desc} **'
        