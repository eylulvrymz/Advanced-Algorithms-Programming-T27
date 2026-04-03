import math

class CategoryNode:
    def __init__(self, category_id, name, post_count):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.left = None
        self.right = None
        self.parent = None  #to be use in find path to root
#2. Metric calculation

def calculate_height(node):
    if node is None:
        return -1
    left_height = calculate_height(node.left)
    right_height = calculate_height(node.right)
    return max(left_height, right_height) + 1 

def calculate_node_height(node, target_id):
    target_node = find_category(target_id, node)
    if target_node is None:
        return -1 
    return calculate_height(target_node)

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

def is_balanced(node):
    if node is None:
        return True
    l_h = calculate_height(node.left)
    r_h = calculate_height(node.right)
    difference = abs(l_h - r_h) 
    
    if difference <= 1 and is_balanced(node.left) and is_balanced(node.right):
        return True
    return False

# 3. tree properties verification

def is_full_binary_tree(node):
   
    if node is None: return True
    if node.left is None and node.right is None: return True
    if node.left is not None and node.right is not None:
        return is_full_binary_tree(node.left) and is_full_binary_tree(node.right)
    return False

def is_perfect_binary_tree(node):
    
    h = calculate_height(node)
    n = count_nodes(node)
    return n == (math.pow(2, h + 1) - 1)

def _is_complete_helper(node, index, total_nodes):

    if node is None: return True
    if index > total_nodes: return False
    left_ok = _is_complete_helper(node.left, 2 * index, total_nodes)
    right_ok = _is_complete_helper(node.right, 2 * index + 1, total_nodes)
    return left_ok and right_ok

def is_complete_binary_tree(node):
    
    total = count_nodes(node)
    return _is_complete_helper(node, 1, total)

# 4. category navigation

def find_category(category_id, node):
 
    if node is None: return None
    if node.category_id == category_id: return node
    left_search = find_category(category_id, node.left)
    if left_search: return left_search
    return find_category(category_id, node.right)

def find_path_to_root(category_id, node):
   
    target = find_category(category_id, node)
    path = []
    current = target
    while current is not None:
        path.append(current.name)
        current = current.parent 
    return path

def lowest_common_ancestor(id1, id2, node):
    
    if node is None: return None
    if node.category_id == id1 or node.category_id == id2:
        return node
    l_lca = lowest_common_ancestor(id1, id2, node.left)
    r_lca = lowest_common_ancestor(id1, id2, node.right)
    if l_lca and r_lca: return node 
    return l_lca if l_lca else r_lca



def build_sample_tree():
  
    tech = CategoryNode("technology", "Technology", 150)
    prog = CategoryNode("programming", "Programming", 85)
    dsgn = CategoryNode("design", "Design", 65)
    tech.left, tech.right = prog, dsgn
    prog.parent, dsgn.parent = tech, tech
    
    python = CategoryNode("python", "Python", 42)
    java = CategoryNode("java", "Java", 30)
    prog.left, prog.right = python, java
    python.parent, java.parent = prog, prog
    
    return tech

def run_all_tests():
    root = build_sample_tree()
    print("--- Exercise 1 Test results ---")
    print(f"Total Nodes: {count_nodes(root)}")         
    print(f"Tree Height: {calculate_height(root)}")     
    print(f"Is Balanced: {is_balanced(root)}")         
    print(f"Path to Root (java): {find_path_to_root('java', root)}")
    
    # Edge Case: Empty Tree [cite: 873]
    print(f"Empty Tree Height: {calculate_height(None)}") 

if __name__ == "__main__":
    run_all_tests()
