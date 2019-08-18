pipeline {
    agent any
    stages {
        stage("Build") {
            steps {
                echo "Building"
            }
            post {
                always {
                    echo "Finished Building"
                }
            }
        }
        stage("Test") {
            steps {
                echo "Testing"
            }
        }
        stage("Deploy") {
            steps {
                echo "Deploying"
            }
        }
    }
    post {
        always {
            echo "Finished Testing"
        }
    }
}