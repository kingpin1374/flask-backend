pipeline {
    agent any

    stages {
        stage('Fetch Code') {
            steps {
                git branch: 'master', 
                    url: 'https://github.com/kingpin1374/flask-backend.git',
                    credentialsId: 'github'
            }
        }
        stage('Install env') {
            steps {
               sh 'which python3 || (sudo apt-get update && sudo apt-get install -y python3 python3-venv python3-pip)'
            }
        }

        stage('Create python env'){
            steps {
                sh 'python3 -m venv myenv'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '. myenv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Deploy') {
            steps {
                // Restarts if exists, otherwise starts new
                sh 'pm2 restart flask-backend || pm2 start app.py --name "flask-backend" --interpreter python3'
            }
        }
    }
}

