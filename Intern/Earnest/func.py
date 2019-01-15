import math
import numpy as np
from scipy import special


class Func:
    def __init__(self):
        self.item_size = None
        self.theta = None
        self.Q = None
        self.lambda_pl = None
        self.mu_pl = None
        self.cl = None
        self.cr = None

        self.L = None
        self.R = None
        self.omega_v = None

        self.lambda_i_lst = None
        self.lambda_wq = None
        self.lambda_wq_ratios = None
        self.pi_wq_lst = None
        self.p_iq_empty_lst = None
        self.H_lst = None

        self.hit = None
        self.E_V = None
        self.E_B = None
        self.E_A = None
        self.pi_b = None

        self.vehicle_limit = int(1e4)
        self.loop_limit = int(1e4)

    def init(self, item_size, theta, lambda_pl, mu_pl, q, cl, cr):
        self.item_size = item_size
        self.theta = theta
        self.lambda_pl = lambda_pl
        self.mu_pl = mu_pl
        self.Q = q
        self.cl = cl
        self.cr = cr

        self.E_V = lambda_pl / mu_pl

        self.vehicle_limit = int(max(self.E_V * 2, self.item_size + 1))

        self.set_r()

    def set_r(self):
        self.omega_v = omega_v = self.omega(self.item_size, self.theta)
        self.R = [(omega_v/pow(i, self.theta)) for i in range(1, self.item_size + 1)]
        self.lambda_i_lst = self.lambda_pl * np.array(self.R)

    def set_l(self, l_lst):
        self.L = l_lst
        self.lambda_wq = None
        self.lambda_wq_ratios = None
        self.max_b = None
        self.calculate_lambda_wq()
        self.calculate_pi_wq_lst()
        self.calculate_iq_empty()
        self.calculate_H()
        self.calculate_pi_b()

    def calculate_lambda_wq(self):
        self.lambda_wq_ratios = np.array([self.lambda_i_lst[i] * self.B(self.lambda_i_lst[i] / self.mu_pl, self.L[i])
                                          for i in range(self.item_size)])
        self.lambda_wq = self.lambda_wq_ratios.sum()
        self.lambda_wq_ratios = self.lambda_wq_ratios / self.lambda_wq

    def calculate_pi_wq_lst(self):
        rho = self.lambda_wq / self.mu_pl
        self.pi_wq_lst = [None] * self.vehicle_limit
        value = math.exp(-rho)
        self.pi_wq_lst[0] = value
        for i in range(1, self.vehicle_limit):
            value *= (rho/i)
            self.pi_wq_lst[i] = value

    def get_pi_wq(self, n):
        if self.pi_wq_lst is None:
            self.calculate_pi_wq_lst()

        if n < self.vehicle_limit:
            return self.pi_wq_lst[n]

        else:
            return 0

    def calculate_iq_empty(self):
        self.p_iq_empty_lst = [0] * self.item_size
        for i in range(self.item_size):
            rho = self.lambda_i_lst[i] / self.mu_pl
            result_inv = 1
            value = 1

            for j in range(1, self.L[i] + 1):
                value *= rho/j
                result_inv += value

            self.p_iq_empty_lst[i] = 1 / result_inv

    def get_p_i_not_in_a(self, i, b):
        if self.p_iq_empty_lst is None:
            self.calculate_iq_empty()

        return self.p_iq_empty_lst[i] * self.get_i_not_in_a_wq(i, b)

    def get_i_not_in_a_wq(self, i, b):
        result = 0
        c_r = (1 - self.lambda_wq_ratios[i])
        exp_v = 1
        for j in range(b, self.vehicle_limit):
            result += self.get_pi_wq(j) * exp_v
            exp_v *= c_r

        return result

    def calculate_H(self):
        self.H_lst = np.zeros(self.vehicle_limit)
        self.E_A = 0

        for i in range(self.item_size):
            for j in range(self.item_size):
                not_a = self.get_p_i_not_in_a(j, i)
                self.H_lst[i] += self.R[j] * (1 - not_a * (1 - min(i / self.item_size, 1)))
                self.E_A += self.R[j]*(1 - not_a)

        for i in range(self.item_size, len(self.H_lst)):
                self.H_lst[i] = 1.0

    def get_H(self, x):
        if self.H_lst is None:
            self.calculate_H()

        if x < self.vehicle_limit:
            return self.H_lst[x]

        else:
            return 1.0

    def calculate_pi_b(self):
        # pi_b[waiting queue size][n]
        self.pi_b = [None] * self.vehicle_limit
        for i in range(self.vehicle_limit):
            self.pi_b[i] = np.zeros(i+1)
            ex_value = 1
            self.pi_b[i][0] = ex_value
            for j in range(1, i+1):
                if j > self.item_size:
                    self.pi_b[i][j] = 0.0
                    break
                else:
                    ex_value *= self.Q * (1 - self.get_H(j-1)) / (j *self.mu_pl)
                    self.pi_b[i][j] = ex_value

            sum_v = self.pi_b[i].sum()
            self.pi_b[i] = self.pi_b[i]/sum_v

    def get_pi_b(self, n):
        result = 0
        for i in range(n, self.vehicle_limit):
            result += self.get_pi_wq(i)*self.pi_b[i][n]

        return result

    def calculate_hit(self, l_lst):
        self.set_l(l_lst)
        self.hit = 0
        self.E_B = 0

        for i in range(min(self.vehicle_limit, self.item_size + 1)):
            b = self.get_pi_b(i)
            self.E_B += b * i
            self.hit += b * self.get_H(i)


    def calculate_cost(self, l_lst):
        self.calculate_hit(l_lst)

        cost = self.Q*(self.cl*self.hit + self.cr*(1-self.hit))
        cost += self.E_B / self.E_V * self.mu_pl * self.E_A
        return cost


    @staticmethod
    def B(a, b):
        invB = 1.0


        for i in range(1, b + 1):
            try:
                invB = 1 + invB * i / a
            except Warning as e:
                print(e)
                print(invB)
                print(i)
                print(a)
                return 0.0
        return 1 / invB



    @staticmethod
    def omega(item_size, theta):
        result = 0
        for i in range(1, item_size + 1):
            result += pow(1 / i, theta)

        return 1/result