class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
        def cross(p1, p2, p3):
            return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

        trees = sorted(trees, key=lambda x: (x[0], x[1]))
        if len(trees) <= 1:
            return trees

        lower = []
        for p in trees:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        upper = []
        for p in reversed(trees):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        return list({(p[0], p[1]): p for p in lower + upper}.values())