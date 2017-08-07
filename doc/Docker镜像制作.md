# 镜像的制作

镜像包的制作有两种方法，一种是在容器内部修改后，直接通过 docker commit 命令来生成新的镜像包，另一种是通过编写 Dockerfile 来描述镜像包的构建过程，并通过docker build 命令来生成，这里对这两种方法做一个介绍

## 用commit命令制作镜像

1. 运行ubuntu容器，并执行bash，-i 参数保持输入打开， -t 分配一个伪终端

        [root@localhost ~]# docker run -i -t ubuntu bash
        root@3b102b069e4a:/# 


2. 宿主机上运行拷贝宿主机jdk目录到容器。3b102b069e4a 为容器ID

        [root@localhost jvm]# docker cp java-1.8.0-openjdk-1.8.0.141-1.b16.el7_3.x86_64/ 3b102b069e4a:/usr/local/

3. 配置环境变量
        
        root@3b102b069e4a:/usr/local# vi /etc/profile

        export JAVA_HOME=/usr/local/java-1.8.0-openjdk-1.8.0.141-1.b16.el7_3.x86_64
        export PATH=$JAVA_HOME/bin:$PATH
        export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar

4. 退出docker容器        

        root@3b102b069e4a:/usr/local# exit

5. 查看刚才运行的容器
        
        [root@localhost ~]# docker ps -a
        CONTAINER ID        IMAGE               COMMAND                   CREATED             STATUS                        PORTS               NAMES
        3b102b069e4a        ubuntu              "bash"                    24 minutes ago      Exited (130) 5 seconds ago                        confident_lumiere
6. 查看不同，3b102b069e4a为容器ID。

        [root@localhost ~]# docker diff 3b102b069e4a
        C /root
        A /root/.bash_history
        C /var
        C /var/lib
        C /var/lib/apt
        C /var/lib/apt/lists
        A /var/lib/apt/lists/lock
        A /var/lib/apt/lists/partial
        C /usr
        C /usr/local
        A /usr/local/java-1.8.0-openjdk-1.8.0.141-1.b16.el7_3.x86_64
        A /usr/local/java-1.8.0-openjdk-1.8.0.141-1.b16.el7_3.x86_64/jre
        A /usr/local/java-1.8.0-openjdk-1.8.0.141-1.b16.el7_3.x86_64/jre/bin
        ...

7. 创建镜像
    
        [root@localhost hello]# docker commit -m "add jdk8" 3b102b069e4a
        sha256:4f9bab60d59d134bd9b7d0b19f527b07d4f81428c221c2e623ebfbafde80fce0

    注：仓库名和TAG没有填写

8. 查看是否生成成功


        [root@localhost hello]# docker images
        REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
        <none>              <none>              4f9bab60d59d        9 seconds ago       250MB
        ubuntu              latest              14f60031763d        2 weeks ago         120MB


## 用Dockerfile制作镜像

此处仅为示例，详细用法请参考[官方文档](https://docs.docker.com/engine/reference/builder/)。

