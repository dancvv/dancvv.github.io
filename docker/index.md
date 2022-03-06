# Docker笔记


# Docker learning script

Docker 目前存在多个国内镜像，以阿里云网易云为主，可以选定永久的和临时的。加速服务需要去对应的网站选择，随后按照步骤配置进入本机

配置文档位于`/etc/sysconfig/docker`,，重启检查是否生效`service docker restart`.

运行hello world sample

## 基础命令

```docker
docker build 
docker pull
docker run 
```

## docker为什么快

容器，是一个运行时环境，也就是集装箱。比VM快的原因：
1. 有更少抽象层，不需要HyperVisor实现硬件资源虚拟化，因此运行效率更高
2. 利用宿主机的内核，而不需要Guest OS。当新建一个虚拟机时， 虚拟机需要重新加载一个操作系统内核。而docker直接利用宿主机内核，因此加载速度极快。



## docker 常用命令

### 镜像命令  
鲸鱼背上有大海  
蓝色的大海中 >>>>> 宿主机系统
鲸鱼 >>>>> docker  
集装箱 >>>>> 容器实例   from 来自我们能的镜像模板

-  `docker images`
> 列出本地主机的镜像
> 可以使用唯一ID和仓库名来管理
```docker
-a 列出本地所有的镜像（含中间镜像层）
-q 只显示当前镜像的id
--digests 描述消息
--no-trunc 显示完整信息
```

- `docker search`
> 搜索某个镜像名字
> 搜索网站为docker hub

- `docker pull`
> 从官方抓取镜像
> 没写版本号，代表直接抓取最新版本
> docker pull tomact 等价 docker pull tomcat:latest

-`docker rmi`
> 移除镜像，remove images
> -f 强制删除
> docker rmi -f 镜像ID
> docker rmi -f 镜像名1：tag 镜像名2：tag
> 删除全部`docker rmi -f $(docker images -qa)`
> 子命令解释，查询出docker所有镜像id，并删除

### 容器命令
可以把容器看为一个简易版的Linux系统。**有镜像才能创建容器**，这是一个根本性的前提
> 新建并启动容器 `docker run [options] image [command]`
> > --name 重命名,将容器名
> `docker run -it --name mycentos centos` 将centos重命名为mycentos
> > -i 以交互模式运行容器，通常与-t同时使用
> > -t 为容器重新分配一个伪输入终端，通常-i同时使用

- 查看容器
> `docker ps`查看当前所有进程
> > -a 列出所有正在运行的容器+历史上运行过的
> -l 最后一次运行的
> -n 显示最近n个创建的容器
> -q **静默模式，只显示容器编号**
> 以上命令都可以组合使用

- 容器重命名
`docker rename oldName newName`   
对部分容器重新命名

- 启动容器

`docker start 容器ID或者容器名`

- 退出容器

```docker
    exit容器停止退出
    ctrl + p + q容器不停止退出
```
- 重启容器

> `docker restart ID`

- 关闭容器

> kill 直接删除掉该进程
> stop 温柔一些的停止

- 删除容器

> `docker rm 容器ID`
> -f 强制删除
> 一次性删除多个镜像
```docker
    docker rm -f $(docker ps -a -q)
    docker ps -a -q | xargs docker rm
```

- 运行容器

该命令启动守护式容器
`docker run -d centos`  
使用centos：latest，以后台模式启动一个容器
前台启动，交互形式-it  

- 日志打印

`docker logs`

查看容器内的运行进程
`docker top 用户id`

查看容器内部细节
`docker inspect 容器id`

- 重新进入容器内环境
退出后进入容器，exec和attach的区别
attach
> 进入已经启动的容器终端，不会启动新的进程
> `docker attach 容器id`
exec
> 是在容器中打开新的终端，并且可以启动新的进程
`docker exec -t 容器id ls -l /tmp`  

- 容器内拷贝文件到本机
`docker cp 容器ID 基本路径`
从主机复制到容器`sudo docker cp host_path containerID:container_path`  
从容器复制到主机`sudo docker cp containerID:container_path host_path`

## Docker镜像
- UnionFS
联合文件系统，是一种分层、轻量级并且高性能的文件系统，支持对文件系统的修改作为一次提交来一层层的叠加。  
- 好处
**共享资源**，如果有多个镜像都从base镜像构建而来，那么宿主机只需在磁盘上保存一份base镜像。

- 特点
镜像都是只读的，这一层通常称作容器层，容器层之下的称作镜像层

