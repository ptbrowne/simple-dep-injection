from collections import defaultdict


def reverse_graph(g):
    g2 = defaultdict(lambda: set())
    for k, v in g.iteritems():
        g2[k]
        for t in v:
            g2[t].add(k)
    return {k: set(v) for k, v in g2.iteritems()}


def iter_sinks(g):
    for k, v in g.iteritems():
        if not len(v):
            yield k
        for n in v:
            if n not in g:
                yield n


def sinks(g):
    return list(iter_sinks(g))


def iter_topsort(g):
    rg = reverse_graph(g)
    q = sinks(rg)  # g's sources
    already = set()

    # invariant, at any point in the algorithm
    # nodes in the queue are sources in reverse_graph(rg)
    while len(q) > 0:
        n = q.pop()
        already.add(n)  # mark as seen
        children = g.get(n, [])
        for child in children:
            # remove the edge from reverse graph
            rg[child].remove(n)

            # insert in queue if the node is now a source
            if len(rg[child]) == 0 and child not in already:
                q.insert(0, child)
        yield n


def topsort(g):
    return list(iter_topsort(g))
