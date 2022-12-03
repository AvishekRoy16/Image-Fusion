pipeline {
    agent any
    
    stages {
        stage('Data-Preprocessing') {
            steps { 
                sh 'python3 test.py'
            }
        }
        

        stage('Build Model') {
            steps { 
                echo "hello"
            }
        }


        stage('Build Flask Application') {
            steps { 
                sh '''
                py
                '''
            }
        }
        
        
        stage('Testing') {
            steps { 
                sh 'python3 test.py'
            }
        }
        
        stage('Deploy') {
            steps { 
                echo 'Deploy Succesdful'
            }
        }
    }
    
    post {
        always {
            emailext body: 'The build failed check to see what happened!', subject: 'Image Fusion Build Failed', to: 'avishek.roy19@st.niituniversity.in'
        }
    }
}
