import time
import os

# 测试开始时间
test_time = time.strftime('%Y%m%d')  # 20200609

# 全局路径起始点
src_path = os.path.dirname(os.path.abspath('__file__'))  # E:\Auto_Demo\Auto_set

# 接口测试用例路径
interface_case_excel_path = f'{src_path}\data\测试用例V1.2.xlsx'
# 接口测试报告路径
interface_result_excel_path = f'{src_path}\\report\\{test_time}测试结果.xlsx'

# 访问地址
src_url = r'http://localhost'
if __name__ == '__main__':
    print(interface_result_excel_path)
