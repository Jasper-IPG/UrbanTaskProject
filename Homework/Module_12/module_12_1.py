# "Проверка на выносливость"
from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(TestCase):
    def test_walk(self):
        first = Runner('Alex')
        for _ in range(10):
            first.walk()
        self.assertEqual(first.distance, 50)

    def test_run(self):
        second = Runner('Pavel')
        for _ in range(10):
            second.run()
        self.assertEqual(second.distance, 100)

    def test_challenge(self):
        third = Runner('Tim')
        fourth = Runner('Mark')
        for _ in range(10):
            third.walk()
            fourth.run()
        self.assertNotEqual(third.distance, fourth.distance)
