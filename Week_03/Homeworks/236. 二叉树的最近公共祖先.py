# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/

class Solution:
    '''
    只要某节点满足下面条件，则为正确答案
    (f_lson && f_rson)    ∣∣    ((x = p ∣∣ x = q) && (f_lson ∣∣ f_rson))
            ^                                ^
            |                                |
     此处表示一个在左子树             此处表示其中一个恰好
      一个在右子树的情况            在另一个的根节点上的情况
    
    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/er-cha-shu-de-zui-jin-gong-gong-zu-xian-by-leetc-2/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.answer = TreeNode(None)
        self.dfs(root, p, q)
        return self.answer
    
    def dfs(self, root, p, q):
        '''
        dfs深度优先搜索的目标：
            f_son -> return True, if 'root' node contains p or q
                     return False, if 'root' node contains nor p nor q
                     并且在每次递归查看是否满足约束条件，如果满足，则将root节点存到self.answer中
        '''
        if root == None: return False   # 返回条件1：都遍历到最深叶节点了，都没找到p or q，因此 return False
        f_lson = self.dfs(root.left, p, q)
        f_rson = self.dfs(root.right, p, q)
        # Process条件，如果当前节点的情况满足上述两种，则表明找到了最近公共祖先
        if (f_lson and f_rson) or ((root == p or root == q) and (f_lson or f_rson)):
            self.answer = root
        
        # 返回条件2：如果一旦碰到p or q，或者在当前节点的子节点f_lson or f_rson发现过p or q，则返回True
        if f_lson or f_rson or (root == p or root == q): return True