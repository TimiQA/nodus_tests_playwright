from playwright.sync_api import Page, expect

TRANSLATIONS = {
    "ru-RU": {
        "user_menu": "Меню пользователя",
        "all_settings": "Все настройки",
        "display_name": "Отображаемое имя",
        "save": "Сохранить",
        "close_dialog": "Закрыть диалог"
    },
    "en-US": {
        "user_menu": "User menu",
        "all_settings": "All settings",
        "display_name": "Display Name",
        "save": "Save",
        "close_dialog": "Close dialog"
    }
}

class ProfilePage:
    def __init__(self, locale, page: Page):
        self.page = page
        self.locale = locale
        t = TRANSLATIONS[self.locale]

        self.user_menu_button = page.get_by_role("button", name=t["user_menu"])
        self.settings_button = page.get_by_text(t["all_settings"])
        self.display_name_input = page.get_by_role("textbox", name=t["display_name"])
        self.save_button = page.get_by_role("button", name=t["save"])
        self.close_button = page.get_by_role("button", name=t["close_dialog"])

    def open_settings(self):
        self.user_menu_button.click()
        self.settings_button.click()

    def change_display_name(self, new_name):
        self.display_name_input.click()
        self.display_name_input.fill(new_name)
        self.save_button.click()
        self.close_button.click()

    def verify_display_name_in_menu(self, expected_name):
        self.user_menu_button.click()
        expect(self.page.get_by_text(expected_name, exact=True)).to_be_visible()