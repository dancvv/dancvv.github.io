# 第一次部署网站&一些想法


# 第一次部署网站&一些想法

## 一些废话
虽然这个标题叫‘第一次部署网站’，但其实我私下里已经部署过另外一个博客了，所以实际上是第二次。之前部署的博客是基于halo这个动态博客框架，为什么会放弃这个已经部署好的网站，而选择另外的框架呢？

主要原因是我比较折腾，halo提供的博客系统其实非常完善了，提供了完善的前后台管理，评论系统，搜索等功能，本来我也非常喜欢的。但是有一个缺点我不太能接受，它需要登录到博客系统后台才能开始写文章，当然你也可以在本地创作完稿子，再把它复制粘贴到后台，然后发布。这个操作也不是不行，对于喜欢本地Markdown创作，然后push到博客上的同学来说，感觉比较别扭。

其实，最为主要的原因是动态博客需要服务器来进行部署，服务器虽然不是太贵，以腾讯云的轻量云服务器来说，第一次购买一年74元，再搭上一个域名，小两百就没了，所以能白嫖就白嫖。

静态博客系统相比于动态博客的优点在于网站部署可以完全不用服务器，也就是说可以省掉74块钱乃至更多，毕竟服务器续费需要花更多钱。

## 正文

部署一个不花钱的博客，有比较多的选项，常用的Github Pages + Hugo/Hexo 等其他静态博客系统，如果觉得Github访问过慢，可以采用国内的Gitee Pages，又或者使用其他云服务商提供的CDN加速。个人推荐使用Hugo来构建自己的博客，倒也没啥太大的原因，就是因为我的电脑不能安装Hexo，就弃坑了（O(∩_∩)O哈哈~）。Hugo也很强大，Github 关注55.6k，而Hexo只有33.8k，用就用最热门的，出bug了也方便找。下面是部署使用的一些环境：

操作系统采用 Ubuntu 20.04 LTS，博客系统采用Hugo，静态托管使用Github Pages。

## Hugo安装和配置

