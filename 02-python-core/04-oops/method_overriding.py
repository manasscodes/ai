# Method Overriding
class Parent:
    def show(self):
        print("Parent show() called")

class Child(Parent):
    def show(self):
        print("Child show() called (overridden)")

c = Child()
c.show()