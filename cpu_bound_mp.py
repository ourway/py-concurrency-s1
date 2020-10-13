from functions import cpu_bound, timing
from multiprocessing import Process, cpu_count
from multiprocessing import Pool


def run_sync():
    for i in [38] * 2:
        cpu_bound(i)


def run_mp():
    # create the process
    # start it
    # wait for it
    jobs = []
    for i in range(cpu_count()):
        p = Process(target=cpu_bound, args=(38,))
        p.start()
        jobs.append(p)

    for each in jobs:
        each.join()


def run_mp2():
    promises = []
    final = []
    with Pool(cpu_count() // 2) as handler:
        for i in [38] * 12:
            r = handler.apply_async(cpu_bound, [i])
            promises.append(r)
        for r in promises:
            final.append(r.get())

    print(final, flush=True)


@timing
def run():
    # run_sync()

    run_mp2()


if __name__ == "__main__":
    run()
