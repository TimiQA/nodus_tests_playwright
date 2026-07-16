from playwright.sync_api import Page, expect

TRANSLATIONS = {
    "ru-RU": {
        "settings_menu": "Настройки",
        "display_name": "Отображаемое имя",
        "save": "Сохранить"
    },
    "en-US": {
        "settings_menu": "Settings",
        "display_name": "Display Name",
        "save": "Save"
    }
}

class ProfilePage:
    def __init__(self, locale, page: Page):
        self.page = page
        self.locale = locale
        t = TRANSLATIONS[self.locale]

        self.user_menu = page.locator(".user-menu-avatar") # Замени локатор на свой, если нужно
        self.settings_button = page.get_by_text(t["settings_menu"])
        self.display_name_input = page.get_by_placeholder(t["display_name"])
        self.save_button = page.get_by_text(t["save"])

    def open_settings(self):
        self.user_menu.click()
        self.settings_button.click()

    def change_display_name(self, new_name):
        self.display_name_input.fill(new_name)
        self.save_button.click()