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
                git branch: 'IF-13-pose-estimator', url: 'https://github.com/AvishekRoy16/Image-Fusion.git'
                bat 'python pose_detection.py'
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
