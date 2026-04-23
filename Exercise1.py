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

  
