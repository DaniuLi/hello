@echo off
echo IE设置中，请不要关闭这个窗口  

echo 添加可信任站点
set svrIP=
set range=
set rangeIP=
set /p svrIP=请输入服务器IP(回车跳过):
set range=HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Ranges\
set rangeIP=%range%%svrIP%
if not "%svrIP%"=="" (
    reg add "%rangeIP%" /f
    reg add "%rangeIP%" /v http /t REG_DWORD /d 2 /f
    reg add "%rangeIP%" /v :Range /t REG_SZ /d %svrIP% /f
) else echo 服务器IP未输入.

echo 去掉对该区域中所有站点要求服务器验证(https://)
::[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2]
::0x00000043(67)=不启用 0x00000047(71)=启用
::"Flags"=dword:67
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v Flags /t REG_DWORD /d 67 /f  

echo ActiveX 控件和插件 - 开始
::--------------------------------------------------
echo ActiveX控件自动提示:启用
::(3＝禁用、0＝启用)
::"2201"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 2201 /t REG_DWORD /d 0 /f  

echo 对标记为可安全执行脚本的ActiveX控件执行脚本:启用
::(3＝禁用、0＝启用、1＝提示)
::"1405"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1405 /t REG_DWORD /d 0 /f  

echo 对未标记为可安全执行脚本的ActiveX控件初始化并执行脚本:启用
::(3＝禁用、0＝启用、1＝提示)
::"1201"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1201 /t REG_DWORD /d 0 /f  

echo 二进制和脚本行为:启用
::(3＝禁用、0＝启用、10000＝管理员认可)
::"2000"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 2000 /t REG_DWORD /d 0 /f  

echo 仅允许经过批准的域在未经提示的情况下使用ActiveX:禁用
::(0＝禁用、3＝启用)
::XP+IE6不存在此项
::"120B"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 120B /t REG_DWORD /d 0 /f  

echo 下载未签名的ActiveX控件:启用
::(3＝禁用、0＝启用、1＝提示)
::"1004"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1004 /t REG_DWORD /d 0 /f  

echo 下载已签名的ActiveX控件:启用
::(3＝禁用、0＝启用、1＝提示)
::"1001"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1001 /t REG_DWORD /d 0 /f  

echo 允许ActiveX筛选:启用
::(3＝禁用、0＝启用)
::XP+IE6不存在此项,Win7+IE8不存在此项
::"2702"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 2702 /t REG_DWORD /d 0 /f  

echo 允许Scriptlet:启用
::(3＝禁用、0＝启用、1＝提示)
::XP+IE6不存在此项
::"1209"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1209 /t REG_DWORD /d 0 /f  

echo 允许运行以前未使用的ActiveX控件而不提示:启用
::(3＝禁用、0＝启用)
::XP+IE6不存在此项
::"1208"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1208 /t REG_DWORD /d 0 /f  

echo 运行ActiveX控件和插件:启用
::(3＝禁用、0＝启用、1＝提示、10000=管理员认可)
::"1200"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1200 /t REG_DWORD /d 0 /f  

echo 在ActiveX控件上运行反恶意软件:启用
::(3＝禁用、0＝启用)
::"270C"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 270C /t REG_DWORD /d 0 /f  

echo 在没有使用外部媒体播放机的网页上显示视频和动画:启用
::(3＝禁用、0＝启用)
::XP+IE6不存在此项
::"120A"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 120A /t REG_DWORD /d 0 /f  

::--------------------------------------------------
::ActiveX 控件和插件 - 结束

echo 文件下载:启用
::(3＝禁用、0＝启用)
::"1803"=dword:0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v 1803 /t REG_DWORD /d 0 /f  

echo 检查存储的页面的较新版本:每次访问网页时(该设置需重启浏览器后生效,请稍候手动重启IE浏览器.)
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v SyncMode5 /t REG_DWORD /d 3 /f

echo 清空兼容性视图列表(该设置需重启浏览器后生效,请稍候手动重启IE浏览器.)
reg add "HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\BrowserEmulation\ClearableListData" /v UserFilter /t REG_DWORD /d 0 /f
echo 清除勾选(在兼容性视图中显示Intranet站点)
reg add "HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\BrowserEmulation" /v IntranetCompatibilityMode /t REG_DWORD /d 0 /f
echo 清除勾选(使用Microsoft兼容性列表)
reg add "HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\BrowserEmulation" /v MSCompatibilityMode /t REG_DWORD /d 0 /f

::set killIE=
::set /p killIE=立即关闭IE浏览器 (确认请按Y)?:
::echo %killIE%
::if "%killIE%"=="Y" (
::    taskkill /im IEXPLORE.EXE
::) else echo 请稍候手动重启IE浏览器.

echo 全部设置结束!  
pause


