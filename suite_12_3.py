# Домашнее задание по теме "Систематизация и пропуск тестов".
# Цель: понять на практике как объединять тесты при помощи TestSuite. Научиться пропускать тесты при
# помощи встроенных в unittest декораторов.

import unittest
import tests_12_3

runnerST = unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerST)