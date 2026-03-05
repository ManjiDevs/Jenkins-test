pipeline {
agent any

environment {
IMAGE_NAME = "jenkins-test-bot"
CONTAINER_NAME = "jenkins-test-bot"
}

stages {

stage('Pull Code') {
steps {
git branch: 'main', url: 'https://github.com/ManjiDevs/Jenkins-test.git'
}
}

stage('Test Code') {
steps {
sh '''
docker run --rm \
-v /var/lib/docker/volumes/jenkins_home/_data/workspace/Test:/app \
-w /app \
python:3.11-slim pip install -r requirements.txt

docker run --rm \
-v /var/lib/docker/volumes/jenkins_home/_data/workspace/Test:/app \
-w /app \
python:3.11-slim python -m compileall .

docker run --rm \
-v /var/lib/docker/volumes/jenkins_home/_data/workspace/Test:/app \
-w /app \
python:3.11-slim python -c "import main"
'''
}
}

stage('Build Docker Image') {
steps {
sh 'docker build -t $IMAGE_NAME .'
}
}

stage('Deploy Container') {
steps {
withCredentials([string(credentialsId: 'BOT_TOKEN', variable: 'BOT_TOKEN')]) {
sh '''
docker stop $CONTAINER_NAME || true
docker rm $CONTAINER_NAME || true

docker run -d \
--name $CONTAINER_NAME \
--restart unless-stopped \
-e BOT_TOKEN=$BOT_TOKEN \
$IMAGE_NAME
'''
}
}
}

}
}