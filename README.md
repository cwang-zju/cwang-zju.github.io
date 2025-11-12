# README

## 修改

1. 修改_config.yml 中的 url 和 repository
2. 修改主页 [About](_pages/about.md) 中的内容
3. 使用 `scripts/add_publication.py` 增添新的论文条目
4. 点击 [Lab](_pages/lab.md) 修改 Lab Members 列表中的内容
5. 点击 [Miscellaneous](_pages/misc.md) 修改 Miscellaneous 列表中的内容

## 本地预览

```shell
./local_deply.sh
```

## 环境配置指南

### 安装 ruby

下载 [RubyInstaller](https://rubyinstaller.org/downloads/)，下载后解压到任意路径。

```shell
ruby -v
```

#### linux or wsl

```shell
sudo apt update && sudo apt upgrade -y
sudo apt install ruby-dev ruby-bundler nodejs
```

```shell
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init - bash)"' >> ~/.bashrc
source ~/.bashrc

git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
```

#### macos

```shell title="macos"
brew install rbenv ruby-build
```

```shell title="macos"
echo 'eval "$(rbenv init - zsh)"' >> ~/.zshrc
source ~/.zshrc
```

```shell
rbenv install 3.2.4
rbenv global 3.2.4
exec $SHELL
```

```shell
ruby -v
```

```shell
$ which rbenv

> /home/user/.rbenv/bin/rbenv

$ rbenv versions
> 看看有没有3.2.4
```

### rubygems

#### MacOS

```shell title="macos"
brew install gem
```

#### Windows

下载 [RubyGems](https://rubygems.org/pages/download)，下载后解压到任意路径。

```shell
cd 解压的路径
```

```shell title="升级 RubyGems"
gem update --system
```

#### 切换镜像源

```shell
# 添加镜像源并移除默认源
gem sources --add https://mirrors.tuna.tsinghua.edu.cn/rubygems/ --remove https://rubygems.org/
```

```shell title="列出已有源"
gem sources -l # 应该只有镜像源一个
```

```shell title="验证"
*** CURRENT SOURCES ***
https://gems.ruby-china.com/
```

### 安装 Jekyll

```shell
gem install jekyll
```

验证 Jekyll

```shell
jekyll -v
```

安装依赖包

```shell
cd cwang-zju.github.io
bundle install
```
