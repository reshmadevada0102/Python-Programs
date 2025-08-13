class MyList:
    def __init__(self, n=None):
        self.data = n

    def show(self):
        print(f"List is {self.data}")

    def __eq__(self, a):
        if len(self.data) != len(a.data):
            return False
        for i in range(len(self.data)):
            if self.data[i] != a.data[i]:
                return False
        return True

def main():
    list1 = MyList([1, 2, 3, 4])
    list2 = MyList([1, 2, 5, 4])
    
    list3 = MyList()

    list1.show()
    list2.show()
    list3.show()
    
    if list1 == list2:
        print("Both lists are the same.")
    else:
        print("Lists are different.")
if __name__ == "__main__":
    main()