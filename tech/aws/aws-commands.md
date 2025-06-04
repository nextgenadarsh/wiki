# `aws` Cheat Sheet

> Reference: https://aws.amazon.com/cli

## Tips

- aws cofig file location: `~/.aws/config`
- aws credentials file location: `~/.aws/credentials`
- Use `--no-verify-ssl` to skip ssl verification
- Use `help` to get help
- Use `aws history list` to list command history

## Configuration

| Command                                                   | Purpose
| --                                                        | --
| `aws configure`   | configure aws access using credentials
| `aws configure sso`   | configure aws access using SSO
| `aws configure set region <region> --profile <profile-name>`  | set region for profile
| `aws configure get region --profile <profile>`    | get region for profile
| `aws configure list`  | get current profile credentials
| `aws configure list-profiles` | get all profiles
| `export AWS_PROFILE='<profile>'`    | set currrent profile
| `echo $AWS_PROFILE`           | get current profile

## Identity / Login

| Command                       | Purpose
| --                            | --
| `aws sts get-caller-identity` | get STS caller / user identity
| `aws sso login`               | sso login to get temporary credentials
| `aws sso login --profile qa`  | sso login to get cred for qa profile

## Elastic Kubernetes Service (EKS)

| Command                       | Purpose
| --                            | --
| `aws eks list-clusters`       | list eks clusters
| `aws eks update-kubeconfig --region <region> --name <cluster-name>`   | update kube config for cluster

## Simple Storage Service (S3)

| Command                       | Purpose
| --                            | --
| `aws s3 ls`   | list S3 buckets



