from ..database import Database as db

MONTH = {
    "JAN": 1,
    "FEB": 2,
    "MAR": 3,
    "APR": 4,
    "MAY": 5,
    "JUN": 6,
    "JUL": 7,
    "AUG": 8,
    "SEP": 9,
    "OCT": 10,
    "NOV": 11,
    "DEC": 12,
}


class Extractor:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.date_month = []
        self.field_name = []
        self.value = []

    def start(self):
        lines = [str(i).split(',') for i in self.raw_data.splitlines()]

        self.date_month = self.get_date_month(lines[0][1:])
        lines = lines[1:]

        self.field_name = [i[0].strip() for i in lines]
        lines = [i[1:] for i in lines]

        lines = self.catch_to_int(lines)
        self.value = lines
        return self.make_object()
        # db.data.insert_one(self.make_object())

    @classmethod
    def get_date_month(cls, date_month):
        new_date_month = [i.strip().split(' ') for i in date_month]
        new_date_month = [[MONTH[i[0]], int(i[1])] for i in new_date_month]
        return new_date_month

    @classmethod
    def catch_to_int(cls, arr):
        new_arr = [[float(j) for j in i if cls._isfloat(j)] for i in arr]
        return new_arr

    @classmethod
    def _isfloat(cls, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def make_object(self):
        obj = {
            "title": "Exchange Rate",
            "graph": "line",
            "fields": self.field_name,
            "data": self.make_field_obj()
        }
        return obj

    def make_field_obj(self):
        l = []
        for i, name in enumerate(self.field_name):
            month_data = []
            for j, m in enumerate(self.date_month):
                month_obj = {
                    "month": m[0],
                    "year": m[1],
                    "value": self.value[i][j]
                }
                month_data.append(month_obj)
            obj = {
                "field_name": name,
                "monthly": month_data,
            }
            l.append(obj)
        return l
