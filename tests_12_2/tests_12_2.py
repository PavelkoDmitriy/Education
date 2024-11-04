import unittest
from runner_and_tournament import Tournament, Runner


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    def test1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        last_runner = max(results.keys())
        self.assertEqual(results[last_runner], 'Ник')
        self.__class__.all_results['test1'] = results

    def test2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        last_runner = max(results.keys())
        self.assertEqual(results[last_runner], 'Ник')
        self.__class__.all_results['test2'] = results

    def test3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        last_runner = max(results.keys())
        self.assertEqual(results[last_runner], 'Ник')
        self.__class__.all_results['test3'] = results

    @classmethod
    def tearDownClass(cls):
        # Выводим все результаты тестов
        for test_name, result in cls.all_results.items():
            printable_result = {place: runner.name for place, runner in result.items()}
            print(printable_result)


if __name__ == "__main__":
    unittest.main()
