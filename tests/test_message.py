import datetime
import unittest

from aiogram import types

data = {
    "date": 1441645532,
    "chat": {
        "last_name": "Test Lastname",
        "id": 1111111,
        "type": "private",
        "first_name": "Test Firstname",
        "username": "Testusername"
    },
    "message_id": 1365,
    "from": {
        "last_name": "Test Lastname",
        "id": 2222222,
        "first_name": "Test Firstname",
        "username": "Testusername"
    },
    "text": "Hello, world!"
}

obj = types.Message.de_json(data)


class TestMessage(unittest.TestCase):
    def test_instance(self):
        self.assertIsInstance(obj, types.Message)

    def test_content_type(self):
        self.assertIn(obj.content_type, types.ContentType.TEXT)

    def test_date(self):
        self.assertEqual(datetime.datetime.fromtimestamp(data['date']), obj.date)

    def test_chat(self):
        self.assertIsNotNone(obj.chat)
        self.assertIsInstance(obj.chat, types.Chat)
        self.assertEqual(obj.chat.id, data['chat']['id'])

    def test_message_id(self):
        self.assertEqual(obj.message_id, data['message_id'])

    def test_text(self):
        self.assertEqual(obj.text, data['text'])

    def test_from_user(self):
        self.assertIsNotNone(obj.from_user)
        self.assertIsInstance(obj.from_user, types.User)
        self.assertEqual(obj.from_user.id, data['from']['id'])

    def test_other_fields(self):
        self.assertIsNone(obj.forward_from)
        self.assertIsNone(obj.forward_from_chat)
        self.assertIsNone(obj.forward_from_message_id)
        self.assertIsNone(obj.forward_date)
        self.assertIsNone(obj.reply_to_message)
        self.assertIsNone(obj.edit_date)
        self.assertIsNone(obj.entities)
        self.assertIsNone(obj.audio)
        self.assertIsNone(obj.document)
        self.assertIsNone(obj.game)
        self.assertIsNone(obj.photo)
        self.assertIsNone(obj.sticker)
        self.assertIsNone(obj.video)
        self.assertIsNone(obj.voice)
        self.assertIsNone(obj.video_note)
        self.assertIsNone(obj.new_chat_members)
        self.assertIsNone(obj.caption)
        self.assertIsNone(obj.contact)
        self.assertIsNone(obj.location)
        self.assertIsNone(obj.venue)
        self.assertIsNone(obj.left_chat_member)
        self.assertIsNone(obj.new_chat_title)
        self.assertIsNone(obj.new_chat_photo)
        self.assertIsNone(obj.delete_chat_photo)
        self.assertIsNone(obj.group_chat_created)
        self.assertIsNone(obj.supergroup_chat_created)
        self.assertIsNone(obj.channel_chat_created)
        self.assertIsNone(obj.migrate_to_chat_id)
        self.assertIsNone(obj.migrate_from_chat_id)
        self.assertIsNone(obj.pinned_message)
        self.assertIsNone(obj.invoice)
        self.assertIsNone(obj.successful_payment)
