## install virtual python environment
```bash
pip install virtualenv
virtualenv umngtven
source umngtven/bin/activate
pip install Flask mysql-connector-python
# run flask app
python app.py
```
```bash
kubectl exec -it mysql-745ccb4959-cg2x2 -- mysql -u root -p
###
USE demo;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);

INSERT INTO users (username, password) VALUES ('tharanga', 'tharanga');

docker build -t my-flask-app .
docker run -d -p 5000:5000 my-flask-app
docker tag my-flask-app:latest dtl1976/my-flask-app:latest
docker push dtl1976/my-flask-app:latest

minikube service flask-app-service

###
```
# commands
## check existing ssh keys
```bash
ls -al ~/.ssh
```
## generate new ssh key
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
## copy ssh key to clipboard
```bash
cat ~/.ssh/id_rsa.pub
```
## build image and publish to docker hub
```bash
docker build -t my-flask-app .
docker run -d -p 5000:5000 my-flask-app
docker tag my-flask-app:latest dtl1976/my-flask-app:latest
docker push dtl1976/my-flask-app:latest

minikube service flask-app-service

```
```bash
helm create my-flask-chart
helm package my-flask-chart
helm install my-flask-release my-flask-chart/
helm list
helm uninstall <release-name> -n <namespace>
## Override values in value.yaml
helm install my-flask-app ./my-flask-app-chart --set replicaCount=2 --set mysql.user=myuser --set mysql.password=mypassword
```bash

# encoding decoding options
```bash
echo -n 'demo_user' | base64
echo -n 'demo@1234' | base64
```bash