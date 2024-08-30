# Домашнее задание по теме "Систематизация и пропуск тестов".
# Цель: понять на практике как объединять тесты при помощи TestSuite. Научиться пропускать тесты при
# помощи встроенных в unittest декораторов.
import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]: # Используем срез, чтобы избежать изменения
                # списка во время итерации
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")  # Так как is_frozen = False то
    # тесты будут выполнены
    def test_walk(self):
        run_cls1 = Runner('test')
        for _ in range(10):
            run_cls1.walk()
        self.assertEqual(run_cls1.distance, 50)
        #self.assertEqual(run_cls1.distance, 150)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        run_cls2 = Runner('test')
        for _ in range(10):
            run_cls2.run()
        self.assertEqual(run_cls2.distance, 100)
        # self.assertEqual(run_cls2.distance, 500)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        run_cls_r = Runner('test')
        run_cls_w = Runner('test')
        for _ in range(10):
            run_cls_r.run()
            run_cls_w.walk()
        self.assertNotEqual(run_cls_r.distance, run_cls_w.distance)


class TournamentTest(TestCase):
    is_frozen = True
    all_results = {}  # для хранения результатов всех тестов создаем пустой словарь

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        # Создаем объекты Runner перед каждым тестом
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

        # Проверка создания объектов
        self.assertEqual(self.runner_1.name, "Усэйн")  # self.runner_1.name д.б.равно "Усэйн"
        self.assertEqual(self.runner_2.name, "Андрей")  # self.runner_1.name д.б.равно "Андрей"
        self.assertEqual(self.runner_3.name, "Ник")  # self.runner_1.name д.б.равно "Ник"

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")  # Так как is_frozen = True то тесты
    # будут пропущены
    def test_run_1(self):
        tour_1 = Tournament(90, self.runner_1, self.runner_3)
        result = tour_1.start()  # запускаем турнир
        self.all_results['test_run_1'] = result
        self.assertTrue(result[max(result)] == "Ник")  # запускаем тест и проверяем что Ник занял последнее место

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run_2(self):
        tour_2 = Tournament(90, self.runner_2, self.runner_3)
        result = tour_2.start()  # запускаем турнир
        self.all_results['test_run_2'] = result
        self.assertTrue(result[max(result)] == "Ник")  # запускаем тест и проверяем что Ник занял последнее место

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run_3(self):
        tour_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = tour_3.start()  # запускаем турнир
        self.all_results['test_run_3'] = result
        self.assertTrue(result[max(result)] == "Ник")  # запускаем тест и проверяем что Ник занял последнее место
