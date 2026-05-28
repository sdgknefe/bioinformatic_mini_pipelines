import sys
from src.pipeline import run_pipeline


file_path = sys.argv[1]

results = run_pipeline(file_path)

print(results)