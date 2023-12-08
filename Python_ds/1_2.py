# 1_2 Executing commands in python
import subprocess

command = "echo Hello, World!"
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

print("Output:", result.stdout)
print("Error:", result.stderr)
print("Return Code:", result.returncode)
