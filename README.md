# AI QA Engineer Agent — Test Demo

A tiny Python repository for demonstrating how an AI QA Engineer Agent handles a passing test and a failing test.

## Project structure

- `app/calculator.py` — simple application code
- `tests/test_calculator.py` — one passing and one intentionally failing test
- `.github/workflows/tests.yml` — runs pytest on GitHub Actions

## Run locally

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

## Expected result

The suite intentionally contains:
- `test_addition_passes` — passes
- `test_subtraction_intentional_failure` — fails because the expected value is deliberately incorrect

Therefore, pytest should report **1 passed, 1 failed**, and GitHub Actions should show a failed workflow run. This failure is intentional and is included for demonstration; it is not a claim that the app itself is broken.

To make the workflow green after the demo, change the expected value in `test_subtraction_intentional_failure` from `3` to `4`.
