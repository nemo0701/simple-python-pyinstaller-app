pipeline {
  agent none
      parameters {
        string(name: 'IBID', defaultValue: '0', description: 'Get build from IBID')
        text(name: 'UTMS_ID', defaultValue: '0', description: 'UTMS ID for report')
        booleanParam(name: 'STOP_ON_ERROR', defaultValue: true, description: 'Stop test when error')
        choice(name: 'AX_or_Local Run', choices: ['AutomatosX', 'Local Run'], description: 'Run from AutomatosX or from local')
        text(name: 'Branch', defaultValue: 'Nighthawk', description: 'Stream of Framework and Test')
        password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter a password')
        file(name: "TestBetXML", description: "Choose a testBed file to upload")
        file(name: "TestSetXML", description: "Choose a testSet file to upload")
    }
  stages {
    stage('Build') {
      agent {
        docker {
          image 'python:2-alpine'
        }

      }
      steps {
        sh 'python --version'
        sh 'pip install --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org'
        sh 'pip install  requests==2.19.1 --trusted-host pypi.org --trusted-host files.pythonhosted.org'
        sh 'python -m py_compile sources/add2vals.py sources/calc.py'
        echo "IBID: ${params.IBID}"
        echo "UTMS_ID: ${params.UTMS_ID}"
        echo "STOP_ON_ERROR: ${params.STOP_ON_ERROR}"
        echo "AX_or_Local: ${params.AX_or_Local}"
        echo "Branch: ${params.Branch}"
        echo "TestBetXML: ${params.TestBetXML}"
        echo "TestBetXML: ${params.TestSetXML}"
      }
    }
    stage('StartAX'){
      agent {
        docker {
          image 'python:2-alpine'
        }

      }
      steps{
        sh 'python --version'
        sh 'pip install --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org'
        sh 'pip install  requests==2.19.1 --trusted-host pypi.org --trusted-host files.pythonhosted.org'
        sh 'python  sources/startAx.py'
      }
    }
    stage('Test') {
      agent {
        docker {
          image 'qnib/pytest'
        }

      }
      post {
        always {
          junit 'test-reports/results.xml'

        }

      }
      steps {
        sh 'pytest --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
      }
    }
    stage('Deliver') {
      agent {
        docker {
          image 'cdrx/pyinstaller-linux:python2'
        }

      }
      post {
        success {
          archiveArtifacts 'dist/add2vals'

        }

      }
      steps {
        sh 'pyinstaller  --onefile sources/add2vals.py'
      }
    }
    stage('Post') {
      steps {
        mail(subject: 'job finished', body: 'JenkinsF', from: 'nemo.li.Jenkins@emc.com', to: 'Nemo.Li@emc.com')
      }
    }
  }
}
