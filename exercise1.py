from dataclasses import dataclass, field
from datetime import datetime
from typing import List
import copy



@dataclass
class CommentNode:
    comment_id: int
    user_id: str
    content: str
    timestamp: datetime
    likes: int
    replies: List['CommentNode'] = field(default_factory=list)



def display_thread(comment: CommentNode, level: int = 0):
    indent = '  ' * level
    print(f"{indent}[{comment.comment_id}] {comment.user_id}: {comment.content}")
    for reply in comment.replies:
        display_thread(reply, level + 1)


def count_total_comments(comment: CommentNode) -> int:
    total = 1
    for reply in comment.replies:
        total += count_total_comments(reply)
    return total


def total_likes(comment: CommentNode) -> int:
    total = comment.likes
    for reply in comment.replies:
        total += total_likes(reply)
    return total


def find_deepest_reply(comment: CommentNode) -> int:
    if not comment.replies:
        return 0
    return 1 + max(find_deepest_reply(reply) for reply in comment.replies)



def search_by_user(user_id: str, comment: CommentNode) -> List[CommentNode]:
    result = []
    if comment.user_id == user_id:
        result.append(comment)
    for reply in comment.replies:
        result.extend(search_by_user(user_id, reply))
    return result


def contains_keyword(keyword: str, comment: CommentNode) -> bool:
    if keyword.lower() in comment.content.lower():
        return True
    for reply in comment.replies:
        if contains_keyword(keyword, reply):
            return True
    return False



def delete_comment(comment_id: int, thread: List[CommentNode]) -> List[CommentNode]:
    new_thread = []
    for comment in thread:
        if comment.comment_id != comment_id:
            comment.replies = delete_comment(comment_id, comment.replies)
            new_thread.append(comment)
    return new_thread


def get_thread_without_comment(comment_id: int, thread: List[CommentNode]) -> List[CommentNode]:
    new_thread = []
    for comment in thread:
        if comment.comment_id != comment_id:
            new_comment = copy.copy(comment)
            new_comment.replies = get_thread_without_comment(comment_id, comment.replies)
            new_thread.append(new_comment)
    return new_thread



def build_main_thread():
    now = datetime.now()
    c401 = CommentNode(401, "Bob",     "It was delicious!",          now, 10)
    c301 = CommentNode(301, "Alice",   "What did you think?",        now, 5,  [c401])
    c201 = CommentNode(201, "Bob",     "I tried it last night!",     now, 8,  [c301])
    c302 = CommentNode(302, "Alice",   "Yes, that works too!",       now, 3)
    c202 = CommentNode(202, "Charlie", "Can I use olive oil instead?",now, 6,  [c302])
    root = CommentNode(101, "Alice",   "This recipe looks amazing!", now, 20, [c201, c202])
    return root


def run_main_test():
    print("MAIN EXAMPLE THREAD")

    root = build_main_thread()

    print("\n display_thread ")
    display_thread(root)

    print(f"\n count_total_comments ")
    print(f"Total comments: {count_total_comments(root)}")

    print(f"\n total_likes ")
    print(f"Total likes: {total_likes(root)}")

    print(f"\n find_deepest_reply ")
    print(f"Max depth: {find_deepest_reply(root)}")

    print(f"\n search_by_user (Alice) ")
    alice_comments = search_by_user("Alice", root)
    print(f"Alice's comment IDs: {[c.comment_id for c in alice_comments]}")

    print(f"\n contains_keyword ")
    print(f"Contains 'delicious': {contains_keyword('delicious', root)}")
    print(f"Contains 'pizza': {contains_keyword('pizza', root)}")

    print(f"\n delete_comment (delete 201) ")
    new_thread = delete_comment(201, [root])
    display_thread(new_thread[0])

    print(f"\n get_thread_without_comment (delete 202) ")
    root2 = build_main_thread()  # fresh copy
    new_thread2 = get_thread_without_comment(202, [root2])
    display_thread(new_thread2[0])


#  Edge Case Tests 

def run_edge_tests():
    now = datetime.now()
    print("EDGE CASE TESTS")

