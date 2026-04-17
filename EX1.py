
import random



# 1. split_region


def split_region(x, y, width, height, min_size):
    
    # Base case: region is too small (or equal) to split further
    if width <= min_size or height <= min_size:
        return [(x, y, width, height)]

    half_w = width / 2
    half_h = height / 2

    # Recurse on all four quadrants
    top_left     = split_region(x,          y,          half_w, half_h, min_size)
    top_right    = split_region(x + half_w, y,          half_w, half_h, min_size)
    bottom_left  = split_region(x,          y + half_h, half_w, half_h, min_size)
    bottom_right = split_region(x + half_w, y + half_h, half_w, half_h, min_size)

    return top_left + top_right + bottom_left + bottom_right



# 2. count_points_in_region


def count_points_in_region(points, region):
   
    x, y, width, height = region
    count = 0
    for (px, py) in points:
        if x <= px < x + width and y <= py < y + height:
            count += 1
    return count


# 3. find_dense_regions


def find_dense_regions(points, x, y, width, height, min_size, density_threshold):
    
    region = (x, y, width, height)
    area = width * height

    # Guard against zero-area region
    if area <= 0:
        return []

    count = count_points_in_region(points, region)
    density = count / area

   
    if density < density_threshold:
        return []

   
    if width < min_size or height < min_size:
        return [region]

    half_w = width / 2
    half_h = height / 2

    dense = []
    dense += find_dense_regions(points, x,          y,          half_w, half_h, min_size, density_threshold)
    dense += find_dense_regions(points, x + half_w, y,          half_w, half_h, min_size, density_threshold)
    dense += find_dense_regions(points, x,          y + half_h, half_w, half_h, min_size, density_threshold)
    dense += find_dense_regions(points, x + half_w, y + half_h, half_w, half_h, min_size, density_threshold)

    return dense



# Helper: generate random points inside a bounding box


def generate_random_points(n, x_min=0, x_max=100, y_min=0, y_max=100, seed=None):
    """Return n random (x, y) points within the given bounds."""
    if seed is not None:
        random.seed(seed)
    return [(random.uniform(x_min, x_max), random.uniform(y_min, y_max))
            for _ in range(n)]


# Demo


if __name__ == "__main__":
    print("=== split_region demo ===")
    leaves = split_region(0, 0, 100, 100, min_size=25)
    print(f"Leaf regions (min_size=25): {len(leaves)} regions")
    for r in leaves:
        print(f"  {r}")

    print("\n=== count_points_in_region demo ===")
    points = generate_random_points(100, seed=42)
    region = (0, 0, 50, 50)   # top-left quadrant
    c = count_points_in_region(points, region)
    print(f"Points in {region}: {c}")

    print("\n=== find_dense_regions demo ===")
   
    clustered = generate_random_points(80, 0, 30, 0, 30, seed=7)
    clustered += generate_random_points(20, 0, 100, 0, 100, seed=99)
    dense = find_dense_regions(clustered, 0, 0, 100, 100,
                               min_size=10, density_threshold=0.05)
    print(f"Dense regions found: {len(dense)}")
    for r in dense:
        print(f"  {r}")
