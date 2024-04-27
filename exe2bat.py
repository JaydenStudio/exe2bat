import base64

# 使用 base64 编码一个 exe 文件
file = input("請輸入要轉換的檔名：")
with open(file, "rb") as f:
    data = f.read()
    data_base64 = base64.b64encode(data)

# 创建一个 bat 文件来运行 exe 文件
str_base64 = data_base64.decode()
output = input("請輸入輸出檔案的名字：")
with open(output, "w") as f:
    f.write("@echo off\n")
    f.write(fr'''
set v="%temp%\x.exe"
del %v% >NUL 2>NUL
certutil -decode "%~f0" %v% >NUL 2>NUL
start "" %v%
exit

-----BEGIN CERTIFICATE-----
{str_base64}
-----END CERTIFICATE-----
''')

