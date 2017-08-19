# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 10:55:09 2017

@author: Quantum Liu
"""

from comic import *
from io import BytesIO
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys

class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form,self).__init__()
        self.url=''
        self.dir=''
        self.show=True
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 180)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        Form.setWindowIcon(QtGui.QIcon('./batman.ico'))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_url = QtWidgets.QLabel(Form)
        self.label_url.setAlignment(QtCore.Qt.AlignCenter)
        self.label_url.setObjectName("label_url")
        self.gridLayout.addWidget(self.label_url, 0, 0, 1, 1)
        self.edit_url = QtWidgets.QLineEdit(Form)
        self.edit_url.setObjectName("edit_url")
        self.gridLayout.addWidget(self.edit_url, 0, 1, 1, 1)
        self.bt_preview = QtWidgets.QPushButton(Form)
        self.bt_preview.setAutoDefault(True)
        self.bt_preview.setDefault(False)
        self.bt_preview.setObjectName("bt_preview")
        self.bt_preview.clicked.connect(self.preview)
        self.gridLayout.addWidget(self.bt_preview, 0, 2, 1, 1)
        self.bt_crawl = QtWidgets.QPushButton(Form)
        self.bt_crawl.setDefault(True)
        self.bt_crawl.setObjectName("bt_crawl")
        self.bt_crawl.clicked.connect(self.crawl)
        self.gridLayout.addWidget(self.bt_crawl, 0, 3, 1, 2)
        self.label_dir = QtWidgets.QLabel(Form)
        self.label_dir.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dir.setObjectName("label_dir")
        self.gridLayout.addWidget(self.label_dir, 1, 0, 1, 1)
        self.edit_dir = QtWidgets.QLineEdit(Form)
        self.edit_dir.setObjectName("edit_dir")
        self.edit_url.textChanged.connect(self.edit_dir.clear)
        self.gridLayout.addWidget(self.edit_dir, 1, 1, 1, 1)
        self.bt_select = QtWidgets.QPushButton(Form)
        self.bt_select.setObjectName("bt_select")
        self.bt_select.clicked.connect(self.select_dir)
        self.gridLayout.addWidget(self.bt_select, 1, 2, 1, 1)
        self.bt_parallel = QtWidgets.QRadioButton(Form)
        self.bt_parallel.setChecked(False)
        self.bt_parallel.setObjectName("bt_parallel")
        self.gridLayout.addWidget(self.bt_parallel, 1, 4, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "漫画爬虫"))
        self.label_url.setText(_translate("Form", "漫画网址"))
        self.bt_preview.setText(_translate("Form", "预览"))
        self.bt_crawl.setText(_translate("Form", "爬取"))
        self.label_dir.setText(_translate("Form", "保存目录"))
        self.bt_select.setText(_translate("Form", "选择目录"))
        self.bt_parallel.setText(_translate("Form", "使用多线程"))

    def select_dir(self):
        self.dir=QFileDialog.getExistingDirectory(self,'选择保存路径',(self.dirname if self.dirname else './'))
    
    def preview(self):
        r_cover=r'src="(.*?)" id="cover_pic"/></a>'#封面url正则
        r_title=r'<span class="anim_title_text"><a href=".*?"><h1>(.*?)</h1></a></span>'
        self.url=self.edit_url.text()
        headers={'use-agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",'Referer':'http://manhua.dmzj.com/tags/s.shtml'}
        try:
            text=requests.get(self.url,headers=headers).text
        except ConnectionError:
            traceback.print_exc()
            return False
        result_cover=re.findall(r_cover,text)
        if result_cover:
            cover_url=result_cover[0]
            if not (self.edit_dir.text()):
                dirname=os.path.join(os.path.abspath('./'),validatetitle(re.findall(r_title,text)[0]))
                self.edit_dir.setText(dirname)
                self.dir=dirname
            try:
                if self.show:
                    res=requests.get(cover_url,headers=headers)
                    if b'403' in res.content:
                        raise ValueError('Got cover img failed')
                    out=BytesIO(res.content)
                    out.seek(0)
                    Image.open(out).show()
                else:
                    print('使用自动设置')
            except (ConnectionError,ValueError):
                traceback.print_exc()
                return False
            return True
        else:
            self.url=''
            print('不正确的漫画地址，请重新指定')
            return False
        
    def crawl(self):
        if not self.url:
            print('请指定漫画地址！')
            return
        if not self.dir:
            self.show=False
            self.preview()
            self.show=True
        comic_url=self.url
        comic_title=None
        comic_dir=self.dir
        self.dir,self.url='',''
        self.parallel=(self.bt_parallel.isChecked() and cpu_count()>1)
        print(('使用多线程下载' if self.parallel else '使用单线程下载'))
        comic=Comic(comic_url,comic_title,comic_dir)
        comic.download_all_chapters_s(self.parallel)
if __name__ == "__main__":
    if sys.platform.startswith('win'):
        freeze_support()
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

