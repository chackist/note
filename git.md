# Git

### 工具:GitBash
### 安装
* 官网下载最新版本Git: https://git-scm.com/download (2.10.x)
* 安装成功后会得到Git Bash, Git GUI这两个工具
* 安装tortoisegit客户端(有中文语言包), 方便在文件管理器上直接执行git命令: https://tortoisegit.org/download/
* 配置tortoisegit客户端使用Git Bash生成的ssh key(参考第1条):
* Settings→Network→SSH client: 选择Git安装目录下的ssh.exe, 比如: C:\Program Files\Git\usr\bin\ssh.exe
* 如果不配置使用Git Bash的ssh key, 会比较麻烦, 需要自行搜索处理方法.
* 每个IDE可能还有不同的git插件,可以进一步配置, eclipse在完成上续过程后就可以直接使用

### SSH KEY配置
* 打开Git Bash命令行客户端, 执行ssh-keygen命令生成ssh key待用
     > ssh-keygen #一路回车, 最终生成的ssh key在$HOME/.ssh/id_rsa.pub文件中
     > cat $HOME/.ssh/id_rsa.pub  #打印出ssh key, 复制待用
     > 当然也可以直接进文件系统用自己喜欢的编辑器打开
     > git config --global user.name evan.chen #创建git相关用户名, 注意替换举例用的evan.chen
     > git config --global user.email email  #创建git相关的邮件账号, 注意替换
     > 以上命令的结果会写在 $HOME/.gitconfig中, 所以也可以直接编辑操作(**这两个配置是必须的**)

### Git分支合并
* git merge

### 常用命令
* git status    #尝试使用git命令
* git fetch     #检测与服务端的交互是否正常
* git clone
* git checkout  #切换分支
* git branch    #列出本地分支
* git branch develop  #创建develop开发分支
* git pull
* git add .
* git commit
* git push