@echo off
echo IE�����У��벻Ҫ�ر��������  

echo ��ӿ�����վ��
set svrIP=
set range=
set rangeIP=
set /p svrIP=�����������IP(�س�����):
set range=HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Ranges\
set rangeIP=%range%%svrIP%
if not "%svrIP%"=="" (
    reg add "%rangeIP%" /f
    reg add "%rangeIP%" /v http /t REG_DWORD /d 2 /f
    reg add "%rangeIP%" /v :Range /t REG_SZ /d %svrIP% /f
) else echo ������IPδ����.

echo ȥ���Ը�����������վ��Ҫ���������֤(https://)
::[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2]
::0x00000043(67)=������ 0x00000047(71)=����
::"Flags"=dword:67
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v Flags /t REG_DWORD /d 67 /f  

echo ActiveX �ؼ��Ͳ�� - ��ʼ
::--------------------------------------------------
echo ActiveX�ؼ��Զ���ʾ:����
::(3�����á�0������)
::"2201"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 2201 /t REG_DWORD /d 0 /f  

echo �Ա��Ϊ�ɰ�ȫִ�нű���ActiveX�ؼ�ִ�нű�:����
::(3�����á�0�����á�1����ʾ)
::"1405"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1405 /t REG_DWORD /d 0 /f  

echo ��δ���Ϊ�ɰ�ȫִ�нű���ActiveX�ؼ���ʼ����ִ�нű�:����
::(3�����á�0�����á�1����ʾ)
::"1201"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1201 /t REG_DWORD /d 0 /f  

echo �����ƺͽű���Ϊ:����
::(3�����á�0�����á�10000������Ա�Ͽ�)
::"2000"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 2000 /t REG_DWORD /d 0 /f  

echo ����������׼������δ����ʾ�������ʹ��ActiveX:����
::(0�����á�3������)
::XP+IE6�����ڴ���
::"120B"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 120B /t REG_DWORD /d 0 /f  

echo ����δǩ����ActiveX�ؼ�:����
::(3�����á�0�����á�1����ʾ)
::"1004"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1004 /t REG_DWORD /d 0 /f  

echo ������ǩ����ActiveX�ؼ�:����
::(3�����á�0�����á�1����ʾ)
::"1001"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1001 /t REG_DWORD /d 0 /f  

echo ����ActiveXɸѡ:����
::(3�����á�0������)
::XP+IE6�����ڴ���,Win7+IE8�����ڴ���
::"2702"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 2702 /t REG_DWORD /d 0 /f  

echo ����Scriptlet:����
::(3�����á�0�����á�1����ʾ)
::XP+IE6�����ڴ���
::"1209"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1209 /t REG_DWORD /d 0 /f  

echo ����������ǰδʹ�õ�ActiveX�ؼ�������ʾ:����
::(3�����á�0������)
::XP+IE6�����ڴ���
::"1208"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1208 /t REG_DWORD /d 0 /f  

echo ����ActiveX�ؼ��Ͳ��:����
::(3�����á�0�����á�1����ʾ��10000=����Ա�Ͽ�)
::"1200"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1200 /t REG_DWORD /d 0 /f  

echo ��ActiveX�ؼ������з��������:����
::(3�����á�0������)
::"270C"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 270C /t REG_DWORD /d 0 /f  

echo ��û��ʹ���ⲿý�岥�Ż�����ҳ����ʾ��Ƶ�Ͷ���:����
::(3�����á�0������)
::XP+IE6�����ڴ���
::"120A"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 120A /t REG_DWORD /d 0 /f  

::--------------------------------------------------
::ActiveX �ؼ��Ͳ�� - ����

echo �ļ�����:����
::(3�����á�0������)
::"1803"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1803 /t REG_DWORD /d 0 /f  

echo ���洢��ҳ��Ľ��°汾:ÿ�η�����ҳʱ(���������������������Ч,���Ժ��ֶ�����IE�����.)
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v SyncMode5 /t REG_DWORD /d 3 /f

echo ��ռ�������ͼ�б�(���������������������Ч,���Ժ��ֶ�����IE�����.)
reg add "HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\BrowserEmulation\ClearableListData" /v UserFilter /t REG_DWORD /d 0 /f
echo �����ѡ(�ڼ�������ͼ����ʾIntranetվ��)
reg add "HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\BrowserEmulation" /v IntranetCompatibilityMode /t REG_DWORD /d 0 /f
echo �����ѡ(ʹ��Microsoft�������б�)
reg add "HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\BrowserEmulation" /v MSCompatibilityMode /t REG_DWORD /d 0 /f

::set killIE=
::set /p killIE=�����ر�IE����� (ȷ���밴Y)?:
::echo %killIE%
::if "%killIE%"=="Y" (
::    taskkill /im IEXPLORE.EXE
::) else echo ���Ժ��ֶ�����IE�����.

echo ȫ�����ý���!  
pause


