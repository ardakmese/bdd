import subprocess
if __name__ == '__main__':
    s = subprocess.run('behave --no-capture',shell=True, check=True)