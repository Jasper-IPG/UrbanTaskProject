# "Проверка на выносливость"
import unittest
import runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        first = runner.Runner('Alex')
        for _ in range(10):
            first.walk()
        self.assertEqual(first.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        second = runner.Runner('Pavel')
        for _ in range(10):
            second.run()
        self.assertEqual(second.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        third = runner.Runner('Tim')
        fourth = runner.Runner('Mark')
        for _ in range(10):
            third.walk()
            fourth.run()
        self.assertNotEqual(third.distance, fourth.distance)
