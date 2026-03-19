from datetime import datetime

now = datetime.now()

def make_post(post_id, likes, comments, shares):
    return Post(post_id, 1, "preview", now, likes, comments, shares)

### Helper ###
def test(name, result, expected):
    status = "PASS" if result == expected else "FAIL"
    print(f"[{status}] {name} → got {result}, expected {expected}")

### Edge Case Posts ###

single    = [make_post(1, 10, 5, 2)]                          # only one post
equal     = [make_post(1, 10, 0, 0), make_post(2, 10, 0, 0)] # equal scores
two_posts = [make_post(1, 50, 0, 0), make_post(2, 0, 0, 0)]  # one zero score
all_zero  = [make_post(i, 0, 0, 0) for i in range(4)]        # all zeros
normal    = [make_post(1, 50, 25, 0),   # 100
             make_post(2, 20, 50, 60),  # 320
             make_post(3, 45, 10, 5),   #  80 (fixed)
             make_post(4, 10, 45, 60)]  # 280

### max_engagement ###
print("\n--- max_engagement ---")
test("Single post",        max_engagement(single, 0, 0), 10)
test("Equal scores",       max_engagement(equal, 0, 1), 10)
test("One zero score",     max_engagement(two_posts, 0, 1), 50)
test("All zeros",          max_engagement(all_zero, 0, 3), 0)
test("Normal case",        max_engagement(normal, 0, 3), 320)

### sum_engagement ###
print("\n--- sum_engagement ---")
test("Single post",        sum_engagement(single, 0, 0), 10)
test("All zeros",          sum_engagement(all_zero, 0, 3), 0)
test("Normal case",        sum_engagement(normal, 0, 3), 790)

### average_engagement ###
print("\n--- average_engagement ---")
test("Single post",        average_engagement(single, 0, 0), 10.0)
test("All zeros",          average_engagement(all_zero, 0, 3), 0.0)
test("Normal case",        average_engagement(normal, 0, 3), 197.5)

### count_above_threshold ###
print("\n--- count_above_threshold ---")
test("None above",         count_above_threshold(normal, 0, 3, 500), 0)
test("All above",          count_above_threshold(normal, 0, 3, 0),   4)
test("Threshold = score",  count_above_threshold(equal,  0, 1, 10),  0) # not strictly >
test("Normal case",        count_above_threshold(normal, 0, 3, 200), 2)

### merge_sort_by_engagement ###
print("\n--- merge_sort_by_engagement ---")

already_sorted = [make_post(1, 0, 0, 0), make_post(2, 5, 0, 0), make_post(3, 10, 0, 0)]
merge_sort_by_engagement(already_sorted, 0, 2)
test("Already sorted", [p.engagement_score for p in already_sorted], [0, 5, 10])

reverse_sorted = [make_post(1, 10, 0, 0), make_post(2, 5, 0, 0), make_post(3, 0, 0, 0)]
merge_sort_by_engagement(reverse_sorted, 0, 2)
test("Reverse sorted", [p.engagement_score for p in reverse_sorted], [0, 5, 10])

equal_scores = [make_post(i, 10, 0, 0) for i in range(3)]
merge_sort_by_engagement(equal_scores, 0, 2)
test("All equal",      [p.engagement_score for p in equal_scores], [10, 10, 10])

### find_peak_hour ###
print("\n--- find_peak_hour ---")
test("Peak at start",  find_peak_hour([30, 20, 10, 5], 0, 3), 0)
test("Peak at end",    find_peak_hour([5, 10, 20, 30], 0, 3), 3)
test("Peak in middle", find_peak_hour([5, 10, 30, 20, 8], 0, 4), 2)
test("Single element", find_peak_hour([42], 0, 0), 0)
test("Two elements",   find_peak_hour([5, 15], 0, 1), 1)
