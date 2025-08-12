class Complex:
    def __init__(self,r = 0,i = 0):
        self.real = r
        self.imag = i
    def show(self):
        print(f"{self.real}+i{self.imag}")
def main():
    p = Complex(7,4)
    p.show()
    q = Complex()
    q.show()
    r = Complex(5)
    r.show()
if __name__ == "__main__":
    main()
        
