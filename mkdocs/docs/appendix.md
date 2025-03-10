## Appendix

Software tested V1.6.0

#### Links

* [X20EDS410 | B&R Industrial Automation](https://www.br-automation.com/de-at/produkte/steuerungssysteme/x20-system/x20-edge/x20eds410/ "https://www.br-automation.com/de-at/produkte/steuerungssysteme/x20-system/x20-edge/x20eds410/")

* [How to use SSH in VS code](https://www.bing.com/videos/riverview/relatedvideo?q=ssh+client+for+vscode&mid=5CFB151A591BAD4729B55CFB151A591BAD4729B5&FORM=VIRE "https://www.bing.com/videos/riverview/relatedvideo?q=ssh+client+for+vscode&mid=5CFB151A591BAD4729B55CFB151A591BAD4729B5&FORM=VIRE")

#### Known issues

*   When you update the image with sudo apt-get the docker is updated to version 28.0.0. With this version, the docker will no longer start. The problem is most likely this issue on Github: [28.0.0: Cannot start with iptables=true · Issue #49505 · moby/moby](https://github.com/moby/moby/issues/49505 "https://github.com/moby/moby/issues/49505")  

To downgrade and freeze the version to 27.1.2, you can use the following commands:

```
sudo apt-get install docker-ce=5:27.1.2-1~debian.12~bookworm docker-ce-cli=5:27.1.2-1~debian.12~bookworm containerd.io
sudo apt-mark hold docker-ce docker-ce-cli containerd.io
sudo systemctl restart docker
```
    

#### Tested Containers

| Name | Success | Command |
| --- | --- | --- |
| portainer | Yes | docker volume create portainer_datadocker run -d -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest |
| node red | Yes | docker run -it -p 1880:1880 --name mynodered nodered/node-red |
| mysql | Yes | docker run -p 3306:3306 --name mysql-container -e MYSQL_ROOT_PASSWORD=my-secret-pw -v mysql-data:/var/lib/mysql -d mysql:latest |
| nginx | Yes | docker run -d -p 82:80 -v /home/admin/web:/usr/share/nginx/html --name my-nginx-container nginx:latest |


#### Useful tools to install on the target

| Name | Command |
| --- | --- |
| pipx | sudo apt install pipx |
| npm | sudo apt install npm |


#### Useful vscode extensions

| Name | Marketplace |
| --- | --- |
| MySql | [Database Client JDBC - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=cweijan.dbclient-jdbc) |
| Remote SSH | [Remote - SSH - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) |


#### Useful commands

| Description | Command |
| --- | --- |
| Show IP addresses | ip addr showhostname -I |
