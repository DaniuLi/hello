# 私有仓库搭建

## Docker Registry

官方提供了Docker Hub网站来作为一个公开的集中仓库。然而，本地访问Docker Hub速度往往很慢，并且很多时候我们需要一个本地的私有仓库只供网内使用。

Docker仓库实际上提供两方面的功能，一个是镜像管理，一个是认证。前者主要由docker-registry项目来实现，通过http服务来上传下载；后者可以通过docker-index（闭源）项目或者利用现成认证方案（如nginx）实现http请求管理。

docker-registry既然也是软件应用，自然最简单的方法就是使用官方提供的已经部署好的镜像registry。官方文档中也给出了建议，直接运行sudo docker run -p 5000:5000 registry命令。这样确实能启动一个registry服务器，但是所有上传的镜像其实都是由docker容器管理，放在了/var/lib/docker/....某个目录下。而且一旦删除容器，镜像也会被删除。因此，我们需要想办法告诉docker容器镜像应该存放在哪里。registry镜像中启动后镜像默认位置是/tmp/registry，因此直接映射这个位置即可，比如到本机的/opt/data/registry目录下。

## 不带安全认证的本地私有仓库

1. 下载私有仓库镜像

        [root@localhost ~]# docker pull registry
        Using default tag: latest
        latest: Pulling from library/registry
        90f4dba627d6: Pull complete 
        3a754cdc94a5: Pull complete 
        bf16d9b6d4c1: Pull complete 
        7eea83c9b7bb: Pull complete 
        23293c727551: Pull complete 
        Digest: sha256:f5552e60ffd56fecbe2f04b61a3089a9cd755bd9352b6b5ab22cf2208af6a3a8
        Status: Downloaded newer image for registry:latest

2. 通过该镜像启动一个容器

        [root@localhost ~]# docker run -d -p 5000:5000 -v /opt/data/registry:/tmp/registry registry
        0d042a2d7efe5f24becf343c26957b77c369054dd2e7c94d14d04f8a4df5715f

   参数说明： 

   -d：表示容器后台运行

   -p：端口映射

   --restart=always：可以理解为开机启动。开机：就是启动docker客户端拉。

   --name registry：给容器取一个名字，方便识别和记忆

   -v:挂在本地文件到容器中。命令格式：hostdir:cdir[:rw|ro] 主机目录:容器目录[:读写权限]
   
   具体参数可以参考[registry官方文档地址](https://docs.docker.com/registry/)

3. 客户端使用




## 搭建有安全认证的docker仓库私服
