# def io/bound function
# def cpu_bound function

# timing function
import time
from functools import wraps
import sys


def cprint(statement, *, out: bool = False, end="\n") -> None:
    print(statement, file=sys.stderr if not out else sys.stdout, flush=True, end=end)


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        cprint(f"func: <{f.__name__}> took: {te-ts:0.2f} secs to finish")
        return result

    return wrap


def io_bound(n) -> None:
    # network operations
    # disk operation
    # any other resource related operation (except CPU)
    time.sleep(2)
    fpath = "/tmp/io_bound-0.txt"
    open(fpath, "w").close()  ## cleans the file
    print(f"I am about to start task number {n}", file=sys.stderr, flush=True)
    with open(fpath, "w") as handler:
        for i in range(10):
            handler.write("0" * (1 << 18))
            handler.flush()
    print(f"I finished task number {n}", file=sys.stderr, flush=True)


def cpu_bound(n: int) -> int:
    if n <= 2:
        return 1
    else:
        return cpu_bound(n - 1) + cpu_bound(n - 2)


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


@timing
def run():
    # io_bound()
    cpu_bound(n=38)


if __name__ == "__main__":
    run()
