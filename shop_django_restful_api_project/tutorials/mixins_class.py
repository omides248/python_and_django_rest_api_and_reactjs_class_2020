class BaseClass:

    def list(self):
        return "abcd"


class MyMixin:

    def list(self):
        return super().list().upper()


class A(BaseClass):
    pass


class B(MyMixin, BaseClass):
    # def list(self):
    #     return "ABCD"
    pass


class C(MyMixin, BaseClass):
    pass


a = A()
print(a.list())
b = B()
print(b.list())
c = C()
print(c.list())
