# -*- coding:UTF-8 -*-

import jenkins

# 远程Jenkins的地址
jenkins_server_url = 'http://10.200.131.5:80'

# 用户名
user_id = 'admin'

# 用户的token值(每个user有对应的token----如本文第3.1节所示)
api_token = 'fbb78f17d398d7edbc33f36d76b52f43'

# 登录密码
# passwd = 'admin'

# server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=passwd)

# 使用  API_Token    进行Jenkins登录操作
server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)

# 使用get.version()方法获取版本号
version = server.get_version()

print(version)
# server.build_job('oschina_selenium_docker')
