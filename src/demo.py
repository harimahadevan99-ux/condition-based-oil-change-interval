from simulate import history
from core import plan

print("Light duty :", plan(history(1.0)))
print("Severe duty:", plan(history(2.2)))
