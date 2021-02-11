class Robot:
    """Представляет робота с именем."""
    population = 0

    def __init__(self, name):
        """Инициализация данных."""
        self.name = name
        print(f'Инициализация {self.name}')
        Robot.population += 1

    def __del__(self):
        """Я умираю."""
        print(f'{self.name} уничтожается!')
        Robot.population -= 1

        if Robot.population == 0:
            print(f'{self.name} был последним.')
        else:
            print(f'Осталось {Robot.population:d} работающих роботов')

    def sayHi(self):
        """Приветствие робота.

        Да, они это могут."""
        print(f'Приветствую! Мои хозяева называют меня {self.name}')

    def howMany():
        """Выводит численность роботов."""
        print(f'У нас есть {Robot.population:d} роботов.')

    howMany = staticmethod(howMany)


droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()
droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()
print("\nЗдесь роботы могут проделать какую-то работую\n")
print("Роботы закончили свою работу. Давайте уничтожим их.")
del droid1
del droid2
Robot.howMany()
