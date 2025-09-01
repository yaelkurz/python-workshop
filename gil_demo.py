import threading
import time


def run_threads(num_tasks, num_threads, fn):
    from queue import Queue

    q = Queue()
    for _ in range(num_tasks):
        q.put(None)

    def worker():
        while not q.empty():
            try:
                q.get_nowait()
            except:
                return
            fn()

    threads = []
    start = time.time()
    for _ in range(num_threads):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(
        f"{fn.__name__}: {num_tasks} tasks on {num_threads} threads took {time.time() - start:.2f}s"
    )


def cpu_bound_task():
    x = 0
    for i in range(2**25):
        x += i * i


if __name__ == "__main__":
    num_tasks = 5
    num_threads = 5
    run_threads(num_tasks, num_threads, cpu_bound_task)
