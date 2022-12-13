import numpy as np
import time
import cvxpy as cp
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import approximation as approx
import itertools as it


def solve_linear_equation_comapre_np_cp():
    np.random.seed(1)
    numpy_time = []
    cvxpy_time = []
    num_of_variables = [25,50,75,100,125,150,175,200,225,250,275,300,325,350,375,400]#,425,450,475,500]
    for a in num_of_variables:
        print(a)
        mat = 10 * np.random.randn(a, a)
        sol = 10 * np.random.randn(a)
        t1 = time.time()
        solution = np.linalg.solve(mat, sol)
        numpy_time.append(time.time() - t1)

        x = cp.Variable(a)
        constraints = [mat @ x == sol]
        obj = cp.Minimize(cp.log_sum_exp(x))
        prob = cp.Problem(obj, constraints)
        t1 = time.time()
        prob.solve()
        cvxpy_time.append(time.time() - t1)
    plt.plot
    plt.plot(num_of_variables, numpy_time, label='numpy solving time')
    plt.plot(num_of_variables, cvxpy_time, label='cvxpy solving time')
    plt.legend()
    plt.show()

# From class example
draw_options = {
    "font_size": 10,
    "node_size": 700,
    "node_color": "yellow",
    "edgecolors": "black",
    "linewidths": 1,
    "width": 1,
    "with_labels": True
}

def exact_maximum_independent_set(G):
    set = []
    for l in range(1, G.number_of_nodes()+1):
        for t in it.combinations(G.nodes,l):
            is_independent = True
            for n in t:
                for k in G.adj[n].keys():
                    if k in t:
                        is_independent = False
                        break
            if is_independent:
                set = t
                break
    return set

def check_independent_set_approx():
    probabilities = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    number_of_nodes = [5,6,8,10,12,13,15,17,18,20]
    approximations_with_different_prob = []

    for p in probabilities:
        approximations = []
        for n in number_of_nodes:
            approx_for_probability = []
            for i in range(5):
                G = nx.gnp_random_graph(n,p,directed=False)
                num_is = len(exact_maximum_independent_set(G))
                num_approx = len(approx.maximum_independent_set(G))
                approx_for_probability.append(num_approx/num_is)
            approximations.append((sum(approx_for_probability))/5)
            print(approximations)
        print(p)
        plt.plot(number_of_nodes, approximations)
        # plt.legend()
        plt.show()
        approximations_with_different_prob.append(approximations)
    print(sum(approximations_with_different_prob)/len(approximations_with_different_prob))





if __name__ == "__main__":

    solve_linear_equation_comapre_np_cp()

    check_independent_set_approx()





