# cursor-nautilus

This repo provides a cursor extension for Nautilus.



&nbsp;



## Install cursor (tuning)
install AppImage from cursor.com, and next
```
cd ~/Downloads
chmod +x cursor-0.44.11x86_64.AppImage
```
note that version can be different from example.
```
cd /opt
sudo mkdir cursor
sudo mv ~/Downloads/cursor-0.44.11x86_64.AppImage /opt/cursor/cursor.AppImage
```
```
sudo vim /usr/share/applications/cursor.desktop 
```
```
[Desktop Entry]
Name=Cursor
Exec=/opt/cursor/cursor.AppImage --no-sandbox %F
Icon=/opt/cursor/cursor.png
Type=Application
Categories=Development
MimeType=text/plain;
StartupNotify=true
Terminal=false
```
and place repo's cursor.png to /opt/cursor/cursor.png



&nbsp;



## Install Extension

```
wget -qO- https://raw.githubusercontent.com/taeraemon/cursor-nautilus/master/install.sh | bash
```



&nbsp;



## Uninstall Extension

```
rm -f ~/.local/share/nautilus-python/extensions/cursor-nautilus.py
```



&nbsp;



### Reference

https://velog.io/@openjr/curosr-%EC%84%A4%EC%B9%98-%EC%9A%B0%EB%B6%84%ED%88%AC
https://github.com/harry-cpp/code-nautilus