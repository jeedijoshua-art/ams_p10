set -e

echo "=========================================="
echo "     AMS DEVOPS PIPELINE STARTED"
echo "=========================================="

echo ""
echo "[1/4] Running Flake8 Code Quality Check..."
python -m flake8 attendance.py tests --max-line-length=100
echo "SUCCESS: Flake8 passed!"

echo ""
echo "[2/4] Running Bandit Security Scan..."
python -m bandit -q -r attendance.py
echo "SUCCESS: Bandit passed!"

echo ""
echo "[3/4] Running Dependency Vulnerability Audit..."
python -m pip_audit -r requirements.txt
echo "SUCCESS: pip-audit passed!"

echo ""
echo "[4/4] Running Pytest and Coverage..."
python -m pytest --cov=attendance --cov-report=term-missing --cov-fail-under=90
echo "SUCCESS: All tests and coverage checks passed!"

echo ""
echo "=========================================="
echo "     AMS DEVOPS PIPELINE COMPLETED"
echo "=========================================="
