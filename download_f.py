# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 21:17:05 2017

@author: Quantum Liu
"""

from comic import *
import sys
def download_from_file(path,m=False):
    with open(path,'r') as f:
        ls=f.readlines()
    for l in ls:
        comic=Comic(l)
        comic.download_all_chapters_s(m)
if __name__=='__main__':
    path=(sys.argv[1] if len(sys.argv)>1 else './url.txt')
    print('Download comics based on file {f}'.format(f=path))
    m= (sys.argv[-1]=='1')
    if m:
        print('Using multi threads...')
    else:
        print('Using single thread...')
    download_from_file(path,m)