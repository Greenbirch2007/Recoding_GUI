#! -*-  coding=utf-8 -*-

import xlrd
import pandas as pd
import os

def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
       # if 去掉表头
       if rowNum > 0:
          dataFile.append(table.row_values(rowNum))

    return dataFile
def get_block(l_l):
    b_l =[]
    for item in l_l:
        if type(item) == str:
            b_l.append(0)
        else:
            b_l.append(item)
    return b_l



# 创建的目录
def mkdir():
    loc_getcwd = os.getcwd()
    path = "{0}/Outputs".format(loc_getcwd)
    #如果存在目录先删除，如果不存在就创建
    if os.path.exists(path):
        os.removedirs(path)
    else:
        os.mkdir(path)
    return path



if __name__ == '__main__':
    loc_getcwd = os.getcwd()
    excelFile = '{0}/RawData.xlsx'.format(loc_getcwd) # 处理了文件属于当前目录下！
    ln = mkdir()

    # 处理在当前目录下创建Output目录，里面包含了所有的需要输出的文件
    # 先把单表的名字容器给弄出来
    location_l =[]
    location_name = []
    all_PC = []

    full_items = read_xlrd(excelFile=excelFile)
    for item in full_items:
        f_item = get_block(item)
        location_name.append(item[0])
        # 先求平均值吧 ,要处理空格的，也就是字符串的情况
        q1_average = round((f_item[1]+f_item[2]+f_item[3])/3,2)
        q2_average = round((f_item[4]+f_item[5]+f_item[6])/3,2)
        q3_average = round((f_item[7]+f_item[8]+f_item[9])/3,2)
        q4_average = round((f_item[10]+f_item[11]+f_item[12])/3,2)
        location_l.append((q1_average,q2_average,q3_average,q4_average))
    for i1,i2 in zip(location_name,location_l):
        all_PC.append((i1,)+i2)


    #
    # 华北再平均
    # 华北5个省市
    hb_q1  = round((location_l[0][0] +location_l[1][0] + location_l[2][0]+location_l[3][0]+location_l[4][0])/5,2)
    hb_q2  = round((location_l[0][1] +location_l[1][1] + location_l[2][1]+location_l[3][1]+location_l[4][1])/5,2)
    hb_q3  = round((location_l[0][2] +location_l[1][2] + location_l[2][2]+location_l[3][2]+location_l[4][2])/5,2)
    hb_q4  = round((location_l[0][3] +location_l[1][3] + location_l[2][3]+location_l[3][3]+location_l[4][3])/5,2)

    columns = ["省市名称","2019年第一季度", "2019年第二季度", "2019年第三季度","2019年第四季度"]
    huabei_dt = ("华北地区",hb_q1,hb_q2,hb_q3,hb_q4)

    # 东北地区３个省份
    db_q1 = round((location_l[5][0]+location_l[6][0]+location_l[7][0]/3),2)
    db_q2 = round((location_l[5][1]+location_l[6][1]+location_l[7][1]/3),2)
    db_q3 = round((location_l[5][2]+location_l[6][2]+location_l[7][2]/3),2)
    db_q4 = round((location_l[5][3]+location_l[6][3]+location_l[7][3]/3),2)
    dongbei_dt = ("东北地区",db_q1,db_q2,db_q3,db_q4)
    # 华东７个省市 8-14

    hd_q1 = round((location_l[8][0]+location_l[9][0]+location_l[10][0]+location_l[11][0]+location_l[12][0]+location_l[13][0]+location_l[14][0])/7,2)
    hd_q2 = round((location_l[8][1]+location_l[9][1]+location_l[11][1]+location_l[11][1]+location_l[12][1]+location_l[13][1]+location_l[14][1])/7,2)
    hd_q3 = round((location_l[8][2]+location_l[9][2]+location_l[12][2]+location_l[11][2]+location_l[12][2]+location_l[13][2]+location_l[14][2])/7,2)
    hd_q4 = round((location_l[8][3]+location_l[9][3]+location_l[13][3]+location_l[11][3]+location_l[12][3]+location_l[13][3]+location_l[14][3])/7,2)
    huadong_dt =("华东地区",hd_q1,hd_q2,hd_q3,hd_q4)

    # 中南地区６个省份  15-20
    zn_q1 = round((location_l[15][0]+location_l[16][0]+location_l[17][0]+location_l[18][0]+location_l[19][0]+location_l[20][0])/5,2)
    zn_q2 = round((location_l[15][1]+location_l[16][1]+location_l[17][1]+location_l[18][1]+location_l[19][1]+location_l[20][1])/5,2)
    zn_q3 = round((location_l[15][2]+location_l[16][2]+location_l[17][2]+location_l[18][2]+location_l[19][2]+location_l[20][2])/5,2)
    zn_q4 = round((location_l[15][3]+location_l[16][3]+location_l[17][3]+location_l[18][3]+location_l[19][3]+location_l[20][3])/5,2)
    zhongnan_dt = ("中南地区",zn_q1,zn_q2,zn_q3,zn_q4)
    #  西南地区５个省市 21-25
    xn_q1 = round((location_l[21][0]+location_l[22][0]+location_l[23][0]+location_l[24][0]+location_l[25][0])/5,2)
    xn_q2 = round((location_l[21][1]+location_l[22][1]+location_l[23][1]+location_l[24][1]+location_l[25][1])/5,2)
    xn_q3 = round((location_l[21][2]+location_l[22][2]+location_l[23][2]+location_l[24][2]+location_l[25][2])/5,2)
    xn_q4 = round((location_l[21][3]+location_l[22][3]+location_l[23][3]+location_l[24][3]+location_l[25][3])/5,2)
    xinan_dt = ("西南地区",xn_q1,xn_q2,xn_q3,xn_q4)

    # 西北地区５个省份　26-30
    xb_q1 = round((location_l[26][0]+location_l[27][0]+location_l[28][0]+location_l[29][0]+location_l[30][0])/5,2)
    xb_q2 = round((location_l[26][1]+location_l[27][1]+location_l[28][1]+location_l[29][1]+location_l[30][1])/5,2)
    xb_q3 = round((location_l[26][2]+location_l[27][2]+location_l[28][2]+location_l[29][2]+location_l[30][2])/5,2)
    xb_q4 = round((location_l[26][3]+location_l[27][3]+location_l[28][3]+location_l[29][3]+location_l[30][3])/5,2)
    xibei_dt =("西北地区",xb_q1,xb_q2,xb_q3,xb_q4)


    # 下载的部分 0-4
    # 华北地区 dt save
    save_huabei_dt = [huabei_dt,all_PC[0],all_PC[1],all_PC[2],all_PC[3],all_PC[4]]
    huabei_dt = pd.DataFrame(save_huabei_dt, columns=columns)
    huabei_dt.to_excel("{0}/华北地区.xlsx".format(ln), index=0)
    # 东北地区 5-7
    save_dongbei_dt = [dongbei_dt,all_PC[5],all_PC[7],all_PC[8]]
    dongbei_dt = pd.DataFrame(save_dongbei_dt,columns=columns)
    dongbei_dt.to_excel("{0}/东北地区.xlsx".format(ln), index=0)
    #华东地区　8-14
    save_huadong_dt =[huadong_dt,all_PC[8],all_PC[9],all_PC[10],all_PC[11],all_PC[12],all_PC[13],all_PC[14]]
    huadong_dt = pd.DataFrame(save_huadong_dt,columns=columns)
    huadong_dt.to_excel("{0}/华东地区.xlsx".format(ln), index=0)
    # 中南地区　　15-20
    save_zhongnan_dt =[zhongnan_dt,all_PC[15],all_PC[16],all_PC[17],all_PC[18],all_PC[19],all_PC[20]]
    zhongnan_dt = pd.DataFrame(save_zhongnan_dt,columns=columns)
    zhongnan_dt.to_excel("{0}/中南地区.xlsx".format(ln), index=0)
    #  西南地区　　21-25
    save_xinan_dt = [xinan_dt,all_PC[21],all_PC[22],all_PC[23],all_PC[24],all_PC[25]]
    xinan_dt = pd.DataFrame(save_xinan_dt,columns=columns)
    xinan_dt.to_excel("{0}/西南地区.xlsx".format(ln), index=0)
    #  西北地区　26-30
    save_xibei_dt = [xibei_dt,all_PC[26],all_PC[27],all_PC[28],all_PC[29],all_PC[30]]
    xibei_dt = pd.DataFrame(save_xibei_dt,columns=columns)
    xibei_dt.to_excel("{0}/西北地区.xlsx".format(ln), index=0)
    # 全国
    save_allCountry_dt = save_huabei_dt+save_dongbei_dt+save_huadong_dt+save_zhongnan_dt+save_xinan_dt+save_xibei_dt
    allC_dt = pd.DataFrame(save_allCountry_dt,columns=columns)
    allC_dt.to_excel("{0}/全国各地区及省份数据.xlsx".format(ln), index=0)



