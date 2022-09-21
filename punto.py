class punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def string(self):
        print("(", self.x, ",", self.y, ")")
    


punto(1,2).string()