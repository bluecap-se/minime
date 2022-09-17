from django.test import TestCase

from .. import utils


class UtilTestCase(TestCase):

    def test_fail_create_stats(self):
        self.assertIsNone(utils.create_stats(None, 'abc'))
