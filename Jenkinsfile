pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python --version'
                sh 'python -m py_compile sources/add2vals.py sources/calc.py'
            }
        }
        stage('Test'){
            agent{
               docker{
                   image 'qnib/pytest'         
               }
            }
            steps{
                sh 'pytest --verbose --junit-xml test-reports/result.xml sources/test_calc.py' 
            }
            post{
                always{
		    junit 'test-reports/results.xml
		}
            }
        }
     }
}
