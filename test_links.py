import unittest
import links


class TestLinks(unittest.TestCase):
    def test_links_format(self):
        for link in links.gachi:
            self.assertTrue(link.startswith('https://'))
            self.assertTrue(len(link) > 0)


if __name__ == "__main__":
    unittest.main()
