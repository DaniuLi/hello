################################################################################
# Chinese Comment:
# 网管版本号
#
# English Comment:
# OMM Versions
################################################################################
# 版本信息位于公共目录时，表示公共的版本号，此版本号必须是所有网元中最高的版本号
# 版本信息若位于网元目录时：
#           表示网元的版本号，网元版本可以不是最新的版本号，但必须是兼容的版本号
################################################################################
#COMM产品名
comm.version.name=COMM
#COMM产品名
comm.version.product=COMM
#主版本号
comm.version.main=V4.30.10
#次版本号
comm.version.patch=B26
#版本制作日期
comm.version.build=0

#OMM商务版本号
comm.app.version.display=V2.03.10.B17
#OMM外部版本号
comm.app.version.show=V2.03.10.B17

#OMM产品名
comm.app.version.name=COMM
#OMM显示产品名
comm.app.version.showname=iNMS
#OMM产品名
comm.app.version.product=COMM
#OMM节点号
comm.app.version.serviceid=100001

#是否显示Build 版本号
comm.app.version.showbversion=true
#是否显示Patch 版本号
comm.app.version.showpversion=true
#是否显示小Patch 版本号
comm.app.version.showspatch=true

#OMM版本号标示
comm.app.version.id=1.0
#OMM主版本号  格式 V*.**.**
comm.app.version.main.id=V4.30.10
#OMM子版本号
comm.app.version.patch.id=B26
#OMM性能统计版本号
comm.app.version.pm.version=1.1.1
#OMM告警版本号
comm.app.version.fm.version=2
################################################################################


################################################################################
# Chinese Comment:
# COMM公共信息
#
# English Comment:
# COMM COMMON message
################################################################################
#网元类型
comm.baseinfo.netype=COMM
#网元号
comm.baseinfo.nenum=1
#平台类型
comm.baseinfo.plattype=1
#网元ID(必须16进制,格式:0x+16*)
comm.baseinfo.netypeid=0x7FFFFFFFFFFFFFFF
#子网元类型
comm.baseinfo.nesubtype=COMM
#服务器语言类型，该字段为保留字，目前默认为操作系统的语言环境
comm.baseinfo.locale=en_US

#FTP类型，默认为SFTP
comm.ftp.protocol=SFTP
#需要响应OMS重启通知的组件列表
comm.OMS_MML.startnotify.neside.list=LICENSE,CLIS,IM
################################################################################
# Chinese Comment:
# 日志清理数据库持久化配置信息
#
# English Comment:
# Log Database Clearing Parameters Configuration
################################################################################
#操作日志保留天数
comm.app.log.clear.cmdlogday=60
#安全日志保留天数
comm.app.log.clear.securityday=60
#系统日志保留天数
comm.app.log.clear.syslogday=60
#每日清理时间点
comm.app.log.clear.clearingtime=2
#是否导出清理数据
comm.app.log.clear.ifexport=1
#导出文件存储路径
comm.app.log.clear.exportpath=log
#导出文件数目限制
comm.app.log.clear.exportfilenum=4
#日志清理国际化
comm.app.log.clear.funtionname_cn=日志管理
comm.app.log.clear.logname_cn=导出清理日志数据
comm.app.log.clear.detail_cn=处理日志的过期数据
comm.app.log.clear.funtionname_en=Log Management
comm.app.log.clear.logname_en=Export and Clear Log Data
comm.app.log.clear.detail_en=Deal with overdue data of log
################################################################################
# Chinese Comment:
# 跟踪管理属性配置
#
# English Comment:
# Trace information configration
################################################################################
#保存文件功能，自动保存个数
comm.tm.maxThread=5
#保存文件功能，写文件压缩阀值，单位K字节
comm.tm.fileSaveCompressSize=30
#保存文件功能，写文件缓冲区大小，单位K字节
comm.tm.fileBufferSize=80
#保存文件功能，每个文件记录写入间隔，即有记录距当前时间这么多间隔还没数据写入文件，则全部记录，单位秒
comm.tm.fileSaveWriteInterval=10
#保存文件功能，每个任务需要保存的文件个数，超过要删除最老的
comm.tm.maxFileNum=100
#CPU门限，超过此百分比，则停止所有跟踪
comm.tm.cpuRateLimit=80
#发送流量限制，单位K比特，超出要停止所有上报数据的跟踪任务
comm.tm.flowLimit=8000
#接收流量限制，单位条，超出停止所有跟踪任务
comm.tm.flowLimitNum=2000
#跟踪测试功能，设置为1，不向前台发消息，直接返回成功
comm.tm.testData=0

