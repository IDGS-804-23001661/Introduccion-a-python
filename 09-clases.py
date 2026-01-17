class OperacionBas:
    num1=0
    num2=0
    res=0
    def __init__(self):
        self.num1=0
        self.num2=0
    def suma(self):
        self.res=self.num1+self.num2
        print(f"La suma es; {self.res}")
    def resta(self):
        self.res=self.num1-self.num2
        print(f"La resta es; {self.res}")


def main():
    obj=OperacionBas()
    obj.suma()

if __name__ == "__main__":
    main()