# "Заморозка кейсов"
import unittest
import runner
import runner_and_tournament as r_a_t


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


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.first = r_a_t.Runner('Усэйн', 10)
        self.second = r_a_t.Runner('Андрей', 9)
        self.third = r_a_t.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        t = r_a_t.Tournament(90, self.first, self.third)
        TournamentTest.all_results.update({1: t.start()})
        self.assertTrue(TournamentTest.all_results[1][max(TournamentTest.all_results[1])] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        t = r_a_t.Tournament(90, self.second, self.third)
        TournamentTest.all_results.update({2: t.start()})
        self.assertTrue(TournamentTest.all_results[2][max(TournamentTest.all_results[2])] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        t = r_a_t.Tournament(90, self.first, self.second, self.third)
        TournamentTest.all_results.update({3: t.start()})
        self.assertTrue(TournamentTest.all_results[3][max(TournamentTest.all_results[3])] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for value in cls.all_results.values():
            print(value.__repr__())
