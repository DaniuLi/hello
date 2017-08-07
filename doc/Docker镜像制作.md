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



示例说明如下：

1. 新建一个名为 Dockerfile 的文件。

2. 在 Docker 文件里描述镜像的构建过程。典型的流程为：
- [1] 引入基础镜像，如本例中的 ubuntu:14.04。
- [2] 在该基础镜像上安装一系列软件，如本例中通过 apt-get 命令来安装了 mysql 以及相关的组件。
- [3] 对软件进行配置。如本例中配置了 mysql 的挂载目录、工作目录、对外暴露的端口号等等。
- [4] 设置容器运行后要执行的命令，例如本例中，设置了当容器运行时，需要通过mysqld_safe 命令来启动 mysql 服务器（上述 FROM， RUN， VOLUME， EXPOSE， CMD 等命令都是 Dockerfile 文件的基本语法元素，可以查看具体[官方文档](https://docs.docker.com/engine/reference/builder/)了解使用方式。）

3. 通过 docker build 命令来制作镜像文件。 -t 选项为镜像取名， .则表示 Docker 文件在当前目录中。

4. 通过 docker images 命令，可以查看新创建的镜像文件。

5. 最后，通过 docker run 命令利用新建的镜像开启一个容器，从打印中可以看到 mysql服务已经生效了