@echo off
set "strA=^<div^>"
set "strB=^</div^>
set "strC=hello"
set "strD=%strA%%strC%%strB%"
echo %strD%
pause

echo ��ӿ�����վ��
set svrIP=
set range=
set rangeIP=

set /p svrIP=�����������IP(�س�����):
echo "%svrIP%"
set range=HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Ranges\
echo "%range%"
set rangeIP=%range%%svrIP%
echo "%rangeIP%"
if not "%svrIP%"=="" (
    reg add "%rangeIP%" /f
    reg add "%rangeIP%" /v http /t REG_DWORD /d 2 /f
    reg add "%rangeIP%" /v :Range /t REG_SZ /d %svrIP% /f
    echo "%rangeIP%"
    echo "%svrIP%"
) else echo ������IPδ����.