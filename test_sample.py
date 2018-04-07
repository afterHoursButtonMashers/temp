""" This is a simple example of a test """

def inc(var_x):
    """Function that increments"""
    return var_x + 1


def test_answer():
    """Simple unit test"""
    assert inc(4) == 5