- commit命令
`docker commit` 提交容器副本使之成为一个新的镜像  
`docker commit -m ="提交的描述信息" -a="作者"` 容器ID要创建的目标镜像名:[标签名]
`docker commit -m ="description" -a="author" newName:1.2`

`docker run -it -p 8080:8080 tomcat`
-p 本地端口:docker端口
-P 随机分配端口

### 容器数据卷
为了放置删除镜像后数据丢失，保存数据，使用卷，完全独立于容器之外的  
完全容器的持久化，容器间继承+共享数据

### 数据卷
容器内添加：直接命令添加，DockerFile添加
- 直接命令添加
`docker run -it -v /宿主机绝对路径目录：/容器目录 镜像名`
> OS X系统链接必须采用绝对路径，以及将`/var`添加进docker设置中的resources>file sharing
> `docker run -it -v /Users/weivang/dataVolume:/datalum centos`
> 带权限的命令
> `docker run -it -v /宿主机绝对路径目录：/容器目录:ro 镜像名`
> 该命令进入之后，不可进行写操作，**仅可读操作**

- 验证映射链接成功
`docker inspect 容器id`

### DockerFile添加
根目录下新建一个DockerFile文件，使用Volume指令添加  
使用DockerFile是出于可移植和分享的考虑;由于宿主机目录是依赖于特定宿主机的，并不能保证所有的宿主机都存在这样的特定目录。

DockerFile文件

```docker
# DockerFile构建
    FROM centos
    VOLUME ["/dataVolume1","/dataVolume2"]
    CMD echo "finished，-----successed"
    CMD echo "finished，-----successed"

```
文件构建命令`docker build -f `
使用dockerfile构建的容器自动挂载的数据卷，docker会在宿主机目录自动生成对应的文件

### 数据卷容器
其他容器可以通过已经挂载在父容器上的数据卷实现数据共享，挂载数据卷的容器，称之为数据卷容器。   
实现数据共享，一条绳上的蚂蚱。  

`-volumes-from`复制容器数据卷

容器之间配置信息的传递，数据卷的生命周期一直持续到没有容器使用为止

## DockerFile解析
Dockerfile是用来构建Docker镜像的构建文件，是由一系列命令和参数构成的脚本。   
- 基础知识
每条保留字指令都必须为大写字母，且后面要跟随至少一个参数   
从上到下，顺序执行
- 大致流程
从基础镜像运行一个容器   
执行一条指令对容器进行修改。

从应用软件的角度来看，DockerFile、Docker镜像与Docker容器分别代表软件的三个不同阶段。
> * DockerFile是软件的原材料
> * Docker镜像是软件的交付品
> * Docker容器则可以认为是软件的运行态

- DockerFile体系结构，保留字指令
> FROM 基础镜像
> MAINTAINER 维护者
> RUN 执行的命令
> EXPOSE 暴露接口
> WORKDIR 工作目录，终端默认登录之后的工作目录
> ENV 用来在构建镜像过程中设置环境变量
> ADD 拷贝+解压缩
> COPY 复制
> VOLUME 容器数据卷
> CMD 容器启动时要运行的命令
> ENTRYPOINT 指定一个容器时要运行的命令,ENTRYPOINT的目的和CMD一样，都是在指定容器启动程序及参数
> ONBUILD 父镜像在子镜像被继承后，父镜像的onbuild被触发

- 案例
自定义一个centos镜像，使得镜像mycentos自己的镜像具备如下：
> 登录后的默认路径
> vim编辑器
> 查看网络配置ifconfig支持

```docker
    FROM CENTOS

    ENV mypath /tmp
    WORKDIR $mypath

    RUN yum -y install vim
    RUN yun -y install net-tools

    EXPOSE 80

    CMD echo $mypath
    CMD echo "success ----- ok"
    CMD /bin/bash

```
构建，`docker build -t 新镜像名字:tag .`，注：最后的 . 代表本次执行的上下文路径，下一节会介绍。   
运行，`docker run -it 新镜像名字:tag`
列出镜像的变更历史，`docker history 镜像名`

CMD和entrypoint的区别

## 安装mysql及使用
```docker
    docker search mysql
    docker pull mysql:5.6
    docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7
    除了这种方式外，还可以挂载数据卷，以mac为例，Linux同样的操作，就是要注意路径为绝对路径不然容易出错
    docker run -p 3306:3306 -v /Users/weivang/DataVolume/mysql:/var/lib/mysql --name mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7
    停止mysql之后，使用restart命令重新进入
    docker restart 容器id
```


