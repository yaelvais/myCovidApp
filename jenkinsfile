pipeline {
    agent any

    stages {
        stage('git') {
            steps {
                git url: 'https://github.com/yaelvais/myCovidApp.git'
            }
        }
	stage('start the service'){
		steps{
		    script{
		        withEnv(['JENKINS_NODE_COOKIE=dontkill']) {
		            sh "python3 covid_app.py &"
		        }
		    }
		}
	}
        stage('query service') {
            steps {
                sh "curl localhost:5000/status"
		sh "curl localhost:5000/newCasesPeak?country=israel"
		sh "curl localhost:5000/newCasesPeak?country=${params.country}"
		sh "curl localhost:5000/recoveredPeak?country=${params.country}"
		sh "curl localhost:5000/deathsPeak?country=${params.country}"
            }
        }
    }
}
