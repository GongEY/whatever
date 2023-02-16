import json
from func import Func
import sys
import copy
import datetime
import math
from datetime import timedelta

start_time = datetime.datetime.now()
print("start time: %s" % start_time.strftime("%Y-%m-%d %p %I:%M:%S"))

lambda_pl = 1/10
mu_pl = 1/650
Q = 1
theta = 0.7
item_size = 10
cl = 1
cr = 100

optimal_lst = None
zero_cost = None
zero_lst = [0 for _ in range(item_size)]

min_cost = sys.maxsize
max_cost = None
max_b = None

c_func = Func()
c_func.init(item_size, theta, lambda_pl, mu_pl, Q, cl, cr)

max_lst = [math.ceil(c_func.E_V * c_func.R[i]) for i in range(item_size)]
l_lst = [None]*item_size

for i in range(int(c_func.E_V) + 1):
    l_lst = [i]*item_size
    cost = c_func.calculate_cost(l_lst)

    if min_cost > cost:
        min_cost = cost
        optimal_lst = copy.deepcopy(l_lst)
        max_b = c_func.max_b

    if l_lst == zero_lst:
        zero_cost = cost


max_cost = c_func.calculate_cost(max_lst)

end_time = datetime.datetime.now()
delta = end_time-start_time

print("end time: %s" % end_time.strftime("%Y-%m-%d %p %I:%M:%S"))
print("time: %s" % str(delta))

print("expected vehicle: %s\n" % c_func.E_V)
print("minimum cost: %s\n" % min_cost)
print("optimal: %s\n" % optimal_lst)
print("zero replica: %s\n" % zero_cost)
print("max replica: %s\n" % max_cost)