pipeline {
agent any

environment {
IMAGE = "jenkins-test-bot"
BOT_TOKEN = credentials('bot-token')
}

stages {

stage('Checkout') {
steps {
checkout scm
}
}

stage('Test') {
steps {
sh '''
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
pytest
'''
}
}

stage('Build Image') {
steps {
sh 'docker build -t $IMAGE:latest .'
}
}

stage('Deploy Blue-Green') {
steps {
sh '''
CURRENT=$(docker ps --format "{{.Names}}" | grep jenkins-test-blue || true)

if [ "$CURRENT" = "jenkins-test-blue" ]; then
NEW="jenkins-test-green"
OLD="jenkins-test-blue"
else
NEW="jenkins-test-blue"
OLD="jenkins-test-green"
fi

echo "Starting $NEW"

docker run -d \
--name $NEW \
--network prod_network \
--restart always \
-e BOT_TOKEN=$BOT_TOKEN \
jenkins-test-bot:latest

sleep 5

echo "Stopping $OLD"
docker stop $OLD || true
docker rm $OLD || true
'''
}
}
}
}