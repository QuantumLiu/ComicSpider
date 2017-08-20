pyinstaller -D -i batman.ico -p c:\Anaconda3\Lib\site-packages\PyQt5\Qt\bin comic_gui.py -y
pyinstaller -D download_f.py -n comicspider_console -i batman.ico -y
copy batman.ico .\dist\comicspider_console
copy url.txt .\dist\comicspider_console
copy batman.ico .\dist\comic_gui