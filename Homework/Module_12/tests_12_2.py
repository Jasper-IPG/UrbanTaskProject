# "методы TestCase"
import unittest
import runner_and_tournament as r_a_t


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.first = r_a_t.Runner('Усэйн', 10)
        self.second = r_a_t.Runner('Андрей', 9)
        self.third = r_a_t.Runner('Ник', 3)

    def test_tournament_1(self):
        t = r_a_t.Tournament(90, self.first, self.third)
        TournamentTest.all_results.update({1: t.start()})
        self.assertTrue(TournamentTest.all_results[1][max(TournamentTest.all_results[1])] == 'Ник')

    def test_tournament_2(self):
        t = r_a_t.Tournament(90, self.second, self.third)
        TournamentTest.all_results.update({2: t.start()})
        self.assertTrue(TournamentTest.all_results[2][max(TournamentTest.all_results[2])] == 'Ник')

    def test_tournament_3(self):
        t = r_a_t.Tournament(90, self.first, self.second, self.third)
        TournamentTest.all_results.update({3: t.start()})
        self.assertTrue(TournamentTest.all_results[3][max(TournamentTest.all_results[3])] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for value in cls.all_results.values():
            print(value.__repr__())
