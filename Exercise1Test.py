

from exercise1 import split_region, count_points_in_region, find_dense_regions

passed = 0
failed = 0

def check(name, condition, detail=""):
    global passed, failed
    status = "PASS" if condition else "FAIL"
    if condition:
        passed += 1
    else:
        failed += 1
    print(f"  [{status}] {name}" + (f" → {detail}" if detail else ""))

# TESTS: split_region

print("\n── split_region ──────────────────────────────────────────────")

# Normal case: 100x100 with min_size=25 should produce 16 leaves
leaves = split_region(0, 0, 100, 100, 25)
check("Normal split (100x100, min=25) → 16 leaves", len(leaves) == 16, f"got {len(leaves)}")

# Normal case: 100x100 with min_size=50 should produce 4 leaves
leaves = split_region(0, 0, 100, 100, 50)
check("Normal split (100x100, min=50) → 4 leaves", len(leaves) == 4, f"got {len(leaves)}")

# Edge: region exactly equal to min_size → should return as-is (no split)
leaves = split_region(0, 0, 10, 10, 10)
check("Region == min_size → 1 leaf (no split)", len(leaves) == 1)


