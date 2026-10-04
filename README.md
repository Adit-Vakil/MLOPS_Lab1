# MLOps Lab 1 — CI/CD with GitHub Actions and Pytest

## Overview

This lab demonstrates Continuous Integration (CI) using GitHub Actions and Pytest. Automated tests are executed whenever code is pushed to the main branch or a pull request is created.

## Project Structure

- `src/calculator.py` — Calculator application
- `test/test_pytest.py` — Pytest test cases
- `test/test_unittest.py` — Unit tests
- `.github/workflows/ci.yml` — GitHub Actions CI workflow
- `requirements.txt` — Python dependencies

## Modifications from Original Lab

The original lab was extended with the following changes:

- Added a `divide()` function to the calculator.
- Added tests for normal division operations.
- Added decimal and negative-number test cases.
- Added division-by-zero exception handling.
- Added invalid-input validation tests.
- Updated the GitHub Actions workflow.
- Added CI execution for both pushes and pull requests to `main`.
- Updated GitHub Actions dependencies to newer versions.
- Added automatic Pytest test-report generation and artifact upload.

## Run Tests Locally

Install dependencies:

```bash
pip install -r requirements.txt
