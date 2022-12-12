import subprocess

proc = subprocess.Popen('./about.sh', stdout=subprocess.PIPE)
output = proc.stdout.read()
print(output.decode("utf-8"))