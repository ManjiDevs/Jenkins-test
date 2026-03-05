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
          -v "$PWD:/app" \
          -w /app \
          python:3.11-slim \
          sh -c "pip install -r requirements.txt && python -m compileall . && python -c 'import main'"
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