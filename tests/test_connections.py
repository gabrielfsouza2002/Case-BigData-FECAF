import unittest
from app.utils.database import DatabaseConnector

class TestDatabaseConnections(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseConnector()
    
    def test_mongodb_connection(self):
        mongo = self.db.connect_mongodb()
        self.assertIsNotNone(mongo)
    
    def test_redis_connection(self):
        redis = self.db.connect_redis()
        self.assertIsNotNone(redis)

if __name__ == '__main__':
    unittest.main()