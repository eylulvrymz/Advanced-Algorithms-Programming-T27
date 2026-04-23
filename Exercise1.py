#  Data Structures
class BSTNode:
    def __init__(self, user_id: int, name: str, friends: list):
        self.user_id: int = user_id
        self.name: str = name
        self.friends: list = friends  # list of user_ids
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None
 
 
class UserBST:
    def __init__(self):
        self.root: BSTNode | None = None
 
    #  Insert
    def _insert(self, root: BSTNode | None, user_id: int, name: str, friends_list: list) -> BSTNode:
        if root is None:
            return BSTNode(user_id, name, friends_list)
        if user_id < root.user_id:
            root.left = self._insert(root.left, user_id, name, friends_list)
        elif user_id > root.user_id:
            root.right = self._insert(root.right, user_id, name, friends_list)
        # duplicate user_id: no action
        return root
 
    def insert(self, user_id: int, name: str, friends_list: list) -> None:
        self.root = self._insert(self.root, user_id, name, friends_list)
        
    #  Find
 
    def _find(self, root: BSTNode | None, user_id: int) -> BSTNode | None:
        if root is None:
            return None
        if user_id == root.user_id:
            return root
        elif user_id < root.user_id:
            return self._find(root.left, user_id)
        else:
            return self._find(root.right, user_id)
 
    def find(self, user_id: int) -> BSTNode | None:
        return self._find(self.root, user_id)
 
    #  Inorder Traversal
  
    def _inorder(self, root: BSTNode | None, result: list) -> None:
        if root is None:
            return
        self._inorder(root.left, result)
        result.append(root.user_id)
        self._inorder(root.right, result)
 
    def inorder_traversal(self) -> list:
        result = []
        self._inorder(self.root, result)
        return result
 
    #  Delete

    def _find_min(self, node: BSTNode) -> BSTNode:
        while node.left is not None:
            node = node.left
        return node
 
    def _delete(self, root: BSTNode | None, user_id: int) -> BSTNode | None:
        if root is None:
            return None
        if user_id < root.user_id:
            root.left = self._delete(root.left, user_id)
        elif user_id > root.user_id:
            root.right = self._delete(root.right, user_id)
        else:
            # Node to delete found
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                # Two children: replace with inorder successor
                successor = self._find_min(root.right)
                root.user_id = successor.user_id
                root.name = successor.name
                root.friends = successor.friends
                root.right = self._delete(root.right, successor.user_id)
        return root
 
    def delete(self, user_id: int) -> None:
        self.root = self._delete(self.root, user_id)
        
    #  Friend-of-Friend Suggestions
    
    def suggest_friends(self, user_id: int, max_suggestions: int = 5) -> list:
        target = self.find(user_id)
        if target is None:
            return []
 
        direct_friends = set(target.friends)   # O(1) lookup
        fof_count = {}                          # fof_id → frequency
 
        for fid in target.friends:
            friend_node = self.find(fid)
            if friend_node is None:
                continue
            for fof_id in friend_node.friends:
                if fof_id != user_id and fof_id not in direct_friends:
                    fof_count[fof_id] = fof_count.get(fof_id, 0) + 1
 
        # Sort by frequency descending
        candidates = sorted(fof_count.items(), key=lambda x: x[1], reverse=True)
        return candidates[:max_suggestions]
 
    #  BST Analytics
    
    def _get_height(self, root: BSTNode | None) -> int:
        if root is None:
            return -1
        left_h = self._get_height(root.left)
        right_h = self._get_height(root.right)
        return 1 + max(left_h, right_h)
 
    def get_height(self) -> int:
        return self._get_height(self.root)
 
    # Returns actual height if balanced, -2 if unbalanced
    def _check_balance(self, root: BSTNode | None) -> int:
        if root is None:
            return -1
        left_h = self._check_balance(root.left)
        if left_h == -2:
            return -2
        right_h = self._check_balance(root.right)
        if right_h == -2:
            return -2
        if abs(left_h - right_h) > 1:
            return -2
        return 1 + max(left_h, right_h)
 
    def is_balanced(self) -> bool:
        return self._check_balance(self.root) != -2
 
    def _get_leaf_count(self, root: BSTNode | None) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self._get_leaf_count(root.left) + self._get_leaf_count(root.right)
 
    def get_leaf_count(self) -> int:
        return self._get_leaf_count(self.root)
