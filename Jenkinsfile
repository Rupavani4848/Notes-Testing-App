pipeline {

    agent any

    tools {
        allure 'Allure'
    }

    options {
        skipDefaultCheckout(true)
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Rupavani4848/Notes-Testing-App.git'
            }
        }

        stage('Install Dependencies') {
            steps {

                bat 'if exist venv rmdir /s /q venv'

                bat 'python -m venv venv'

                bat 'venv\\Scripts\\python -m ensurepip --upgrade'

                bat 'venv\\Scripts\\python -m pip install --upgrade pip setuptools wheel'

                bat 'venv\\Scripts\\python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests (Parallel)') {
            steps {

                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {

                    bat '''
                    venv\\Scripts\\python -m pytest ^
                    -n 4 ^
                    --alluredir=allure-results ^
                    --html=report.html ^
                    --self-contained-html
                    '''
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML([
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Pytest HTML Report',
                    keepAll: true,
                    alwaysLinkToLastBuild: true,
                    allowMissing: false
                ])
            }
        }
    }

    post {
        always {

            archiveArtifacts(
                artifacts: 'report.html, allure-results/**, screenshots/**, logs/**',
                fingerprint: true
            )
        }
    }
}