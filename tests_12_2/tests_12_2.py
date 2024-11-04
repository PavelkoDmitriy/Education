import unittest
from runner_and_tournament import Tournament, Runner  # Импортируем необходимые классы

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        # Создаем бегунов с заданными именами и скоростями
        self.runner_1 = Runner(name="Усэйн", speed=10)
        self.runner_2 = Runner(name="Андрей", speed=9)
        self.runner_3 = Runner(name="Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        # Выводим результаты всех тестов
        for key in sorted(cls.all_results.keys()):
            print(f"{key}: {cls.all_results[key]}")

    def test_race_usain_and_nick(self):
        tournament = Tournament(distance=90)
        results = tournament.start(self.runner_1, self.runner_3)
        self.all_results[max(results.keys())] = results[max(results.keys())]
        self.assertEqual(results[max(results.keys())], "Ник")

    def test_race_andrey_and_nick(self):
        tournament = Tournament(distance=90)
        results = tournament.start([self.runner_2, self.runner_3])
        self.all_results[max(results.keys())] = results[max(results.keys())]
        self.assertEqual(results[max(results.keys())], "Ник")

    def test_race_usain_andrey_and_nick(self):
        tournament = Tournament(distance=90)
        results = tournament.start([self.runner_1, self.runner_2, self.runner_3])
        self.all_results[max(results.keys())] = results[max(results.keys())]
        self.assertEqual(results[max(results.keys())], "Ник")

if __name__ == "__main__":
    unittest.main()