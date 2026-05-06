pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Rupavani4848/Notes-Testing-App.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -n 4 --alluredir=allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat 'allure generate allure-results -o allure-report --clean'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-report/**', fingerprint: true
        }
    }
}