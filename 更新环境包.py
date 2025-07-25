import subprocess

# 升级requirements.txt中的所有包
subprocess.check_call(["pip", "install", "--upgrade", "-r", "requirements.txt"])

# 生成新的requirements.txt（带版本号）
with open("requirements.txt", "w") as f:
    subprocess.check_call(["pip", "freeze"], stdout=f)

print("requirements.txt已更新至最新版本")