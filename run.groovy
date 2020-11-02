pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'python3 -m pytest --junit-xml results.xml test_with_pytest.py'
            }
            post {
                always {
                    println "Test result\n${env.RUN_TESTS_DISPLAY_URL}"
                    junit 'results.xml'
                }
            }
        }
    }
}