import pytest
# resource cleanup

@pytest.fixture
def opened_file():
    f = open("filename.txt")
    try:
        yield f
    finally:
        f.close()


def test_a(opened_file):
    assert opened_file.read() == "file content"


# resource cleanup for factories

# @pytest.yield_ fixture
@pytest.fixture
def open_file():
    f = None
    def opener(filename):
        nonlocal f
        f = open(filename)
        return f
    yield opener
    if f is not None:
        f.close()


def test_b(open_file):
    assert open_file("file_A.txt").read() == "Content A"
    assert open_file("file_B.txt").read() == "Content B"