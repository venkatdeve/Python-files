import os
import subprocess
cmd1 = "dir"
result = os.system(cmd1)
print(result)


subprocess.run("dir",shell=True)