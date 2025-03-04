import re

text = re.sub(f"{'6'}{{{10},}}", "27", input())
print(re.sub(f"{'6'}{{{4},}}", "9", text))
