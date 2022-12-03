pipeline {
    agent any
    
    stages {
        stage('Data-Preprocessing') {
            steps { 
                echo 'Data Preprocessing Succesdful'
            }
        }
        

        stage('Build Model') {
            steps { 
                echo "hello"
            }
        }


        stage('Build Flask Application') {
            steps { 
                dir('/src/flask_app/') {
                    sh "python3 app.py"
                }
            sh "pwd"
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
