from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def DoLinkedListsIntersect(linked_lists, toFind):
    def build_graph(linked_lists):
        graph = defaultdict(list)
        for ll in linked_lists:
            nodes = ll.split("->")
            graph[nodes[0]].append(nodes[1])
        return graph

    def bfs(start_node, target):
        queue = [start_node]
        visited = set()

        while queue:
            current_node = queue.pop(0)
            if current_node == target:
                return True
            visited.add(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)

        return False

    def has_cycle_dfs(node, visited, recursion_stack):
        visited.add(node)
        recursion_stack.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if has_cycle_dfs(neighbor, visited, recursion_stack):
                    return True
            elif neighbor in recursion_stack:
                return True

        recursion_stack.remove(node)
        return False

    graph = build_graph(linked_lists)

    results = []
    for ll in toFind:
        start_nodes = ll.split(',')
        has_intersection = False

        # Check if there is a cycle in the graph
        for node in graph:
            if node not in set():
                if has_cycle_dfs(node, set(), set()):
                    results.append("Error Thrown! Cycle detected!")
                    break

        # If no cycle found, check for intersection
        else:
            for i in range(len(start_nodes) - 1):
                if bfs(start_nodes[i], start_nodes[i+1]):
                    has_intersection = True
                    break
            results.append(has_intersection)

    return results


# Example usage:
linked_lists = ["a->b", "r->s", "b->c", "x->c", "q->r", "y->x", "w->z"]
to_find = ["a,q,w", "a,c,r", "y,z,a,r", "a,w", "w,a"]

results = DoLinkedListsIntersect(linked_lists, to_find)
for res in results:
    print(res)
