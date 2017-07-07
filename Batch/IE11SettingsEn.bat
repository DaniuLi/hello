@echo off

echo To add trusted sites
set svrIP=
set range=
set rangeIP=

set /p svrIP=Please enter server IP(pess Enter to skip):
set range=HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Ranges\
set rangeIP=%range%%svrIP%
if not "%svrIP%"=="" (
    reg add "%rangeIP%" /f
    reg add "%rangeIP%" /v http /t REG_DWORD /d 2 /f
    reg add "%rangeIP%" /v :Range /t REG_SZ /d %svrIP% /f
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

echo File Download:open
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1803 /t REG_DWORD /d 0 /f  

echo Internet Settings-SyncMode(Internet Explorer need to be restarted,Please restart Internet Explorer manually.)
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v SyncMode5 /t REG_DWORD /d 3 /f

echo Clears the compatibility view list (Internet Explorer need to be restarted,Please restart Internet Explorer manually.)
reg add "HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\BrowserEmulation\ClearableListData" /v UserFilter /t REG_DWORD /d 0 /f

echo Clear the IntranetCompatibilityMode
reg add "HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\BrowserEmulation" /v IntranetCompatibilityMode /t REG_DWORD /d 0 /f

echo Clear the MSCompatibilityMode
reg add "HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\BrowserEmulation" /v MSCompatibilityMode /t REG_DWORD /d 0 /f

::set killIE=
::set /p "killIE=Close Internet Explorer immediately (press Y to do)?:"
::if "%killIE%"=="Y"  (
::    taskkill /im IEXPLORE.EXE
::) else echo Please restart Internet Explorer manually.

echo All settings completed!  
pause



