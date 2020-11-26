import unittest
from src.task_decider import get_preferred_option
from src.task import Task


class TestTaskDecider(unittest.TestCase):

    def setUp(self):
        self.clean_dishes = Task("Clean Dishes", 45)
        self.cook_dinner = Task("Cook Dinner", 60)
        self.clean_windows = Task("Clean Windows", 30)

    def test_get_preferred_option__prefers_dishes_over_dinner(self):
        self.assertEqual("Clean Dishes", get_preferred_option(self.clean_dishes,self.cook_dinner))