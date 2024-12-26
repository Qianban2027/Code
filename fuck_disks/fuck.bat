@echo off
copy fuckE.bat e:
copy fuckF.bat f:
e:
start "fuckE" cmd /k call fuckE.bat
f:
start "fuckF" cmd /k call fuckF.bat