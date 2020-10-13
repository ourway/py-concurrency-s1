from functions import io_bound, timing, chunks
from threading import Thread

# concurent.futures


def run_sync():
    for i in range(10):
        io_bound(n=i)


def run_async():
    # run this func in threading mode

    # 1- create the thread
    # 2- start the thread
    # 3- wait for it to finish

    tasks = []
    for each in chunks(range(1000), 8):
        for i in each:
            t = Thread(target=io_bound, args=(i,))
            t.start()
            tasks.append(t)

        for every in tasks:
            every.join()


@timing
def run():
    # run_sync()
    run_async()


if __name__ == "__main__":
    run()