#跟踪压缩功能，设置为1，则所有消息等待压缩发送（废弃不用了）
comm.tm.isCompress=0
#跟踪条件是否需要心跳同步的指示，用于业务侧保存客户端临时发起的，不经过跟踪服务器跟踪条件（无心跳也不删除跟踪条件）
comm.tm.bl8IfHeartBeat=1
#是bl8IfHeartBeat为false场景下跟踪条件的存活期，业务进程需要定时删除
comm.tm.dwDuration=1
#解码结果压缩大小，超过这个值就进行压缩，单位K字节
comm.tm.decodecompresssize=1

#自动保存任务FTP最多重传次数
comm.tm.ftpMaxUpload=3
#自动保存任务FTP重传间隔，单位秒
comm.tm.ftpUploadInterval=10
#自动保存任务FTP文件信息最长保存时长，单位小时
comm.tm.ftpFileInfoSaveTime=24
#自动保存任务重起间隔,单位100毫秒(5分钟)
comm.tm.autosave.startinterval=3000

#CTS保存参数
#至少保存的时间,单位天
comm.tm.ctsfile.keep.days=3
#保存最多文件数
comm.tm.ctsfile.maxnum=100
#每个数据文件的条目数
comm.tm.ctsfile.all.item=5000


################################################################################
# Chinese Comment:
# CLIS属性配置(timeout请求超时时间单位:10秒)
#
# English Comment:
# CLIS information configration
################################################################################
comm.clis.dispthread.num=3
comm.clis.request.timeout=4
comm.clis.session.timeout=120
comm.clis.ems.session.timeout=30

comm.clis.ndf.enable=true
comm.clis.auth.enable=true
comm.clis.ackfilter.enable=true
comm.clis.cmdfilter.enable=false
comm.clis.chklicwhenlogin.enable=false
comm.clis.mml.loadsource.type=swf
comm.clis.entermode.mode.default=-9223372036854775808

################################################################################
# Chinese Comment:
# CM属性配置
# 全局空间: comm.cm
#
# English Comment:
# CM configrations
# namespace: comm.cm
################################################################################
# 需要支持的最大并发事务数量, 有效值: 10-255
comm.cm.MAX_TRANSACTION=64

# 一个事务内的最多命令数量,有效值: 10-1000
comm.cm.MAX_MML_PER_TRANSACTION=100

# 数据库连接空闲时间(有效性检查启用时有效) (分钟, 默认=30, 0-12h,0=disable)
comm.cm.DB_SESSION_IDLE_MINUTES=30

# 数据库连接有效性检测时间. (秒,默认60, 有效范围: 0 - 3600) , 0=disable)
comm.cm.DB_SESSION_CHECK_INTERVAL=0

# 大数据量写文件开关，缺省1-打开，0-关闭
comm.cm.ROWSETS_TO_CSV_ENABLE=1

# 大数据量写文件门限，缺省2000条写文件
comm.cm.ROWSETS_MAX_COUNT=2000


# 发送消息超时设定, 单位:秒, 有效值: 5-100
comm.cm.3GPL_TRANSLATE_TIMEOUT=50

# 是否发送平台持久化消息(调试用,1=启用/0=禁用)
#comm.cm.TRANSLATE_PLATFORM_MSG=1

# 是否记录日志(0关闭/1开启)
#comm.cm.LOG_ENABLED=1

#配置持久化日志文件路径(必须以/结束)
#comm.cm.LOG_FILE_PATH=../data/

# 日志缓冲数量(>0,<65535)
#comm.cm.LOG_BUFFER_NO=10

# 日志缓冲区超时入库时间(>0,<65535,单位:秒)
#comm.cm.LOG_BUFFER_TIME_OUT=600

# 是否记录本地配置持久化模型(0/1)
#comm.cm.LOG_LOCALE_PERSISTENT_MODEL=0

# 本地配置持久化模型位置(必须以/结束)
#comm.cm.PERSISTENT_MODEL_DIR=./models/

# 发送通知消息(开=1/关=0, 默认0)
#comm.cm.SEND_NOTIFY_MESSAGE=0

# 测试用VHLRID
#comm.cm.DEFINE_SYSVAR_VHLRID=0

# 大数据量写文件开关，缺省1-打开，0-关闭
comm.cm.ROWSETS_TO_CSV_ENABLE=1

