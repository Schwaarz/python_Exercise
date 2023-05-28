from config.read_config import ReadConf


# 读取config.ini配置文件,传入sections值
dis = ReadConf('D:\python\Rookie_automation\config\config.ini')
# 获取值
host_url = dis.get_option("api_section","url")
username = dis.get_option("api_section","username")
password = dis.get_option("api_section","password")
token = dis.get_option("api_section","token")

# print(token)
