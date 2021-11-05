import os

def test_python3_version():
    stream = os.popen('python3 --version')
    version = stream.read().split(' ')[1].strip()
    assert version == '3.8.10'

def test_pip_version():
    stream = os.popen('pip --version')
    version = stream.read().split(' ')[1].strip()
    assert version == '20.0.2'

def test_pip_stockfish_version():
    stream = os.popen('pip show stockfish')
    version = stream.read().split('\n')[1].split(' ')[1].strip()
    assert version == '3.17.0'

def test_pip_pytest_version():
    stream = os.popen('pip show pytest')
    version = stream.read().split('\n')[1].split(' ')[1].strip()
    assert version == '6.2.5'

def test_stockfish_version():
    stream = os.popen('stockfish compiler')
    stream_split = stream.read().split('\n')
    stream_split_0_split = stream_split[0].split(' ')
    version_p1 = stream_split_0_split[1].strip()
    version_p2 = stream_split_0_split[2].strip()
    assert version_p1 == '11'
    assert version_p2 == '64'
