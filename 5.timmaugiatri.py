def find_satisfying_assignment(expression: str):
    """
    Tìm một tập giá trị cho các biến logic sao cho biểu thức mệnh đề là đúng.

    Args:
        expression (str): Biểu thức logic mệnh đề.

    Returns:
        dict: Một mẫu giá trị nếu tồn tại.
        str: Thông báo nếu không có mẫu giá trị nào.
    """
    from itertools import product

    # Lấy danh sách các biến trong biểu thức
    variables = sorted(set(filter(str.isalpha, expression)))

    # Tạo tất cả các tổ hợp giá trị True/False cho các biến
    truth_combinations = list(product([True, False], repeat=len(variables)))

    # Thay thế ký hiệu logic bằng các phép toán Python
    def replace_logic_symbols(expression):
        replacements = {
            '∧': ' and ',
            '∨': ' or ',
            '¬': ' not ',
            '→': ' <= ',  # A → B tương đương not A or B hoặc A <= B
            '↔': ' == '   # A ↔ B tương đương A == B
        }
        for symbol, replacement in replacements.items():
            expression = expression.replace(symbol, replacement)
        return expression

    expression = replace_logic_symbols(expression)

    # Tìm tổ hợp thỏa mãn biểu thức
    for combination in truth_combinations:
        assignment = dict(zip(variables, combination))
        try:
            if eval(expression, {}, assignment):
                return assignment
        except Exception as e:
            continue

    return "Không có mẫu giá trị nào thỏa mãn."

# Demo chương trình
if __name__ == "__main__":
    # Các kịch bản demo
    demo_expressions = [
        "(A ∨ B) ∧ (¬A ∨ C)",
        "A ∧ B ∨ ¬C",
        "(A → B) ∧ (¬B → C)",
        "¬A ∨ (B ↔ C)",
        "A ↔ (B ∨ ¬C)"
    ]

    for i, expression in enumerate(demo_expressions, start=1):
        print(f"\nDemo {i}: Biểu thức: {expression}")
        result = find_satisfying_assignment(expression)
        if isinstance(result, dict):
            print(f"Mẫu giá trị thỏa mãn: {result}")
        else:
            print(result)
