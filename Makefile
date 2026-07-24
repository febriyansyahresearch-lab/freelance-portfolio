.PHONY: setup install test lint train-api train-phishing run-api run-siem run-scanner run-phishing docker-build docker-run clean

setup: install train-api train-phishing

install:
	pip install -r requirements.txt

test:
	python -m pytest cyber_ml/tests/ stock_ml/tests/ fraud_detection/tests/ siem_dashboard/tests/ vulnerability_scanner/tests/ phishing_detector/tests/ -v

lint:
	ruff check .

train-api:
	python -m fraud_detection.src.train

train-phishing:
	python -m phishing_detector.src.train

run-api:
	uvicorn fraud_detection.src.api:app --reload

run-siem:
	python -m siem_dashboard.src.app

run-scanner:
	python -m vulnerability_scanner.src.scanner --target scanme.nmap.org

run-phishing:
	python -m phishing_detector.src.classify --url "http://suspicious-login.com"

docker-build:
	docker build -t freelance-portfolio .

docker-run:
	docker run --rm freelance-portfolio bash -c "python -m pytest cyber_ml/tests/ stock_ml/tests/ fraud_detection/tests/ siem_dashboard/tests/ vulnerability_scanner/tests/ phishing_detector/tests/ -v"

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
