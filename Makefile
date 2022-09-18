.PHONY: install infrastructure-create infrastructure-update infrastructure-delete infrastructure-describe \
		deploy update undeploy test test-coverage

AWS_STACK_NAME=Minime

#
# INSTALL
#

install:
	pipenv install
	pipenv shell

#
# RESOURCES
#

infrastructure-create:
	aws cloudformation create-stack --stack-name $(AWS_STACK_NAME) --template-body file://deploy/zappa/cloudformation.yml --parameters file://deploy/zappa/cloudformation-parameters.json

infrastructure-update:
	aws cloudformation update-stack --stack-name $(AWS_STACK_NAME) --template-file deploy/zappa/cloudformation.yml --parameters file://deploy/zappa/cloudformation-parameters.json

infrastructure-delete:
	aws cloudformation delete-stack --stack-name $(AWS_STACK_NAME)

infrastructure-describe:
	aws cloudformation describe-stacks --stack-name $(AWS_STACK_NAME) --query "Stacks[0].Outputs"


#
# DEPLOY
#

deploy:
	set -e
	rm -f deploy/zappa/zappa_settings.json deploy/zappa/zappa_settings.json.tmp
	cp deploy/zappa/zappa_settings.json.example deploy/zappa/zappa_settings.json.tmp

	$(eval S3_BUCKET = $(shell aws cloudformation describe-stacks --stack-name $(AWS_STACK_NAME) --query "Stacks[0].Outputs[4].OutputValue"))
	$(eval DB_URL = $(shell aws cloudformation describe-stacks --stack-name $(AWS_STACK_NAME) --query "Stacks[0].Outputs[7].OutputValue"))
	$(eval REDIS_URL = $(shell aws cloudformation describe-stacks --stack-name $(AWS_STACK_NAME) --query "Stacks[0].Outputs[2].OutputValue"))

	sed -i '' -e "s|\%S3_BUCKET_NAME|$(S3_BUCKET)|g" deploy/zappa/zappa_settings.json.tmp
	sed -i '' -e "s|\%DATABASE_URL|$(DB_URL)|g" deploy/zappa/zappa_settings.json.tmp
	sed -i '' -e "s|\%REDIS_URL|$(REDIS_URL)|g" deploy/zappa/zappa_settings.json.tmp

	mv deploy/zappa/zappa_settings.json.tmp deploy/zappa/zappa_settings.json
	zappa deploy prod

update:
	zappa update prod

undeploy:
	zappa undeploy prod

#
# TEST
#

test:
	pipenv run python manage.py test

test-coverage:
	pipenv install --dev
	coverage run --source='.' manage.py test app.minime
	coverage html
