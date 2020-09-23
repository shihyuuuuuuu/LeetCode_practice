class Foo:
    def __init__(self):
        self.f = False
        self.s = False
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.f = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.f == False:
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.s = True
        

    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.s == False:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
