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
                sh 'python3 -m pytest --junit-xml results.xml test_with_pytest.py'
            }
            post {
                println "Test result\n${env.RUN_TESTS_DISPLAY_URL}"
                always {
                    junit 'results.xml'
                }
            }
        }
    }
}