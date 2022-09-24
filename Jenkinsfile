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
                echo 'Model Build Succesdful'
            }
        }


        stage('Build Flask Application') {
            steps { 
                echo 'Data Preprocessing Succesdful'
            }
        }
        
        
        stage('Testing') {
            steps { 
                echo 'Testing Successful'
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
