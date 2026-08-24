#!/bin/bash
# Benchmark runner for ${IDE_NAME} Lab

set -euo pipefail

OUTPUT_DIR="benchmarks/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$OUTPUT_DIR"

echo "=== ${IDE_NAME} ${LANGUAGE} Benchmarks ==="
echo "Output: $OUTPUT_DIR"

# Placeholder for actual benchmark commands
echo "Run your ${LANGUAGE} benchmarks here" > "$OUTPUT_DIR/results.txt"
echo "Example: wrk -t4 -c100 -d30s http://localhost:$((8080 + PORT_OFFSET))/health" >> "$OUTPUT_DIR/results.txt"

echo "Benchmarks complete. Results in $OUTPUT_DIR"
