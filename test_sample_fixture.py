import pytest
import random


@pytest.fixture
def rnd():
    return random.random()


def test_rnd(rnd):
    print(rnd)


@pytest.fixture
def rnd_gen():
    return random.Random(123456)


@pytest.fixture
def rnd(rnd_gen):
    return rnd_gen.random()


@pytest.fixture
def fixture_a(rnd):
    return rnd


@pytest.fixture
def fixture_b(rnd):
    return rnd


def test_a(fixture_a, fixture_b):
    print((fixture_a, fixture_b))
    assert fixture_a == fixture_b


@pytest.fixture
def make_rnd(rnd_gen):
    def maker():
        return rnd_gen.random()
    return maker


def test_b(make_rnd):
    assert make_rnd() != make_rnd()