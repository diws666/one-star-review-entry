import os

# Fixed one-star review of gravity: a deadpan, earnest complaint about an
# everyday essential that cannot be fixed. The line must not change.
LINE = "One star. Gravity promised to keep my feet on the ground, but it dropped my phone face-down again."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
path = os.path.join(output_dir, "entry.txt")

with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
