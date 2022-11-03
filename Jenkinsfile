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
                git branch: 'sample-2', url: 'https://github.com/adarshcode12/sample.git'
                bat label:'',script:'python 2oddnumber.py'
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
