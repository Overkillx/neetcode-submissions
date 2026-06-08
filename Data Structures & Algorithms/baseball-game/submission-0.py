class Solution:
    def calPoints(self, operations: List[str]) -> int:
        op = 0
        ops = []

        for i in range(len(operations)):
            if operations[i].lstrip("-").isdigit():
                ops.append(int(operations[i]))

            elif operations[i] == "+":
                op = ops[-1] + ops[-2]
                ops.append(op)

            elif operations[i] == "D":
                op = ops[-1] * 2
                ops.append(op)

            elif operations[i] == "C":
                ops.pop()

        return sum(ops)



        