"""
tool to put bugs in your code!
"""
import argparse

from random import random, choice
import cPickle
import string

def enbug_data(data, num_iter=1):
    try:
        errors = cPickle.load(file("errors.pickle"))
    except:
        errors = []

    N = len(data)
    for iter in range(num_iter):
        while True:
            i = int(random() * N)
            old = data[i - 1:i + 2]
            if old == "   ":
                continue
            break

        new = choice(string.printable)

        before = data[:i]
        lineno = before.count("\n")
        if lineno == 0:
            cols = i
        else:
            last_line_end = before.rindex("\n")
            cols = i - last_line_end

        errors.append([i, lineno, cols, old, new])
        data = data[:i] + new + data[i + 1:]

    cPickle.dump(errors, file("errors.pickle", "wb"))
    return data


def enbug(filename, num):
    data = file(filename).read()
    data = enbug_data(data, num)
    file(filename, "wb").write(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Put bugs in your code!')
    parser.add_argument('-n', default=100,
                        help="number of bugs per file")
    parser.add_argument('targets', metavar='F', type=str, nargs='+',
                        help='target files to enbug')

    args = parser.parse_args()
    for f in args.targets:
        enbug(f, args.n)
