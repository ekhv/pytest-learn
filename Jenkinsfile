#!/usr/bin/env groovy

import hudson.AbortException

pipeline {
    agent any
    parameters {
        string(defaultValue: '', description: 'app server', name: 'app_server')
    }

    environment {
        app_server = "$app_server"
    }

    stages {
        stage('Checks') {
            steps {
                script {
                    if (env.app_server.isEmpty()) {
                        currentBuild.result = "FAILURE"
                        throw new AbortException("Error. app_server is empty.")
                    }
                }
            }
        }

        stage('Info') {
            steps {
                println "app server $app_server"
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest --junit-xml results.xml test_with_pytest.py'
            }
        }
    }
    post {
        always {
            println "Test result\n${env.RUN_TESTS_DISPLAY_URL}"
            junit 'results.xml'
        }
    }
}