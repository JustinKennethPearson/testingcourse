import bibtex
import unittest

class TestBibtexExtract(unittest.TestCase):
    def setUp(self):
        self.bibtex_entry_1 = "@Book{key1,\n\
        author={Smith, John},\n\
        title={A very silly book},\n\
        publisher = {Silly Publisher},\n\
        year={1987}\n\
        }"
        self.bibtex_entry_2 = "@Article{key2,\n\
        author={Smith, John},\n\
        title = {Another very silly article},\n\
        publisher = {Silly Publisher},\n\
        year={1988}\n\
        }"
    def test_entry_type(self):
        entry_1 = bibtex.entry_type(self.bibtex_entry_1)
        self.assertEqual(entry_1,'Book')
        entry_2 = bibtex.entry_type(self.bibtex_entry_2)
        self.assertEqual(entry_2,'Article')
    def test_get_key(self):
        key_1 = bibtex.get_key(self.bibtex_entry_1)
        self.assertEqual(key_1,'key1')
        key_2 = bibtex.get_key(self.bibtex_entry_2)
        self.assertEqual(key_2,'key2')

    def test_get_entries(self):
        list_1 = bibtex.get_entries(self.bibtex_entry_1)
        list_1_correct = [('author','Smith, John'),
                          ('title','A very silly book'),
                          ('publisher','Silly Publisher'),
                          ('year','1987')]
        self.assertEqual(list_1,list_1_correct)
        list_2 = bibtex.get_entries(self.bibtex_entry_2)
        list_2_correct = [('author','Smith, John'),
                          ('title','Another very silly article'),
                          ('publisher','Silly Publisher'),
                          ('year','1988')]
        self.assertEqual(list_2,list_2_correct)

    def test_find_stuff(self):
        entry_1 = '{ stuff1 } the rest of the stuff'
        (stuff1,rest_entry) = bibtex.find_stuff(entry_1)
        self.assertEqual(stuff1,'stuff1')
        self.assertEqual(rest_entry,' the rest of the stuff')
        entry_2 = '{ stuff{more stuff}} the rest of the stuff'
        (stuff2,rest_of_entry_2) = bibtex.find_stuff(entry_2)
        self.assertEqual(stuff2,'stuff{more stuff}')
        self.assertEqual(rest_of_entry_2,' the rest of the stuff')


if __name__ == '__main__':
    unittest.main()

