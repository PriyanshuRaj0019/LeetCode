class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)
        idx = 0

        def parse_expr() -> set[str]:
            nonlocal idx
            union_set = set()
            while idx < n and expression[idx] != '}':
                union_set |= parse_term()
                if idx < n and expression[idx] == ',':
                    idx += 1  # consume ','
            return union_set

        def parse_term() -> set[str]:
            nonlocal idx
            curr_set = {""}
            while idx < n and expression[idx] not in {',', '}'}:
                if expression[idx] == '{':
                    idx += 1  # consume '{'
                    sub_set = parse_expr()
                    idx += 1  # consume '}'
                    curr_set = {a + b for a in curr_set for b in sub_set}
                else:
                    ch = expression[idx]
                    idx += 1
                    curr_set = {a + ch for a in curr_set}
            return curr_set

        return sorted(parse_expr())