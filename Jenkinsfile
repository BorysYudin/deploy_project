pipeline {
    agent any
    stages {
        stage("Build") {
            echo "Building"
        }
        stage("Test") {
            echo "Testing"
        }
        stage("Deploy") {
            echo "Deploying"
        }
        post {
            always {
                echo "Finished stage"
            }
        }
    }
}