class Category:
  def __init__(self, name):
      self.ledger = []
      self.name = name

  def deposit(self, amount, description=""):
      self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
      if self.check_funds(amount):
          self.ledger.append({"amount": -amount, "description": description})
          return True
      return False

  def get_balance(self):
      return sum(item["amount"] for item in self.ledger)

  def transfer(self, amount, budget_cat):
      if self.check_funds(amount):
          self.withdraw(amount, f"Transfer to {budget_cat.name}")
          budget_cat.deposit(amount, f"Transfer from {self.name}")
          return True
      return False

  def check_funds(self, amount):
      return amount <= self.get_balance()

  def __str__(self):
      output = self.name.center(30, "*") + "\n"
      for item in self.ledger:
          output += f"{item['description'][:23]:23}{item['amount']:7.2f}\n"
      output += f"Total: {self.get_balance():.2f}"
      return output

def create_spend_chart(categories):
  category_names = []
  spent = []
  final_spent = []

  for category in categories:
      total = sum(item["amount"] for item in category.ledger if item["amount"] < 0)
      spent.append(round(total, 2))
      category_names.append(category.name)

  for percents in spent:
      final_spent.append(round(percents / sum(spent), 2) * 100)

  graph_return = "Percentage spent by category\n"

  axis = range(100, -1, -10)

  for label in axis:
      graph_return += str(label).rjust(3) + "| "
      for percents in final_spent:
          if percents >= label:
              graph_return += "o  "
          else:
              graph_return += "   "
      graph_return += "\n"

  graph_return += "    " + ("---" * len(category_names)) + "-\n"

  max_name_length = max(len(name) for name in category_names)

  for i in range(max_name_length):
      graph_return += "     "
      for name in category_names:
          if len(name) > i:
              graph_return += name[i] + "  "
          else:
              graph_return += "   "
      if i < max_name_length - 1:
          graph_return += "\n"

  return graph_return
