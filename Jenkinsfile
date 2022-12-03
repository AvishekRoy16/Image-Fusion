pipeline {
    agent any
    
    stages {
        stage('Data-Preprocessing') {

            steps {
                sh "pip3 install python==3.8" 
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
        

        stage('Build Model') {
            steps { 
                sh 'python3 test.py'
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
    
    // post {
    //     always {
    //         emailext body: 'The build failed check to see what happened!', subject: 'Image Fusion Build Failed', to: 'avishek.roy19@st.niituniversity.in'
    //     }
    // }
}
