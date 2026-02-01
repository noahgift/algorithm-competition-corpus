"""Tree algorithms.

Binary tree data structures and operations.
"""

from __future__ import annotations

from algorithm_corpus.tree.bst import (
    bst_insert,
    bst_search,
    is_valid_bst,
)
from algorithm_corpus.tree.tree_node import TreeNode
from algorithm_corpus.tree.tree_properties import (
    diameter,
    height,
    is_balanced,
    is_symmetric,
)
from algorithm_corpus.tree.tree_traversal import (
    inorder,
    level_order,
    postorder,
    preorder,
)

__all__: list[str] = [
    "TreeNode",
    "bst_insert",
    "bst_search",
    "diameter",
    "height",
    "inorder",
    "is_balanced",
    "is_symmetric",
    "is_valid_bst",
    "level_order",
    "postorder",
    "preorder",
]
