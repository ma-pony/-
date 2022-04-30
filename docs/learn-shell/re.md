# 查找git地址
```shell
grep -r 'url.*'  .git/config | sed -r "s/url = (.*)\.git/\1/g"
```
