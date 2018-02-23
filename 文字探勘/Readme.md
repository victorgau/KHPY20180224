# 文字探勘簡介

在這個範例裡面，我們介紹結巴 (jieba) 中文斷詞的使用，並使用 wordcloud 來畫出文字雲。

### 安裝：

結巴安裝：

```
pip install jieba
```

wordcloud 安裝：

1. 到 [https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud](https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud) 下載 .whl 檔
2. 使用下面指令安裝：

```
pip install xxx.whl
```

xxx.whl 為步驟一下載的 .whl 檔檔名。

### 關於中文字型：

如果要使用 wordcloud 套件來顯示中文字型，需在 wordcloud 內提供中文字型的路徑。

如果不知道自己的中文字型路徑，可在 google 上面搜尋免費中文字型，再下載來使用即可。譬如底下網址：

* [免費中文字型下載](https://briian.com/tag/%E5%85%8D%E8%B2%BB%E4%B8%AD%E6%96%87%E5%AD%97%E5%9E%8B%E4%B8%8B%E8%BC%89/)
* [16個合法免費高品質字體 (附載點)](https://forum.gamer.com.tw/C.php?bsn=60076&snA=3906436)
* [《字體安裝》繁體中文字體免費下載，超多可愛、個性文字任你用。](https://www.pkstep.com/archives/5693)

### 使用：

使用方式參考 .ipynb 檔。
