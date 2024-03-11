# app.py

import random

# Generate two random values
value1 = random.randint(1, 100)
value2 = random.randint(101, 200)

# Write values to a file
with open('/output/output.txt', 'w') as file:
    file.write(f'VAR1={value1}\nVAR2={value2}\n')

print(f'Values written to /output/output.txt: VAR1={value1}, VAR2={value2}')
