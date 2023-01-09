from io import StringIO
import subprocess
import citations

# case = StringIO("Corr v IBC Vehicles Ltd 2008 UKHL 13\n")

# def test_year(monkeypatch, capsys):
#     subprocess.run(["python", "citations.py"], stdout=subprocess.PIPE, check=True)
#     monkeypatch.setattr('sys.stdin', case)
#     captured = capsys.readouterr()
#     assert captured.out == {'party': 'Corr v IBC Vehicles Ltd ', 'year': '', 'court': '', 'case_no': ''}

    # https://stackoverflow.com/questions/73354667/how-to-test-a-single-python-file-having-no-functions-in-it-how-to-test-for-mult 
def test_hi(capsys):
    subprocess.run(["python", "citations.py"], stdout=subprocess.PIPE, check=True)
    captured = capsys.readouterr()
    assert captured.out == "Hello!\n"

# https://stackoverflow.com/questions/73354667/how-to-test-a-single-python-file-having-no-functions-in-it-how-to-test-for-mult 