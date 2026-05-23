class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(entry["amount"] for entry in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        lines = ""
        for entry in self.ledger:
            description = entry["description"][:23]
            amount = f"{entry['amount']:.2f}"
            lines += f"{description:<23}{amount:>7}\n"
        total_line = f"Total: {self.get_balance():.2f}"
        return title + lines + total_line


def create_spend_chart(categories):
    spent_amounts = []
    for category in categories:
        spent = 0
        for entry in category.ledger:
            if entry["amount"] < 0:
                spent += -entry["amount"]
        spent_amounts.append(spent)

    total_spent = sum(spent_amounts)
    percentages = []
    for amount in spent_amounts:
        if total_spent == 0:
            percentages.append(0)
        else:
            percentages.append(int((amount / total_spent) * 100) // 10 * 10)

    chart_lines = ["Percentage spent by category"]
    for level in range(100, -1, -10):
        row = f"{level:>3}|"
        for percent in percentages:
            row += " o " if percent >= level else "   "
        row += " "
        chart_lines.append(row)

    chart_lines.append("    " + "-" * (len(categories) * 3 + 1))

    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        row = "     "
        for category in categories:
            if i < len(category.name):
                row += category.name[i] + "  "
            else:
                row += "   "
        chart_lines.append(row)

    return "\n".join(chart_lines)