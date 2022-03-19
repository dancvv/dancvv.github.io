# Docker安装常用的数据库


## 写在前面

在接触到Docker之后，发现他火起来不是没有道理的，极大的简化了安装过程，特别是本机还有一些老旧项目的数据库，但是又不能直接删掉弄新的。最近学习一个项目，需要安装各种数据，像MySQL，MongoDB之类的安装，只需要几个命令就能轻松搞起来。下面我会分章来讲解怎么利用Docker安装MySQL和MongoDB。
<!-- 和Redis数据库。 -->

## MySQL安装

1. 选择版本
选择需要安装的版本，可以直接在命令输入`docker search mysql`查询可用的版本，或者上docker hub上查询；

2. 拉取镜像
默认拉去最新版本的镜像
```docker
docker pull mysql:latest
```

3.查看本地镜像
使用`images`命令查看是否拉取下来：
```docker
docker images
```

4. 运行容器
使用`run`命令运行MySQL容器：
```docker
docker run -itd --name localsql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql
```
参数说明：
- -p 3306:3306 ：映射容器服务的 3306 端口到宿主机的 3306 端口，外部主机可以直接通过 宿主机ip:3306 访问到 MySQL 的服务。
- MYSQL_ROOT_PASSWORD=123456：设置 MySQL 服务 root 用户的密码。

还可以做一个改进，如果直接在容器内存放数据，一旦容器被误删，数据在没有做备份的情况下直接就丢失了，所以docker使用容器卷技术进行数据分离，类似于共享的概念。添加数据卷命令如下：
```docker
docker run -d --name localsql -v /data/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 mysql
```
5. 检查运行进程
运行完成之后使用`docker ps`检查使用成功运行。

## MongoDB安装
MongoDB的安装和MySQL的安装大同小异，因此下文对其具体操作进行简述，详细操作参照上节。
1. 选择版本
选择需要安装的版本，可以直接在命令输入`docker search mogond查询可用的版本，或者上docker hub上查询；

2. 拉取镜像
默认拉去最新版本的镜像
```docker
docker pull mongo:latest
```

3.查看本地镜像
使用`images`命令查看是否拉取下来：
```docker
docker images
```

4. 运行容器
使用`run`命令运行MySQL容器：
```docker
docker run -itd --name localmongo -p 27017:27017 -e mongo
```
参数说明：
- -p 3306:3306 ：映射容器服务的 3306 端口到宿主机的 3306 端口，外部主机可以直接通过 宿主机ip:3306 访问到 MySQL 的服务。
- MYSQL_ROOT_PASSWORD=123456：设置 MySQL 服务 root 用户的密码。

还可以做一个改进，如果直接在容器内存放数据，一旦容器被误删，数据在没有做备份的情况下直接就丢失了，所以docker使用容器卷技术进行数据分离，类似于共享的概念。添加数据卷命令如下：
```docker
docker run -itd -p 27017:27017 -v /data/mongo:/data/db --name localmongo mongo
```
在上面的命令中，几个命令参数的详细解释如下：
- -p 映射容器服务的 27017 端口到宿主机的 27017 端口。外部可以直接通过 宿主机 ip:27017 访问到 mongo 的服务
- -v 为设置容器的挂载目录，这里是将本机的“/data/mongo”目录挂载到容器中的/data/db中，作为 mongodb 的存储目录

5. 检查运行进程
运行完成之后使用`docker ps`检查使用成功运行。

<!-- ## Redis安装 -->


