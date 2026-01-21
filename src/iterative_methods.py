# -*- coding: utf-8 -*-

"""
Python 3
19 / 07 / 2024
@author: z_tjona
"""

import logging
import os
from sys import stdout
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

logging.basicConfig(
    level=logging.INFO,
    format=f"[%(asctime)s][%(levelname)s][{os.environ.get('USERNAME')}] %(message)s",
    stream=stdout,
    datefmt="%m-%d %H:%M:%S",
)
logging.info(datetime.now())


def gauss_jacobi(
    *, A: np.ndarray, b: np.ndarray, x: np.ndarray, tol: float, max_iter: int
) -> np.ndarray:
    if not isinstance(A, np.ndarray):
        logging.debug("Convirtiendo A a numpy array.")
        A = np.array(A, dtype=float)
    assert A.shape[0] == A.shape[1], "La matriz A debe ser de tamaño n-by-(n)."

    if not isinstance(b, np.ndarray):
        logging.debug("Convirtiendo b a numpy array.")
        b = np.array(b, dtype=float)
    assert b.shape[0] == A.shape[0], "El vector b debe ser de tamaño n."

    if not isinstance(x, np.ndarray):
        x = np.array(x, dtype=float, ndmin=2).T
    assert x.shape[0] == A.shape[0], "El vector x0 debe ser de tamaño n."

    n = A.shape[0]
    history = [x.flatten()]

    logging.info(f"i= {0} x: {x.T}")
    for k in range(1, max_iter + 1):
        x_new = np.zeros((n, 1))
        for i in range(n):
            suma = sum([A[i, j] * x[j] for j in range(n) if j != i])
            x_new[i] = (b[i] - suma) / A[i, i]

        history.append(x_new.flatten())

        if np.linalg.norm(x_new - x) < tol:
            return np.array(history)
        x = x_new.copy()

    logging.info(f"i= {k} x: {x_new.T}")
    return np.array(history)


def gauss_seidel(
    *, A: np.ndarray, b: np.ndarray, x: np.ndarray, tol: float, max_iter: int
) -> np.ndarray:
    if not isinstance(A, np.ndarray):
        logging.debug("Convirtiendo A a numpy array.")
        A = np.array(A, dtype=float)
    assert A.shape[0] == A.shape[1], "La matriz A debe ser de tamaño n-by-(n)."

    if not isinstance(b, np.ndarray):
        logging.debug("Convirtiendo b a numpy array.")
        b = np.array(b, dtype=float)
    assert b.shape[0] == A.shape[0], "El vector b debe ser de tamaño n."

    if not isinstance(x, np.ndarray):
        x = np.array(x, dtype=float, ndmin=2).T
    assert x.shape[0] == A.shape[0], "El vector x0 debe ser de tamaño n."

    n = A.shape[0]
    history = [x.flatten()]

    logging.info(f"i= {0} x: {x.T}")
    for k in range(1, max_iter + 1):
        x_new = np.zeros((n, 1))
        for i in range(n):
            suma = sum([A[i, j] * x_new[j] for j in range(i) if j != i]) + sum(
                [A[i, j] * x[j] for j in range(i, n) if j != i]
            )
            x_new[i] = (b[i] - suma) / A[i, i]

        history.append(x_new.flatten())

        if np.linalg.norm(x_new - x) < tol:
            return np.array(history)

        x = x_new.copy()
        logging.info(f"i= {k} x: {x.T}")

    return np.array(history)


def plot_trajectory_2d(histories, labels, title, real_solution=None):
    plt.figure(figsize=(8, 6))
    markers = ['o-', 's-', '^-']
    
    for i, (hist, label) in enumerate(zip(histories, labels)):
        plt.plot(hist[:, 0], hist[:, 1], markers[i % len(markers)], label=label, alpha=0.7, markersize=4)
        plt.plot(hist[0, 0], hist[0, 1], 'go', markersize=8, label='Inicio' if i==0 else "")
        plt.plot(hist[-1, 0], hist[-1, 1], 'rx', markersize=8, label='Fin iteración' if i==0 else "")

    if real_solution is not None:
        plt.plot(real_solution[0], real_solution[1], 'k*', markersize=12, label='Solución Exacta')

    plt.title(title)
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.show()