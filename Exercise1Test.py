

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

# Edge: region smaller than min_size → should return as-is immediately
leaves = split_region(0, 0, 5, 10, 10)
check("Region smaller than min_size → 1 leaf", len(leaves) == 1)

# Edge: min_size = 1 on a 4x4 region → 16 leaves
leaves = split_region(0, 0, 4, 4, 1)
check("min_size=1, 4x4 region → 16 leaves", len(leaves) == 16, f"got {len(leaves)}")

# Edge: non-square region (200x100, min=50)
leaves = split_region(0, 0, 200, 100, 50)
check("Non-square region produces leaves", len(leaves) > 0)

# Edge: all leaves together should cover the full area (no overlap / no gap)
leaves = split_region(0, 0, 100, 100, 25)
total_area = sum(w * h for (_, _, w, h) in leaves)
check("Leaf areas sum to original area", abs(total_area - 100 * 100) < 1e-9,
      f"sum={total_area}")

# Edge: offset origin – leaves should start at (10, 20), not (0,0)
leaves = split_region(10, 20, 100, 100, 50)
xs = [x for (x, _, _, _) in leaves]
check("Offset origin: all x >= 10", all(x >= 10 for x in xs))


# TESTS: count_points_in_region

print("\n── count_points_in_region ────────────────────────────────────")

# Normal: all points inside
pts = [(10, 10), (20, 20), (30, 30)]
check("All 3 points inside region", count_points_in_region(pts, (0, 0, 50, 50)) == 3)

# Normal: no points inside
pts = [(60, 60), (70, 80)]
check("No points inside region", count_points_in_region(pts, (0, 0, 50, 50)) == 0)

# Edge: empty point list
check("Empty point list → 0", count_points_in_region([], (0, 0, 100, 100)) == 0)

# Edge: point exactly on the left/top boundary → inside (x <= px < x+w)
pts = [(0, 0)]
check("Point on top-left corner → inside", count_points_in_region(pts, (0, 0, 10, 10)) == 1)

# Edge: point exactly on the right boundary → outside (half-open interval)
pts = [(10, 5)]
check("Point on right boundary → outside", count_points_in_region(pts, (0, 0, 10, 10)) == 0)

# Edge: point exactly on the bottom boundary → outside
pts = [(5, 10)]
check("Point on bottom boundary → outside", count_points_in_region(pts, (0, 0, 10, 10)) == 0)

# Edge: zero-size region → nothing can be inside
pts = [(5, 5)]
check("Zero-width region → 0", count_points_in_region(pts, (5, 5, 0, 0)) == 0)

# Edge: negative coordinates
pts = [(-5, -5), (-1, -1)]
check("Negative coordinates counted correctly",
      count_points_in_region(pts, (-10, -10, 10, 10)) == 2)


# TESTS: find_dense_regions

print("\n── find_dense_regions ────────────────────────────────────────")

# Normal: all points in one corner → that corner should be dense
pts = [(x, y) for x in range(0, 20) for y in range(0, 20)]  # 400 pts in 0-20 box
dense = find_dense_regions(pts, 0, 0, 100, 100, min_size=10, density_threshold=0.01)
check("Clustered points → at least 1 dense region", len(dense) > 0)

# Verify dense regions are actually inside the original space
check("Dense regions within bounds",
      all(x >= 0 and y >= 0 and x + w <= 100 and y + h <= 100
          for (x, y, w, h) in dense))

# Edge: no points → no dense regions
dense = find_dense_regions([], 0, 0, 100, 100, min_size=10, density_threshold=0.01)
check("No points → no dense regions", len(dense) == 0)

# Edge: very high threshold → nothing passes
pts = [(50, 50)]
dense = find_dense_regions(pts, 0, 0, 100, 100, min_size=10, density_threshold=999)
check("Impossibly high threshold → no dense regions", len(dense) == 0)

# Edge: threshold = 0 → every non-empty region qualifies (at least 1 result)
pts = [(50, 50)]
dense = find_dense_regions(pts, 0, 0, 100, 100, min_size=10, density_threshold=0)
check("Threshold=0 with 1 point → at least 1 region found", len(dense) > 0)

# Edge: min_size larger than region → treated as leaf immediately if dense
pts = [(5, 5)] * 50
dense = find_dense_regions(pts, 0, 0, 10, 10, min_size=20, density_threshold=0.01)
check("min_size > region → returns region as leaf if dense", len(dense) == 1)

# Edge: region with zero area
dense = find_dense_regions([(5, 5)], 5, 5, 0, 0, min_size=1, density_threshold=0.01)
check("Zero-area region → no dense regions returned", len(dense) == 0)


# Summary

print(f"\n{'='*50}")
print(f"Results: {passed} passed, {failed} failed out of {passed + failed} tests")
if failed == 0:
    print("All tests passed ✓")
else:
    print(f"{failed} test(s) failed ✗")
