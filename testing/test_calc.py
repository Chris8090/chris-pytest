import pytest
import yaml

from pythoncode.calculator import Calculator

def get_datas():
    with open("./datas/calc.yml") as f:
        datas =yaml.safe_load(f)
    add_datas =datas['add','ids']


class TestCalc():
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect',[[1,1,2],[100,100,200],[0.1,0.1,0.2]],
                             ids=['int_case','bignum_case','float_case'])
    def test_add(self,a,b,expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect
