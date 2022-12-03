pipeline {
    agent any

    
    stages {
        stage('Data-Preprocessing') {

            steps {
                sh '''
                pip3 --version
                pip3 install -r requirements.txt
                '''
                echo 'building the application'
            }
        }
        

        stage('Build Model') {
            steps { 
                sh 'python3 app.py'
            }
        }


        stage('Build Flask Application') {
            steps { 
                echo "Hello"
            }
        }
        
        
        stage('Testing') {
            steps { 
                echo "testing part"
            }
        }
        
        stage('Deploy') {
            steps { 
                sh "docker build -t myapp ."
                sh "docker run -d -P myapp"
            }
        }
    }
    
    post {
        always {
            emailext body: 'The build failed check to see what happened!', subject: 'Image Fusion Build Failed', to: 'avishek.roy19@st.niituniversity.in'
        }
    }
}
