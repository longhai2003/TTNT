def prove_propositional_logic(premises: list, conclusion: str) -> bool:
    """
    Chứng minh một phát biểu trong logic mệnh đề sử dụng bảng chân trị.

    Args:
        premises (list): Tập các mệnh đề.
        conclusion (str): Kết luận cần chứng minh.

    Returns:
        bool: True nếu kết luận đúng, False nếu sai.
    """
    from itertools import product

    # Lấy danh sách các biến trong tập mệnh đề và kết luận
    all_statements = premises + [conclusion]
    variables = sorted(set(filter(str.isalpha, "".join(all_statements))))

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

    premises = [replace_logic_symbols(p) for p in premises]
    conclusion = replace_logic_symbols(conclusion)

    # Kiểm tra tính hợp lệ
    for combination in truth_combinations:
        assignment = dict(zip(variables, combination))

        # Đánh giá các mệnh đề và kết luận
        premise_results = [eval(p, {}, assignment) for p in premises]
        conclusion_result = eval(conclusion, {}, assignment)

        # Nếu tất cả mệnh đề đúng nhưng kết luận sai, thì không hợp lệ
        if all(premise_results) and not conclusion_result:
            return False

    return True

# Demo chương trình
if __name__ == "__main__":
    # Các kịch bản demo
    demo_scenarios = [
        {
            "premises": ["P → Q", "Q → R"],
            "conclusion": "P → R"
        },
        {
            "premises": ["P ∨ Q", "¬P"],
            "conclusion": "Q"
        },
        {
            "premises": ["P ∧ Q", "Q → R"],
            "conclusion": "P ∧ R"
        },
        {
            "premises": ["P → (Q ∨ R)", "¬Q"],
            "conclusion": "P → R"
        },
        {
            "premises": ["¬P ∨ Q", "¬Q"],
            "conclusion": "¬P"
        }
    ]

    for i, scenario in enumerate(demo_scenarios, start=1):
        print(f"\nDemo {i}: Premises: {scenario['premises']}, Conclusion: {scenario['conclusion']}")
        result = prove_propositional_logic(scenario['premises'], scenario['conclusion'])
        print(f"Kết quả: {'Đúng' if result else 'Sai'}")
