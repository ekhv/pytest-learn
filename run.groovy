pipeline {
    agent any

    stages {
        stage("Env Variables") {
            steps {
                sh "printenv"
            }
        }
        stage('Test') {
            steps {
                sh 'py.test --junit-xml results.xml test_with_pytest.py'
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }
    }
}