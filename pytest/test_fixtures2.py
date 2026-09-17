
# practice a browser-like fixture without a browser

import pytest

@pytest.fixture
def test_environment():
    print("Opening test environment")

    environment={
        "url" : "https;//example.com",
        "browser" : "chrome"
    }
    yield environment

    print("Closing test environment")

def test_url(test_environment):
    assert test_environment["url"].startswith("http")

def test_browser(test_environment):
    assert test_environment["browser"] == "chrome"