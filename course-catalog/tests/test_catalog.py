import unittest

from catalog import check_plan, load_courses, search, total_credits


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.courses = load_courses()

    def test_load_courses(self):
        self.assertIn("BIO-101", self.courses)
        self.assertEqual(self.courses["BIO-201"].prereqs, ["BIO-101"])

    def test_search_by_code(self):
        codes = [c.code for c in search(self.courses, "CHEM")]
        self.assertEqual(codes, ["CHEM-101", "CHEM-210"])

    def test_search_by_title(self):
        codes = [c.code for c in search(self.courses, "Genetics")]
        self.assertEqual(codes, ["BIO-310"])

    def test_plan_in_order_is_valid(self):
        plan = [["BIO-101", "CHEM-101"], ["BIO-201"], ["BIO-310"]]
        self.assertEqual(check_plan(self.courses, plan), [])

    def test_plan_missing_prereq(self):
        plan = [["BIO-201"]]
        self.assertEqual(check_plan(self.courses, plan), ["Term 1: BIO-201 needs BIO-101 first"])

    def test_plan_unknown_course(self):
        self.assertEqual(check_plan(self.courses, [["ART-999"]]), ["Term 1: unknown course ART-999"])

    def test_total_credits(self):
        self.assertEqual(total_credits(self.courses, ["BIO-101", "CS-101"]), 7)


if __name__ == "__main__":
    unittest.main()
