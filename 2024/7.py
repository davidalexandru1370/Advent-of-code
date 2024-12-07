def solve_part1() -> int:
    with open("inputs/7.txt", "r") as file:
        lines = file.readlines()
        count = 0
        operators = ["+", "*"]
        for line in lines:
            words = line.split(":")
            result = int(words[0].strip())
            numbers = [int(x.strip()) for x in words[1].split(" ") if x != ""]
            len_operators = len(numbers) - 1
            for i in range(1 << len_operators):
                expression = ""
                expression_result: int = numbers[0]
                for j in range(1, len_operators + 1):
                    pos = j - 1
                    expression_result = eval(str(expression_result) + operators[(i >> pos) & 1] + str(numbers[j]))
                # expression += str(numbers[-1])
                if expression_result == result:
                    print(expression_result)
                    count += result
                    break
    return count


def custom_eval(left_hand_side: int, operator: str, right_hand_side: int) -> int:
    if operator == "+":
        return left_hand_side + right_hand_side
    elif operator == "*":
        return left_hand_side * right_hand_side
    elif operator == "||":
        return int(str(left_hand_side) + str(right_hand_side))

    return 0


def solve_part2() -> int:
    with open("inputs/7.txt", "r") as file:
        lines = file.readlines()
        count = 0
        operators = ["+", "*", "||"]
        for line in lines:
            words = line.split(":")
            result = int(words[0].strip())
            numbers = [int(x.strip()) for x in words[1].split(" ") if x != ""]
            len_operators = len(operators)

            def dfs(index: int, current_result: int) -> bool:
                nonlocal count
                if index >= len(numbers):
                    if current_result == result:
                        count += current_result
                        return True
                    return False

                found: bool = False

                for operator_index in range(len_operators):
                    found: bool = dfs(index + 1, custom_eval(current_result, operators[operator_index], numbers[index]))
                    if found == True:
                        break

                return found

            dfs(1, numbers[0])
    return count


if __name__ == "__main__":
    # print(solve_part1())
    print(solve_part2())
