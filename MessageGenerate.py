# -*- coding: UTF-8 -*-
import time
from ftplib import FTP
import glob
import os
import json
import requests


class MessageGenerateAndUpload():
    def __init__(self):
        self.localpath = r'\\10.127.192.121\Data'
        self.host = '10.124.32.202'
        self.port = 21
        self.user = "BFZF"
        self.password = 'BFZFBFZF'
        self.mbox1_path = self.localpath+ r'\fwb\96121信箱\1'

    def  newestOrNot(self):
        newfile = self.get_newst_file(self.mbox1_path, '.txt')
        new_file_base =  os.path.basename(newfile)
        with open(self.localpath + r'\fwb\Zjxsp\record.txt', 'r+', encoding='gbk') as f:
            last_ybyj_record = f.readline()
            if new_file_base ==last_ybyj_record:
                flag = 0
            else:
                flag = 1
                f.seek(0)
                f.truncate()
                f.write(new_file_base)
            f.close()
        return flag,newfile


    def get_newst_file(self, filepath, matchstr):
        filelist = []
        for file in os.listdir(filepath):
            if matchstr in file:
                filelist.append(file)
        filelist.sort(key=lambda fn: os.path.getmtime(filepath + "\\" + fn))
        filenew = os.path.join(filepath, filelist[-1])
        return filenew

    def list_add(self, list1, list2):
        list = []
        for i in range(len(list1)):
            list.append(list1[i] + list2[i])
        for i in range(1, len(list)):
            list[i] = list[i - 1] + list[i]
        return list

    def xsp_content_replace_split_rule(self, text, num):
        text = text.replace('℃', '度')
        text = text.replace(',', '，')
        text = text.replace('.', '。')
        text = text.replace(':', '：')
        text1 = text.replace(' ', '')
        text = str.encode(text1, encoding='gbk')
        length = len(text)
        lendiv = length // num
        mlendiv = lendiv // 4
        nlendiv = lendiv % 4
        len_list1 = [mlendiv] * 4
        len_list2 = [1] * nlendiv + [0] * (4 - nlendiv)
        lenlist = self.list_add(len_list1, len_list2)
        xsp_all = [text[:lenlist[0] * num], text[lenlist[0] * num:lenlist[1] * num],
                   text[lenlist[1] * num:lenlist[2] * num], text[lenlist[2] * num:]]
        xsp_all = self.split_rule(xsp_all)
        xsp_all = self.split_rule(xsp_all)
        xsp_all = self.split_rule(xsp_all)
        xsp_all = self.split_rule(xsp_all)
        xsp_all = self.split_rule(xsp_all)
        xsp_all = self.split_rule(xsp_all)
        return text1,xsp_all

    def split_rule(self, list):
        list1 = list.copy()
        len_list = [len(list1[i]) for i in range(0, len(list1))]
        for i in range(0, len(list1) - 1):
            try:
                a = list1[i][:len_list[i]]
                b = list1[i][len_list[i]:]
                list1[i] = a
                list1[i + 1] = b + list1[i + 1]
                list1[i].decode('gbk')
            except  UnicodeDecodeError as e:
                a = list1[i][-1]
                list1[i] = list1[i][:-1]
                list1[i + 1] = bytes([a]) + list1[i + 1]
        return list1


    def GetMessageBox1Content(self):
        flag,newfile = self.newestOrNot()
        if flag:
            day = newfile.split('.txt')[0][-4:-2]
            hour = newfile.split('.txt')[0][-2:]
            text = []
            with open(newfile, 'r', encoding='gbk') as f:
                a = True
                while a:
                    a = f.readline()
                    text.append(a)
            text = [i.strip('\n') for i in text]
            text = ''.join(i for i in text)
            content = text.split('天气预报')[1]
            MessageBox1Content = '镇江市气象台{}日{}时发布天气预报:{}'.format(day, hour, content)
        else:
            with open(self.localpath + r'\fwb\Zjxsp\市台最新时次预报.txt', 'r+', encoding='gbk') as f:
                MessageBox1Content=f.readline()
                f.close()
        return flag,MessageBox1Content

    def GenerateSplitYbyj(self,content):
        text,xsp_list = self.xsp_content_replace_split_rule(content, 48)
        for i in range(1, 5):
            with open(self.localpath + r'\fwb\Zjxsp' + os.sep + "Bsyb{}.xsp".format(str(i)), 'w') as xsp_out:
                xspi = xsp_list[i - 1].decode('gbk')
                xsp_out.write('<WEA{}>'.format(str(i)) + xspi)
            xsp_out.close()
        return text

    def GenerateSplitJsyb(self,content):
        text,xsp_list = self.xsp_content_replace_split_rule(content, 48)
        for i in range(1, 5):
            with open(self.localpath + r'\fwb\Zjxsp' + os.sep + "Styb{}.xsp".format(str(i)), 'w') as xsp_out:
                xspi = xsp_list[i - 1].decode('gbk')
                xsp_out.write('<AD0{}>'.format(str(i)) + xspi)
            xsp_out.close()
        return text

    def GenerateYBYJAndUpload(self,ybyj_text,state):
        flag,content = self.GetMessageBox1Content()

        with open(self.localpath+r"\fwb\Zjxsp\市台最新时次预警.txt","r+",encoding="gbk") as f:
            ybyj = f.readline()
            f.close()
        text_new=self.GenerateSplitYbyj(content)
        if state==0 :
            content_new = content
            if flag:
                try:
                    text_new = self.GenerateSplitYbyj(content_new)
                    ybyj_log1 = '[{}]：市台资讯制作成功！\n{}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S"), text_new)
                    ftp_log, ftp_flag = self.xsp_ftp_upload()
                    http_log = self.GangWuHttpPost(text_new)
                    ybyj_log = ybyj_log1+ftp_log+http_log
                    if ftp_flag:
                        with open(self.localpath + r'\fwb\Zjxsp\市台最新时次预报.txt', 'r+', encoding='gbk') as f:
                            f.seek(0)
                            f.truncate()
                            f.write(text_new)
                            f.close()
                except Exception as e:
                    ybyj_log = '[{}]：市台资讯制作失败，失败原因::{}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S"), e)

            else:
                ybyj_log = '[{}]：市台资讯未更新,无需制作上传！\n'.format(time.strftime("%Y-%m-%d %H:%M:%S"))

        if state==2:
            content_new = "{}         {}".format(content, ybyj_text)
            if flag or (ybyj_text!=ybyj):
                try:
                    text_new = self.GenerateSplitYbyj(content_new)
                    ybyj_log1 = '[{}]：市台资讯制作成功！\n{}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S"), text_new)
                    ftp_log, ftp_flag = self.xsp_ftp_upload()
                    http_log = self.GangWuHttpPost(text_new)
                    ybyj_log = ybyj_log1+ftp_log+http_log

                    if ftp_flag:
                        with open(self.localpath + r'\fwb\Zjxsp\市台最新时次预报.txt', 'r+', encoding='gbk') as f:
                            f.seek(0)
                            f.truncate()
                            f.write(text_new)
                            f.close()
                        with open(self.localpath + r'\fwb\Zjxsp\市台最新时次预警.txt', 'r+', encoding='gbk') as f:
                            f.seek(0)
                            f.truncate()
                            f.write(ybyj_text)
                            f.close()
                except Exception as e:
                    ybyj_log = '[{}]：市台资讯制作失败，失败原因::{}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S"), e)
            else:
                ybyj_log = '[{}]：市台资讯未更新,无需制作上传！\n'.format(time.strftime("%Y-%m-%d %H:%M:%S"))

        if state==1:
            content_new = ybyj_text
            if ybyj_text!=ybyj:
                try:
                    text_new = self.GenerateSplitYbyj(content_new)
                    ybyj_log1 = '[{}]：市台预警制作成功！\n{}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S"), text_new)
                    ftp_log, ftp_flag = self.xsp_ftp_upload()
                    http_log = self.GangWuHttpPost(text_new)
                    ybyj_log = ybyj_log1+ftp_log+http_log
                    if ftp_flag:
                        with open(self.localpath + r'\fwb\Zjxsp\市台最新时次预警.txt', 'r+', encoding='gbk') as f:
                            f.seek(0)
                            f.truncate()
                            f.write(ybyj_text)
                            f.close()
                except Exception as e:
                    ybyj_log = '[{}]：市台预警制作失败，失败原因::{}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S"), e)
            else:
                ybyj_log = '[{}]：市台预警未更新,无需制作上传！\n'.format(time.strftime("%Y-%m-%d %H:%M:%S"))
        return ybyj_log,text_new


    def GenerateJSYBAndUpload(self,jsyb_text):
        flag, content = self.GetMessageBox1Content()
        with open(self.localpath + r"\fwb\Zjxsp\省台最新时次预报.txt", "r+", encoding="gbk") as f:
            jsyb= f.readline()
            f.close()
            print("上次时次：",jsyb)
            print("当前时次：",content)
        if jsyb!=content:
            try:
                text_new = self.GenerateSplitJsyb(content)
                jsyb_log = '[{}]：省台预报制作成功！\n{}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S"), text_new)
                ftp_log, ftp_flag = self.xsp_ftp_upload()
                jsyb_log += ftp_log
                if ftp_flag:
                    with open(self.localpath + r"\fwb\Zjxsp\省台最新时次预报.txt", "r+", encoding="gbk") as f:
                        f.seek(0)
                        f.truncate()
                        f.write(text_new)
                        f.close()
            except Exception as e:
                jsyb_log = '[{}]：省台资讯制作失败，失败原因::{}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S"), e)
        else:
            text_new = jsyb
            jsyb_log = '[{}]：省台资讯未更新,无需制作上传！\n'.format(time.strftime("%Y-%m-%d %H:%M:%S"))
        return jsyb_log,text_new

    def xsp_ftp_upload(self):
            ftp = FTP()
            ftp.connect(self.host, self.port)
            # ftp.set_pasv(False)
            ftp.login(self.user, self.password)

            remotepath = r'\SEVP\DXYB\ZYFW'

            #上传文件
            localfiles = glob.glob(self.localpath + r"\fwb\Zjxsp"+os.sep +"*.xsp")
            try:
                for file in localfiles:
                    bufsize = 1024
                    fp = open(file, 'rb')
                    file = os.path.basename(file)
                    ftp.storbinary('STOR ' + remotepath + os.sep + file, fp, bufsize)
                    ftp.set_debuglevel(0)
                ftp_log = '[{}]：LCD屏推送成功!\n'.format(time.strftime("%Y-%m-%d %H:%M:%S"))
                ftp_flag=1
            except Exception as e:
                ftp_log = '[{}]：LCD屏推送失败!\n{}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S"), e)
                ftp_flag = 0
            ftp.close()
            return ftp_log,ftp_flag

    def GangWuHttpPost(self,text):
        #港务集团http服务器地址
        url = 'http://api.portzj.com/psys-gateway-service/api/external/weather_forecast/insert'
        #json格式文件
        data = {"content": text, "createName": "tqyb"}
        headers = {
            'Content-Type': 'application/json',
            'accesstoken': 'btulVR0+Oghty39WSD1fE9Rg+LJZ8SHyfZzg0hgEkCLk5ebgDrvJGhYQA40hFSJtoGsAvBENXsE0uuyKahM5oZYwYrrpubR/qy4xXKoFIz+YKtwgpSUl+Uvfd0z5aQ3AT8C47PWjY/SJR+Kvk0m64Uown/rCG0pnXBxLQjKaH9PqvwVHbRG2QQk/PSqk/eX6OLGVIdWUqmdvF/JqSHebEw=='
        }
        response = requests.post(url, headers=headers, json=data).json()
        if "插入成功" in response['msg']:
            http_log = '[{}]：港务集团HTTP推送成功!\n'.format(time.strftime("%Y-%m-%d %H:%M:%S"))
        else:
            http_log = '[{}]：港务集团HTTP推送失败！\n{}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S"),response['msg'])
        return http_log

def run():
    fwb = FWB()
    fwb.xsp_ftp_upload_xsp()

if __name__ == "__main__":
    # schedule.every().hour.at(":05").do(run)
    # schedule.every().hour.at(":25").do(run)
    # schedule.every().minute.do(run)
    #
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    fwb = FWB()
    fwb.GetMessageBox1Content()
