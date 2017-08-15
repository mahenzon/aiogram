import unittest

from aiogram import types

data = {
    "last_name": "Test Lastname",
    "id": 1111111,
    "type": "private",
    "first_name": "Test Firstname",
    "username": "Testusername"
}

obj = types.Chat.de_json(data)


class TestChat(unittest.TestCase):
    def test_instance(self):
        self.assertIsInstance(obj, types.Chat)

    def test_id(self):
        self.assertEqual(obj.id, data['id'])

    def test_first_name(self):
        self.assertEqual(obj.first_name, data['first_name'])

    def test_last_name(self):
        self.assertEqual(obj.last_name, data['last_name'])

    def test_username(self):
        self.assertEqual(obj.username, data['username'])

    def test_full_name(self):
        full_name = f"{data['first_name']} {data['last_name']}"
        self.assertEqual(obj.full_name, full_name)

    def test_mention(self):
        self.assertEqual(f"@{data['username']}", obj.mention)

    def test_type(self):
        self.assertEqual(obj.type, data['type'])

    def test_others(self):
        self.assertIsNone(obj.title)
        self.assertEqual(obj.all_members_are_administrators, False)
        self.assertIsNone(obj.photo)
        self.assertIsNone(obj.description)
        self.assertIsNone(obj.invite_link)
