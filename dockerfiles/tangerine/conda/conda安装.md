Linux环境下的Anaconda安装及使用

update
摘要： Anaconda对于python就相当于Ubuntu对于Linux，即Anaconda是python的一个发行版，将python和许多常用的package打包，方便pythoners直接使用。

Anaconda对于python就相当于Ubuntu对于Linux，即Anaconda是python的一个发行版，将python和许多常用的package打包，方便pythoners直接使用。像virtualenv、pyenv等工具管理虚拟环境，起到的作用也是类似的。

Anaconda不同于其他python发行版的一点在于它是一个用于科学计算的Python发行版。Anaconda是一个打包的集合，里面预装好了conda、某个版本的python、众多packages、科学计算工具等等。Anaconda支持 Linux, Mac, Windows系统，提供了包管理与环境管理的功能，可以很方便地解决多版本python并存、切换以及各种第三方包安装问题。Anaconda利用工具/命令conda来进行package和environment的管理，并且已经包含了Python和相关的配套工具。

conda相当于pip与virtualenv的结合，是Anaconda里面的包管理与环境管理工具。conda将所有工具和第三方包（包括python和conda自身）当作package对待，所以切换和安装各种package都非常方便。

安装步骤
1）官网下载安装文件
https://www.anaconda.com/download/

2）找到安装文件所在的目录，直接使用命令./xxx.xxx执行.sh文件安装
./Anaconda3-4.4.0-Linux-x86_64.sh

根据安装说明，按照Anaconda默认的行为安装而不使用root权限，安装目录设置在个人主目录下。这样在同一台机器上的不同用户完全可以安装、配置自己的Anaconda而不会互相影响。

3）配置路径
安装时，安装程序会把bin目录加入PATH（Linux/Mac写入~/.bashrc，Windows添加到系统变量PATH），这些操作也完全可以自己完成。

对于Mac、Linux系统，Anaconda安装好后，实际上就是在主目录下多了个文件夹（~/anaconda）而已，Windows会写入注册表。安装时，安装程序会把bin目录加入PATH（Linux/Mac写入~/.bashrc，Windows添加到系统变量PATH），这些操作也完全可以自己完成。以Linux/Mac为例，安装完成后设置PATH的操作是：

# 将anaconda的bin目录加入PATH，根据版本不同，也可能是~/anaconda3/bin
echo 'export PATH="~/anaconda2/bin:$PATH"' >> ~/.bashrc
# 更新bashrc以立即生效
source ~/.bashrc
配置好PATH后，可以通过which conda或conda –version命令检查是否正确。假如安装的是Python 2.7对应的版本，运行python –version或python -V可以得到Python 2.7.12 :: Anaconda 4.1.1 (64-bit)，也说明该发行版默认的环境是Python 2.7。

4）使用conda管理conda以及python等的版本
# 更新conda，保持conda最新
conda update conda

# 更新anaconda
conda update anaconda

# 更新python
conda update python
# 假设当前环境是python 3.4, conda会将python升级为3.4.x系列的当前最新版本
conda 常用命令：

# 查看当前环境下已安装的包
conda list

# 查看某个指定环境的已安装包
conda list -n python34

# 查找package信息
conda search numpy

# 安装package
conda install -n python34 numpy
# 如果不用-n指定环境名称，则被安装在当前活跃环境
# 也可以通过-c指定通过某个channel安装

# 更新package
conda update -n python34 numpy

# 删除package
conda remove -n python34 numpy
5）设置国内镜像
由于Anaconda.org的服务器在国外，所以通常在国内使用conda下载速度会很慢。所以在国内通常使用清华TUNA镜像源。

# 添加Anaconda的TUNA镜像
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
# TUNA的help中镜像地址加有引号，需要去掉

# 设置搜索时显示通道地址
conda config --set show_channel_urls yes
执行完上述命令后，会生成~/.condarc(Linux/Mac)或C:UsersUSER_NAME.condarc文件，记录着我们对conda的配置，直接手动创建、编辑该文件是相同的效果。

6）卸载Anaconda
删除安装文件夹 
由于Anaconda的安装文件都包含在一个目录中，所以直接将该目录删除即可。

rm -rf anaconda
清理.bashrc中的路径 
文件末尾用#号注释掉之前添加的路径或者直接删除该行：


# export PATH=/home/lq/anaconda3/bin:$PATH
使其立即生效，在终端执行：

source ~/.bashrc
如需重新安装，重启一个新的终端，不然在原终端上还是绑定有anaconda。



参考资料：
Anaconda使用总结 by Peter Yuan 
Anaconda Docs 
Conda Docs