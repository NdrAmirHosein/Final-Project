from app.data_structures.stack import Stack

def calculateSpan(drivers):
    n = len(drivers)
    span = [1] * n
    stk = Stack(1000)

    for i in range(n - 1, -1, -1):
        while not len(stk) == 0 and drivers[stk.top].neg_scores >= drivers[i].neg_scores:
            span[i] += span[stk.pop()]
        stk.push(i)

    return span
