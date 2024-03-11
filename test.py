# test.py

import subprocess

# Run the app.py script using native Python
subprocess.run(['python', 'app.py'])

# Read values from the output file
with open('/output/output.txt', 'r') as file:
    values = file.read()

# Export VAR1 and VAR2 as environment variables
lines = values.strip().split('\n')
for line in lines:
    key, value = line.split('=')
    key = key.strip()
    value = value.strip()
    print(f'Exporting {key}={value}')
    export_command = f'export {key}={value}'
    subprocess.run(['/bin/bash', '-c', export_command])

# Display the exported values (optional)
print(f"Exported values: {values}")
