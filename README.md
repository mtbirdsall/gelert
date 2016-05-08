# Gelert
![Gelert Irish Wolf Hound](https://upload.wikimedia.org/wikipedia/commons/e/e0/Gelert.jpg)

A Flask boiler-plate app for web-dev including within it's stack Jinja2 Templates, PostgreSQL, Python 3.5 and Vue.js or React.js.   

## Purpose
Creating a template app that can be deployed at the onset of projects. 
## References


### VM setup 

Upgrade the server
```
sudo apt-get update
sudo apt-get upgrade-dist
```

Begin the installation of the required packages

```
sudo apt-get install git
sudo apt-get install python3-dev
sudo apt-get install python3-pip
```
There is a need to get a virtualenv set up.  I would follow this [config tutorial](https://linuxconfig.org/setting-up-the-python-virtualenv-development-environment-on-debian-linux).
With the exception of one line.
```
sudo apt install virtualenv
virtualenv env
cd env
source bin/activate
```

Now within your environment use `pip` to install the other components
```
pip3 install virtualenv
pip3 install virtualenvwrapper
pip3 install pandas
pip3 install ipython
pip3 install jupyter
pip3 install flask
```
This should take care of a majority of the packages that you will need to develop the rest of this app's boilerplate.

### File Structure
The file strucute for Flask is simiar to Django, but can be less structured.
```
mkdir ~/projects
mkdir ~/projects/flask-projects
cd projects/flask-projects
git clone <this repo>
```


#### Using rmate 

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
