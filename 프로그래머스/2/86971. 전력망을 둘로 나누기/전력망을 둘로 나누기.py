def solution(n, wires):
    result = n
    for i in range(len(wires)):
        cut_wires = wires[:i] + wires[i+1:]
        nodes = set(cut_wires[0])
        for _ in cut_wires:
            for cw in cut_wires:
                cw = set(cw)
                if nodes & cw:
                    nodes.update(cw)
        result = min(result, abs(n - 2 * len(nodes)))
    return result
                