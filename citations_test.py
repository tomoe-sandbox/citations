import builtins
import importlib
import io
import sys
# def test_PA0(monkeypatch, capfd):
#     PA0.main()
#     monkeypatch.setattr('builtins.input', lambda _: "A v B [2020] 3 SLR 322")
#     monkeypatch.setattr('builtins.input', lambda _: "Quit")
#     out, err = capfd.readouterr()
#     assert out == "A v B [2020] 3 SLR 322"
# https://stackoverflow.com/questions/73354667/how-to-test-a-single-python-file-having-no-functions-in-it-how-to-test-for-mult

# Testing loops where input must be repeatedly entered: Use a generator https://stackoverflow.com/questions/70597270/pytest-not-looping-while-testing-with-monkeypatching

# helper functions
def make_mock_input(generator):
    def mock_input(*args, **kwargs): # ignore any arguments
        return next(generator) # the state of the generator is stored in the enclosing scope of make_mock_input
    return mock_input

def input_generator(user_input):
        yield from user_input

# tests
# https://code-maven.com/slides/python/pytest-mock-stdin 
#  We don't use monkeypatch because we need the original input prompt, as opposedto the one that monkeypatch mocks.
def test_input_exists(capsys):
    '''
    1. Checks that input exists and has the prompt "Please input your complete case citation here, Quit to exit: "
    '''
    user_input = ("\n", "Quit")
    gen = input_generator(user_input)
    mock_input = make_mock_input(gen)
    sys.modules.pop('PA0', None)
    sys.stdin = io.StringIO("\n" + "Quit") # lmao
    import PA0
    out, err = capsys.readouterr()

    assert "Please input your complete case citation here, Quit to exit: " * 2 in out # Note that prompt will be asked twice (newline, and Quit)
    
def test_input_parse(monkeypatch, capsys):
    user_input = ("A v B [2020] 3 SLR 322", "Quit")
    gen = input_generator(user_input) # create the generator from your input values
    mock_input = make_mock_input(gen)
    monkeypatch.setattr("builtins.input", mock_input)
    sys.modules.pop('PA0', None)
    import PA0
    out, err = capsys.readouterr()
    assert "A v B, [2020] 3 SLR 322\n" in out # We use this instead of checking for equality as there may be other outputs
    # https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/ - Python adds a new line character at the end of a string as the default value of the end parameter of print() is \n.


def test_citation_array(monkeypatch, capsys):
    
    user_input = ("A v B [2020] 3 SLR 322", "B v C [2019] 4 SLR 344", "Quit")
    gen = input_generator(user_input) # create the generator from your input values
    mock_input = make_mock_input(gen)
    monkeypatch.setattr("builtins.input", mock_input)
    sys.modules.pop('PA0', None)
    import PA0
    out, err = capsys.readouterr()
    assert out == "A v B, [2020] 3 SLR 322\nB v C, [2019] 4 SLR 344\n['A v B', 'B v C']\n['[2020] 3 SLR 322', '[2019] 4 SLR 344']\n" # We use this instead of checking for equality as there may be other outputs
    # https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/ - Python adds a new line character at the end of a string as the default value of the end parameter of print() is \n.



# def test_input_parsed(capsys, monkeypatch):
#     ''''''
#     mocked_stdout = io.StringIO()
#     with monkeypatch.context() as m:
#         m.setattr(builtins, "input", lambda prompt="": "A v B [2020] 3 SLR 322")

#         m.setattr(sys, "stdout", mocked_stdout)
   
#         sys.modules.pop('PA0', None)
#         importlib.import_module(name="PA0", package="citations")
#         m.setattr(builtins, "input", lambda prompt="": "Quit") 
#     assert mocked_stdout.getvalue().strip() == "A v B, [2020] 3 SLR 322"


'''

Notes:

test_PA0 works when it is a straightforward 
    user_input = input("Please input your complete case citation here, Quit to exit: ")
    print(user_input*10)
situation.
Perhaps the problem lies with loops and the need to accept input -> print -> wait for multiple input

Next steps: Redirect stdout to another file and then 
'''
    

'''
Test cases
1. Check that a program asks for an input case citation with the following point: Please input your complete case citation here, Quit to exit
2. Accepts a case citation as input. No validation needed. (Pf v Df [Year] Vol CitatorName Page)
3. Separate case name from the case citation and print the result, separated by a comma
4. Case name and case citation are saved in 2 separate lists. 
5. Have the program repeat steps 1 to 4 to ask for and process input case citations repetitively. one at a time, until the user types Quit.
6. On exit, print out lists of case names and case citations. 


'''