# 大数据量写文件门限，缺省2000条写文件
comm.cm.ROWSETS_MAX_COUNT=2000

# 锁变化表服务-全局锁开关（1开启，0关闭）
comm.cm.USERLOCKSERVICE_GLBLOCK=1

# 锁变化表服务-用户锁开关（1开启，0关闭）
comm.cm.USERLOCKSERVICE_USERLOCK=1

# 锁变化表服务-变化表开关（1开启，0关闭）
comm.cm.USERLOCKSERVICE_CHGTABLE=1

# 锁变化表服务-离线开关（1离线，0在线）
comm.cm.USERLOCKSERVICE_OFFLINE=1

# 在线(增量)传送-传送后是否存盘
comm.cm.INCR_TRANS_SAVE_OMP=true

# EMS分用户开关（1开启，0关闭）
comm.cm.USERLOCKSERVICE_EMSFLAG=1

# 模型集路径(必须以/结束)
comm.cm.USERLOCKSERVICE_TRANSCONF_PATH=../mml/transconf/

#扩展备份基准文件需备份的表列表(表以逗号分割)
cm.sync.backup.banchmark.ext=CHG_TABLES

#数据传送与3G平台接口类型（sftp：SFTP方式，3gplat：文件管理方式）。默认为：3gplat
#comm.cm.FILE_MANAGER_UPLOAD_TYPE=3gplat
comm.cm.FILE_MANAGER_UPLOAD_TYPE=sftp

#3G平台的SFTP端口号（comm.cm.FILE_MANAGER_UPLOAD_TYPE取值为sftp时，才生效）
#comm.cm.FILE_MANAGER_FTP_PORT=22

#3G平台的SFTP用户名（comm.cm.FILE_MANAGER_UPLOAD_TYPE取值为sftp时，才生效）
#comm.cm.FILE_MANAGER_FTP_USER=

#3G平台的SFTP密码（comm.cm.FILE_MANAGER_UPLOAD_TYPE取值为sftp时，才生效）
#comm.cm.FILE_MANAGER_FTP_PASSWORD=


################################################################################
# Chinese Comment:
# IM属性配置
# 全局空间: comm.im
#
# English Comment:
# IM configrations
# namespace: comm.
################################################################################
# IM数据库绝对路径，安装的时候填写。
comm.im.db.path=/home/ngomm_data/ngomm_db/inms_254
#Oracle数据库的SID
comm.db.oraclesid=%ORACLE_SID%
#数据库的类型
comm.db.type=FIREBIRD
#网元数据库路径
comm.db.path=/home/ngomm_data/ngomm_db/inms_254

################################################################################
# Chinese Comment:
# PATROL属性配置
# 全局空间: comm.patrol
#
# English Comment:
# PATROL configrations
# namespace: comm.patrol
################################################################################
#巡检任务配置文件名
comm.patrol.itemconf=*-patrol-item-config.xml

#巡检对象配置文件名
comm.patrol.objext=*-patrol-objectgeter-extensionimpl.xml

#自动巡检结果保存时间，单位是天，缺省180天
comm.patrol.history=180
################################################################################
# Chinese Comment:
# BRM属性配置
# 全局空间: comm.brm
#
# English Comment:
# BRM configrations
# namespace: comm.brm
################################################################################
# 备份恢复在备份TABLE类型数据时的兼容性,缺省是V4,可覆盖为V3
comm.brm.table_compatibility=V4

# 备份失败是否调用备份后事件,缺省是0-不调用,可覆盖为1-调用
comm.brm.backupfailpost=0

# 恢复失败是否调用恢复后事件,缺省是0-不调用,可覆盖为1-调用
comm.brm.restorefailpost=0

# 恢复前台数据后是否复位单板，缺省是1-复位单板,可覆盖为0-不复位单板
comm.brm.restoreresetboard=1

# 备份恢复预计执行时间，单位毫秒，缺省是120000毫秒（即120秒），最小值-30000(即30秒),最大值-600000（即10分钟）
comm.brm.taskruntime=120000

# 恢复状态标志，0-未设置，1-设置
comm.brm.restorestatus=0

#EMS备份保留最大时间，单位秒，默认为：86400，即1天
comm.brm.ems.backupreservertime=86400

#备份恢复锁超时时间，各应用模块使用，通过该配置来确定超时时间，单位（分钟）
comm.brm.timeout=4

comm.sm.lock.period=65535
comm.sm.log.login=1
comm.sm.log.lock=1
comm.sm.log.userenable=1

