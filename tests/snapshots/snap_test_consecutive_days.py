# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestConsecutiveDays::test_days few_days'] = '''START,END,LENGTH
2023-03-23,2023-03-24,2
'''

snapshots['TestConsecutiveDays::test_days few_invalid'] = '''START,END,LENGTH
2023-03-23,2023-03-24,2
'''

snapshots['TestConsecutiveDays::test_days sort_days'] = '''START,END,LENGTH
2023-03-23,2023-03-24,2
2023-03-20,2023-03-20,1
'''

snapshots['TestConsecutiveDays::test_days two_days'] = '''START,END,LENGTH
2023-03-23,2023-03-24,2
'''
