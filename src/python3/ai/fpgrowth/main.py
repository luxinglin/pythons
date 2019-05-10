# -* - coding: UTF-8 -* -

import time

import fpgrowth


def calculate_fp(_parsed_data, _min_support):
    init_set = fpgrowth.create_init_set(_parsed_data)
    my_fp_tree, my_header_tab = fpgrowth.create_fp_tree(init_set, _min_support)
    freq_items = []
    fpgrowth.mine_fp_tree(my_fp_tree, my_header_tab, _min_support, set([]), freq_items)
    for x in freq_items:
        print(x)

    # compute support values of freq_items
    supp_data = fpgrowth.cal_supply_data(my_header_tab, freq_items, len(_parsed_data))
    supp_data[frozenset([])] = 1.0
    # for x, v in supp_data.iteritems():
    for x, v in supp_data.items():
        print(x, v)

    # calculate relation ratio
    print('begin calculate ration')
    freq_items = [frozenset(x) for x in freq_items]
    fpgrowth.generate_rules(freq_items, supp_data)


if __name__ == '__main__':
    start = time.time()
    n = 20000
    with open("./data/kosarak.dat", "rb") as f:
        parsed_data = [line.split() for line in f.readlines()]
    print("total records: ", parsed_data.__sizeof__() / 10000, "w, min_support: ", n / 10000, "w")
    calculate_fp(parsed_data, n)
