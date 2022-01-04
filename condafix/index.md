# conda报错：An unexpected error has occurred. Conda has prepared the above report. Upload did not complete.

# 创建conda环境，激活其他虚拟环境时报错
今天本来正常从github找到一个项目，打算按照常规操作跑起来看看结果，结果一下子出现一堆报错，一下子慌了神，bing（必应）了半天总算找到症结所在。

## 问题复现

创建环境、切换环境时，出现以下报错信息：

```powershell
C:\Users\windows>conda create -n na python=3.6
Collecting package metadata (current_repodata.json): failed

# >>>>>>>>>>>>>>>>>>>>>> ERROR REPORT <<<<<<<<<<<<<<<<<<<<<<

    Traceback (most recent call last):
      File "D:\ProgramData\Anaconda3\lib\site-packages\conda\exceptions.py", line 1079, in __call__
        return func(*args, **kwargs)
      File "D:\ProgramData\Anaconda3\lib\site-packages\conda\cli\main.py", line 84, in _main
        exit_code = do_call(args, p)
      File "D:\ProgramData\Anaconda3\lib\site-packages\conda\cli\conda_argparse.py", line 83, in do_call
        return getattr(module, func_name)(args, parser)
      File "D:\ProgramData\Anaconda3\lib\site-packages\conda\cli\main_create.py", line 41, in execute
        install(args, parser, 'create')
      File "D:\ProgramData\Anaconda3\lib\site-packages\conda\cli\install.py", line 261, in install
        unlink_link_transaction = solver.solve_for_transaction(
      File "D:\ProgramData\Anaconda3\lib\site-packages\conda\core\solve.py", line 114, in solve_for_transaction
        unlink_precs, link_precs = self.solve_for_diff(update_modifier, deps_modifier,
      File "D:\ProgramData\Anaconda3\lib\site-packages\conda\core\solve.py", line 157, in solve_for_diff
        final_precs = self.solve_final_state(update_modifier, deps_modifier, prune, ignore_pinned,
      File "D:\ProgramData\Anaconda3\lib\site-packages\conda\core\solve.py", line 262, in solve_final_state
        ssc = self._collect_all_metadata(ssc)
      File "D:\ProgramData\Anaconda3\lib\site-packages\conda\common\io.py", line 88, in decorated
        return f(*args, **kwds)
      File "D:\ProgramData\Anaconda3\lib\site-packages\conda\core\solve.py", line 425, in _collect_all_metadata
        index, r = self._prepare(prepared_specs)
      File "D:\ProgramData\Anaconda3\lib\site-packages\conda\core\solve.py", line 1020, in _prepare
        reduced_index = get_reduced_index(self.prefix, self.channels,
      File "D:\ProgramData\Anaconda3\lib\site-packages\conda\core\index.py", line 288, in get_reduced_index
        new_records = SubdirData.query_all(spec, channels=channels, subdirs=subdirs,
      File "D:\ProgramData\Anaconda3\lib\site-packages\conda\core\subdir_data.py", line 140, in query_all
        result = tuple(concat(executor.map(subdir_query, channel_urls)))
      File "D:\ProgramData\Anaconda3\lib\concurrent\futures\_base.py", line 611, in result_iterator
        yield fs.pop().result()
      File "D:\ProgramData\Anaconda3\lib\concurrent\futures\_base.py", line 439, in result
        return self.__get_result()
      File "D:\ProgramData\Anaconda3\lib\concurrent\futures\_base.py", line 388, in __get_result
        raise self._exception
      File "D:\ProgramData\Anaconda3\lib\concurrent\futures\thread.py", line 57, in run
        result = self.fn(*self.args, **self.kwargs)
      File "D:\ProgramData\Anaconda3\lib\site-packages\conda\core\subdir_data.py", line 132, in <lambda>
        subdir_query = lambda url: tuple(SubdirData(Channel(url), repodata_fn=repodata_fn).query(
      File "D:\ProgramData\Anaconda3\lib\site-packages\conda\core\subdir_data.py", line 145, in query
        self.load()
      File "D:\ProgramData\Anaconda3\lib\site-packages\conda\core\subdir_data.py", line 209, in load
        _internal_state = self._load()
      File "D:\ProgramData\Anaconda3\lib\site-packages\conda\core\subdir_data.py", line 371, in _load
        raw_repodata_str = fetch_repodata_remote_request(
      File "D:\ProgramData\Anaconda3\lib\site-packages\conda\core\subdir_data.py", line 694, in fetch_repodata_remote_request
        resp = session.get(join_url(url, filename), headers=headers, proxies=session.proxies,
      File "D:\ProgramData\Anaconda3\lib\site-packages\requests\sessions.py", line 555, in get
        return self.request('GET', url, **kwargs)
      File "D:\ProgramData\Anaconda3\lib\site-packages\requests\sessions.py", line 542, in request
        resp = self.send(prep, **send_kwargs)
      File "D:\ProgramData\Anaconda3\lib\site-packages\requests\sessions.py", line 655, in send
        r = adapter.send(request, **kwargs)
      File "D:\ProgramData\Anaconda3\lib\site-packages\requests\adapters.py", line 439, in send
        resp = conn.urlopen(
      File "D:\ProgramData\Anaconda3\lib\site-packages\urllib3\connectionpool.py", line 696, in urlopen
        self._prepare_proxy(conn)
      File "D:\ProgramData\Anaconda3\lib\site-packages\urllib3\connectionpool.py", line 964, in _prepare_proxy
        conn.connect()
      File "D:\ProgramData\Anaconda3\lib\site-packages\urllib3\connection.py", line 359, in connect
        conn = self._connect_tls_proxy(hostname, conn)
      File "D:\ProgramData\Anaconda3\lib\site-packages\urllib3\connection.py", line 500, in _connect_tls_proxy
        return ssl_wrap_socket(
      File "D:\ProgramData\Anaconda3\lib\site-packages\urllib3\util\ssl_.py", line 432, in ssl_wrap_socket
        ssl_sock = _ssl_wrap_socket_impl(sock, context, tls_in_tls)
      File "D:\ProgramData\Anaconda3\lib\site-packages\urllib3\util\ssl_.py", line 474, in _ssl_wrap_socket_impl
        return ssl_context.wrap_socket(sock)
      File "D:\ProgramData\Anaconda3\lib\ssl.py", line 500, in wrap_socket
        return self.sslsocket_class._create(
      File "D:\ProgramData\Anaconda3\lib\ssl.py", line 997, in _create
        raise ValueError("check_hostname requires server_hostname")
    ValueError: check_hostname requires server_hostname

`$ D:\ProgramData\Anaconda3\Scripts\conda-script.py create -n na python=3.6`

  environment variables:
                 CIO_TEST=<not set>
        CONDA_DEFAULT_ENV=tmc
                CONDA_EXE=D:\ProgramData\Anaconda3\condabin\..\Scripts\conda.exe
               CONDA_EXES="D:\ProgramData\Anaconda3\condabin\..\Scripts\conda.exe"
             CONDA_PREFIX=D:\ProgramData\Anaconda3\envs\tmc
           CONDA_PREFIX_1=D:\ProgramData\Anaconda3
    CONDA_PROMPT_MODIFIER=(tmc)
         CONDA_PYTHON_EXE=D:\ProgramData\Anaconda3\python.exe
               CONDA_ROOT=D:\ProgramData\Anaconda3
              CONDA_SHLVL=2
           CURL_CA_BUNDLE=<not set>
                 HOMEPATH=\Users\windows
                NODE_PATH=D:\Program Files\nodejs\node_modules
                     PATH=D:\ProgramData\Anaconda3;D:\ProgramData\Anaconda3\Library\mingw-w64\bi
                          n;D:\ProgramData\Anaconda3\Library\usr\bin;D:\ProgramData\Anaconda3\Li
                          brary\bin;D:\ProgramData\Anaconda3\Scripts;D:\ProgramData\Anaconda3\bi
                          n;D:\ProgramData\Anaconda3\envs\tmc;D:\ProgramData\Anaconda3\envs\tmc\
                          Library\mingw-w64\bin;D:\ProgramData\Anaconda3\envs\tmc\Library\usr\bi
                          n;D:\ProgramData\Anaconda3\envs\tmc\Library\bin;D:\ProgramData\Anacond
                          a3\envs\tmc\Scripts;D:\ProgramData\Anaconda3\envs\tmc\bin;D:\ProgramDa
                          ta\Anaconda3\condabin;D:\Program Files\Python38\Scripts;D:\Program
                          Files\Python38;C:\Program Files\Eclipse
                          Adoptium\jdk-8.0.312.7-hotspot\bin;C:\Program Files\Eclipse
                          Foundation\jdk-11.0.12.7-hotspot\bin;D:\Program Files
                          (x86)\VMware\VMware Workstation\bin;C:\Program Files (x86)\Common File
                          s\Oracle\Java\javapath;C:\ProgramData\Oracle\Java\javapath;C:\WINDOWS\
                          system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\Windo
                          wsPowerShell\v1.0;C:\WINDOWS\System32\OpenSSH;D:\Program
                          Files\Maven\apache-maven-3.8.1\bin;C:\Program Files\MySQL\MySQL Server
                          8.0\bin;C:\Program Files\Java\jdk1.8.0_144\bin;D:\Program
                          Files\Python38;D:\Program Files\nodejs;C:\Program Files
                          (x86)\NetSarang\Xshell 7;C:\MinGW\bin;C:\Program Files\Git\cmd;C:\User
                          s\windows\AppData\Local\Google\Chrome\Application;D:\ProgramDa
                          ta\Anaconda3\Scripts;C:\Program Files\MySQL\MySQL Shell 8.0\bin;C:\Use
                          rs\windows\AppData\Local\Microsoft\WindowsApps;C:\Program
                          Files\JetBrains\IntelliJ IDEA 2021.3\bin;D:\Program
                          Files\JetBrains\WebStorm
                          2021.3\bin;C:\Users\windows\AppData\Roaming\npm;C:\Program
                          Files\JetBrains\PyCharm
                          2021.3\bin;C:\Users\windows\AppData\Local\Programs\Microsoft
                          VS Code\bin;D:\Program Files\JetBrains\DataGrip 2021.3.1\bin;.
             PSMODULEPATH=C:\Users\windows\Documents\WindowsPowerShell\Modules;C:\Progra
                          m Files\WindowsPowerShell\Modules;C:\WINDOWS\system32\WindowsPowerShel
                          l\v1.0\Modules
       REQUESTS_CA_BUNDLE=<not set>
            SSL_CERT_FILE=<not set>

     active environment : tmc
    active env location : D:\ProgramData\Anaconda3\envs\tmc
            shell level : 2
       user config file : C:\Users\windows\.condarc
 populated config files : C:\Users\windows\.condarc
          conda version : 4.10.1
    conda-build version : 3.21.4
         python version : 3.8.8.final.0
       virtual packages : __cuda=11.4=0
                          __win=0=0
                          __archspec=1=x86_64
       base environment : D:\ProgramData\Anaconda3  (writable)
      conda av data dir : D:\ProgramData\Anaconda3\etc\conda
  conda av metadata url : https://repo.anaconda.com/pkgs/main
           channel URLs : https://repo.anaconda.com/pkgs/main/win-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/win-64
                          https://repo.anaconda.com/pkgs/r/noarch
                          https://repo.anaconda.com/pkgs/msys2/win-64
                          https://repo.anaconda.com/pkgs/msys2/noarch
          package cache : D:\ProgramData\Anaconda3\pkgs
                          C:\Users\windows\.conda\pkgs
                          C:\Users\windows\AppData\Local\conda\conda\pkgs
       envs directories : D:\ProgramData\Anaconda3\envs
                          C:\Users\windows\.conda\envs
                          C:\Users\windows\AppData\Local\conda\conda\envs
               platform : win-64
             user-agent : conda/4.10.1 requests/2.25.1 CPython/3.8.8 Windows/10 Windows/10.0.19041
          administrator : False
             netrc file : None
           offline mode : False


An unexpected error has occurred. Conda has prepared the above report.

If submitted, this report will be used by core maintainers to improve
future releases of conda.
Would you like conda to send this report to the core maintainers?

[y/N]: n

No report sent. To permanently opt-out, use

    $ conda config --set report_errors false
```

## 解决方案
出现这个问题后，有比较多的解决方案：
- 使用命令清理缓存，`conda clean -i`
- 删除 ~/.condarc (C:\Users\admin)
- 关闭梯子（大杀招）

反正就是让人头大，解决方案希望对大家有用
