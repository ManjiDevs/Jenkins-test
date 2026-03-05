pipeline {
agent any

environment {
BOT_NAME = "jenkins-test-bot"
IMAGE_NAME = "jenkins-test-bot"
}

stages {

stage('Pull Code') {
steps {
git branch: 'main',
url: 'https://github.com/ManjiDevs/Jenkins-test.git'
}
}

stage('Test Code') {
steps {
sh 'python3 -m py_compile main.py'
}
}

stage('Build Docker Image') {
steps {
sh 'docker build -t jenkins-test-bot .'
}
}

stage('Deploy Container') {
steps {
sh '''
docker stop jenkins-test-bot || true
docker rm jenkins-test-bot || true

docker run -d \
--name jenkins-test-bot \
--restart unless-stopped \
--env-file /opt/bots/jenkins-test/.env \
jenkins-test-bot
'''
}
}

}
}