from collections import deque


class Stacks:
    def __init__(self):
        self.cont = deque()

    def push(self, val):
        self.cont.append(val)

    def pop(self):
        return self.cont.pop()

    def is_empty(self):
        return len(self.cont) == 0

    def top(self):
        return self.cont[-1]

    def lent(self):
        return len(self.cont)


def balanp(string):
    bracketo = ["[", "{", "("]
    bracketc = ["]", "}", ")"]

    def isrev(bracket):
        if bracket == "[":
            return "]"
        if bracket == "{":
            return "}"
        if bracket == "(":
            return ")"
        if bracket == "]":
            return "["
        if bracket == "}":
            return "{"
        if bracket == ")":
            return "("

    s = Stacks()

    for i in range(len(string)):
        if string[i] in bracketo or string[i] in bracketc:

            if string[i] in bracketo:
                s.push(string[i])

            if string[i] in bracketc:
                if s.lent() == 0:
                    s.push(string[i])

                if s.top() == isrev(string[i]):
                    s.pop()

                else:
                    print("Not Balanced")
                    return

    if s.lent() == 0:
        print("Balanced")
        return

    print("Not Balanced")
    return


balanp("(})")
