from playwright.sync_api import Page

TRANSLATIONS = {
    "ru-RU": {
        "username": "Имя пользователя",
        "password": "Пароль",
        "login_btn": "Войти" 
    },
    "en-US": {
        "username": "Username",
        "password": "Password",
        "login_btn": "Login" 
    }
}

class LoginPage:
    def __init__(self, locale, page: Page):
        self.page = page
        self.locale = locale
        t = TRANSLATIONS[self.locale]

        self.username_input = page.get_by_placeholder(t["username"])
        self.password_input = page.get_by_placeholder(t["password"], exact=True)
        self.login_button = page.get_by_text(t["login_btn"])

    def open(self):
        self.page.goto("https://web.nodlab.ru/#/login")

    def fill_login_form(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()