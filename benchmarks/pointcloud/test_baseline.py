"""Conformance tests for numerical and boundary contracts; no network required."""
from fractions import Fraction
import json
import unittest

import baseline as b


class Contracts(unittest.TestCase):
    def test_decimal_scale_boundary_rounding_is_explicit(self):
        # Correctly rounded fused decoding differs from separate multiply/add.
        exact = float(Fraction(500) * Fraction(0.01) + Fraction(-5))
        self.assertEqual(b.fused_decoder()(500, 0.01, -5), exact)
        self.assertNotEqual(exact, 500 * 0.01 - 5)
        self.assertGreater(exact, 0)

    def test_generated_fixture_matches_hand_calculation(self):
        path = b.ROOT / "data/boundaries.copc.laz"
        header = b.point_header(path)
        self.assertEqual(header["scale"], [0.125, 0.125, 0.125])
        self.assertEqual(header["offset"], [100, 200, -5])
        self.assertEqual(header["crs_authority"], ["EPSG", "32618"])
        cases = b.make_cases(header, fixture=True)
        actual = b.reference(path, cases)
        expected = json.loads((b.ROOT / "fixtures/expected.json").read_text())
        for name, result in actual.items():
            with self.subTest(case=name):
                item = expected[name]
                b.assert_result(result, {"count": item["count"],
                    "mean_z": item["sum_z"] / item["count"] if item["count"] else None})

    def test_comparison_rejects_wrong_count_nan_and_false_empty(self):
        for actual, expected in [
            ({"count": 1, "mean_z": 0}, {"count": 2, "mean_z": 0}),
            ({"count": 1, "mean_z": float("nan")}, {"count": 1, "mean_z": 0}),
            ({"count": 0, "mean_z": 0}, {"count": 0, "mean_z": None}),
        ]:
            with self.subTest(actual=actual), self.assertRaises(AssertionError):
                b.assert_result(actual, expected)

    def test_metadata_requires_real_statistics(self):
        with self.assertRaises(KeyError):
            b.parse_stats({"stages": {}})
        b.assert_result(b.parse_stats({"stages": {"filters.stats": {"statistic": [
            {"name": "Z", "count": 0, "average": 0}]}}}), {"count": 0, "mean_z": None})


if __name__ == "__main__":
    unittest.main()
