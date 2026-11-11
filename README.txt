AMS — Practicum 10: Developing a DevOps Pipeline

This folder is reconstructed from the current public main-branch files of:
https://github.com/jeedijoshua-art/ams-devops-practicum10

PROJECT CONTENTS
----------------
attendance.py                         AMS attendance-status module
tests/test_attendance.py              Automated unit tests (19 cases)
requirements.txt                      Python test dependencies
.github/workflows/devops-pipeline.yml GitHub Actions CI/CD workflow
Dockerfile                            Container build and test instructions
.gitignore                            Local Python/cache exclusions

LOCAL SETUP (macOS)
-------------------
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install flake8 bandit pip-audit

Run checks:
flake8 attendance.py tests --max-line-length=100
bandit -q -r attendance.py
pip-audit -r requirements.txt
python -m pytest --cov=attendance --cov-report=term-missing --cov-fail-under=90

Docker checks (requires Docker Desktop locally):
docker build -t ams-devops-demo .
docker run --rm ams-devops-demo

GitHub Actions runs on pushes and pull requests to main, or manual workflow dispatch.
This is a focused attendance-status demo, not the full production AMS application.
