class a:
    __privateVar=50
    def __privMeth(self):
        print('Inside private function')
    def hello(self):
        print(a.__privateVar)
        O1.__privMeth()
O1=a()
O1.hello()
O1.__privMeth()