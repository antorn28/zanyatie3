import random
class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_job(self):
        self.job = Job(job_list)
    def eat(self):
        pass
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4
    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        if manage == "fuel":
            print('I bought fuel')
            self.money -= 100
            self.car.fuel += 100
            self.satiety += 2
    def chill(self):
        pass
    def clean_home(self):
        pass
    def to_repair(self):
        pass
    def day_indexes(self, day):
        day + f"Today the {day} of {self.name}'s life"
        
    def is_alive(self):
        pass
    def live(self, day):
        pass


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.strength -= 1
            self.fuel -=self.consumption
            return True
        else:
            print("The car cannot move!")
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        pass




job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "C++ developer": {"salary": 70, "gladness_less": 20},
    "Python developer": {"salary": 40, "gladness_less": 50},
    "Rust developer": {"salary": 60, "gladness_less": 40},
}

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 8},
    "Lada": {"fuel": 80, "strength": 40, "consumption": 12},
    "Volvo": {"fuel": 60, "strength": 150, "consumption": 6},
    "Ford": {"fuel": 50, "strength": 120, "consumption": 9  },
}