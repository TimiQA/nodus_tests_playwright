import pytest

@pytest.fixture(params=["ru-RU", "en-US"])
def locale(request):
    return request.param

@pytest.fixture
def browser_context_args(locale, browser_context_args):
    return {
        **browser_context_args,
        "locale": locale,
    }