from playwright.sync_api import Page

TRANSLATIONS = {
    "ru-RU": {
        "username": "Имя пользователя",
        "password": "Пароль",
        "login_btn": "Войти",
        "skip_verification": "Пока пропустить проверку", 
        "verify_later": "Я заверю позже"
    },
    "en-US": {
        "username": "Username",
        "password": "Password",
        "login_btn": "Sign in",
        "skip_verification": "Skip verification for now", 
        "verify_later": "I'll verify later"  
    }
}

class LoginPage:
    def __init__(self, locale, page: Page):
        self.page = page
        self.locale = locale
        t = TRANSLATIONS[self.locale]

        self.username_input = page.get_by_role("textbox", name=t["username"])
        self.password_input = page.get_by_placeholder(t["password"], exact=True)
        self.login_button = page.get_by_role("button", name=t["login_btn"])
        # Локаторы модалок безопасности
        self.skip_verification_button = page.get_by_role("button", name=t["skip_verification"])
        self.verify_later_button = page.get_by_role("button", name=t["verify_later"])
    def open(self):
        self.page.goto("https://web.nodlab.ru/#/login", timeout=60000, wait_until="domcontentloaded")

    def fill_login_form(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()
    def skip_security_onboarding(self):
        # Клик по крестику
        self.skip_verification_button.click()
        # Клик по подтверждению "Я заверю позже"
        self.verify_later_button.click()