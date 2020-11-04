#!/usr/bin/env groovy

import hudson.AbortException

pipeline {
    agent any
    parameters {
        string(defaultValue: '', description: 'app server', name: 'app_server')
        password(defaultValue: '', description: 'Passphrase private key', name: 'pass_private_key')
    }

    environment {
        app_server = "$app_server"
        passphrase = "$pass_private_key"
    }

    stages {
        stage('Checks') {
            steps {
                script {
                    if (env.pass_private_key.size() == 0) {
                        currentBuild.result = "FAILURE"
                        throw new AbortException("Error. pass_private_key is empty.")
                    }

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