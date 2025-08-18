from readylist.core import ReadyList

def test_greet():
    readylist = ReadyList()
    assert readylist.greet("Alice") == "Hello, Alice!"
