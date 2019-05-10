# -* - coding: UTF-8 -* -

import time

import fpgrowth

'''
load kosarak data from data folder
by supplier
'''
start = time.time()
n = 20000
with open("./data/kosarak.dat", "rb") as f:
    parsed_dat = [line.split() for line in f.readlines()]
init_set = fpgrowth.create_init_set(parsed_dat)
my_fp_tree, my_header_tab = fpgrowth.create_fp_tree(init_set, n)
freq_items = []
fpgrowth.mine_fp_tree(my_fp_tree, my_header_tab, n, set([]), freq_items)
for x in freq_items:
    print(x)

# print time spent
print(time.time() - start, 'sec')

# compute support values of freq_items
supp_data = fpgrowth.cal_supp_data(my_header_tab, freq_items, len(parsed_dat))
supp_data[frozenset([])] = 1.0
# for x, v in supp_data.iteritems():
for x, v in supp_data.items():
    print(x, v)

freq_items = [frozenset(x) for x in freq_items]
fpgrowth.generate_rules(freq_items, supp_data)
