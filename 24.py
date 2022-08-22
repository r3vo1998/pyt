class Square():
    square_list = []
     
    def __init__(self, l):
        self.length = l
        self.square_list.append((self.length))
        
    def calculate_perimeter(self):
        return self.length * 4
    
    def change_size(self, l):
        self.length = l

    def print_size(self, l1, l2, l3, l4):
        self.length1 = l1
        self.length2 = l2
        self.length3 = l3
        self.length4 = l4
        print("{} на {} на {} на {}".format(self.length1,
                                            self.length2,
                                            self.length3,
                                            self.length4))
    
