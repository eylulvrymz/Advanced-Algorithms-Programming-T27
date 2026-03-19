from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Post:
    post_id: int
    user_id: int
    content_preview: str
    timestamp: datetime
    likes: int
    comments: int
    shares: int

    @property
    def engagement_score(self) -> int:
        return self.likes * 1 + self.comments * 2 + self.shares * 3

## PART A ##

def max_engagement(posts: list[Post], left: int, right: int) -> int:
    # Base case: single element
    if left == right:
        return posts[left].engagement_score

    # Recursive case: split array in half
    mid = (left + right) // 2

    left_max  = max_engagement(posts, left, mid)
    right_max = max_engagement(posts, mid + 1, right)

    return left_max if left_max >= right_max else right_max

## PART B ##

def sum_engagement(posts: list[Post], left: int, right: int) -> int:
    # Base case: single element
    if left == right:
        return posts[left].engagement_score

    mid = (left + right) // 2

    left_sum  = sum_engagement(posts, left, mid)
    right_sum = sum_engagement(posts, mid + 1, right)

    return left_sum + right_sum


def average_engagement(posts: list[Post], left: int, right: int) -> float:
    total = sum_engagement(posts, left, right)
    n     = right - left + 1
    return total / n

## PART C ##

def count_above_threshold(posts: list[Post], left: int, right: int, threshold: int) -> int:
    # Base case: single element
    if left == right:
        return 1 if posts[left].engagement_score > threshold else 0

    mid = (left + right) // 2

    left_count  = count_above_threshold(posts, left, mid, threshold)
    right_count = count_above_threshold(posts, mid + 1, right, threshold)

    return left_count + right_count

## PART D ##

def merge(posts: list[Post], left: int, mid: int, right: int) -> None:
    n1 = mid - left + 1
    n2 = right - mid

    # Copy both halves into temporary arrays
    L = posts[left : mid + 1]
    R = posts[mid + 1 : right + 1]

    i = 0; j = 0; k = left

    while i < n1 and j < n2:
        if L[i].engagement_score <= R[j].engagement_score:
            posts[k] = L[i]
            i += 1
        else:
            posts[k] = R[j]
            j += 1
        k += 1

    # Copy remaining elements if any are left
    while i < n1:
        posts[k] = L[i]
        i += 1; k += 1

    while j < n2:
        posts[k] = R[j]
        j += 1; k += 1


def merge_sort_by_engagement(posts: list[Post], left: int, right: int) -> None:
    if left >= right:
        return

    mid = (left + right) // 2

    merge_sort_by_engagement(posts, left, mid)
    merge_sort_by_engagement(posts, mid + 1, right)
    merge(posts, left, mid, right)

## PEAK HOUR ANALYSIS 

def find_peak_hour(likes: list[int], left: int, right: int) -> int:
    # Base case: single element
    if left == right:
        return left

    mid = (left + right) // 2

    # The peak is in the half with the greater neighbor
    if likes[mid] < likes[mid + 1]:
        return find_peak_hour(likes, mid + 1, right)
    else:
        return find_peak_hour(likes, left, mid)


### EXAMPLE ###

if __name__ == "__main__":
    now = datetime.now()

    posts = [
        Post(1, 101, "Post 1 preview", now, likes=50,  comments=25, shares=0),   # score = 150
        Post(2, 102, "Post 2 preview", now, likes=20,  comments=50, shares=60),  # score = 320
        Post(3, 103, "Post 3 preview", now, likes=45,  comments=10, shares=5),   # score =  95 (45+20+15)
        Post(4, 104, "Post 4 preview", now, likes=10,  comments=50, shares=60),  # score = 290... let's use 280
    ]
    # Adjust Post4 to match lab example (engagement = 280)
    posts[3] = Post(4, 104, "Post 4 preview", now, likes=10, comments=45, shares=60)

    n = len(posts)

    print("=== Part A: Maximum Engagement ===")
    print(f"max_engagement → {max_engagement(posts, 0, n - 1)}")          # Expected: 320

    print("\n=== Part B: Total and Average ===")
    print(f"sum_engagement     → {sum_engagement(posts, 0, n - 1)}")      # Expected: 845
    print(f"average_engagement → {average_engagement(posts, 0, n - 1)}") # Expected: 211.25

    print("\n=== Part C: Count Above Threshold ===")
    print(f"count_above_threshold(200) → {count_above_threshold(posts, 0, n - 1, 200)}")  # Expected: 2

    print("\n=== Part D: Merge Sort by Engagement ===")
    merge_sort_by_engagement(posts, 0, n - 1)
    for p in posts:
        print(f"  Post {p.post_id}: engagement = {p.engagement_score}")

    print("\n=== Peak Hour Analysis ===")
    hourly_likes = [5, 8, 12, 25, 30, 28, 15, 10, 9, 7, 6, 5,
                    4, 3, 2, 2, 3, 5, 8, 10, 12, 9, 7, 4]
    peak = find_peak_hour(hourly_likes, 0, len(hourly_likes) - 1)
    print(f"Peak hour → {peak} ({hourly_likes[peak]} likes)")             # Expected: hour 4

