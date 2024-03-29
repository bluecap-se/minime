.PHONY: install docker-run docker-down docker-build docker-push frontend-run frontend-test frontend-build \
        infra-init infra-format infra-validate infra-apply infra-show infra-destroy \
		infra-k8s-apply infra-k8s-dashboard test test-coverage


#
# INSTALL
#

install:
	pipenv install
	pipenv shell

docker-run:
	docker-compose -f devops/docker/docker-compose.yml up -d --build

docker-down:
	docker-compose -f devops/docker/docker-compose.yml down

docker-build:
	docker build -t bluecap/minime:latest -f devops/docker/Dockerfile .

docker-push: docker-build
	docker push bluecap/minime:latest


#
# FRONTEND
#

frontend-run:
	npm run start --prefix frontend

frontend-test:
	npm run test --prefix frontend

frontend-build:
	npm run build --prefix frontend


#
# DEPLOY
#


infra-init:
	terraform -chdir=devops/terraform init

infra-format:
	terraform -chdir=devops/terraform fmt

infra-validate:
	terraform -chdir=devops/terraform validate

infra-apply:
	terraform -chdir=devops/terraform apply

infra-show:
	terraform -chdir=devops/terraform show

infra-destroy:
	terraform -chdir=devops/terraform destroy

infra-k8s-apply:
	kubectl apply -f devops/kubernetes/postgres/
	kubectl apply -f devops/kubernetes/redis/
	kubectl apply -f devops/kubernetes/app/

infra-k8s-dashboard:
	open `minikube dashboard --url`


#
# TEST
#

test:
	pipenv run python manage.py test

test-coverage:
	pipenv install --dev
	coverage run --source='.' manage.py test app.minime
	coverage html
