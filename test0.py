import calendar
import datetime


class Separation:
    def __init__(self):
        self.tp = input()
        dt1, dt2 = input().split()
        dt1, dt2 = dt1.split('-'), dt2.split('-')
        self.dt1 = datetime.date(int(dt1[0]), int(dt1[1]), int(dt1[2]))
        self.dt2 = datetime.date(int(dt2[0]), int(dt2[1]), int(dt2[2]))
        self.dates = []
        if self.tp == 'WEEK':
            self.on_week()
        elif self.tp == 'MONTH':
            self.on_month()
        elif self.tp == 'QUARTER':
            self.on_quarter()
        elif self.tp == 'YEAR':
            self.on_year()
        elif self.tp == 'REVIEW':
            self.on_review()
        print(len(self.dates))
        for date in self.dates:
            print(date[0], date[1])

    def on_week(self):
        if self.dt1.weekday() != 0:
            self.dates.append(
                [self.dt1.isoformat(), (self.dt1 + datetime.timedelta(days=6 - self.dt1.weekday())).isoformat()])
            self.dt1 = self.dt1 + datetime.timedelta(days=7 - self.dt1.weekday())
        if self.dt2 - self.dt1 < datetime.timedelta(weeks=1):
            self.dates.append([self.dt1.isoformat(), self.dt2.isoformat()])
        else:
            self.dates.append([self.dt1.isoformat(), (self.dt1 + datetime.timedelta(days=6)).isoformat()])
            self.dt1 = self.dt1 + datetime.timedelta(days=7)
            self.on_week()

    def on_month(self):
        days_in_month = calendar.monthrange(self.dt1.year, self.dt1.month)[1]
        if (self.dt2 - self.dt1).days < days_in_month:
            self.dates.append([self.dt1.isoformat(), self.dt2.isoformat()])
        else:
            if self.dt1.day != 1:
                self.dates.append([self.dt1.isoformat(),
                                   (self.dt1 + datetime.timedelta(days=days_in_month - self.dt1.day)).isoformat()])
                self.dt1 = self.dt1 + datetime.timedelta(days=days_in_month - self.dt1.day + 1)
            else:
                self.dates.append(
                    [self.dt1.isoformat(), (self.dt1 + datetime.timedelta(days=days_in_month)).isoformat()])
                self.dt1 = self.dt1 + datetime.timedelta(days=days_in_month)
            self.on_month()

    def on_quarter(self):
        if self.dt1.month < 4:
            delta_in_days = datetime.date(self.dt1.year, 4, 1) - self.dt1
        elif 3 < self.dt1.month < 7:
            delta_in_days = datetime.date(self.dt1.year, 7, 1) - self.dt1
        elif 6 < self.dt1.month < 10:
            delta_in_days = datetime.date(self.dt1.year, 10, 1) - self.dt1
        else:
            delta_in_days = datetime.date(self.dt1.year + 1, 1, 1) - self.dt1

        if self.dt2 - self.dt1 < delta_in_days:
            self.dates.append([self.dt1.isoformat(), self.dt2.isoformat()])
        else:
            self.dates.append(
                [self.dt1.isoformat(), (self.dt1 + delta_in_days - datetime.timedelta(days=1)).isoformat()])
            self.dt1 = self.dt1 + delta_in_days
            self.on_quarter()

    def on_year(self):
        next_year = datetime.date(self.dt1.year + 1, 1, 1)
        delta_of_days = next_year - self.dt1
        if self.dt2 - self.dt1 < delta_of_days:
            self.dates.append([self.dt1.isoformat(), self.dt2.isoformat()])
        else:
            self.dates.append([self.dt1.isoformat(), (self.dt1 + delta_of_days).isoformat()])
            self.dt1 = self.dt1 + delta_of_days
            self.on_year()

    def on_review(self):
        if self.dt1.month < 4:
            delta_in_days = datetime.date(self.dt1.year, 4, 1) - self.dt1
        elif self.dt1.month > 9:
            delta_in_days = datetime.date(self.dt1.year + 1, 4, 1) - self.dt1
        else:
            delta_in_days = datetime.date(self.dt1.year, 10, 1) - self.dt1
        if self.dt2 - self.dt1 < delta_in_days:
            self.dates.append([self.dt1.isoformat(), self.dt2.isoformat()])
        else:
            self.dates.append(
                [self.dt1.isoformat(), (self.dt1 + delta_in_days - datetime.timedelta(days=1)).isoformat()])
            self.dt1 = self.dt1 + delta_in_days
            self.on_review()


Separation()
