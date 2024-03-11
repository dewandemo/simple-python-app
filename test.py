# test.py

import subprocess

# Run the app.py script using native Python
subprocess.run(['python', 'app.py'])

# Write VAR1 and VAR2 values to the output file
with open('/output/output.txt', 'w') as output_file:
    output_file.write(f'VAR1={VAR1}, VAR2={VAR2}\n')
