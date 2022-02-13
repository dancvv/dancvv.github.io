# Springdoc


# SpringBoot生成OpenAPI 3.0文档

## 概述
开发过程中需要写大量的接口文档，如果手写的话需要花费一定的时间，并且还需要额外的时间进行维护，为了避免这样的情况，开发人员可以引入文档管理工具进行自动生成。

目前，可以生成RESTful风格文档最为成熟，规范且完整的框架是Swagger。国内局大部分人还在用过时的Swagger2，已于17年停止维护并更名为Swagger3。

但是，本文并不会使用Swagger，而是使用与之类似的springdoc-openapi，这也是一个基于OpneAPI 3的Java库，帮助Spring boot工程自动生成API文档。在运行时检查应用程序，来推断基于spring配置，类结构和各种注释的API语义，同时，还支持Swagger-ui界面。


## pom引入
整合spring-boot和swagger-ui，添加以下的依赖即可完成，不需要其他的设置
```maven
    <dependency>
        <groupId>org.springdoc</groupId>
        <artifactId>springdoc-openapi-ui</artifactId>
        <version>1.6.6</version>
    </dependency>
```
这个依赖会自动部署swagger-ui到spring-boot应用：
* 文档以HTML的形式展现
* 文档也可以yaml格式展现，路径如下：`/v3/api-docs.yaml`

## 文档设置
* swagger-ui路径
自定义访问路径
```java
    springdoc.swagger-ui.path=/swagger-ui.html
```
* swagger-ui开启
是否开启功能
```java
    springdoc.api-docs.enabled=true
```
简单的配置之后，启动项目，在本地端口加上自定义的路径就可以进入API接口文档。以默认项目8080端口为例，其访问路径为`htttp://localhost:8080/swagger-ui.html`
