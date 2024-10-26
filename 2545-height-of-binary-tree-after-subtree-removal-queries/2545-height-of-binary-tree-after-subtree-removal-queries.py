class Solution:
    def treeQueries(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[int]:
        def dfs(root, depth):
            if not root:
                return
    
            node_index_map[root.val] = len(node_depths)
            node_depths.append(depth)
    
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        def calculate_subtree_size(root):
            if not root:
                return 0
    
            left_size = calculate_subtree_size(root.left)
            right_size = calculate_subtree_size(root.right)
    
            total_size = left_size + right_size + 1
            subtree_size[root.val] = total_size
    
            return total_size

        node_index_map = {}
        subtree_size = {}

        node_depths = []
        max_depth_from_left = []
        max_depth_from_right = []

        dfs(root, 0)

        total_nodes = len(node_depths)

        calculate_subtree_size(root)

        max_depth_from_left.append(node_depths[0])
        max_depth_from_right.append(node_depths[-1])

        for i in range(1, total_nodes):
            max_depth_from_left.append(
                max(max_depth_from_left[i - 1], node_depths[i])
            )
            max_depth_from_right.append(
                max(
                    max_depth_from_right[i - 1],
                    node_depths[total_nodes - i - 1],
                )
            )

        max_depth_from_right.reverse()

        results = []
        for query_node in queries:
            start_index = node_index_map[query_node] - 1
            end_index = start_index + 1 + subtree_size[query_node]

            max_depth = max_depth_from_left[start_index]
            if end_index < total_nodes:
                max_depth = max(max_depth, max_depth_from_right[end_index])

            results.append(max_depth)

        return results
