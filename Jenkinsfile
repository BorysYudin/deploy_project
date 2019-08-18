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
            post {
                always {
                    echo "Finished Testing"
                }
            }
        }
        stage("Deploy") {
            steps {
                echo "Deploying"
            }
            post {
                always {
                    echo "Finished Deploying"
                }
            }
        }
    }
    post {
        always {
            echo "Finished Stages"
            echo "Tested GitHub webhook"
            echo "Tested GitHub webhook Jenkins 2......."
        }
    }
}