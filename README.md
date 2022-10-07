# 將login頁面用docker部屬

### 步驟一:
修改dockerfile
### 步驟二:
將要用到的套件寫到requirements.txt中
### 步驟三:
將dockerfile變成映像檔
```
docker create [OPTIONS] IMAGE [COMMAND] [ARG...]
```
### 步驟四:
將映像檔啟動成 Container
```
docker run -d -p 80:80 --name my_image nginx
```
詳細教學可參考 : https://github.com/twtrubiks/docker-tutorial
