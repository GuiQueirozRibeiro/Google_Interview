'''
04.09 BST Sequences: A binary search tree was created by traversing through an array from left to right
    and inserting each element. Given a binary search tree with distinct elements, print all possible
    arrays that could have led to this tree.

    EXAMPLE

    Input:
        1 <- 2 -> 3
    Output: {2, 1, 3}, {2, 3, 1}
'''

# Time: O(2^n * n!) Space: O(2^n * n!)
def find_bst_sequences(bst):
    if not bst.root:
        return []
    return helper(bst.root)

# Time: O(2^n * n!) Space: O(2^n * n!)
def helper(node):
    if not node:
        return [[]]

    right_sequences = helper(node.right)
    left_sequences = helper(node.left)
    sequences = []
    for right in right_sequences:
        for left in left_sequences:
            sequences = weave(left, right, [node.key], sequences)
    return sequences

# Time: O(2^n * n!) Space: O(2^n * n!)
def weave(first, second, prefix, results):
    if len(first) == 0 or len(second) == 0:
        result = prefix.copy()
        result.extend(first)
        result.extend(second)
        results.append(result)
        return results

    head = first[0]
    prefix.append(head)
    results = weave(first[1:], second, prefix, results)
    prefix.pop()
    head = second[0]
    prefix.append(head)
    results = weave(first, second[1:], prefix, results)
    prefix.pop()
    return results

# Time: O(2^n * n!) Space: O(2^n * n!)
def find_bst_sequences_backtracking(bst):
    if not bst.root:
        return []

    ret_backtracking = []

    def backtracking(choices, weave):
        if not len(choices):
            ret_backtracking.append(weave)
            return

        for i in range(len(choices)):
            nextchoices = choices[:i] + choices[i + 1 :]
            if choices[i].left:
                nextchoices += [choices[i].left]
            if choices[i].right:
                nextchoices += [choices[i].right]
            backtracking(nextchoices, weave + [choices[i].key])

    backtracking([bst.root], [])
    return ret_backtracking