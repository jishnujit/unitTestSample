from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Harry Potter", "J K Rawling")

        self.assertEqual("Harry Potter", b.title)
        self.assertEqual("J K Rawling", b.author)
        self.assertEqual([], b.posts)