# How to run

## Precondition

1. Install requirements: `pip install -r requiremenets.txt`

## Run SEED

1. Run python script `python main.py`

## Run tests

1. Run the python module `python -m unittest`

# Testing

I'm using `snapshottest` for the testing.

To add more test cases you need to extend `SAMPLES` in the `test_consecutive_days.py`

You can check snapshots in the `tests/snaphots/snap_test_consecutive_days.py`. New span shots will be generated in the first run.