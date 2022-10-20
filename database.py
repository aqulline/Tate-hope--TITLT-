import datetime
import json


class DataBase:
    mnth_name = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                 "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    day = ["Mon", "Tue", "Wed", "Thu",
           "Fri", "Sat", "Sun"]
    week_no = 0
    day = 0

    def update_week(self, week_n):
        self.date_format()
        data = self.read_data("database/data.json")
        total = data["data"]["total"]
        week = data["data"]["this_week"]
        month = data["data"]["this_month"]
        p_date = data["data"]["prev_date"]
        p_day = data["data"]["previous_day"]
        star_one = data["data"]["star_one"]
        star_two = data["data"]["star_two"]
        star_three = data["data"]["star_three"]
        if p_date != int(self.day):
            total = str(int(total) + 1)
            week = week_n
            month = str(int(month) + 1)
            self.star_one_count(star_one)
            self.star_two_count(star_two)
            self.star_three_count(star_three)
            if self.day == "01" and p_date == 31 or self.day == "01" and p_date == 30:
                p_day = "yes"
            elif int(self.day) - p_date == 1:
                p_day = "yes"
            elif int(self.day) - p_date > 1 and total != "1":
                p_day = "no"
                self.day_missed()

            new_data = {"data": {
                "total": total,
                "this_week": week,
                "this_month": month,
                "previous_day": p_day,
                "prev_date": int(self.day),
                "star_one": self.star_one_count(star_one),
                "star_two": self.star_two_count(star_two),
                "star_three": self.star_three_count(star_three)
            }}
            data.update(new_data)
            self.write_data("database/data.json", data)
            return True
        else:
            return False

    def day_missed(self):
        self.date_format()
        data = self.read_data("database/data.json")
        total = data["data"]["total"]
        week = data["data"]["this_week"]
        month = data["data"]["this_month"]
        p_date = data["data"]["prev_date"]
        p_day = data["data"]["previous_day"]
        star_one = data["data"]["star_one"]
        star_two = data["data"]["star_two"]
        star_three = data["data"]["star_three"]
        total = str(int(total) - 1)
        week = str(int(week) - 1)
        month = str(int(month) - 1)
        star_one = str(int(star_one) - 1)
        star_two = str(int(star_two) - 1)
        star_three = str(int(star_three) - 1)
        new_data = {"data": {
            "total": total,
            "this_week": week,
            "this_month": month,
            "previous_day": "yes",
            "prev_date": int(self.day),
            "star_one": star_one,
            "star_two": star_two,
            "star_three": star_three
        }}
        data.update(new_data)
        self.write_data("database/data.json", data)

    def star_one_count(self, num):
        if num < 30:
            num = num + 1

            return num
        elif num >= 30:
            return num

    def star_two_count(self, num):
        if num < 60:
            num = num + 1

            return num

        elif num >= 60:

            return num

    def star_three_count(self, num):
        if num < 90:
            num = num + 1

            return num
        elif num >= 90:

            return num

    def query_data(self):
        data = self.read_data("database/data.json")
        total = data["data"]["total"]
        week = data["data"]["this_week"]
        month = data["data"]["this_month"]
        p_date = data["data"]["prev_date"]
        p_day = data["data"]["previous_day"]
        star_one = data["data"]["star_one"]
        star_two = data["data"]["star_two"]
        star_three = data["data"]["star_three"]
        # 0      1       2       3       4       5       6           7
        return [total, week, month, p_date, p_day, star_one, star_two, star_three]

    def check_status(self):
        data = self.read_data("database/data.json")
        self.date_format()
        date = data["data"]["prev_date"]
        if int(self.day) == date:
            return True
        else:
            return False

    def get_date(self):
        return str(datetime.datetime.now()).split(" ")[0]

    def week_number(self, date):
        if 1 <= date <= 7:
            return "w1"
        elif 8 <= date <= 14:
            return "w2"
        elif 15 <= date <= 21:
            return "w3"
        elif date >= 22:
            return "w4"

    def date_format(self):
        date = self.get_date()
        year, month, self.day = date.strip().split("-")
        if int(month) >= 10:
            month_update = int(month) - 1
        else:
            month_update = int(month.replace("0", "")) - 1
        month_name = self.mnth_name[month_update]
        self.week_no = self.week_number(int(self.day))
        date_frmt = f"{month_name} {str(self.day)}"
        return date_frmt

    def write_data(self, file_name, data):
        with open(file_name, "w") as file:
            data_dump = json.dumps(data, indent=6)
            file.write(data_dump)
            file.close()

    def read_data(self, file_name):
        with open(file_name, "r") as file:
            data = json.load(file)

            return data
