pipeline {
    agent any
    environment {
        DOCKERHUB_CREDS = credentials('dockerhub-creds')
        IMAGE_NAME = 'shiwanee129/demo-build-project'
    }
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/Shiwanee111/demo-build-project.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER .'
            }
        }
        stage('Push to DockerHub') {
            steps {
                sh 'echo $DOCKERHUB_CREDS_PSW | docker login -u $DOCKERHUB_CREDS_USR --password-stdin'
                sh 'docker push $IMAGE_NAME:$BUILD_NUMBER'
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                    docker stop demo-app || true
                    docker rm demo-app || true
                    docker run -d --name demo-app -p 3000:3000 $IMAGE_NAME:$BUILD_NUMBER
                '''
            }
        }
    }
    post {
        success { echo '✅ Pipeline successful! App is live!' }
        failure { echo '❌ Pipeline failed! Check logs.' }
    }
}