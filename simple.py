class Simple:
    name = "Test"

    def no_self():
        print("This is a method that can't access anything about the class or object")

    @classmethod
    def cls_not_self(cls):
        print(cls.name)

    def __init__(self, secret):
        self.secret = secret

    def getSecret(self):
        return self.secret

    def __str__(self):
        return "I can't be bothered"


print(Simple.name)

simple_o = Simple("this is not that secret")
simple_o_again = Simple("Still not very secret")

print(simple_o.getSecret())
print(simple_o_again.getSecret())
print(simple_o)

Simple.no_self()