pipeline{
  agent any
  stages{
    stages('Checkout'){
      steps{
        checkout scm
      }
    }
    stage('Build'){
      steps{
        echo 'Checking Python application'
        bat 'python -m py_complile app.py'
      }
    }
    stage('Test'){
      
