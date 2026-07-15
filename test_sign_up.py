import time
from playwright.sync_api import expect
from pages.registration_page import RegistrationPage
def test_github_title(locale,page):
    registration_page = RegistrationPage(locale,page)
    # 2. Открываем сайт
    registration_page.open()
    # 3. Наша старая проверка заголовка (оставляем как есть)
    assert "Element" in page.title()
    page.wait_for_timeout(3000) # подождать 3000 миллисекунд (3 секунды)
    # page.screenshot(path="before_click_error.png")
    registration_page.click_sign_up_button()
    registration_page.fill_form()
    registration_page.click_submit_button()
    registration_page.fill_token()
    registration_page.click_next_button()
    registration_page.password_input.fill("N0du$Pa$$123")
    registration_page.click_next_button()
    expect(page).to_have_url("https://web.nodlab.ru/#/home", timeout=40000)
    expect(registration_page.home_label).to_be_visible(timeout=10000)
