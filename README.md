# gelert

##Purpose

##References


### Using rmate 

If you don’t already have Sublime Text’s wonderful package manager, [install it](http://wbond.net/sublime_packages/package_control/installation).

Hit `Cmd+Shift+P`, start typing “install” and select “Install Package”
Start typing “rsub” and select it.

Once it’s installed, get on your terminal and do
```
nano ~/.ssh/config
```
Paste the following lines:
```
Host star-destroyer
    RemoteForward 52698 127.0.0.1:52698
```
Save (`ctrl+w`) and SSH into your server `ssh username@star-destroyer`.
Install the rsub remote script:
```
sudo wget -O /usr/local/bin/rsub https://raw.github.com/aurora/rmate/master/rmate
```
Make that script executable:
```
sudo chmod +x /usr/local/bin/rsub
```
Lastly, run rsub on the remote file you want to edit locally:
```
rsub ~/my_project/my_file.html
```
and it should magically open in Sublime Text!
