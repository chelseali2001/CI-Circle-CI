import calculator

class TestCalculatorApp:
    def test(self):
        assert 3 == calculator.add(1, 2)

    def test0(self):
        assert 1 == calculator.sub(3, 2)
    
    def test1(self):
        assert 4 == calculator.mul(2, 2)

    def test2(self):
        assert 2.0 == calculator.div(4, 2)