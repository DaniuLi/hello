@echo off

echo To add trusted sites

set srvip=
set /p "srvip=Please enter server IP(pess Enter to skip):"
if defined srvip (
    set rangeip=HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet" "Settings\ZoneMap\Ranges\%srvip%
    reg add %rangeip% /f
    reg add %rangeip% /v http /t REG_DWORD /d 2 /f
    reg add %rangeip% /v :Range /t REG_SZ /d %srvip% /f
) else echo Sever IP is empty.

echo To set ActiveX controls and plug-ins
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v Flags /t REG_DWORD /d 67 /f  
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 2201 /t REG_DWORD /d 0 /f  
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1405 /t REG_DWORD /d 0 /f  
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1201 /t REG_DWORD /d 0 /f  
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 2000 /t REG_DWORD /d 0 /f  
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 120B /t REG_DWORD /d 0 /f  
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1004 /t REG_DWORD /d 0 /f  
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1001 /t REG_DWORD /d 0 /f  
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 2702 /t REG_DWORD /d 0 /f  
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1209 /t REG_DWORD /d 0 /f  
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1208 /t REG_DWORD /d 0 /f  
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1200 /t REG_DWORD /d 0 /f  
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 270C /t REG_DWORD /d 0 /f  
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 120A /t REG_DWORD /d 0 /f  

echo File Download: open
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1803 /t REG_DWORD /d 0 /f  

echo Clears the compatibility view list (Internet Explorer need to be restarted)
reg add "HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\BrowserEmulation\ClearableListData" /v UserFilter /t REG_DWORD /d 0 /f

set killIE=
set /p "killIE=Close Internet Explorer immediately (press Y to do)?:"
if "%killIE%"=="Y"  (
    taskkill /im IEXPLORE.EXE
) else echo Please restart Internet Explorer manually.

echo All settings completed!  
pause



