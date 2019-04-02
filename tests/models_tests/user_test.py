from tests import OhmTestCase


class UserTest(OhmTestCase):
    def test_get_multi(self):
        assert self.chuck.get_multi("PHONE") == ['+14086441234', '+14086445678']
        assert self.justin.get_multi("PHONE") == []
    
    def test_migrations(self):
        # This section should be deleted because it's not any bz logic!
        # But I added this to make it easy for you to check my delivery
        self.assertEqual(self.chuck.point_balance, 1000.0)
        self.assertEqual(self.elvis.location, 'USA')
        self.assertEqual(self.justin.tier, 'Silver')
