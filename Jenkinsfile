pipeline {
    agent any
        stages {
            stage('git scm copy'){
                steps{
                    sh 'echo git copy'
                }
            }
        }
    post{
      success{
        echo "git copy without stage command success"
      }
      failure{
        echo "git copy failed without stage command"
      }
    }
}
