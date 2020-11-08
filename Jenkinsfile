#!/usr/bin/env groovy
import hudson.AbortException

lib = library(
        identifier: 'utils@main',
        retriever: modernSCM(
                [
                        $class: 'GitSCMSource',
                        remote: 'https://github.com/ekhv/jenkins-libs.git'
                ]
        )
)

def title = lib.org.foo.Title.new()

pipeline {
    agent any

    options {
        ansiColor('xterm')
    }

    parameters {
        string(defaultValue: '', description: 'app server', name: 'app_server')
    }

    environment {
        app_server = "$app_server"
    }

    stages {
        stage('Checks') {
            steps {
                println(title.titleStage("Checks"))
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
                println(title.titleStage("Info"))
                println "app server $app_server"
            }
        }

        stage('Test') {
            steps {
                println(title.titleStage("Run test"))
                sh 'python3 -m pytest --junit-xml results.xml test_with_pytest.py'
            }
        }
    }
    post {
        always {
            println(title.titleStage("Result"))
            println "Test result\n${env.RUN_TESTS_DISPLAY_URL}"
            junit 'results.xml'
        }
    }
}