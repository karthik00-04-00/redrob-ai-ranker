from src.job_understanding import (
    extract_job_signals,
)

with open(
    "sample_jd.txt",
    "r",
    encoding="utf-8",
) as f:

    jd = f.read()

signals = extract_job_signals(
    jd
)

print(signals)