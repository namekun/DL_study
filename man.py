# -*-coding: utf-8-*-

#__init__ : 클래스를 초기화 하는 방법을 정의한다. 이를 생성자 라고 하며, 클래스의 인스턴스가 만들어질 때 한번만 불린다.

class Man:
    def __init__(self, name): #생성자
        self.name = name
        print("initialized!")

    def hello(self): #메서드
        print("hello" + self.name + "!")

    def goodbye(self):
        print("goodbye!"  + self.name + "!")

m = Man("David")
m.hello()
m.goodbye()

