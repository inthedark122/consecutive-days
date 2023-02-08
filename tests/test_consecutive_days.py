from snapshottest import TestCase
from app import ConsecutiveDays
from app.exceptions import EmptyException

SAMPLES = [
  ("few_days", ["2023-03-24 05:02:54", "2023-03-23 08:02:54"]),
  ("sort_days", ["2023-03-24 05:02:54", "2023-03-23 08:02:54", "2023-03-20 08:02:54"]),
  ("two_days", ["2023-03-24 05:02:54", "2023-03-23 08:02:54", "2023-03-24 08:02:54"]),
  ("few_invalid", ["2023-03-24 05:02:54", "xx", "2023-03-23 08:02:54", "yy", "2023-03-24 08:02:54"]),
]

class TestConsecutiveDays(TestCase):
  def test_days(self):
    for name, days in SAMPLES:
      with self.subTest(name=name):
        consecutive_days = ConsecutiveDays(days)
        self.assertMatchSnapshot(
          consecutive_days.process().to_csv(index=False),
          name=name,
        )

  def test_days_empty(self):
    with self.assertRaises(EmptyException):
      consecutive_days = ConsecutiveDays(["xx", "yy", "no-valid"])
