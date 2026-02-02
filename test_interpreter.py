from interpreter import CommandInterpreter
def test_add():
    ci=CommandInterpreter()
    assert ci.interpret("add 5 3")==8
def test_sub():
    ci=CommandInterpreter()
    assert ci.interpret("sub 10 4")==6
def test_invalid_input():
    ci=CommandInterpreter()
    assert ci.interpret("add five six") ="Invalid command format"
