def solution(n, wires):
    result = n
    for i in range(len(wires)):
        cut_wires = wires[:i] + wires[i+1:]
        nodes = set(cut_wires[0])
        for _ in cut_wires:
            for wire in cut_wires:
                if wire[0] in nodes or wire[1] in nodes:
                    nodes.update(wire)
        result = min(result, abs(n - 2 * len(nodes)))
                
    return result
    