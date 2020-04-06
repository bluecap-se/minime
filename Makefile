.PHONY: infrastructure ecr-login build-image push-image

# As env variable:
# AWS_REPO_ID

AWS_ECR_URI=$(AWS_REPO_ID).dkr.ecr.eu-west-1.amazonaws.com/minime
TAG?=latest


#
# Setup database
#
infrastructure-create:
	aws cloudformation create-stack --template-body file://cloudformation.yml --stack-name RDS-test  --parameters file://cloudformation-parameters.json

infrastructure-deploy:
	aws cloudformation deploy --template-file cloudformation.yml --stack-name RDS-test  --parameters file://cloudformation-parameters.json

#
# DEPLOY
#

ecr-login:
	aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin $(AWS_ECR_URI)

build-image:
	docker build -t minime .
	docker tag minime:$(TAG) $(AWS_ECR_URI)

push-image: ecr-login build-image
	docker push $(AWS_ECR_URI):$(TAG)
