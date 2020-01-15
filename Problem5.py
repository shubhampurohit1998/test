class Demo:
    def getString(self,s):
        self.s = s

    def printString(self):
        print(str.upper(self.s))
d = Demo()
d.getString('hello')
d.printString()