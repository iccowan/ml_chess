import os

def test_python3_version():
    stream = os.popen('python3 --version')
    version = stream.read().split(' ')[1].strip()
    assert version == tool_version('python')

def test_pip_version():
    stream = os.popen('pip --version')
    version = stream.read().split(' ')[1].strip()
    assert version == tool_version('pip')

def test_stockfish_version():
    stream = os.popen('stockfish compiler')
    stream_split = stream.read().split('\n')
    stream_split_0_split = stream_split[0].split(' ')
    version_p1 = stream_split_0_split[1].strip()
    version_p2 = stream_split_0_split[2].strip()
    assert version_p1 == '11'
    assert version_p2 == '64'

def tool_version(app):
    cwd = os.getcwd()
    tool_versions = open(cwd + '/../../.tool-versions', 'r')

    for line in tool_versions:
        line_split = line.split(' ')
        if line_split[0] == app:
            return line_split[1].strip()

    return ''
