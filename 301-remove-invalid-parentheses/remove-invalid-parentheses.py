
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string):
            count = 0

            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1

                if count < 0:
                    return False

            return count == 0

        queue = [s]
        visited = {s}
        result = []
        found = False

        while queue:
            current = queue.pop(0)

            if is_valid(current):
                result.append(current)
                found = True

            if found:
                continue

            for i in range(len(current)):
                if current[i] not in '()':
                    continue

                new_string = current[:i] + current[i + 1:]

                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(new_string)

        return result
