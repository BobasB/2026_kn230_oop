#!/Users/administrator/.pyenv/shims/python

"""Простий консольний калькулятор."""

import ast
import operator


OPERATORS = {
	ast.Add: operator.add,
	ast.Sub: operator.sub,
	ast.Mult: operator.mul,
	ast.Div: operator.truediv,
	ast.Mod: operator.mod,
	ast.Pow: operator.pow,
	ast.USub: operator.neg,
	ast.UAdd: operator.pos,
}


def calculate(expression: str) -> int | float:
	"""Обчислює арифметичний вираз без виконання довільного коду."""
	try:
		tree = ast.parse(expression, mode="eval")
	except SyntaxError as error:
		raise ValueError("некоректний вираз") from error

	def evaluate(node: ast.AST) -> int | float:
		if isinstance(node, ast.Expression):
			return evaluate(node.body)
		if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
			return node.value
		if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
			left = evaluate(node.left)
			right = evaluate(node.right)
			return OPERATORS[type(node.op)](left, right)
		if isinstance(node, ast.UnaryOp) and type(node.op) in OPERATORS:
			return OPERATORS[type(node.op)](evaluate(node.operand))
		raise ValueError("дозволені лише числа та арифметичні операції")

	return evaluate(tree)


def main() -> None:
	print("Калькулятор")
	print("Операції: +, -, *, /, %, **")
	print("Введіть 'q', щоб завершити роботу.\n")

	while True:
		expression = input("Вираз: ").strip()
		if expression.lower() in {"q", "quit", "вихід"}:
			print("До побачення!")
			break
		if not expression:
			continue

		try:
			result = calculate(expression)
			print(f"Результат: {result}\n")
		except (ValueError, ZeroDivisionError, OverflowError) as error:
			print(f"Помилка: {error}\n")


if __name__ == "__main__":
	main()
