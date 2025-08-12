class Complex:
    def __init__(self,r,i):
        self.real = r
        self.imag = i
    def show(self):
        print(f"{self.real}+i{self.imag}")
def main():
    p = Complex(7,4)
    p.show()
if __name__ == "__main__":
    main()
