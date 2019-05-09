# coding:utf-8
class TreeNode:
    def __init__(self, name_value, num_occur, parent_node):
        self.name = name_value
        self.count = num_occur
        self.nodeLink = None
        self.parent = parent_node
        self.children = {}

    def inc(self, num_occur):
        self.count += num_occur

    def disp(self, ind=1):
        print('  ' * ind, self.name, ' ', self.count)
        for child in self.children.values():
            child.disp(ind + 1)


def update_header(node_2_test, target_node):
    while node_2_test.nodeLink != None:
        node_2_test = node_2_test.nodeLink
    node_2_test.nodeLink = target_node


def update_fp_tree(items, in_tree, header_table, count):
    if items[0] in in_tree.children:
        # 判断items的第一个结点是否已作为子结点
        in_tree.children[items[0]].inc(count)
    else:
        # 创建新的分支
        in_tree.children[items[0]] = TreeNode(items[0], count, in_tree)
        if header_table[items[0]][1] == None:
            header_table[items[0]][1] = in_tree.children[items[0]]
        else:
            update_header(header_table[items[0]][1], in_tree.children[items[0]])
    # 递归
    if len(items) > 1:
        update_fp_tree(items[1::], in_tree.children[items[0]], header_table, count)


def create_fp_tree(data_set, min_sup=1):
    header_table = {}
    for trans in data_set:
        for item in trans:
            header_table[item] = header_table.get(item, 0) + data_set[trans]
    for k in list(header_table.keys()):
        if header_table[k] < min_sup:
            # del (header_table[k])  # 删除不满足最小支持度的元素
            header_table.pop(k)
    freq_item_set = set(header_table.keys())  # 满足最小支持度的频繁项集
    if len(freq_item_set) == 0:
        return None, None
    for k in header_table:
        header_table[k] = [header_table[k], None]  # element: [count, node]

    ret_tree = TreeNode('Null Set', 1, None)
    for tranSet, count in data_set.items():
        # data_set：[element, count]
        local_d = {}
        for item in tranSet:
            if item in freq_item_set:  # 过滤，只取该样本中满足最小支持度的频繁项
                local_d[item] = header_table[item][0]  # element : count
        if len(local_d) > 0:
            # 根据全局频数从大到小对单样本排序
            ordered_item = [v[0] for v in sorted(local_d.items(), key=lambda p: (p[1], int(p[0])), reverse=True)]
            # 用过滤且排序后的样本更新树
            update_fp_tree(ordered_item, ret_tree, header_table, count)
    return ret_tree, header_table


# 回溯
def ascend_fp_tree(leaf_node, prefix_path):
    if leaf_node.parent != None:
        prefix_path.append(leaf_node.name)
        ascend_fp_tree(leaf_node.parent, prefix_path)


# 条件模式基
def find_prefix_path(base_pat, my_header_tab):
    # basePat在FP树中的第一个结点
    tree_node = my_header_tab[base_pat][1]
    cond_pats = {}
    while tree_node != None:
        prefix_path = []
        # prefixPath是倒过来的，从treeNode开始到根
        ascend_fp_tree(tree_node, prefix_path)
        if len(prefix_path) > 1:
            # 关联treeNode的计数
            cond_pats[frozenset(prefix_path[1:])] = tree_node.count
        # 下一个basePat结点
        tree_node = tree_node.nodeLink
    return cond_pats


def mine_fp_tree(in_tree, header_table, min_sup, pre_fix, freq_item_list):
    # 最开始的频繁项集是headerTable中的各元素
    # 根据频繁项的总频次排序
    big_l = [v[0] for v in sorted(header_table.items(), key=lambda p: p[1])]
    for base_pat in big_l:  # 对每个频繁项
        new_freq_set = pre_fix.copy()
        new_freq_set.add(base_pat)
        freq_item_list.append(new_freq_set)
        # 当前频繁项集的条件模式基
        cond_patt_bases = find_prefix_path(base_pat, header_table)
        # 构造当前频繁项的条件FP树
        my_cond_tree, my_head = create_fp_tree(cond_patt_bases, min_sup)
        if my_head != None:
            # print 'conditional tree for: ', new_freq_set
            #  my_cond_tree.disp(1)
            # 递归挖掘条件FP树
            mine_fp_tree(my_cond_tree, my_head, min_sup, new_freq_set, freq_item_list)


def load_simple_dat():
    simple_dat = [['r', 'z', 'h', 'j', 'p'],
                  ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
                  ['z'],
                  ['r', 'x', 'n', 'o', 's'],
                  ['y', 'r', 'x', 'z', 'q', 't', 'p'],
                  ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simple_dat


def create_init_set(data_set):
    ret_dict = {}
    for trans in data_set:
        key = frozenset(trans)
        if key in ret_dict:
            ret_dict[frozenset(trans)] += 1
        else:
            ret_dict[frozenset(trans)] = 1
    return ret_dict


def cal_supp_data(header_table, freq_item_list, total):
    supp_data = {}
    for Item in freq_item_list:
        # 找到最底下的结点
        Item = sorted(Item, key=lambda x: header_table[x][0])
        base = find_prefix_path(Item[0], header_table)
        # 计算支持度
        support = 0
        for B in base:
            if frozenset(Item[1:]).issubset(set(B)):
                support += base[B]
        # 对于根的儿子，没有条件模式基
        if len(base) == 0 and len(Item) == 1:
            support = header_table[Item[0]][0]

        supp_data[frozenset(Item)] = support / float(total)
    return supp_data


def apollo_gen(lk, k):
    ret_list = []
    len_lk = len(lk)
    for i in range(len_lk):
        for j in range(i + 1, len_lk):
            l1 = list(lk[i])[:k - 2];
            l2 = list(lk[j])[:k - 2]
            l1.sort();
            l2.sort()
            if l1 == l2:
                ret_list.append(lk[i] | lk[j])
    return ret_list


def calc_conf(freq_set, h, support_data, br1, min_conf=0.7):
    pruned_h = []
    for conseq in h:
        conf = support_data[freq_set] / support_data[freq_set - conseq]
        if conf >= min_conf:
            print("{0} --> {1} conf:{2}".format(freq_set - conseq, conseq, conf))
            br1.append((freq_set - conseq, conseq, conf))
            pruned_h.append(conseq)
    return pruned_h


def rules_from_conseq(freq_set, H, support_data, br1, min_conf=0.7):
    m = len(H[0])
    if len(freq_set) > m + 1:
        hmp1 = apollo_gen(H, m + 1)
        hmp1 = calc_conf(freq_set, hmp1, support_data, br1, min_conf)
        if len(hmp1) > 1:
            rules_from_conseq(freq_set, hmp1, support_data, br1, min_conf)


def generate_rules(freq_item_list, support_data, min_conf=0.7):
    big_rule_list = []
    for freq_set in freq_item_list:
        h1 = [frozenset([item]) for item in freq_set]
        if len(freq_set) > 1:
            rules_from_conseq(freq_set, h1, support_data, big_rule_list, min_conf)
        else:
            calc_conf(freq_set, h1, support_data, big_rule_list, min_conf)
    return big_rule_list
