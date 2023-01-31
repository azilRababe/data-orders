from nbresult import ChallengeResultTestCase

class TestWaitTime(ChallengeResultTestCase):

    def test_wait_time(self):
        self.assertEqual(self.result.shape, (96478, 5))
        self.assertGreaterEqual(self.result.dve_min, 0)
        self.assertGreater(self.result.dve_max, 0)
        self.assertEqual(self.result.dve_type, float)
