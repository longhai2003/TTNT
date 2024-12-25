import re
from typing import Dict
"""
1.Hàm "is_valid_expression" kiểm tra tính hợp lệ của biểu thức:

Xác định xem biểu thức chỉ chứa các ký tự hợp lệ (chữ cái in hoa, ngoặc (), và các phép toán ∧, ∨, ¬, →, ↔).
Kiểm tra sự cân bằng của ngoặc mở ( và ngoặc đóng ).

2. Hàm tính "evaluate_expression" giá trị biểu thức logic:

Thay các ký hiệu logic (∧, ∨, ¬, →, ↔) bằng toán tử Python (and, or, not,...).
Thay các biến trong biểu thức bằng giá trị Boolean (True/False) từ một từ điển đầu vào.
Dùng eval() để tính giá trị của biểu thức.

3.Chương trình chính:
Kiểm tra một số biểu thức mẫu với giá trị các biến cụ thể.
In kết quả:
Nếu biểu thức hợp lệ, tính toán và hiển thị kết quả.
Nếu không hợp lệ, báo lỗi.
Mục tiêu: Kiểm tra và đánh giá biểu thức logic một cách tự động, dễ hiểu và có thể mở rộng
"""

def is_valid_expression(expression: str) -> bool:
    """
    Kiểm tra xem biểu thức logic có hợp lệ hay không.
    """
    # Mẫu regex kiểm tra biểu thức logic cơ bản
    valid_tokens = re.compile(r'^[A-Z()\s∧∨¬→↔]*$')
    
    # Kiểm tra ký tự không hợp lệ
    if not valid_tokens.match(expression):
        return False

    # Kiểm tra số ngoặc mở và đóng có cân bằng không
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

def evaluate_expression(expression: str, values: Dict[str, bool]) -> bool:
    """
    Tính giá trị của biểu thức logic với các giá trị biến đầu vào.
    """
    # Thay thế các ký hiệu logic bằng các phép toán Python
    expression = expression.replace('∧', ' and ')
    expression = expression.replace('∨', ' or ')
    expression = expression.replace('¬', ' not ')
    expression = expression.replace('→', ' or not ')  # Thay thế A → B thành (not A or B)
    expression = expression.replace('↔', ' == ')  # Thay thế A ↔ B thành (A == B)

    # Thay thế các biến bằng giá trị True/False
    for var, val in values.items():
        expression = expression.replace(var, str(val))

    # Tính toán biểu thức
    try:
        return eval(expression)
    except Exception as e:
        raise ValueError(f"Lỗi khi tính toán biểu thức: {e}")

# Demo chương trình
if __name__ == "__main__":
    scenarios = [
        {"expression": "(A ∧ B) → ¬C", "values": {"A": True, "B": False, "C": True}},
        {"expression": "(A ∨ ¬B) ∧ (C ↔ D)", "values": {"A": True, "B": False, "C": True, "D": True}},
        {"expression": "A → B", "values": {"A": False, "B": True}},
        {"expression": "¬(A ∧ B) ∨ C", "values": {"A": True, "B": True, "C": False}},
        {"expression": "(A ↔ B) ∧ (¬C ∨ D)", "values": {"A": True, "B": True, "C": False, "D": False}}
    ]

    for i, scenario in enumerate(scenarios, start=1):
        expr = scenario["expression"]
        values = scenario["values"]
        print(f"Kịch bản {i}:")
        print(f"Biểu thức: {expr}")
        print(f"Giá trị các biến: {values}")
        
        if is_valid_expression(expr):
            print("Biểu thức hợp lệ.")
            result = evaluate_expression(expr, values)
            print(f"Kết quả: {result}")
        else:
            print("Biểu thức không hợp lệ.")
        print("-" * 30)
