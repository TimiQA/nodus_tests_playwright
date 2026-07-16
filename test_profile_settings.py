from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage

def test_change_display_name(locale, page):
    login_page = LoginPage(locale, page)
    profile_page = ProfilePage(locale, page)
    
    # 1. Сначала логинимся
    login_page.open()
    login_page.fill_login_form("test1784045800", "N0du$Pa$$123")
    login_page.click_login()
    expect(page).to_have_url("https://web.nodlab.ru/#/home", timeout=40000)
    
    # 2. Идем в настройки и меняем имя
    profile_page.open_settings()
    profile_page.change_display_name("Nodus Auto Tester")
    
    # Проверка, что имя обновилось на странице
    expect(page.get_by_text("Nodus Auto Tester").first).to_be_visible()