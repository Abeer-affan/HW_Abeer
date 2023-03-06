class Rectongle:
    name = "Rectongle"
    def __init__(self,width,height):
            self.width = width
            self.height = height
    def area(self):
        return (self.width*self.height)

rec= Rectongle(5,4)
print(rec.area())