""" This is a simple example of a test """

def inc(var_x):
    """Function that increments"""
    return var_x + 1


def test_answer():
    """Simple unit test"""
    assert inc(4) == 5


def test_bad_answer():
    """test other stuff"""
    assert inc(3) != 5
