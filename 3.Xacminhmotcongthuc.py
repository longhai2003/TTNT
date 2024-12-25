def evaluate_predicate_logic(expression: str, domain: set, predicates: dict) -> bool:
    """
    Kiểm tra tính đúng/sai của một công thức logic vị từ.

    Args:
        expression (str): Công thức logic vị từ.
        domain (set): Miền giá trị của các biến.
        predicates (dict): Định nghĩa của các vị từ.

    Returns:
        bool: True nếu công thức đúng, False nếu sai.
    """
    # Thay thế các ký hiệu logic bằng các phép toán Python
    replacements = {
        '∧': ' and ',
        '∨': ' or ',
        '¬': ' not ',
        '→': ' <= ',  # A → B tương đương not A or B hoặc A <= B
        '↔': ' == '   # A ↔ B tương đương A == B
    }
    for symbol, replacement in replacements.items():
        expression = expression.replace(symbol, replacement)

    # Hàm thay thế các lượng từ ∀ và ∃
    def replace_quantifiers(expr):
        if '∀' in expr:
            variable = expr[expr.index('∀') + 1]
            inner = expr[expr.index('(') + 1:expr.rindex(')')]
            return f"all({inner} for {variable} in domain)"
        elif '∃' in expr:
            variable = expr[expr.index('∃') + 1]
            inner = expr[expr.index('(') + 1:expr.rindex(')')]
            return f"any({inner} for {variable} in domain)"
        return expr

    expression = replace_quantifiers(expression)

    # Thay thế vị từ bằng định nghĩa tương ứng
    for predicate, func in predicates.items():
        expression = expression.replace(predicate, func)

    # Đánh giá biểu thức
    try:
        return eval(expression)
    except Exception as e:
        raise ValueError(f"Lỗi khi đánh giá công thức: {e}")

# Demo chương trình
if __name__ == "__main__":
    # Các kịch bản demo
    demo_scenarios = [
        {
            "expression": "∀x (P(x) → Q(x)) ∧ ∃y P(y)",
            "domain": {1, 2, 3},
            "predicates": {
                "P(x)": "x > 1",
                "Q(x)": "x % 2 == 0"
            }
        },
        {
            "expression": "∀x (P(x) ∨ ¬Q(x))",
            "domain": {0, 1, 2},
            "predicates": {
                "P(x)": "x >= 1",
                "Q(x)": "x % 2 == 1"
            }
        },
        {
            "expression": "∃x (P(x) ∧ Q(x))",
            "domain": {10, 15, 20},
            "predicates": {
                "P(x)": "x > 10",
                "Q(x)": "x < 20"
            }
        },
        {
            "expression": "∀x (¬P(x) ∨ Q(x))",
            "domain": {5, 10, 15},
            "predicates": {
                "P(x)": "x % 5 == 0",
                "Q(x)": "x > 8"
            }
        },
        {
            "expression": "∃x (P(x) ↔ Q(x))",
            "domain": {2, 4, 6},
            "predicates": {
                "P(x)": "x % 2 == 0",
                "Q(x)": "x > 3"
            }
        }
    ]

    for i, scenario in enumerate(demo_scenarios, start=1):
        print(f"\nDemo {i}: Biểu thức: {scenario['expression']}")
        try:
            result = evaluate_predicate_logic(
                scenario['expression'],
                scenario['domain'],
                scenario['predicates']
            )
            print(f"Kết quả: {'Đúng' if result else 'Sai'}")
        except ValueError as e:
            print(e)

