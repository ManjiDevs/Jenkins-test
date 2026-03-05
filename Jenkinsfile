pipeline {
agent any

environment {
BOT_NAME = "jenkins-test-bot"
IMAGE_NAME = "jenkins-test-bot"
WORK_DIR = "/demon-project/jenkins_test/Jenkins-test"
}

stages {

stage('Pull Code') {
steps {
git 'https://github.com/ManjiDevs/Jenkins-test'
}
}

stage('Test Code') {
steps {
sh 'python3 -m py_compile main.py'
}
}

stage('Build Docker Image') {
steps {
sh 'docker build -t $IMAGE_NAME .'
}
}

stage('Deploy Container') {
steps {
sh '''
docker stop $BOT_NAME || true
docker rm $BOT_NAME || true

docker run -d \
--name $BOT_NAME \
--restart unless-stopped \
--env-file /opt/bots/jenkins-test/.env \
$IMAGE_NAME
'''
}
}

}
}