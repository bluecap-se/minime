# core

variable "region" {
  description = "The AWS region to create resources in."
  default     = "eu-north-1"
}


# networking

variable "public_subnet_1_cidr" {
  description = "CIDR Block for Public Subnet 1"
  default     = "10.0.1.0/24"
}
variable "public_subnet_2_cidr" {
  description = "CIDR Block for Public Subnet 2"
  default     = "10.0.2.0/24"
}
variable "private_subnet_1_cidr" {
  description = "CIDR Block for Private Subnet 1"
  default     = "10.0.3.0/24"
}
variable "private_subnet_2_cidr" {
  description = "CIDR Block for Private Subnet 2"
  default     = "10.0.4.0/24"
}
variable "availability_zones" {
  description = "Availability zones"
  type        = list(string)
  default     = ["eu-north-1b", "eu-north-1c"]
}


# load balancer

variable "health_check_path" {
  description = "Health check path for the default target group"
  default     = "/ping/"
}


# ecs

variable "ecs_cluster_name" {
  description = "Name of the ECS cluster"
  default     = "minime"
}
variable "instance_type" {
  default = "t3.small"
}
variable "docker_image_url_django" {
  description = "Docker image to run in the ECS cluster"
  default     = "bluecap/minime:latest"
}
variable "docker_image_url_nginx" {
  description = "Docker image to run in the ECS cluster"
  default     = "bluecap/minime-nginx:latest"
}
variable "app_count" {
  description = "Number of Docker containers to run"
  default     = 2
}
variable "allowed_hosts" {
  description = "Domain name for allowed hosts"
  default     = "*"
}


# logs

variable "log_retention_in_days" {
  default = 30
}


# key pair

variable "ssh_pubkey_file" {
  description = "Path to an SSH public key"
  default     = "~/.ssh/id_rsa.pub"
}


# auto scaling

variable "autoscale_min" {
  description = "Minimum autoscale (number of EC2)"
  default     = "1"
}
variable "autoscale_max" {
  description = "Maximum autoscale (number of EC2)"
  default     = "4"
}
variable "autoscale_desired" {
  description = "Desired autoscale (number of EC2)"
  default     = "2"
}


# rds

variable "rds_db_name" {
  description = "RDS database name"
  default     = "main"
}
variable "rds_username" {
  description = "RDS database username"
  default     = "mini"
}
variable "rds_password" {
  description = "RDS database password"
  default     = "password"
}
variable "rds_instance_class" {
  description = "RDS instance type"
  default     = "db.t4g.micro"
}


# elasticache

variable "elasticache_name" {
  description = "ElastiCache instance name"
  default     = "minime-redis-cluster"
}
variable "elasticache_instance_class" {
  description = "ElastiCache instance type"
  default     = "cache.t4g.micro"
}


# S3

variable "s3_bucket_name" {
  description = "Minime bucket name for static files"
  default     = "minime-static-frontend"
}


# domain

variable "certificate_arn" {
  description = "AWS Certificate Manager ARN for validated domain"
  default     = "YOUR ARN"
}
