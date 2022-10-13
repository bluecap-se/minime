terraform {
  backend "s3" {
    bucket  = "minime-terraform-states"
    key     = "prod/terraform.state"
    region  = "eu-north-1"
    profile = "default"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.33"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = var.region
  profile = "default"
}
