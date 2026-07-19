import time
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage

def test_change_display_name(locale, page):
    login_page = LoginPage(locale, page)
    profile_page = ProfilePage(locale, page)
    
    # Авторизация
    login_page.open()
    login_page.fill_login_form("test1784045800", "N0du$Pa$$123")
    login_page.click_login()
    login_page.skip_security_onboarding()
    expect(page).to_have_url("https://web.nodlab.ru/#/home", timeout=40000)
    
    # Генерация уникального имени
    new_name = f"User_{locale}_{int(time.time())}"
    
    # Смена имени
    profile_page.open_settings()
    profile_page.change_display_name(new_name)
    
    # Проверка
    profile_page.verify_display_name_in_menu(new_name)