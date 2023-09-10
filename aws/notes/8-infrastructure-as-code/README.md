Infrastructure As Code (IaC)
====

# Infrastructure as Code

- Using an infrastructure as code (IaC) model, instead of manually provisioning or using scripting languages, helps remove the dependency on human intervention when you create and manage infrastructure over time.

# Using AWS CloudFormation to Deploy Infrastructure

## What Is AWS CloudFormation?

- AWS CloudFormation aims to alleviate previous deployment issues with the use of a service that allows you to describe your infrastructure with standardized JSON or YAML template syntax. The template contains the infrastructure that AWS will deploy and all the related configuration properties. When you submit this template to the AWS CloudFormation service, it creates a stack, which is a logical group of resources that the template describes.

## AWS CloudFormation Concepts

### Stacks

- represents a collection of resources to deploy and manage by AWS CloudFormation

### Change Sets

### Permissions

### Template Structure

### AWSTemplateFormatVersion

### Description

### Metadata

### Parameters

### Mappings

### Conditions

### Transforms

### Resources

### Outputs

### Intrinsic Functions

### Ref

### Condition Functions

### Built-in Metadata Keys

### PACKAGES

### GROUPS

### USERS

### SOURCES

### FILES

### COMMANDS

### SERVICES

### CONFIGSETS

### PARAMETERGROUPS

### PARAMETERLABELS

### AWS CloudFormation Designer

### Custom Resources

### AWS Lambda Backed Custom Resources

### Custom Resources Associated with Amazon SNS

### Custom Resource Success/Failure

### Resource Relationships

### Creation Policies

### Wait Conditions

### Stack Create, Update, and Delete Statuses

### Stack Updates

### Update Policies

### Deletion Policies

### Exports and Nested Stacks

### Export and Import Stack Outputs

### Nesting with the AWS::CloudFormation::Stack Resource

### Stack Policies

### AWS CloudFormation Command Line Interface

### Packaging Local Dependencies

### Deploy Templates with Transforms

### AWS CloudFormation Helper Scripts

### Daemon Configuration File

### Hooks Configuration File

### AWS CloudFormation StackSets

### Stack Set

### Stack Instance

### Stack Set Operations

### Stack Set Permissions

### Target Account Gate

## AWS CloudFormation Service Limits

## Using AWS CloudFormation with AWS CodePipeline

### Deployment Configuration Properties

#### Action Mode

#### Stack or Change Set Name

#### Template

#### Template Configuration

#### Capabilities

#### Role Name

#### Output File Name

#### Parameter Overrides

