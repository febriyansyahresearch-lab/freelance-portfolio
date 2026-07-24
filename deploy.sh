#!/bin/bash
set -e

echo "=== Building Docker image ==="
docker build -t freelance-portfolio .

echo "=== Running all tests ==="
docker run --rm freelance-portfolio bash scripts/setup.sh

echo "=== Done ==="
