import threading
import time
import math
from functools import wraps
import numpy as np

def c_bound_task_numpy():
    a = np.random.rand(1000, 1000)
    b = np.random.rand(1000, 1000)
    np.dot(a, b)


def python_bound_task():
    sum(x*x for x in range(10**6)) 


# def timeit(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = fn(*args, **kwargs)
#         print(f"{fn.__name__} took {time.time() - start:.2f}s")
#         return result
#     return wrapper


# def run_threads(count, fn, *args, **kwargs):
#     threads = []
#     for _ in range(count):
#         t = threading.Thread(target=fn, args=args, kwargs=kwargs)
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()


# @timeit
# def demo_numpy_threads(count: int):
#     run_threads(count, c_bound_task_numpy)

# @timeit
# def demo_python_threads(count: int):
#     run_threads(count, python_bound_task)


# if __name__ == "__main__":
#     count = 100
#     demo_numpy_threads(count)
#     demo_python_threads(count)

