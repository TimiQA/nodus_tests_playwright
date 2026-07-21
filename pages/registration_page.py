from playwright.sync_api import Page, expect 
import time # если time больше не нужен в этом файле, его лучше убрать для чистоты

TRANSLATIONS = {
    "ru-RU": {
        "sign_up": "Создать учётную запись",
        "home_label": "Главная",
        "username": "Имя пользователя",
        "password": "Пароль",
        "confirm_password": "Подтвердите пароль",
        "submit": "Зарегистрироваться",
        "reg_token": "Регистрационный токен",
        "next": "Продолжить"
    },
    "en-US": {
        "sign_up": "Create Account",
        "home_label": "Home",
        "username": "Username",
        "password": "Password",
        "confirm_password": "Confirm password",
        "submit": "Register", 
        "reg_token": "Registration token",
        "next": "Continue"
    }
}

class RegistrationPage:
    def __init__(self, locale, page: Page):
        self.page = page
        self.locale = locale
        
        t = TRANSLATIONS[self.locale]

        
        self.username_input = page.get_by_placeholder(t["username"])
        self.password_input = page.get_by_placeholder(t["password"], exact=True)
        self.confirm_password_input = page.get_by_placeholder(t["confirm_password"], exact=True)
        self.sing_up = page.get_by_role("link", name=t["sign_up"])
        self.submit_button = page.get_by_text(t["submit"])
        self.reg_token = page.get_by_placeholder(t["reg_token"])
        self.next_button = page.get_by_text(t["next"])
        self.home_label = page.get_by_text(t["home_label"])

    # Дальше идут методы open, click_sign_up_button и т.д.
    def open(self):
         self.page.goto("https://web.nodlab.ru/", timeout=60000, wait_until="domcontentloaded")
    def click_sign_up_button(self):
         self.sing_up.click() 
    def fill_form(self):
         self.username_input.fill("test"+str(int(time.time())))
         self.password_input.fill("N0du$Pa$$123")
         self.confirm_password_input.fill("N0du$Pa$$123")
    def click_submit_button(self):
         self.submit_button.click()
    def check_server_name(self):
         expect(self.page.get_by_text("nodlab.ru")).to_be_visible()   
    def fill_token(self):
         self.reg_token.fill("priv1sun")
    def click_next_button(self):
         self.next_button.click(timeout=30000)