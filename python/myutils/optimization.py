import numpy as np
import pulp


def solve_int_ls_min_sum(A, b):
    """
    Solve the integer least squares problem min sum(x_j) subject to Ax = b,
    where A is a 2D array of shape (m, n) and b is a 1D array of shape (m,).
    :param A: 2D numpy array of shape (m, n)
    :param b: 1D numpy array of shape (m,)
    :return: 1D numpy array x of shape (n,) that minimizes sum(x_j)
    """
    m, n = A.shape

    # Define the problem: minimize sum(x_j)
    prob = pulp.LpProblem("Find_x", pulp.LpMinimize)

    # Create integer variables x_j >= 0
    x = [pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer") for j in range(n)]

    # Objective: minimize sum(x_j)
    prob += pulp.lpSum(x)

    # Constraints: for each row i, sum_j B[i, j] * x_j == A[i]
    for i in range(m):
        prob += pulp.lpSum(A[i, j] * x[j] for j in range(n)) == b[i]

    # Solve
    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    # Check status
    # print("Status:", pulp.LpStatus[prob.status])

    if pulp.LpStatus[prob.status] == "Optimal":
        x_sol = np.array([v.value() for v in x], dtype=float)
        return x_sol.sum()
    else:
        raise ValueError("No integer solution found")
