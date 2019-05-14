
import numpy as np
import pandas as pd
import pickle
import os



def testSample():
    '''
    sample_id: 样本id;
    AD_id: 广告id;
    time: 创建时间；
    size: 素材尺寸；
    industry_id: 广告行业id；
    product_type: 商品类型；
    product_id: 商品id;
    account: 广告账户id；
    deliver_time: 投放时段；
    user: 人群定向；
    expo_bid: 出价
    
    '''
    with open('./data/testA/test_sample.dat', 'r', encoding = 'utf-8') as f:
        new = open('./data/testA/test_sample.csv', 'w')
        new.write('sample_id\tAD_id\ttime\tsize\tindustry_id\tproduct_type\tproduct_id\t'
                  'account\tdeliver_time\tuser\texpo_bid\n')
        j = 0
        for line in f:
#             print(line)
            lineContent = line.split('\t')
            if len(lineContent) != 11:
                print('Warning: Expected 11 rows!')
            if j % 100000 == 0:
                print('j',j)
            new.write(line)
            j += 1
        new.close()
        print('total line has {}'.format(j))
    tmpfile = pd.read_csv('./data/testA/test_sample.csv', sep = '\t', engine = 'python')


    
def ADOperation():
    '''
    AD_id: 广告id
    time: 创建/修改时间
    operation_type: 1 - 修改； 2- 新建
    modify_field: 修改字段 1 - 广告状态 2 - 出价， 3-人群定向 4 - 广告时段
    operation_value: 操作后的字段值。
    '''
    with open('./data/testA/ad_operation.dat', 'r', encoding = 'utf-8') as f:
        new = open('./data/testA/ad_operation.csv', 'w')
        new.write('AD_id\ttime\toperation_type\tmodify_field\toperation_value\n')
        j = 0
        for line in f:
            if j % 100000 == 0:
                print('j',j)
            new.write(line)
            j += 1
        new.close()
        print('total line has {}'.format(j))
    tmpfile = pd.read_csv('./data/testA/ad_operation.csv', sep = '\t', engine = 'python')


def preADStatic():
    '''
    Ad_id: 广告id
    time:广告创建时间
    account_id: 广告账户id；
    product_id: 商品id；
    product_class: 商品类型；
    industry_id：广告行业id；
    size:素材尺寸（同一个广告可能有不同尺寸）
    
    '''
    with open('./data/testA/ad_static_feature.out', 'r', encoding='utf-8') as f:
        new = open('./data/testA/ad_static_feature.csv', 'w')
        new.write('AD_id\ttime\taccount_id\tproduct_id\tproduct_class\tindustry_id\t'
                  'size\n')
        j = 0
        for line in f:
            lineContent = line.split('\t')
            if j % 500000 == 0:
                print(lineContent[0])
            new.write(line)
            j += 1


        new.close()
        print('total line has {}'.format(j))
    tmpfile = pd.read_csv('./data/testA/ad_static_feature.csv', sep = '\t', engine = 'python')


def preUser():
    '''
    用户特征属性文件。
    user_id : 用户id; 
    age: 年龄；映射后的值；
    gender：性别；
    area：地域；
    status:婚恋状态，可能多值；
    education：学历；
    consumption_ability:消费能力
    device:设备
    work：工作状态
    connection_type:连接类型；
    behavior:行为兴趣，每个兴趣点一个id。
    '''
    with open('./data/testA/user/user_data', 'r', encoding='utf-8') as f:
        new = open('./data/testA/user_data.csv', 'w')
        i = 0
        for line in f:
            if i == 0:
                new.write('user_id\tage\tgender\tarea\tstatus\teducation\tconsumption_ability\t'
                          'device\twork\tconnect_type\tbehavior\n')
            lineContent = line.split('\t')
            if len(lineContent) != 11:
                print('Warning：length != 11.\n')
                print('the line is:{}\n'.format(lineContent))
            if i % 100000 == 0:
                print(line[0])
            i += 1
            new.write(line)
        new.close()
        print('total line has {}'.format(i))
    tmpfile = pd.read_csv('./data/testA/user_data.csv', sep = '\t')



def countTotalExposure():
    '''
    把历史曝光文件转换为pickle形式。
    Ad_id: 广告请求id;
    time: 广告请求时间；
    Ad_loc_id: 广告位id;
    user_id: 用户id;
    expo_id: 曝光广告id;
    expo_size: 曝光广告素材尺寸；
    expo_bid: 曝光广告出价bid；
    expo_pctr: 曝光广告pctr；
    expo_quality_ecpm：曝光广告quality_ecpm ;
    expo_total_ecpm: 曝光广告排序的分数依据；'''
    with open('./data/testA/imps_log/totalExposureLog.out', 'r', encoding='utf-8') as f:
        csvfile = open('./data/testA/totalExposureLog.csv', 'w')
        i = 0
        for line in f:
            if i == 0:
                csvfile.write('AD_id,time,AD_loc_id,user_id,expo_id,expo_size,expo_bid,'
                              'expo_pctr,expo_quality_ecpm,expo_total_ecpm\n')
            lineContent = line.split('\t') 
            if i % 1000000 == 0:
                print(lineContent[0])
            if len(lineContent) != 10:
                print('Warning：length != 10.')
                print('the line is:{}\n'.format(lineContent))
            line = line.replace('\t', ',')
            csvfile.write(line)
            i += 1

        csvfile.close()
        print('total line has {}'.format(i))
    tmpfile = pd.read_csv('./data/testA/totalExposureLog.csv',)
