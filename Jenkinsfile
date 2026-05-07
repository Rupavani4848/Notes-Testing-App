pipeline {

    agent any

    tools {
        allure 'Allure'
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

                // Delete old venv if exists
                bat 'if exist venv rmdir /s /q venv'

                // Create fresh virtual environment
                bat 'python -m venv venv'

                // Upgrade pip
                bat 'venv\\Scripts\\python -m pip install --upgrade pip'

                // Install requirements
                bat 'venv\\Scripts\\python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests (Parallel)') {
            steps {

                // Continue pipeline even if tests fail
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

        stage('Publish Reports') {
            steps {

                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Pytest HTML Report'
                ])
            }
        }

        stage('Archive Artifacts') {
            steps {

                archiveArtifacts(
                    artifacts: 'report.html, allure-results/**, screenshots/**, logs/**',
                    fingerprint: true
                )
            }
        }
    }
}