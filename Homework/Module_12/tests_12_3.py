# "Заморозка кейсов"
import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        first = Runner('Alex')
        for _ in range(10):
            first.walk()
        self.assertEqual(first.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        second = Runner('Pavel')
        for _ in range(10):
            second.run()
        self.assertEqual(second.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        third = Runner('Tim')
        fourth = Runner('Mark')
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
        self.first = Runner('Усэйн', 10)
        self.second = Runner('Андрей', 9)
        self.third = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        t = Tournament(90, self.first, self.third)
        TournamentTest.all_results.update({1: t.start()})
        self.assertTrue(TournamentTest.all_results[1][max(TournamentTest.all_results[1])] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        t = Tournament(90, self.second, self.third)
        TournamentTest.all_results.update({2: t.start()})
        self.assertTrue(TournamentTest.all_results[2][max(TournamentTest.all_results[2])] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        t = Tournament(90, self.first, self.second, self.third)
        TournamentTest.all_results.update({3: t.start()})
        self.assertTrue(TournamentTest.all_results[3][max(TournamentTest.all_results[3])] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for value in cls.all_results.values():
            print(value.__repr__())
