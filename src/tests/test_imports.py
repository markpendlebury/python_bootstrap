import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_module_one():
    from utilities.module1 import module_one

    module_one()
    assert True


def test_module_two():
    from utilities.module2 import module_two

    module_two()
    assert True
