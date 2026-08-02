import pytest
import os
from dotenv import load_dotenv

# Загружаем переменные окружения при старте тестов
load_dotenv()

@pytest.fixture(params=["ru-RU", "en-US"])
def locale(request):
    return request.param

@pytest.fixture
def browser_context_args(locale, browser_context_args):
    return {
        **browser_context_args,
        "locale": locale,
    }