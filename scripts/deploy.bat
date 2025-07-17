@echo off
set STACK_NAME=my-secure-bucket-stack
set TEMPLATE_FILE=templates\secure-s3-bucket.yml

echo Deploying stack: %STACK_NAME%
aws cloudformation deploy --stack-name %STACK_NAME% --template-file %TEMPLATE_FILE% --capabilities CAPABILITY_NAMED_IAM

if %ERRORLEVEL% EQU 0 (
    echo Deployment successful!
) else (
    echo Deployment failed. Check the CloudFormation console for error details.
)