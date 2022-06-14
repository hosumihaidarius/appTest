import pytest

from utils.data import Urls


@pytest.fixture
def setup(page):
    page.goto(Urls.BASE_URL.value)
    yield page
