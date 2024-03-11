# test.py

import subprocess

# Run the Docker container with a mounted volume
subprocess.run([
    'docker', 'run', '--rm',
    '-v', '/harness/output',  # Adjust this path based on your host machine
    'my-python-app'
])
