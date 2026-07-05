"""0853: リロード順序とトポロジカルソートのリファレンス実装。"""

import heapq


def reload_order(deps: dict[str, list[str]]) -> list[str]:
    """依存されるモジュールが先に来るリロード順序を返す。

    次に選べるモジュールが複数あるときは名前が辞書式順序で最小のものを選ぶ。
    依存関係に閉路があれば ValueError を送出する。
    """
    modules = set(deps)
    for required in deps.values():
        modules.update(required)

    dependents: dict[str, list[str]] = {module: [] for module in modules}
    indegree: dict[str, int] = dict.fromkeys(modules, 0)
    for module, required in deps.items():
        for dep in set(required):
            dependents[dep].append(module)
            indegree[module] += 1

    ready = [module for module in modules if indegree[module] == 0]
    heapq.heapify(ready)
    order: list[str] = []
    while ready:
        module = heapq.heappop(ready)
        order.append(module)
        for dependent in dependents[module]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                heapq.heappush(ready, dependent)

    if len(order) < len(modules):
        raise ValueError("dependency cycle detected")
    return order
