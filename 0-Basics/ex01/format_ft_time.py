from time import time
from datetime import date
print(f"seconds since January 1, 1970: {time()} or {time():.2e} in scientific notation")
d = date.today().strftime("%b %d %Y")
print(f"{d}")