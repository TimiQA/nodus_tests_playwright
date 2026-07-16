from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_login(locale, page):
    login_page = LoginPage(locale, page)
    
    login_page.open()
    login_page.fill_login_form("test1784045800", "N0du$Pa$$123")
    login_page.click_login()
    
    # Ждем, пока URL поменяется на домашнюю страницу после успешного входа
    expect(page).to_have_url("https://web.nodlab.ru/#/home", timeout=40000)