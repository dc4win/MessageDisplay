# -*- coding: UTF-8 -*-
import schedule
import time
from ftplib import FTP
import glob
import os

class FWB():
    def __init__(self):
        self.localpath = r'\\10.127.192.121\Data'
        self.host='10.124.32.202'
        self.port = 21
        self.user = "BFZF"
        self.password='BFZFBFZF'

    def get_newst_file(self,filepath,matchstr):
        filelist=[]
        for file in os.listdir(filepath):
            if matchstr in file:
                filelist.append(file)
        filelist.sort(key=lambda fn: os.path.getmtime(filepath + "\\" + fn))
        filenew = os.path.join(filepath, filelist[-1])
        return  filenew

    def list_add(self,list1,list2):
        list=[]
        for i in  range(len(list1)):
            list.append(list1[i]+list2[i])
        for i in range(1,len(list)):
            list[i]=list[i-1]+list[i]
        return list
    
    def xsp_content_replace_split_rule(self,text,num):
        text = text.replace('℃', '度')
        text = text.replace(',', '，')
        text = text.replace('.', '。')
        text = text.replace(':', '：')
        text = text.replace(' ', '')
        text = str.encode(text, encoding='gbk')
        length = len(text)
        lendiv = length // num
        mlendiv = lendiv // 4
        nlendiv = lendiv % 4
        len_list1 = [mlendiv] * 4
        len_list2 = [1] * nlendiv + [0] * (4 - nlendiv)
        lenlist = self.list_add(len_list1, len_list2)
        xsp_all = [text[:lenlist[0]*num], text[lenlist[0]*num:lenlist[1]*num], text[lenlist[1]*num:lenlist[2]*num], text[lenlist[2]*num:]]
        xsp_all = self.split_rule(xsp_all)
        xsp_all = self.split_rule(xsp_all)
        xsp_all = self.split_rule(xsp_all)
        xsp_all = self.split_rule(xsp_all)
        xsp_all = self.split_rule(xsp_all)
        xsp_all = self.split_rule(xsp_all)
        return xsp_all

    def split_rule(self,list):
        list1 = list.copy()
        len_list = [len(list1[i]) for i in range(0,len(list1))]
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

    def generate_xsp_from_jsst(self,newfile):
        text=[]
        with open(newfile,'r',encoding='gbk') as f:
            file = os.path.basename(newfile)
            daystr,timestr=file.split('.')[0][-2:],file.split('.')[1][:2]
            a=True
            while a:
                a = f.readline()
                text.append(a)
            text_para = ''.join(i for i in text).split("\n\n")
            text1 = text_para[0]
            text2 = '，'+text_para[1].split('\n')[0]+'。'
            text = ''.join([text1,text2])
            text=text.replace('\n','，')
            xsp_all = "江苏省气象台{}日{}时发布全省天气预报{}".format(daystr,timestr,text.split('天气提示')[1])
            xsp=self.xsp_content_replace_split_rule(xsp_all,48)
        for i in range(1, 5):
            with open(self.localpath + r'\fwb\Zjxsp' + os.sep + "Styb{}.xsp".format(str(i)), 'w') as xsp_out:
                xspi = xsp[i - 1].decode('gbk')
                xsp_out.write('<AD0{}>'.format(str(i)) + xspi)
            xsp_out.close()

    def generate_xsp_from_messagebox1(self,newfile):
        day = newfile.split('.txt')[0][-4:-2]
        hour = newfile.split('.txt')[0][-2:]
        text =[]
        with open(newfile,'r',encoding='gbk') as f:
            a = True
            while a:
                a = f.readline()
                text.append(a)
        text = [i.strip('\n') for i in text]
        text = ''.join(i for i in text)
        content = text.split('天气预报')[1]
        forecaster = text.split('号预报员')[0].split('气象台')[1]+"号预报员"
        xsp_all = '镇江市气象台{}日{}时发布天气预报:{}({})'.format(day,hour,content,forecaster)
        xsp = self.xsp_content_replace_split_rule(xsp_all,48)

        for i in range(1,5):
            with open(self.localpath+r'\fwb\Zjxsp'+os.sep+"Bsyb{}.xsp".format(str(i)),'w') as xsp_out:
               xspi=xsp[i-1].decode('gbk')
               xsp_out.write('<WEA{}>'.format(str(i))+xspi)
            xsp_out.close()

    def xsp_ftp_upload_xsp(self):
        mbox1_path = self.localpath+r'\fwb\96121信箱\1'
        jsst_path = self.localpath+r'\fwb\96121信箱\6'

        newfile = self.get_newst_file(mbox1_path,'.txt')
        newfile1 = self.get_newst_file(jsst_path,'.txt')

        basefile=os.path.basename(newfile)
        basefile1 = os.path.basename(newfile1)

        localpath = r'\\10.127.192.121\Data\fwb\Zjxsp'
        localtime = time.strftime("%Y-%m-%d %H:%M:%S")

        try:
            self.generate_xsp_from_messagebox1(newfile)
        except Exception as e:
            print('[{}]:{} Generate Error:{}'.format(localtime,basefile,e))
        else:

            print("[{}]:{} Generate Success!".format(localtime, basefile))
        try:
            self.generate_xsp_from_jsst(newfile1)
        except Exception as e:
            print('[{}]:{} Generate Error:{}'.format(localtime, basefile1, e))
        else:
            print("[{}]:{} Generate Success!".format(localtime, basefile1))
        ##将最新文件basename写入record.txt文件,便于下一时次对比使用
        with open(localpath+r'\record.txt','r+',encoding='gbk') as f:
            base_record = f.readline()
            base_record1 =f.readline()
            f.seek(0)
            f.truncate()
            if (base_record!=(basefile+'\n')) or (base_record1!=basefile1):
                self.xsp_ftp_upload1(localpath,basefile,basefile1,localtime)
                f.write(basefile+'\n')
                f.write(basefile1)
            else:
                f.write(basefile+'\n')
                f.write(basefile1)
                print('[{}]:No Need To UpLoad!'.format(localtime))
            f.close()

    def xsp_ftp_upload1(self,localpath,basefile,basefile1,localtime):
        ftp = FTP()
        ftp.close()
        ftp.connect(self.host,self.port)
        ftp.login(self.user,self.password)
        remotepath = r'\SEVP\DXYB\ZYFW'

        #上传文件
        localfiles = glob.glob(localpath+os.sep+'*.xsp')
        try:
            for file in localfiles:
                bufsize = 1024
                fp = open(file, 'rb')
                file = os.path.basename(file)
                ftp.storbinary('STOR ' + remotepath+os.sep+file, fp, bufsize)
                ftp.set_debuglevel(0)
            print('[{}]:{}{} UpLoad Success!'.format(localtime,basefile,basefile1) )
        except Exception as e:
            print('[{}]:{}{}UpLoad Failed!'.format(localtime,basefile,basefile1)+e)
        ftp.close()

def run():
    fwb=FWB()
    fwb.xsp_ftp_upload_xsp()

if __name__=="__main__":
    schedule.every().hour.at(":05").do(run)
    schedule.every().hour.at(":35").do(run)
    while True:
        schedule.run_pending()
        time.sleep(1)
