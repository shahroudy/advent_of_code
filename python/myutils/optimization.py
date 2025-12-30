from typing import List, Union

import numpy as np
import pulp
from myutils.geometry import Point, Point3D


def find_Nd_to_Nd_transformation(
    A: List[Union[Point, Point3D]], B: List[Union[Point, Point3D]]
) -> np.ndarray:
    """
    Find the best-fit linear transformation matrix X (4x3) such that AX = B
    using least squares.
    :param A: List of N points in source coordinate system
    :param B: List of N points in target coordinate system
    :return: Transformation matrix X as a numpy array of shape (n+1, n) where n is the dimension of
    each point
    """
    A = np.array([a.tuple + (1,) for a in A])
    B = np.array([b.tuple for b in B])
    X, residuals, rank, singular_values = np.linalg.lstsq(A, B, rcond=None)
    return X


def apply_transformation(
    input: Union[List[Union[Point, Point3D]], Point, Point3D], X: np.ndarray
) -> Union[List[Union[Point, Point3D]], Point, Point3D]:
    """
    Apply the transformation matrix X to the given point/points.
    """
    if isinstance(input, list):
        A = np.array([a.tuple + (1,) for a in input])
        B = A.dot(X)
        return [type(input[0])(*b) for b in B]
    else:
        A = np.array(input.tuple + (1,))
        B = A.dot(X)
        return type(input)(*B)


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