Hugo的安装比较简单，Windows平台需要进入[Hugo官网](https://gohugo.io/)下载Hugo，Ubuntu只需要在终端输入以下命令：

```linux
sudo apt-get install hugo
```

不确定是否安装完成，可以验证一下：

```linux
hugo version
```

确认安装完成之后，找到一个喜欢的目录

```linux
hugo new site myfirstblog
```

运行以上的命令会生成一个`myfirstblog`文件夹，请熟记这个目录，他就是以后的大本营，可千万别给删了，这个文件夹里包含了博客系统的所有文件。

创建完一个博客项目后，去[官网](https://themes.gohugo.io/)选一个喜欢的主题

```linux
cd myfirstblog
git clone https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod 
```

在这里，我选择了一个比较经典的主题--PaperMod，使用git clone的方式下载themes文件夹中。每一个主题都有自己特有的配置，为了让这些配置生效，需要将它们写入到配置文档中。

Hugo提供了一个文档`config.toml`来编写自己的主题设置，该文件位于主目录下，以PaperMod主题为例，官方会提供一个完整的配置示例，在初期我们只要将这个配置复制粘贴就可以用了，后期上手之后可以做更多定制化的内容，配置如下：
```
baseURL: "https://examplesite.com/"
title: ExampleSite
paginate: 5
theme: PaperMod

enableRobotsTXT: true
buildDrafts: false
buildFuture: false
buildExpired: false

googleAnalytics: UA-123-45

minify:
  disableXML: true
  minifyOutput: true

params:
  env: production # to enable google analytics, opengraph, twitter-cards and schema.
  title: ExampleSite
  description: "ExampleSite description"
  keywords: [Blog, Portfolio, PaperMod]
  author: Me
  # author: ["Me", "You"] # multiple authors
  images: ["<link or path of image for opengraph, twitter-cards>"]
  DateFormat: "January 2, 2006"
  defaultTheme: auto # dark, light
  disableThemeToggle: false

  ShowReadingTime: true
  ShowShareButtons: true
  ShowPostNavLinks: true
  ShowBreadCrumbs: true
  ShowCodeCopyButtons: false
  disableSpecial1stPost: false
  disableScrollToTop: false
  comments: false
  hidemeta: false
  hideSummary: false
  showtoc: false
  tocopen: false

  assets:
    # disableHLJS: true # to disable highlight.js
    # disableFingerprinting: true
    favicon: "<link / abs url>"
    favicon16x16: "<link / abs url>"
    favicon32x32: "<link / abs url>"
    apple_touch_icon: "<link / abs url>"
    safari_pinned_tab: "<link / abs url>"

  label:
    text: "Home"
    icon: /apple-touch-icon.png
    iconHeight: 35

  # profile-mode
  profileMode:
    enabled: false # needs to be explicitly set
    title: ExampleSite
    subtitle: "This is subtitle"
    imageUrl: "<img location>"
    imageWidth: 120
    imageHeight: 120
    imageTitle: my image
    buttons:
      - name: Posts
        url: posts
      - name: Tags
        url: tags

  # home-info mode
  homeInfoParams:
    Title: "Hi there \U0001F44B"
    Content: Welcome to my blog

  socialIcons:
    - name: twitter
      url: "https://twitter.com/"
    - name: stackoverflow
      url: "https://stackoverflow.com"
    - name: github
      url: "https://github.com/"

  analytics:
    google:
      SiteVerificationTag: "XYZabc"
    bing:
      SiteVerificationTag: "XYZabc"
    yandex:
      SiteVerificationTag: "XYZabc"

  cover:
    hidden: true # hide everywhere but not in structured data
    hiddenInList: true # hide on list pages and home
    hiddenInSingle: true # hide on single page

  editPost:
    URL: "https://github.com/<path_to_repo>/content"
    Text: "Suggest Changes" # edit text
    appendFilePath: true # to append file path to Edit link

  # for search
  # https://fusejs.io/api/options.html
  fuseOpts:
    isCaseSensitive: false
    shouldSort: true
    location: 0
    distance: 1000
    threshold: 0.4
    minMatchCharLength: 0
    keys: ["title", "permalink", "summary", "content"]
menu:
  main:
    - identifier: categories
      name: categories
      url: /categories/
      weight: 10
    - identifier: tags
      name: tags
      url: /tags/
      weight: 20
    - identifier: example
      name: example.org
      url: https://example.org
      weight: 30
# Read: https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs#using-hugos-syntax-highlighter-chroma
# pygmentsUseClasses: true
# markup:
#     highlight:
#         # anchorLineNos: true
#         codeFences: true
#         guessSyntax: true
#         lineNos: true
#         style: monokai
```

上面的操作完成了骨干的构建，下面开始完善博客的血肉，即文章内容，创建一篇新的文章采用以下命令：

```linux
hugo new post/first.md
```

当前上面的操作准备就绪后，可以使用Hugo的功能进行本地预览

```linux
hugo server
```

开启服务后，在浏览器输入`http://localhost:1313`即可进入网站，在网站中可以看见刚下载好的主题和创建的第一篇文章。至此，Hugo的初步搭建就完成了，使用下面的命令可以完成Hugo的生产环境搭建：
```linux
hugo -D
```

## Github Pages配置
完成上面的工作之后，就可以进行下面的工作，将自己的静态博客部署到Github Pages上，实现全网访问(理论上，受限于国内的网络)。

进入Github官网，点击右上方的"+"，新建一个仓库，仓库名为"xxx.github.io"，第一个xxx必须为用户的昵称，没有商量的余地。比如我的Github用户名为"dancingmonkey"，那么仓库名就为"dancingmonkey.github.io"，这个极容易出错，不按照命名规则来，可能就要花很长时间来debug了。

仓库创建好之后，将博客目录下的public文件夹中的所有内容上传到该仓库：
```git
cd public
git init
git commit -m "first commit"
git remote add origin 仓库名
git push -u origin master
```
如果按照步骤来的话，每个配置都保持一致，那么这个时候你的博客就可以在全网访问了。追求更好的用户体验可以购买一个域名，在域名提供商的DNS解析处，将域名解析到对应的Github仓库名。同时，还需要在仓库的设置页面中，找到Pages设置项，在其中的Custom Domain(自定义域名)处输入自己购买的域名。

至此，使用Hugo和Github Pages搭建一个免费的静态博客就完成了，唯一需要额外花费的就是域名了。
