import os
import uuid
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage

def test_change_display_name(locale, page):
    login_page = LoginPage(locale, page)
    profile_page = ProfilePage(locale, page)
    
    # 1. Авторизация (Данные берутся из переменных окружения)
    login_page.open()
    login_page.fill_login_form(
        os.getenv("NODUS_LOGIN"), 
        os.getenv("NODUS_PASSWORD")
    )
    login_page.click_login()
    login_page.skip_security_onboarding()
    
    # Дефолтный таймаут expect в Playwright — 5 секунд. Этого достаточно.
    expect(page).to_have_url("https://web.nodlab.ru/#/home")
    
    # 2. Генерация уникального имени через короткий UUID (надежнее, чем time)
    unique_suffix = uuid.uuid4().hex[:6]
    new_name = f"User_{locale}_{unique_suffix}"
    
    # 3. Бизнес-логика теста
    profile_page.open_settings()
    profile_page.change_display_name(new_name)
    
    # 4. Проверка результата
    profile_page.verify_display_name_in_menu(new_name)