import unittest
from similarity import compute_text_similarity, compute_tag_similarity, compute_dom_structure_similarity, compute_combined_similarity
from parser import parse_html_file

class TestSimilarityFunctions(unittest.TestCase):

    def setUp(self):
        # Încărcăm două fișiere HTML de test
        self.doc1 = parse_html_file('test1.html')
        self.doc2 = parse_html_file('test2.html')

    def test_text_similarity(self):
        similarity = compute_text_similarity([self.doc1, self.doc2])
        self.assertGreater(similarity[0][1], 0.5, "Text similarity should be greater than 0.5")

    def test_tag_similarity(self):
        tag_sim = compute_tag_similarity(self.doc1, self.doc2)
        self.assertGreater(tag_sim, 0.5, "Tag similarity should be greater than 0.5")

    def test_dom_structure_similarity(self):
        dom_sim = compute_dom_structure_similarity(self.doc1, self.doc2)
        self.assertGreater(dom_sim, 0.5, "DOM structure similarity should be greater than 0.5")

    def test_combined_similarity(self):
        combined_sim = compute_combined_similarity([self.doc1, self.doc2])
        self.assertGreater(combined_sim[0][1], 0.5, "Combined similarity should be greater than 0.5")

if __name__ == '__main__':
    unittest.main()