comm.sm.pwdtactic.pwddictmaxlength=10000
comm.sm.pwdtactic.repeat=0

################################################################################
历史数据迁移的开始结束时间由应用在配置文件中指定，精确到秒，以5分钟为一个周期，默认120秒到290秒，
即每个5分钟区间内，从2分钟过后开始迁移，到4分50秒结束。
另外一次迁移后释放数据库锁休眠的时间也由应用在配置文件中指定，默认为3秒。
comm.pm.datatransfer.begintime //历史数据迁移开始时间点,默认值为120
comm.pm.datatransfer.endtime //历史数据迁移结束时间点,默认值为290
comm.pm.datatransfer.sleeptime//一次历史数据迁移后休息时间,默认值为3
comm.pm.datatransfer.transfernum//一次历史数据迁移的数据条数,默认值为10000
################################################################################
#巡检任务配置文件名
comm.pm.datatransfer.begintime=120
comm.pm.datatransfer.endtime=290
comm.pm.datatransfer.sleeptime=3
comm.pm.datatransfer.transfernum=10000

################
#网元内组件向OMP自注册会话
comm.oamsession.selfreg=1

#是否执行传送后自动备份
dbagent.backup.execable=true

#传送后自动备份超时时长(单位:秒)
dbagent.backup.waittime=1200

################################################################################
# Chinese Comment:
# 数据导入导出到EMS
# 全局空间: comm.export.ems
#
# English Comment:
# DBAPI configrations
# namespace: comm.export.ems
################################################################################
#EMS导出数据保留最大时间，单位秒，默认为：21600，即6小时
comm.export.ems.reservertime=21600
#EMS导出数据清理扫描间隔，单位秒，默认为：600，即10分钟
comm.export.ems.scanintervaltime=600
#EMS导出数据最大任务数量，默认为：1，即1个任务，不能执行多个任务
comm.export.ems.maxtaskcount=1
#EMS导出数据配置命令执行的APPNAME，默认为：cmRule
comm.export.ems.appname=cmRule
#MML命令超时时间，单位秒，默认为：60，即1分钟
comm.export.ems.mmltimeout=60
comm.im.lisence=1
#命令覆盖配置文件*-tablebrowser-override-cmd.xml是否生效，取值：0-不生效,1-生效；默认值：0-不生效
comm.export.ems.overridecmd=0

#ip协议栈支持是否共板的属性, 默认是非共板模式
ipstack.shareboard=false

################################################################################
#MML命令是否必须由admin用户执行开关，默认为true
#当配置项为true的时候，开关打开，相关命令必须只能有admin用户才能执行(假设在配置文件中没有配置，也默认为true)
#当配置项为false的时候，开关关闭，相关命令走命令鉴权通道，即有权限的用户就能执行此命令。
################################################################################

comm.mml.admin.execute.switch=true

################################################################################
# Chinese Comment:
# LICENSE属性配置
#
# English Comment:
# LICENSE information configration
################################################################################
#控制查询License项的缺省值,false 返回Licesne;true 返回 BOQ
comm.license.BOQ=false
@echo off

net start "ip helper"
netsh int ipv6 reset

netsh int teredo set state default
netsh int 6to4 set state default
netsh int isatap set state default
netsh int teredo set state server=teredo.remlab.net
netsh int ipv6 set teredo enterpriseclient
netsh int ter set state enterpriseclient
route DELETE ::/0
netsh int ipv6 add route ::/0 "Teredo Tunneling Pseudo-Interface"
netsh int ipv6 set prefix 2002::/16 30 1
netsh int ipv6 set prefix 2001::/32 5 1
Reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\Dnscache\Parameters /v AddrConfigControl /t REG_DWORD /d 0 /f

netsh int teredo set state default
netsh int 6to4 set state default
netsh int isatap set state default
netsh int teredo set state server=teredo.remlab.net
netsh int ipv6 set teredo enterpriseclient
netsh int ter set state enterpriseclient
route DELETE ::/0
netsh int ipv6 add route ::/0 "Teredo Tunneling Pseudo-Interface"
netsh int ipv6 set prefix 2002::/16 30 1
netsh int ipv6 set prefix 2001::/32 5 1
Reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\Dnscache\Parameters /v AddrConfigControl /t REG_DWORD /d 0 /f

ipconfig /all
ipconfig /flushdns
netsh int ipv6 show teredo
netsh int ipv6 show route
netsh int ipv6 show int
netsh int ipv6 show prefix
netsh int ipv6 show address
route print
cmd