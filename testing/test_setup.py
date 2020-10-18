def test_case1():
    print("case1")

def setup_function():
    print("setup function ready")

def teardown_function():
    print("teardown funciton done")

class TestDemo:
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")
    def setup(self):
        print("TestDemo setup")

    def teardown(self):
        print("TestDemo teardown")
    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")