import json
from func import Func
import sys
import copy
import datetime
import csv
import os

start_time = datetime.datetime.now()
print("start time: %s" % start_time.strftime("%Y-%m-%d %p %I:%M:%S"))

lambda_pl_lst = [1 / (10 * 2 * i) for i in range(1, 6)]
mu_pl_lst = [1 / (650 * 2 * i) for i in range(1, 6)]
Q = 1
theta = 0.7
item_size_lst = [10 * i for i in range(1, 16)]
cl = 1
cr_lst = [10 * i * 2 for i in range(1, 6)]

result_keys = ('thetha', 'lambda_pl', 'mu_pl', 'item size', 'Q', 'cl', 'cr',
                   'min_cost', 'zero_replica', 'max_replica', 'optimal replica')

start_str = start_time.strftime("%Y%m%d_%H%M%S")

for lambda_pl_idx in range(len(lambda_pl_lst)):
    lambda_pl = lambda_pl_lst[lambda_pl_idx]
    for mu_pl_idx in range(len(mu_pl_lst)):
        mu_pl = mu_pl_lst[mu_pl_idx]
        for cr_idx in range(len(cr_lst)):
            cr = cr_lst[cr_idx]

            env_str="_%s_%s_%s" % (lambda_pl_idx, mu_pl_idx, cr_idx)
            file_name = start_str+env_str+".csv"

            print(file_name)

            with open(file_name, "w", newline='') as f:
                dict_writer = csv.DictWriter(f, result_keys)
                dict_writer.writeheader()

                for item_size in item_size_lst:
                    optimal_lst = None
                    zero_cost = None
                    zero_lst = [0 for _ in range(item_size)]

                    min_cost = sys.maxsize
                    max_cost = None
                    max_b = None
                    u_b = None
                    hit = None

                    c_func = Func()
                    c_func.init(item_size, theta, lambda_pl, mu_pl, Q, cl, cr)   # parking lot option

                    max_lst = [int(c_func.E_V+20) for i in range(item_size)]
                    l_lst = [None]*item_size

                    for i in range(int(c_func.E_V) + 1):
                        l_lst = [i]*item_size  # set my strategy
                        cost = c_func.calculate_cost(l_lst)  # calculate strategy

                        if min_cost > cost:
                            min_cost = cost
                            optimal_lst = copy.deepcopy(l_lst)
                            max_b = c_func.max_b
                            u_b = c_func.E_B
                            hit = c_func.hit

                        if l_lst == zero_lst:
                            zero_cost = cost

                    max_cost = c_func.calculate_cost(max_lst)
                    print("expected vehicle: %s" % c_func.E_V)
                    print("using vehicle: %s" % u_b)
                    print("hit ratio: %s" % hit)
                    print("minimum cost: %s" % min_cost)
                    print("optimal: %s" % optimal_lst)
                    print("zero replica: %s" % zero_cost)
                    print("max replica: %s" % max_cost)
                    result = {
                                'thetha': theta, 'lambda_pl': lambda_pl, 'mu_pl': mu_pl,
                                'item size': item_size, 'Q': Q, 'cl': cl, 'cr': cr,
                                'min_cost': min_cost, 'zero_replica': zero_cost,
                                'max_replica': max_cost, 'optimal replica': optimal_lst[0]
                             }
                    dict_writer.writerow(result)

end_time = datetime.datetime.now()
delta = end_time-start_time

print("end time: %s" % end_time.strftime("%Y-%m-%d %p %I:%M:%S"))
print("time: %s" % str(delta))
