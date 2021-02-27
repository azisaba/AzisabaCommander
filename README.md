# AzisabaCommander
azisabaのシステムに指令を行うBOT
## 開発環境
Python-3.8  
PyYaml  
discord.py  

VScode
## 導入方法
・ライブラリをインストール
```shell
pip3 install pyyaml
python3 -m pip install -U "discord.py[voice]"
```
・レポジトリのクローン
```shell
git clone https://github.com/azisaba/AzisabaCommander/tree/main
```
・Configファイルの準備  
1. [Discord Developer Portal](https://discordapp.com/developers/applications/)でTokenを取得する  
2. [Example](example/config.yml)をベースにConfig.ymlを用意する  
3. Token, DiscordGuild ID, Channel IDを入れる  
4. Command Prefixを設定する(今回は'%'とする)  

・コマンドを追加する  
```
%start <option>
```
optionには[bungee,lobby,pvp]が入る  
実行するコマンド  
```shell
docker-compose up -d %OPTION%
```
%OPTION%にはoptionが実行時に置き換えられる  

このようなコマンドを追加してみる　　
commandの要素下に追加する  
```yaml
command:
    start:
        base-command: 'docker-compose up -d %OPTION%'
        option:
            bungee: 'azisaba-bungee'
            lobby: 'azisaba-lobby'
            pvp: 'azisaba-pvp'
```
1. commandの直下にコマンド名を書く  
2. 実行するCommandをbase-commandに追加する  
3. optionをkey-valueで追加する name: 代入する値  
  
・実行してみる
```shell
python3 script/main.py {Configファイルのパス}
```

## LICENSE
Apache-2.0ライセンスが適応されます

## 開発者
- [testusuke](https://github.com/testusuke)
