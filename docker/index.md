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
> > --name 重命名
> `docker run -it --name mycentos centos` 将centos重命名为mycentos
> > -i 以交互模式运行容器，通常与-t同时使用
> > -t 为容器重新分配一个伪输入终端，通常-i同时使用

- 查看容器
> `docker ps`查看当前所有进程
> > -a 列出所有正在运行的容器+历史上运行过的
> -l 上一次运行的
> -n 显示最近n个创建的容器
> -q **静默模式，只显示容器编号**
> 以上命令都可以组合使用

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
