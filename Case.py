from auto_set import Config
from auto_set.ExcelManagerLib import Excel_operation
from auto_set.RequestLogic import sendRequest

if __name__ == '__main__':

    # 复制excel工作表，并另存为此次测试记录表
    Excel_operation(Config.interface_case_excel_path,'课程管理').copyExcel(Config.interface_result_excel_path)
    # 获取测试用例
    report_excel = Excel_operation(Config.interface_result_excel_path, '课程管理')
    case = report_excel.readExcel()
    for i in range(len(case)):
        result = sendRequest(case[i])
        if case[i][-1]['code'] == result.json()['retcode']:
            print('第%d条测试通过'%(i+1))
            if 'Set-Cookie' in result.headers:
                cookie = result.cookies['sessionid']
                for j in case:
                    j[2]['cookie'] = 'sessionid=%s'%(cookie)
            s_data=result.text.encode(encoding='UTF-8').decode('unicode_escape')
            report_excel.writeExcel(i, 'PASS',s_data)
        else:
            f_reason=result.text.encode(encoding='UTF-8').decode('unicode_escape')
            print('第%d条测试失败，失败原因:%s' % (i+1,f_reason))
            report_excel.writeExcel(i, 'FALSE', f_reason)
    #处理报告
    report_excel.optimizeReport()
    print('测试完成')
