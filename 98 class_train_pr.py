class Train:
    def __init__(self):
        self.seats=99
        self.fare=200

    def book(self):
        self.seats= self.seats -1

    def Status(self):
        print(self.seats)
    
    def FareInfo(self):
        print(self.fare)

tt=Train()
tt.FareInfo()
tt.Status()
tt.book()
tt.Status()