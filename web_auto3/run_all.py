import unittest
from common import HTMLTestRunner

# 设置执行用例的路径
case_path = 'D:\\PyPrg\\web_auto3\\case'
# 设置匹配文件的规则
rule = 'test*.py'
# 查找用例
discover = unittest.defaultTestLoader.discover(start_dir=case_path, pattern=rule)

reportPath = 'D:\\PyPrg\\web_auto3\\report\\'+'report.html'
fp = open(reportPath, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告", description="登录功能测试", )
runner.run(discover)
fp.close()