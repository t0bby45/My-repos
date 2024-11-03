import random

class Student:
    def __init__(self, name):
        self.name = name
        self.money = 100  
        self.studying = True
        self.grades = 5  
        self.work_hours = 0

    def study(self):
        if self.studying:
            self.grades += 1
            self.grades = min(self.grades, 10) 
            print(f"{self.name} учится. Оценка: {self.grades}")
        else:
            print(f"{self.name} не учится.")

    def work(self):
        earned_money = random.randint(10, 30)
        self.money += earned_money
        self.work_hours += 1
        print(f"{self.name} работает и зарабатывает {earned_money} денег. Всего денег: {self.money}")

    def rest(self):
        spent_money = random.randint(5, 15)
        self.money -= spent_money
        self.money = max(self.money, 0)
        print(f"{self.name} отдыхает и тратит {spent_money} денег. Осталось: {self.money}")

    def live_year(self):
        for month in range(12):
            print(f"\nМесяц {month + 1}:")
            if self.money < 20:
                self.work()  
            elif self.grades < 4:
                self.studying = True
                self.study()
            elif random.choice([True, False]):
                self.rest()
            else:
                self.study()

# Пример использования
student = Student("Torehan")
student.live_year()
