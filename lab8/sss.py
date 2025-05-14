from guizero import App, Box, Text, Combo, PushButton
import calendar
from datetime import datetime

class InvalidDateError(Exception):
    pass

class InteractiveCalendar:
    def __init__(self, app):
        self.app = app
        self.app.title = "Интерактивный Календарь"
        self.app.width = 500
        self.app.height = 350

        self.init_ui()

    def init_ui(self):
        self.header = Text(self.app, text="Выберите дату", size=16)

        controls_box = Box(self.app, layout="grid", align="top")

        # Выбор месяца
        self.month = Combo(controls_box, options=list(calendar.month_name)[1:], grid=[0, 0])
        self.month.value = calendar.month_name[datetime.now().month]
        # Выбор года
        self.year = Combo(controls_box, options=[str(y) for y in range(1990, 2051)], grid=[1, 0])
        self.year.value = str(datetime.now().year)

        # Выбор дня
        self.day = Combo(controls_box, options=[str(d) for d in range(1, 32)], grid=[2, 0])
        self.day.value = str(datetime.now().day)

        PushButton(controls_box, text="Определить день недели", command=self.show_day_of_week, grid=[3, 0])
        self.result = Text(self.app, text="", size=12, color="navy")

    def show_day_of_week(self):
        try:
            year = int(self.year.value)
            month = list(calendar.month_name).index(self.month.value)
            day = int(self.day.value)

            # Проверка на корректную дату
            if day > calendar.monthrange(year, month)[1]:
                raise InvalidDateError("Такого дня нет в выбранном месяце!")

            date = datetime(year, month, day)
            weekday = calendar.day_name[date.weekday()]
            self.result.value = f"{day} {self.month.value} {year} — это {weekday}"
        except InvalidDateError as e:
            self.result.value = f"Ошибка: {str(e)}"
        except Exception:
            self.result.value = "Произошла ошибка при определении дня недели."

# Запуск
if __name__ == "__main__":
    app = App()
    cal = InteractiveCalendar(app)
    app.display()
