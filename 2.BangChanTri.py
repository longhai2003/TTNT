from itertools import product

def generate_truth_table(expression: str):
    """
    Tạo bảng chân trị cho một biểu thức logic mệnh đề.
    """
    # Lấy danh sách các biến trong biểu thức
    variables = sorted(set(filter(str.isalpha, expression)))

    # Thay thế ký hiệu logic bằng các phép toán Python
    replacements = {
        '∧': ' and ',
        '∨': ' or ',
        '¬': ' not ',
        '→': ' or not ',  # A → B tương đương not A or B
        '↔': ' == '       # A ↔ B tương đương A == B
    }
    for symbol, replacement in replacements.items():
        expression = expression.replace(symbol, replacement)

    # Tạo tất cả các tổ hợp giá trị True/False
    truth_combinations = list(product([True, False], repeat=len(variables)))

    # Tạo bảng chân trị
    print(" ".join(variables) + " | Kết quả")
    print("-" * (len(variables) * 2 + 10))
    for combination in truth_combinations:
        values = dict(zip(variables, combination))
        # Thay thế các biến bằng giá trị True/False
        eval_expression = expression
        for var, val in values.items():
            eval_expression = eval_expression.replace(var, str(val))

        try:
            result = eval(eval_expression)
        except Exception as e:
            result = f"Error: {e}"

        # In dòng trong bảng chân trị
        row = " ".join("T" if val else "F" for val in combination)
        print(f"{row} | {'T' if result else 'F'}")

# Demo chương trình
if __name__ == "__main__":
    demo_expressions = [
        "(A ∨ ¬B) ∧ C",
        "A ∧ B ∨ ¬C",
        "A → (B ∧ C)",
        "(A ↔ B) ∨ ¬C",
        "¬(A ∨ B) ∧ C"
    ]

    for i, expression in enumerate(demo_expressions, start=1):
        print(f"\nDemo {i}: Biểu thức: {expression}")
        generate_truth_table(expression)