#Test 1: Single comment, no replies
    single = CommentNode(1, "Alice", "This recipe looks amazing!", now, 5)
    assert count_total_comments(single) == 1
    assert total_likes(single) == 5
    assert find_deepest_reply(single) == 0
    print(" Test 1 passed: Single comment, no replies")

    # Test 2: Empty replies list
    empty_replies = CommentNode(2, "Bob", "I tried it last night!", now, 3, [])
    assert count_total_comments(empty_replies) == 1
    display_thread(empty_replies)
    print(" Test 2 passed: Empty replies list")

    #Test 3: Linear chain  A->B->C->D->E (depth=4, count=5)
    c5 = CommentNode(5, "Bob",     "It was delicious!",           now, 1)
    c4 = CommentNode(4, "Alice",   "What did you think?",         now, 1, [c5])
    c3 = CommentNode(3, "Charlie", "Can I use olive oil instead?",now, 1, [c4])
    c2 = CommentNode(2, "Bob",     "I tried it last night!",      now, 1, [c3])
    c1 = CommentNode(1, "Alice",   "This recipe looks amazing!",  now, 1, [c2])
    assert find_deepest_reply(c1) == 4
    assert count_total_comments(c1) == 5
    print(" Test 3 passed: Linear chain, depth=4, count=5")

    #Test 4:  Wide tree (1 root + 100 direct replies, depth=1, count=101)
    wide_replies = [
        CommentNode(i, "Bob", f"Reply number {i}", now, 1)
        for i in range(2, 102)
    ]
    wide_root = CommentNode(1, "Alice", "This recipe looks amazing!", now, 1, wide_replies)
    assert find_deepest_reply(wide_root) == 1
    assert count_total_comments(wide_root) == 101
    print(" Test 4 passed: Wide tree, depth=1, count=101")

    #Test 5: Delete child + cascade (only root remains)
    sub   = CommentNode(3, "Charlie", "Can I use olive oil instead?", now, 1)
    child = CommentNode(2, "Bob",     "I tried it last night!",       now, 1, [sub])
    root5 = CommentNode(1, "Alice",   "This recipe looks amazing!",   now, 1, [child])
    new_thread5 = delete_comment(2, [root5])
    assert count_total_comments(new_thread5[0]) == 1
    print(" Test 5 passed: Delete child cascades to sub-replies")

    #Test 6: Delete non-existent id (thread unchanged)
    root6 = CommentNode(1, "Alice", "This recipe looks amazing!", now, 1, [
        CommentNode(2, "Bob", "I tried it last night!", now, 1)
    ])
    new_thread6 = delete_comment(999, [root6])
    assert count_total_comments(new_thread6[0]) == 2
    print(" Test 6 passed: Delete non-existent id, thread unchanged")

    #Test 7: Delete root itself (returns empty list)
    root7 = CommentNode(1, "Alice", "This recipe looks amazing!", now, 1)
    new_thread7 = delete_comment(1, [root7])
    assert new_thread7 == []
    print(" Test 7 passed: Delete root returns empty list")
    
    # Test 8: Search user not in thread (returns empty list)
    root8 = CommentNode(1, "Alice", "This recipe looks amazing!", now, 1, [
        CommentNode(2, "Bob", "I tried it last night!", now, 1)
    ])
    result8 = search_by_user("Charlie", root8)
    assert result8 == []
    print(" Test 8 passed: Search non-existent user returns empty list")

    # Test 9: Keyword buried 5 levels deep
    deep5 = CommentNode(5, "Bob",     "It was absolutely delicious!",now, 1)
    deep4 = CommentNode(4, "Alice",   "What did you think?",         now, 1, [deep5])
    deep3 = CommentNode(3, "Charlie", "Can I use olive oil instead?",now, 1, [deep4])
    deep2 = CommentNode(2, "Bob",     "I tried it last night!",      now, 1, [deep3])
    deep1 = CommentNode(1, "Alice",   "This recipe looks amazing!",  now, 1, [deep2])
    assert contains_keyword("delicious", deep1) == True
    assert contains_keyword("pizza",     deep1) == False
    print(" Test 9 passed: Keyword found 5 levels deep")

    #Test 10: All comments by same user (returns all 5)
    same_replies = [
        CommentNode(i, "Alice", f"Alice comment {i}", now, 1)
        for i in range(2, 6)
    ]
    root10 = CommentNode(1, "Alice", "This recipe looks amazing!", now, 1, same_replies)
    result10 = search_by_user("Alice", root10)
    assert len(result10) == 5
    print(" Test 10 passed: All comments by same user returns all 5")

    #Test 11: All likes = 0
    root11 = CommentNode(1, "Alice", "This recipe looks amazing!", now, 0, [
        CommentNode(2, "Bob", "I tried it last night!", now, 0)
    ])
    assert total_likes(root11) == 0
    print(" Test 11 passed: All likes = 0, total_likes returns 0")

    print("\n All edge case tests passed!")



if __name__ == "__main__":  # ← colon here
    run_main_test()
    run_edge_tests()
