# Advanced-Algorithms-Programming-T27
TPs of the class for T27
Team 27

Elenie Girma Wakjira: Q1&Q4

Eylül Safiye Varyemez: Q2&Q4

Yan Shen: Q3&Q4

Q1 For exercise 1 we analyze a given message and also check for spam. For each character in the message we count the number of upper case letters, total number of letters, punctuations and also number of repeating letters to check for spamming. And then we use these counts to determine the sentiment of the messages. And the time complexity is O(n) because the loop goes from the first character to the last only one time. Space complexity is O(1) because we are only using a few variables to store counts, which doesn't change regardless of how long the message is.

Q2:

Explanation: This code builds a social network engine using Set Theory to compare and connect users. We used three main functions to achieve that (mutuals, different ones and unions). Then we set up a score system to see the similarity between users. Using this score, we returned suggestions to the user.

Complexity Analysis Questions:

The time complexity for this set intersection is O(min(m,n)). Because in order to find the intersection, you typically iterate through the smaller set and check if they exist in the larger set.

Hash set takes the same amount of time even if you have 10 friends or 10M friends. Sorted array is great for memory but you need to binary search to find people. If the users nicks are continuous integers, you can use Bit Arrays.

I would choose the Hash set.

## Exercise 3: Friend Recommendation by Common Interests
Done by: yanshen (Java)

Used a 2D matrix to store how much each user likes each interest (0–10).
Implemented cosine similarity to compare users, then recommended the top-K
most similar users who aren't already friends. Also added collaborative
filtering to suggest new interests based on what similar users like.

---

## Exercise 4: Mutual Followers Matrix
Done by: yan shen (Java)

Used a 2D boolean matrix to represent who follows who.
Implemented follow, unfollow, get followers/following, mutual follow detection,
and an influence score based on follower + following count.
