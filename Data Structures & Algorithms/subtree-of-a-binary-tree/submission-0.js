/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @param {TreeNode} subRoot
     * @return {boolean}
     */
    isSubtree(root, subRoot) {

    // Checks if two trees are exactly the same
    function isSameTree(node1, node2) {

        // Both are null
        if (node1 === null && node2 === null) {
            return true;
        }

        // One is null
        if (node1 === null || node2 === null) {
            return false;
        }

        // Values differ
        if (node1.val !== node2.val) {
            return false;
        }

        // Compare left and right subtrees
        return isSameTree(node1.left, node2.left) &&
               isSameTree(node1.right, node2.right);
    }

    // DFS to search every node in root
    function dfs(node) {

        if (node === null) {
            return false;
        }

        // Found a potential starting point
        if (isSameTree(node, subRoot)) {
            return true;
        }

        // Keep searching
        return dfs(node.left) || dfs(node.right);
    }

    return dfs(root);
}
}