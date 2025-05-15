# AWS Provider Resources

This document lists all resources available in the Terraform AWS Provider, organized by service.

## Contents


- [accessanalyzer](#accessanalyzer)

- [account](#account)

- [acm](#acm)

- [acmpca](#acmpca)

- [amp](#amp)

- [amplify](#amplify)

- [apigateway](#apigateway)

- [apigatewayv2](#apigatewayv2)

- [appautoscaling](#appautoscaling)

- [appconfig](#appconfig)

- [appfabric](#appfabric)

- [appflow](#appflow)

- [appintegrations](#appintegrations)

- [applicationinsights](#applicationinsights)

- [appmesh](#appmesh)

- [apprunner](#apprunner)

- [appstream](#appstream)

- [appsync](#appsync)

- [athena](#athena)

- [auditmanager](#auditmanager)

- [autoscaling](#autoscaling)

- [backup](#backup)

- [batch](#batch)

- [bcmdataexports](#bcmdataexports)

- [bedrock](#bedrock)

- [bedrockagent](#bedrockagent)

- [budgets](#budgets)

- [ce](#ce)

- [chatbot](#chatbot)

- [chime](#chime)

- [chimesdkmediapipelines](#chimesdkmediapipelines)

- [chimesdkvoice](#chimesdkvoice)

- [cleanrooms](#cleanrooms)

- [cloud9](#cloud9)

- [cloudcontrol](#cloudcontrol)

- [cloudformation](#cloudformation)

- [cloudfront](#cloudfront)

- [cloudfrontkeyvaluestore](#cloudfrontkeyvaluestore)

- [cloudhsmv2](#cloudhsmv2)

- [cloudsearch](#cloudsearch)

- [cloudtrail](#cloudtrail)

- [cloudwatch](#cloudwatch)

- [codeartifact](#codeartifact)

- [codebuild](#codebuild)

- [codecatalyst](#codecatalyst)

- [codecommit](#codecommit)

- [codeconnections](#codeconnections)

- [codeguruprofiler](#codeguruprofiler)

- [codegurureviewer](#codegurureviewer)

- [codepipeline](#codepipeline)

- [codestarconnections](#codestarconnections)

- [codestarnotifications](#codestarnotifications)

- [cognitoidentity](#cognitoidentity)

- [cognitoidp](#cognitoidp)

- [comprehend](#comprehend)

- [computeoptimizer](#computeoptimizer)

- [configservice](#configservice)

- [connect](#connect)

- [controltower](#controltower)

- [costoptimizationhub](#costoptimizationhub)

- [cur](#cur)

- [dataexchange](#dataexchange)

- [datapipeline](#datapipeline)

- [datasync](#datasync)

- [datazone](#datazone)

- [dax](#dax)

- [deploy](#deploy)

- [detective](#detective)

- [devicefarm](#devicefarm)

- [devopsguru](#devopsguru)

- [directconnect](#directconnect)

- [dlm](#dlm)

- [dms](#dms)

- [docdb](#docdb)

- [docdbelastic](#docdbelastic)

- [drs](#drs)

- [ds](#ds)

- [dynamodb](#dynamodb)

- [ec2](#ec2)

- [ecr](#ecr)

- [ecrpublic](#ecrpublic)

- [ecs](#ecs)

- [efs](#efs)

- [eks](#eks)

- [elasticache](#elasticache)

- [elasticbeanstalk](#elasticbeanstalk)

- [elasticsearch](#elasticsearch)

- [elb](#elb)

- [elbv2](#elbv2)

- [emr](#emr)

- [emrcontainers](#emrcontainers)

- [emrserverless](#emrserverless)

- [events](#events)

- [evidently](#evidently)

- [finspace](#finspace)

- [firehose](#firehose)

- [fis](#fis)

- [fms](#fms)

- [fsx](#fsx)

- [gamelift](#gamelift)

- [glacier](#glacier)

- [globalaccelerator](#globalaccelerator)

- [glue](#glue)

- [grafana](#grafana)

- [guardduty](#guardduty)

- [iam](#iam)

- [identitystore](#identitystore)

- [imagebuilder](#imagebuilder)

- [inspector](#inspector)

- [inspector2](#inspector2)

- [internetmonitor](#internetmonitor)

- [iot](#iot)

- [ivs](#ivs)

- [ivschat](#ivschat)

- [kafka](#kafka)

- [kafkaconnect](#kafkaconnect)

- [kendra](#kendra)

- [keyspaces](#keyspaces)

- [kinesis](#kinesis)

- [kinesisanalytics](#kinesisanalytics)

- [kinesisanalyticsv2](#kinesisanalyticsv2)

- [kinesisvideo](#kinesisvideo)

- [kms](#kms)

- [lakeformation](#lakeformation)

- [lambda](#lambda)

- [lexmodels](#lexmodels)

- [lexv2models](#lexv2models)

- [licensemanager](#licensemanager)

- [lightsail](#lightsail)

- [location](#location)

- [logs](#logs)

- [m2](#m2)

- [macie2](#macie2)

- [mediaconvert](#mediaconvert)

- [medialive](#medialive)

- [mediapackage](#mediapackage)

- [mediapackagev2](#mediapackagev2)

- [mediastore](#mediastore)

- [memorydb](#memorydb)

- [mq](#mq)

- [mwaa](#mwaa)

- [neptune](#neptune)

- [networkfirewall](#networkfirewall)

- [networkmanager](#networkmanager)

- [networkmonitor](#networkmonitor)

- [oam](#oam)

- [opensearch](#opensearch)

- [opensearchserverless](#opensearchserverless)

- [opsworks](#opsworks)

- [organizations](#organizations)

- [osis](#osis)

- [paymentcryptography](#paymentcryptography)

- [pinpoint](#pinpoint)

- [pinpointsmsvoicev2](#pinpointsmsvoicev2)

- [pipes](#pipes)

- [qldb](#qldb)

- [quicksight](#quicksight)

- [ram](#ram)

- [rbin](#rbin)

- [rds](#rds)

- [redshift](#redshift)

- [redshiftserverless](#redshiftserverless)

- [rekognition](#rekognition)

- [resiliencehub](#resiliencehub)

- [resourceexplorer2](#resourceexplorer2)

- [resourcegroups](#resourcegroups)

- [rolesanywhere](#rolesanywhere)

- [route53](#route53)

- [route53domains](#route53domains)

- [route53profiles](#route53profiles)

- [route53recoverycontrolconfig](#route53recoverycontrolconfig)

- [route53recoveryreadiness](#route53recoveryreadiness)

- [route53resolver](#route53resolver)

- [rum](#rum)

- [s3](#s3)

- [s3control](#s3control)

- [s3outposts](#s3outposts)

- [s3tables](#s3tables)

- [sagemaker](#sagemaker)

- [scheduler](#scheduler)

- [schemas](#schemas)

- [secretsmanager](#secretsmanager)

- [securityhub](#securityhub)

- [securitylake](#securitylake)

- [serverlessrepo](#serverlessrepo)

- [servicecatalog](#servicecatalog)

- [servicecatalogappregistry](#servicecatalogappregistry)

- [servicediscovery](#servicediscovery)

- [servicequotas](#servicequotas)

- [ses](#ses)

- [sesv2](#sesv2)

- [sfn](#sfn)

- [shield](#shield)

- [signer](#signer)

- [sns](#sns)

- [sqs](#sqs)

- [ssm](#ssm)

- [ssmcontacts](#ssmcontacts)

- [ssmincidents](#ssmincidents)

- [ssmquicksetup](#ssmquicksetup)

- [ssoadmin](#ssoadmin)

- [storagegateway](#storagegateway)

- [swf](#swf)

- [synthetics](#synthetics)

- [timestreaminfluxdb](#timestreaminfluxdb)

- [timestreamwrite](#timestreamwrite)

- [transcribe](#transcribe)

- [transfer](#transfer)

- [verifiedpermissions](#verifiedpermissions)

- [vpclattice](#vpclattice)

- [waf](#waf)

- [wafregional](#wafregional)

- [wafv2](#wafv2)

- [worklink](#worklink)

- [workspaces](#workspaces)

- [xray](#xray)



## accessanalyzer

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Analyzer | aws_accessanalyzer_analyzer | SDK |


### Examples


#### Analyzer

```hcl
resource "aws_accessanalyzer_analyzer" "example" {
  # Example configuration for Analyzer
  name = "example-analyzer"

  # Common attributes
  tags = {
    Name        = "example-analyzer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## account

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Region | aws_account_region | SDK |


### Examples


#### Region

```hcl
resource "aws_account_region" "example" {
  # Example configuration for Region
  name = "example-region"

  # Common attributes
  tags = {
    Name        = "example-region"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## acm

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Certificate | aws_acm_certificate | SDK |


### Examples


#### Certificate

```hcl
resource "aws_acm_certificate" "example" {
  # Example configuration for Certificate
  name = "example-certificate"

  # Common attributes
  tags = {
    Name        = "example-certificate"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## acmpca

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Certificate | aws_acmpca_certificate | SDK |
| Certificate Authority | aws_acmpca_certificate_authority | SDK |
| Certificate Authority Certificate | aws_acmpca_certificate_authority_certificate | SDK |
| Permission | aws_acmpca_permission | SDK |
| Policy | aws_acmpca_policy | SDK |


### Examples


#### Certificate

```hcl
resource "aws_acmpca_certificate" "example" {
  # Example configuration for Certificate
  name = "example-certificate"

  # Common attributes
  tags = {
    Name        = "example-certificate"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Certificate Authority

```hcl
resource "aws_acmpca_certificate_authority" "example" {
  # Example configuration for Certificate Authority
  name = "example-certificate_authority"

  # Common attributes
  tags = {
    Name        = "example-certificate_authority"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Certificate Authority Certificate

```hcl
resource "aws_acmpca_certificate_authority_certificate" "example" {
  # Example configuration for Certificate Authority Certificate
  name = "example-certificate_authority_certificate"

  # Common attributes
  tags = {
    Name        = "example-certificate_authority_certificate"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Permission

```hcl
resource "aws_acmpca_permission" "example" {
  # Example configuration for Permission
  name = "example-permission"

  # Common attributes
  tags = {
    Name        = "example-permission"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Policy

```hcl
resource "aws_acmpca_policy" "example" {
  # Example configuration for Policy
  name = "example-policy"

  # Common attributes
  tags = {
    Name        = "example-policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## amp

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Alert Manager Definition | aws_prometheus_alert_manager_definition | SDK |
| Rule Group Namespace | aws_prometheus_rule_group_namespace | SDK |
| Scraper | N/A | Framework |
| Workspace | aws_prometheus_workspace | SDK |


### Examples


#### Alert Manager Definition

```hcl
resource "aws_prometheus_alert_manager_definition" "example" {
  # Example configuration for Alert Manager Definition
  name = "example-alert_manager_definition"

  # Common attributes
  tags = {
    Name        = "example-alert_manager_definition"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Rule Group Namespace

```hcl
resource "aws_prometheus_rule_group_namespace" "example" {
  # Example configuration for Rule Group Namespace
  name = "example-rule_group_namespace"

  # Common attributes
  tags = {
    Name        = "example-rule_group_namespace"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Scraper

```hcl
resource "aws_amp_scraper" "example" {
  # Example configuration for Scraper
  name = "example-scraper"

  # Common attributes
  tags = {
    Name        = "example-scraper"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Workspace

```hcl
resource "aws_prometheus_workspace" "example" {
  # Example configuration for Workspace
  name = "example-workspace"

  # Common attributes
  tags = {
    Name        = "example-workspace"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## amplify

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| App | aws_amplify_app | SDK |
| Backend Environment | aws_amplify_backend_environment | SDK |
| Branch | aws_amplify_branch | SDK |
| Domain Association | aws_amplify_domain_association | SDK |
| Webhook | aws_amplify_webhook | SDK |


### Examples


#### App

```hcl
resource "aws_amplify_app" "example" {
  # Example configuration for App
  name = "example-app"

  # Common attributes
  tags = {
    Name        = "example-app"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Backend Environment

```hcl
resource "aws_amplify_backend_environment" "example" {
  # Example configuration for Backend Environment
  name = "example-backend_environment"

  # Common attributes
  tags = {
    Name        = "example-backend_environment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Branch

```hcl
resource "aws_amplify_branch" "example" {
  # Example configuration for Branch
  name = "example-branch"

  # Common attributes
  tags = {
    Name        = "example-branch"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain Association

```hcl
resource "aws_amplify_domain_association" "example" {
  # Example configuration for Domain Association
  name = "example-domain_association"

  # Common attributes
  tags = {
    Name        = "example-domain_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Webhook

```hcl
resource "aws_amplify_webhook" "example" {
  # Example configuration for Webhook
  name = "example-webhook"

  # Common attributes
  tags = {
    Name        = "example-webhook"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## apigateway

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| API Key | aws_api_gateway_api_key | SDK |
| Authorizer | aws_api_gateway_authorizer | SDK |
| Base Path Mapping | aws_api_gateway_base_path_mapping | SDK |
| Client Certificate | aws_api_gateway_client_certificate | SDK |
| Deployment | aws_api_gateway_deployment | SDK |
| Documentation Part | aws_api_gateway_documentation_part | SDK |
| Documentation Version | aws_api_gateway_documentation_version | SDK |
| Domain Name | aws_api_gateway_domain_name | SDK |
| Domain Name Access Association | N/A | Framework |
| Gateway Response | aws_api_gateway_gateway_response | SDK |
| Integration | aws_api_gateway_integration | SDK |
| Integration Response | aws_api_gateway_integration_response | SDK |
| Method | aws_api_gateway_method | SDK |
| Method Response | aws_api_gateway_method_response | SDK |
| Method Settings | aws_api_gateway_method_settings | SDK |
| Model | aws_api_gateway_model | SDK |
| REST API | aws_api_gateway_rest_api | SDK |
| REST API Policy | aws_api_gateway_rest_api_policy | SDK |
| Request Validator | aws_api_gateway_request_validator | SDK |
| Resource | aws_api_gateway_resource | SDK |
| Stage | aws_api_gateway_stage | SDK |
| Usage Plan | aws_api_gateway_usage_plan | SDK |
| Usage Plan Key | aws_api_gateway_usage_plan_key | SDK |
| VPC Link | aws_api_gateway_vpc_link | SDK |


### Examples


#### API Key

```hcl
resource "aws_api_gateway_api_key" "example" {
  # Example configuration for API Key
  name = "example-api_key"

  # Common attributes
  tags = {
    Name        = "example-api_key"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Authorizer

```hcl
resource "aws_api_gateway_authorizer" "example" {
  # Example configuration for Authorizer
  name = "example-authorizer"

  # Common attributes
  tags = {
    Name        = "example-authorizer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Base Path Mapping

```hcl
resource "aws_api_gateway_base_path_mapping" "example" {
  # Example configuration for Base Path Mapping
  name = "example-base_path_mapping"

  # Common attributes
  tags = {
    Name        = "example-base_path_mapping"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Client Certificate

```hcl
resource "aws_api_gateway_client_certificate" "example" {
  # Example configuration for Client Certificate
  name = "example-client_certificate"

  # Common attributes
  tags = {
    Name        = "example-client_certificate"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Deployment

```hcl
resource "aws_api_gateway_deployment" "example" {
  # Example configuration for Deployment
  name = "example-deployment"

  # Common attributes
  tags = {
    Name        = "example-deployment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Documentation Part

```hcl
resource "aws_api_gateway_documentation_part" "example" {
  # Example configuration for Documentation Part
  name = "example-documentation_part"

  # Common attributes
  tags = {
    Name        = "example-documentation_part"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Documentation Version

```hcl
resource "aws_api_gateway_documentation_version" "example" {
  # Example configuration for Documentation Version
  name = "example-documentation_version"

  # Common attributes
  tags = {
    Name        = "example-documentation_version"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain Name

```hcl
resource "aws_api_gateway_domain_name" "example" {
  # Example configuration for Domain Name
  name = "example-domain_name"

  # Common attributes
  tags = {
    Name        = "example-domain_name"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain Name Access Association

```hcl
resource "aws_apigateway_domain_name_access_association" "example" {
  # Example configuration for Domain Name Access Association
  name = "example-domain_name_access_association"

  # Common attributes
  tags = {
    Name        = "example-domain_name_access_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Gateway Response

```hcl
resource "aws_api_gateway_gateway_response" "example" {
  # Example configuration for Gateway Response
  name = "example-gateway_response"

  # Common attributes
  tags = {
    Name        = "example-gateway_response"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Integration

```hcl
resource "aws_api_gateway_integration" "example" {
  # Example configuration for Integration
  name = "example-integration"

  # Common attributes
  tags = {
    Name        = "example-integration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Integration Response

```hcl
resource "aws_api_gateway_integration_response" "example" {
  # Example configuration for Integration Response
  name = "example-integration_response"

  # Common attributes
  tags = {
    Name        = "example-integration_response"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Method

```hcl
resource "aws_api_gateway_method" "example" {
  # Example configuration for Method
  name = "example-method"

  # Common attributes
  tags = {
    Name        = "example-method"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Method Response

```hcl
resource "aws_api_gateway_method_response" "example" {
  # Example configuration for Method Response
  name = "example-method_response"

  # Common attributes
  tags = {
    Name        = "example-method_response"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Method Settings

```hcl
resource "aws_api_gateway_method_settings" "example" {
  # Example configuration for Method Settings
  name = "example-method_settings"

  # Common attributes
  tags = {
    Name        = "example-method_settings"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Model

```hcl
resource "aws_api_gateway_model" "example" {
  # Example configuration for Model
  name = "example-model"

  # Common attributes
  tags = {
    Name        = "example-model"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### REST API

```hcl
resource "aws_api_gateway_rest_api" "example" {
  name        = "example-api"
  description = "Example API Gateway"
}
```


#### REST API Policy

```hcl
resource "aws_api_gateway_rest_api_policy" "example" {
  # Example configuration for REST API Policy
  name = "example-rest_api_policy"

  # Common attributes
  tags = {
    Name        = "example-rest_api_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Request Validator

```hcl
resource "aws_api_gateway_request_validator" "example" {
  # Example configuration for Request Validator
  name = "example-request_validator"

  # Common attributes
  tags = {
    Name        = "example-request_validator"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource

```hcl
resource "aws_api_gateway_resource" "example" {
  # Example configuration for Resource
  name = "example-resource"

  # Common attributes
  tags = {
    Name        = "example-resource"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Stage

```hcl
resource "aws_api_gateway_stage" "example" {
  # Example configuration for Stage
  name = "example-stage"

  # Common attributes
  tags = {
    Name        = "example-stage"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Usage Plan

```hcl
resource "aws_api_gateway_usage_plan" "example" {
  # Example configuration for Usage Plan
  name = "example-usage_plan"

  # Common attributes
  tags = {
    Name        = "example-usage_plan"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Usage Plan Key

```hcl
resource "aws_api_gateway_usage_plan_key" "example" {
  # Example configuration for Usage Plan Key
  name = "example-usage_plan_key"

  # Common attributes
  tags = {
    Name        = "example-usage_plan_key"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Link

```hcl
resource "aws_api_gateway_vpc_link" "example" {
  # Example configuration for VPC Link
  name = "example-vpc_link"

  # Common attributes
  tags = {
    Name        = "example-vpc_link"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## apigatewayv2

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| API | aws_apigatewayv2_api | SDK |
| API Mapping | aws_apigatewayv2_api_mapping | SDK |
| Authorizer | aws_apigatewayv2_authorizer | SDK |
| Deployment | aws_apigatewayv2_deployment | SDK |
| Domain Name | aws_apigatewayv2_domain_name | SDK |
| Integration | aws_apigatewayv2_integration | SDK |
| Integration Response | aws_apigatewayv2_integration_response | SDK |
| Model | aws_apigatewayv2_model | SDK |
| Route | aws_apigatewayv2_route | SDK |
| Route Response | aws_apigatewayv2_route_response | SDK |
| Stage | aws_apigatewayv2_stage | SDK |
| VPC Link | aws_apigatewayv2_vpc_link | SDK |


### Examples


#### API

```hcl
resource "aws_apigatewayv2_api" "example" {
  # Example configuration for API
  name = "example-api"

  # Common attributes
  tags = {
    Name        = "example-api"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### API Mapping

```hcl
resource "aws_apigatewayv2_api_mapping" "example" {
  # Example configuration for API Mapping
  name = "example-api_mapping"

  # Common attributes
  tags = {
    Name        = "example-api_mapping"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Authorizer

```hcl
resource "aws_apigatewayv2_authorizer" "example" {
  # Example configuration for Authorizer
  name = "example-authorizer"

  # Common attributes
  tags = {
    Name        = "example-authorizer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Deployment

```hcl
resource "aws_apigatewayv2_deployment" "example" {
  # Example configuration for Deployment
  name = "example-deployment"

  # Common attributes
  tags = {
    Name        = "example-deployment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain Name

```hcl
resource "aws_apigatewayv2_domain_name" "example" {
  # Example configuration for Domain Name
  name = "example-domain_name"

  # Common attributes
  tags = {
    Name        = "example-domain_name"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Integration

```hcl
resource "aws_apigatewayv2_integration" "example" {
  # Example configuration for Integration
  name = "example-integration"

  # Common attributes
  tags = {
    Name        = "example-integration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Integration Response

```hcl
resource "aws_apigatewayv2_integration_response" "example" {
  # Example configuration for Integration Response
  name = "example-integration_response"

  # Common attributes
  tags = {
    Name        = "example-integration_response"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Model

```hcl
resource "aws_apigatewayv2_model" "example" {
  # Example configuration for Model
  name = "example-model"

  # Common attributes
  tags = {
    Name        = "example-model"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Route

```hcl
resource "aws_apigatewayv2_route" "example" {
  # Example configuration for Route
  name = "example-route"

  # Common attributes
  tags = {
    Name        = "example-route"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Route Response

```hcl
resource "aws_apigatewayv2_route_response" "example" {
  # Example configuration for Route Response
  name = "example-route_response"

  # Common attributes
  tags = {
    Name        = "example-route_response"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Stage

```hcl
resource "aws_apigatewayv2_stage" "example" {
  # Example configuration for Stage
  name = "example-stage"

  # Common attributes
  tags = {
    Name        = "example-stage"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Link

```hcl
resource "aws_apigatewayv2_vpc_link" "example" {
  # Example configuration for VPC Link
  name = "example-vpc_link"

  # Common attributes
  tags = {
    Name        = "example-vpc_link"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## appautoscaling

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Scaling Policy | aws_appautoscaling_policy | SDK |
| Target | aws_appautoscaling_target | SDK |


### Examples


#### Scaling Policy

```hcl
resource "aws_appautoscaling_policy" "example" {
  # Example configuration for Scaling Policy
  name = "example-scaling_policy"

  # Common attributes
  tags = {
    Name        = "example-scaling_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Target

```hcl
resource "aws_appautoscaling_target" "example" {
  # Example configuration for Target
  name = "example-target"

  # Common attributes
  tags = {
    Name        = "example-target"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## appconfig

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Application | aws_appconfig_application | SDK |
| Configuration Profile | aws_appconfig_configuration_profile | SDK |
| Deployment | aws_appconfig_deployment | SDK |
| Deployment Strategy | aws_appconfig_deployment_strategy | SDK |
| Environment | N/A | Framework |
| Extension | aws_appconfig_extension | SDK |


### Examples


#### Application

```hcl
resource "aws_appconfig_application" "example" {
  # Example configuration for Application
  name = "example-application"

  # Common attributes
  tags = {
    Name        = "example-application"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Configuration Profile

```hcl
resource "aws_appconfig_configuration_profile" "example" {
  # Example configuration for Configuration Profile
  name = "example-configuration_profile"

  # Common attributes
  tags = {
    Name        = "example-configuration_profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Deployment

```hcl
resource "aws_appconfig_deployment" "example" {
  # Example configuration for Deployment
  name = "example-deployment"

  # Common attributes
  tags = {
    Name        = "example-deployment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Deployment Strategy

```hcl
resource "aws_appconfig_deployment_strategy" "example" {
  # Example configuration for Deployment Strategy
  name = "example-deployment_strategy"

  # Common attributes
  tags = {
    Name        = "example-deployment_strategy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Environment

```hcl
resource "aws_appconfig_environment" "example" {
  # Example configuration for Environment
  name = "example-environment"

  # Common attributes
  tags = {
    Name        = "example-environment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Extension

```hcl
resource "aws_appconfig_extension" "example" {
  # Example configuration for Extension
  name = "example-extension"

  # Common attributes
  tags = {
    Name        = "example-extension"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## appfabric

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| App Authorization | N/A | Framework |
| App Authorization Connection | N/A | Framework |
| App Bundle | N/A | Framework |
| Ingestion | N/A | Framework |
| Ingestion Destination | N/A | Framework |


### Examples


#### App Authorization

```hcl
resource "aws_appfabric_app_authorization" "example" {
  # Example configuration for App Authorization
  name = "example-app_authorization"

  # Common attributes
  tags = {
    Name        = "example-app_authorization"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### App Authorization Connection

```hcl
resource "aws_appfabric_app_authorization_connection" "example" {
  # Example configuration for App Authorization Connection
  name = "example-app_authorization_connection"

  # Common attributes
  tags = {
    Name        = "example-app_authorization_connection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### App Bundle

```hcl
resource "aws_appfabric_app_bundle" "example" {
  # Example configuration for App Bundle
  name = "example-app_bundle"

  # Common attributes
  tags = {
    Name        = "example-app_bundle"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Ingestion

```hcl
resource "aws_appfabric_ingestion" "example" {
  # Example configuration for Ingestion
  name = "example-ingestion"

  # Common attributes
  tags = {
    Name        = "example-ingestion"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Ingestion Destination

```hcl
resource "aws_appfabric_ingestion_destination" "example" {
  # Example configuration for Ingestion Destination
  name = "example-ingestion_destination"

  # Common attributes
  tags = {
    Name        = "example-ingestion_destination"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## appflow

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Connector Profile | aws_appflow_connector_profile | SDK |
| Flow | aws_appflow_flow | SDK |


### Examples


#### Connector Profile

```hcl
resource "aws_appflow_connector_profile" "example" {
  # Example configuration for Connector Profile
  name = "example-connector_profile"

  # Common attributes
  tags = {
    Name        = "example-connector_profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Flow

```hcl
resource "aws_appflow_flow" "example" {
  # Example configuration for Flow
  name = "example-flow"

  # Common attributes
  tags = {
    Name        = "example-flow"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## appintegrations

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Data Integration | aws_appintegrations_data_integration | SDK |
| Event Integration | aws_appintegrations_event_integration | SDK |


### Examples


#### Data Integration

```hcl
resource "aws_appintegrations_data_integration" "example" {
  # Example configuration for Data Integration
  name = "example-data_integration"

  # Common attributes
  tags = {
    Name        = "example-data_integration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Event Integration

```hcl
resource "aws_appintegrations_event_integration" "example" {
  # Example configuration for Event Integration
  name = "example-event_integration"

  # Common attributes
  tags = {
    Name        = "example-event_integration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## applicationinsights

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Application | aws_applicationinsights_application | SDK |


### Examples


#### Application

```hcl
resource "aws_applicationinsights_application" "example" {
  # Example configuration for Application
  name = "example-application"

  # Common attributes
  tags = {
    Name        = "example-application"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## appmesh

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Gateway Route | aws_appmesh_gateway_route | SDK |
| Route | aws_appmesh_route | SDK |
| Service Mesh | aws_appmesh_mesh | SDK |
| Virtual Gateway | aws_appmesh_virtual_gateway | SDK |
| Virtual Node | aws_appmesh_virtual_node | SDK |
| Virtual Router | aws_appmesh_virtual_router | SDK |
| Virtual Service | aws_appmesh_virtual_service | SDK |


### Examples


#### Gateway Route

```hcl
resource "aws_appmesh_gateway_route" "example" {
  # Example configuration for Gateway Route
  name = "example-gateway_route"

  # Common attributes
  tags = {
    Name        = "example-gateway_route"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Route

```hcl
resource "aws_appmesh_route" "example" {
  # Example configuration for Route
  name = "example-route"

  # Common attributes
  tags = {
    Name        = "example-route"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Service Mesh

```hcl
resource "aws_appmesh_mesh" "example" {
  # Example configuration for Service Mesh
  name = "example-service_mesh"

  # Common attributes
  tags = {
    Name        = "example-service_mesh"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Virtual Gateway

```hcl
resource "aws_appmesh_virtual_gateway" "example" {
  # Example configuration for Virtual Gateway
  name = "example-virtual_gateway"

  # Common attributes
  tags = {
    Name        = "example-virtual_gateway"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Virtual Node

```hcl
resource "aws_appmesh_virtual_node" "example" {
  # Example configuration for Virtual Node
  name = "example-virtual_node"

  # Common attributes
  tags = {
    Name        = "example-virtual_node"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Virtual Router

```hcl
resource "aws_appmesh_virtual_router" "example" {
  # Example configuration for Virtual Router
  name = "example-virtual_router"

  # Common attributes
  tags = {
    Name        = "example-virtual_router"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Virtual Service

```hcl
resource "aws_appmesh_virtual_service" "example" {
  # Example configuration for Virtual Service
  name = "example-virtual_service"

  # Common attributes
  tags = {
    Name        = "example-virtual_service"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## apprunner

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| AutoScaling Configuration Version | aws_apprunner_auto_scaling_configuration_version | SDK |
| Connection | aws_apprunner_connection | SDK |
| Custom Domain Association | aws_apprunner_custom_domain_association | SDK |
| Default AutoScaling Configuration Version | N/A | Framework |
| Deployment | N/A | Framework |
| Observability Configuration | aws_apprunner_observability_configuration | SDK |
| Service | aws_apprunner_service | SDK |
| VPC Connector | aws_apprunner_vpc_connector | SDK |
| VPC Ingress Connection | aws_apprunner_vpc_ingress_connection | SDK |


### Examples


#### AutoScaling Configuration Version

```hcl
resource "aws_apprunner_auto_scaling_configuration_version" "example" {
  # Example configuration for AutoScaling Configuration Version
  name = "example-autoscaling_configuration_version"

  # Common attributes
  tags = {
    Name        = "example-autoscaling_configuration_version"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Connection

```hcl
resource "aws_apprunner_connection" "example" {
  # Example configuration for Connection
  name = "example-connection"

  # Common attributes
  tags = {
    Name        = "example-connection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Custom Domain Association

```hcl
resource "aws_apprunner_custom_domain_association" "example" {
  # Example configuration for Custom Domain Association
  name = "example-custom_domain_association"

  # Common attributes
  tags = {
    Name        = "example-custom_domain_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Default AutoScaling Configuration Version

```hcl
resource "aws_apprunner_default_autoscaling_configuration_version" "example" {
  # Example configuration for Default AutoScaling Configuration Version
  name = "example-default_autoscaling_configuration_version"

  # Common attributes
  tags = {
    Name        = "example-default_autoscaling_configuration_version"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Deployment

```hcl
resource "aws_apprunner_deployment" "example" {
  # Example configuration for Deployment
  name = "example-deployment"

  # Common attributes
  tags = {
    Name        = "example-deployment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Observability Configuration

```hcl
resource "aws_apprunner_observability_configuration" "example" {
  # Example configuration for Observability Configuration
  name = "example-observability_configuration"

  # Common attributes
  tags = {
    Name        = "example-observability_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Service

```hcl
resource "aws_apprunner_service" "example" {
  # Example configuration for Service
  name = "example-service"

  # Common attributes
  tags = {
    Name        = "example-service"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Connector

```hcl
resource "aws_apprunner_vpc_connector" "example" {
  # Example configuration for VPC Connector
  name = "example-vpc_connector"

  # Common attributes
  tags = {
    Name        = "example-vpc_connector"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Ingress Connection

```hcl
resource "aws_apprunner_vpc_ingress_connection" "example" {
  # Example configuration for VPC Ingress Connection
  name = "example-vpc_ingress_connection"

  # Common attributes
  tags = {
    Name        = "example-vpc_ingress_connection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## appstream

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Fleet | aws_appstream_fleet | SDK |
| Image Builder | aws_appstream_image_builder | SDK |
| Stack | aws_appstream_stack | SDK |


### Examples


#### Fleet

```hcl
resource "aws_appstream_fleet" "example" {
  # Example configuration for Fleet
  name = "example-fleet"

  # Common attributes
  tags = {
    Name        = "example-fleet"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Image Builder

```hcl
resource "aws_appstream_image_builder" "example" {
  # Example configuration for Image Builder
  name = "example-image_builder"

  # Common attributes
  tags = {
    Name        = "example-image_builder"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Stack

```hcl
resource "aws_appstream_stack" "example" {
  # Example configuration for Stack
  name = "example-stack"

  # Common attributes
  tags = {
    Name        = "example-stack"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## appsync

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| API Cache | aws_appsync_api_cache | SDK |
| API Key | aws_appsync_api_key | SDK |
| Data Source | aws_appsync_datasource | SDK |
| Domain Name | aws_appsync_domain_name | SDK |
| Domain Name API Association | aws_appsync_domain_name_api_association | SDK |
| Function | aws_appsync_function | SDK |
| GraphQL API | aws_appsync_graphql_api | SDK |
| Resolver | aws_appsync_resolver | SDK |
| Source API Association | N/A | Framework |
| Type | aws_appsync_type | SDK |


### Examples


#### API Cache

```hcl
resource "aws_appsync_api_cache" "example" {
  # Example configuration for API Cache
  name = "example-api_cache"

  # Common attributes
  tags = {
    Name        = "example-api_cache"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### API Key

```hcl
resource "aws_appsync_api_key" "example" {
  # Example configuration for API Key
  name = "example-api_key"

  # Common attributes
  tags = {
    Name        = "example-api_key"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Data Source

```hcl
resource "aws_appsync_datasource" "example" {
  # Example configuration for Data Source
  name = "example-data_source"

  # Common attributes
  tags = {
    Name        = "example-data_source"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain Name

```hcl
resource "aws_appsync_domain_name" "example" {
  # Example configuration for Domain Name
  name = "example-domain_name"

  # Common attributes
  tags = {
    Name        = "example-domain_name"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain Name API Association

```hcl
resource "aws_appsync_domain_name_api_association" "example" {
  # Example configuration for Domain Name API Association
  name = "example-domain_name_api_association"

  # Common attributes
  tags = {
    Name        = "example-domain_name_api_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Function

```hcl
resource "aws_appsync_function" "example" {
  # Example configuration for Function
  name = "example-function"

  # Common attributes
  tags = {
    Name        = "example-function"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### GraphQL API

```hcl
resource "aws_appsync_graphql_api" "example" {
  # Example configuration for GraphQL API
  name = "example-graphql_api"

  # Common attributes
  tags = {
    Name        = "example-graphql_api"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resolver

```hcl
resource "aws_appsync_resolver" "example" {
  # Example configuration for Resolver
  name = "example-resolver"

  # Common attributes
  tags = {
    Name        = "example-resolver"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Source API Association

```hcl
resource "aws_appsync_source_api_association" "example" {
  # Example configuration for Source API Association
  name = "example-source_api_association"

  # Common attributes
  tags = {
    Name        = "example-source_api_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Type

```hcl
resource "aws_appsync_type" "example" {
  # Example configuration for Type
  name = "example-type"

  # Common attributes
  tags = {
    Name        = "example-type"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## athena

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Data Catalog | aws_athena_data_catalog | SDK |
| Prepared Statement | aws_athena_prepared_statement | SDK |
| WorkGroup | aws_athena_workgroup | SDK |


### Examples


#### Data Catalog

```hcl
resource "aws_athena_data_catalog" "example" {
  # Example configuration for Data Catalog
  name = "example-data_catalog"

  # Common attributes
  tags = {
    Name        = "example-data_catalog"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Prepared Statement

```hcl
resource "aws_athena_prepared_statement" "example" {
  # Example configuration for Prepared Statement
  name = "example-prepared_statement"

  # Common attributes
  tags = {
    Name        = "example-prepared_statement"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### WorkGroup

```hcl
resource "aws_athena_workgroup" "example" {
  # Example configuration for WorkGroup
  name = "example-workgroup"

  # Common attributes
  tags = {
    Name        = "example-workgroup"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## auditmanager

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Assessment | N/A | Framework |
| Control | N/A | Framework |
| Framework | N/A | Framework |


### Examples


#### Assessment

```hcl
resource "aws_auditmanager_assessment" "example" {
  # Example configuration for Assessment
  name = "example-assessment"

  # Common attributes
  tags = {
    Name        = "example-assessment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Control

```hcl
resource "aws_auditmanager_control" "example" {
  # Example configuration for Control
  name = "example-control"

  # Common attributes
  tags = {
    Name        = "example-control"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Framework

```hcl
resource "aws_auditmanager_framework" "example" {
  # Example configuration for Framework
  name = "example-framework"

  # Common attributes
  tags = {
    Name        = "example-framework"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## autoscaling

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Attachment | aws_autoscaling_attachment | SDK |
| Group | aws_autoscaling_group | SDK |
| Group Tag | aws_autoscaling_group_tag | SDK |
| Launch Configuration | aws_launch_configuration | SDK |
| Lifecycle Hook | aws_autoscaling_lifecycle_hook | SDK |
| Notification | aws_autoscaling_notification | SDK |
| Policy | aws_autoscaling_policy | SDK |
| Scheduled Action | aws_autoscaling_schedule | SDK |
| Traffic Source Attachment | aws_autoscaling_traffic_source_attachment | SDK |


### Examples


#### Attachment

```hcl
resource "aws_autoscaling_attachment" "example" {
  # Example configuration for Attachment
  name = "example-attachment"

  # Common attributes
  tags = {
    Name        = "example-attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Group

```hcl
resource "aws_autoscaling_group" "example" {
  # Example configuration for Group
  name = "example-group"

  # Common attributes
  tags = {
    Name        = "example-group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Group Tag

```hcl
resource "aws_autoscaling_group_tag" "example" {
  # Example configuration for Group Tag
  name = "example-group_tag"

  # Common attributes
  tags = {
    Name        = "example-group_tag"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Launch Configuration

```hcl
resource "aws_launch_configuration" "example" {
  # Example configuration for Launch Configuration
  name = "example-launch_configuration"

  # Common attributes
  tags = {
    Name        = "example-launch_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Lifecycle Hook

```hcl
resource "aws_autoscaling_lifecycle_hook" "example" {
  # Example configuration for Lifecycle Hook
  name = "example-lifecycle_hook"

  # Common attributes
  tags = {
    Name        = "example-lifecycle_hook"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Notification

```hcl
resource "aws_autoscaling_notification" "example" {
  # Example configuration for Notification
  name = "example-notification"

  # Common attributes
  tags = {
    Name        = "example-notification"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Policy

```hcl
resource "aws_autoscaling_policy" "example" {
  # Example configuration for Policy
  name = "example-policy"

  # Common attributes
  tags = {
    Name        = "example-policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Scheduled Action

```hcl
resource "aws_autoscaling_schedule" "example" {
  # Example configuration for Scheduled Action
  name = "example-scheduled_action"

  # Common attributes
  tags = {
    Name        = "example-scheduled_action"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Traffic Source Attachment

```hcl
resource "aws_autoscaling_traffic_source_attachment" "example" {
  # Example configuration for Traffic Source Attachment
  name = "example-traffic_source_attachment"

  # Common attributes
  tags = {
    Name        = "example-traffic_source_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## backup

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Framework | aws_backup_framework | SDK |
| Global Settings | aws_backup_global_settings | SDK |
| Logically Air Gapped Vault | N/A | Framework |
| Plan | aws_backup_plan | SDK |
| Region Settings | aws_backup_region_settings | SDK |
| Report Plan | aws_backup_report_plan | SDK |
| Restore Testing Plan | N/A | Framework |
| Restore Testing Plan Selection | N/A | Framework |
| Selection | aws_backup_selection | SDK |
| Vault | aws_backup_vault | SDK |
| Vault Lock Configuration | aws_backup_vault_lock_configuration | SDK |
| Vault Notifications | aws_backup_vault_notifications | SDK |
| Vault Policy | aws_backup_vault_policy | SDK |


### Examples


#### Framework

```hcl
resource "aws_backup_framework" "example" {
  # Example configuration for Framework
  name = "example-framework"

  # Common attributes
  tags = {
    Name        = "example-framework"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Global Settings

```hcl
resource "aws_backup_global_settings" "example" {
  # Example configuration for Global Settings
  name = "example-global_settings"

  # Common attributes
  tags = {
    Name        = "example-global_settings"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Logically Air Gapped Vault

```hcl
resource "aws_backup_logically_air_gapped_vault" "example" {
  # Example configuration for Logically Air Gapped Vault
  name = "example-logically_air_gapped_vault"

  # Common attributes
  tags = {
    Name        = "example-logically_air_gapped_vault"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Plan

```hcl
resource "aws_backup_plan" "example" {
  # Example configuration for Plan
  name = "example-plan"

  # Common attributes
  tags = {
    Name        = "example-plan"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Region Settings

```hcl
resource "aws_backup_region_settings" "example" {
  # Example configuration for Region Settings
  name = "example-region_settings"

  # Common attributes
  tags = {
    Name        = "example-region_settings"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Report Plan

```hcl
resource "aws_backup_report_plan" "example" {
  # Example configuration for Report Plan
  name = "example-report_plan"

  # Common attributes
  tags = {
    Name        = "example-report_plan"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Restore Testing Plan

```hcl
resource "aws_backup_restore_testing_plan" "example" {
  # Example configuration for Restore Testing Plan
  name = "example-restore_testing_plan"

  # Common attributes
  tags = {
    Name        = "example-restore_testing_plan"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Restore Testing Plan Selection

```hcl
resource "aws_backup_restore_testing_plan_selection" "example" {
  # Example configuration for Restore Testing Plan Selection
  name = "example-restore_testing_plan_selection"

  # Common attributes
  tags = {
    Name        = "example-restore_testing_plan_selection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Selection

```hcl
resource "aws_backup_selection" "example" {
  # Example configuration for Selection
  name = "example-selection"

  # Common attributes
  tags = {
    Name        = "example-selection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Vault

```hcl
resource "aws_backup_vault" "example" {
  # Example configuration for Vault
  name = "example-vault"

  # Common attributes
  tags = {
    Name        = "example-vault"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Vault Lock Configuration

```hcl
resource "aws_backup_vault_lock_configuration" "example" {
  # Example configuration for Vault Lock Configuration
  name = "example-vault_lock_configuration"

  # Common attributes
  tags = {
    Name        = "example-vault_lock_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Vault Notifications

```hcl
resource "aws_backup_vault_notifications" "example" {
  # Example configuration for Vault Notifications
  name = "example-vault_notifications"

  # Common attributes
  tags = {
    Name        = "example-vault_notifications"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Vault Policy

```hcl
resource "aws_backup_vault_policy" "example" {
  # Example configuration for Vault Policy
  name = "example-vault_policy"

  # Common attributes
  tags = {
    Name        = "example-vault_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## batch

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Compute Environment | aws_batch_compute_environment | SDK |
| Job Definition | aws_batch_job_definition | SDK |
| Job Queue | N/A | Framework |
| Scheduling Policy | aws_batch_scheduling_policy | SDK |


### Examples


#### Compute Environment

```hcl
resource "aws_batch_compute_environment" "example" {
  # Example configuration for Compute Environment
  name = "example-compute_environment"

  # Common attributes
  tags = {
    Name        = "example-compute_environment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Job Definition

```hcl
resource "aws_batch_job_definition" "example" {
  # Example configuration for Job Definition
  name = "example-job_definition"

  # Common attributes
  tags = {
    Name        = "example-job_definition"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Job Queue

```hcl
resource "aws_batch_job_queue" "example" {
  # Example configuration for Job Queue
  name = "example-job_queue"

  # Common attributes
  tags = {
    Name        = "example-job_queue"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Scheduling Policy

```hcl
resource "aws_batch_scheduling_policy" "example" {
  # Example configuration for Scheduling Policy
  name = "example-scheduling_policy"

  # Common attributes
  tags = {
    Name        = "example-scheduling_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## bcmdataexports

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Export | N/A | Framework |


### Examples


#### Export

```hcl
resource "aws_bcmdataexports_export" "example" {
  # Example configuration for Export
  name = "example-export"

  # Common attributes
  tags = {
    Name        = "example-export"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## bedrock

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Custom Model | N/A | Framework |
| Guardrail | N/A | Framework |
| Guardrail Version | N/A | Framework |
| Inference Profile | N/A | Framework |
| Model Invocation Logging Configuration | N/A | Framework |
| Provisioned Model Throughput | N/A | Framework |


### Examples


#### Custom Model

```hcl
resource "aws_bedrock_custom_model" "example" {
  # Example configuration for Custom Model
  name = "example-custom_model"

  # Common attributes
  tags = {
    Name        = "example-custom_model"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Guardrail

```hcl
resource "aws_bedrock_guardrail" "example" {
  # Example configuration for Guardrail
  name = "example-guardrail"

  # Common attributes
  tags = {
    Name        = "example-guardrail"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Guardrail Version

```hcl
resource "aws_bedrock_guardrail_version" "example" {
  # Example configuration for Guardrail Version
  name = "example-guardrail_version"

  # Common attributes
  tags = {
    Name        = "example-guardrail_version"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Inference Profile

```hcl
resource "aws_bedrock_inference_profile" "example" {
  # Example configuration for Inference Profile
  name = "example-inference_profile"

  # Common attributes
  tags = {
    Name        = "example-inference_profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Model Invocation Logging Configuration

```hcl
resource "aws_bedrock_model_invocation_logging_configuration" "example" {
  # Example configuration for Model Invocation Logging Configuration
  name = "example-model_invocation_logging_configuration"

  # Common attributes
  tags = {
    Name        = "example-model_invocation_logging_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Provisioned Model Throughput

```hcl
resource "aws_bedrock_provisioned_model_throughput" "example" {
  # Example configuration for Provisioned Model Throughput
  name = "example-provisioned_model_throughput"

  # Common attributes
  tags = {
    Name        = "example-provisioned_model_throughput"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## bedrockagent

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Agent | N/A | Framework |
| Agent Action Group | N/A | Framework |
| Agent Alias | N/A | Framework |
| Agent Collaborator | N/A | Framework |
| Agent Knowledge Base Association | N/A | Framework |
| Data Source | N/A | Framework |
| Knowledge Base | N/A | Framework |


### Examples


#### Agent

```hcl
resource "aws_bedrockagent_agent" "example" {
  # Example configuration for Agent
  name = "example-agent"

  # Common attributes
  tags = {
    Name        = "example-agent"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Agent Action Group

```hcl
resource "aws_bedrockagent_agent_action_group" "example" {
  # Example configuration for Agent Action Group
  name = "example-agent_action_group"

  # Common attributes
  tags = {
    Name        = "example-agent_action_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Agent Alias

```hcl
resource "aws_bedrockagent_agent_alias" "example" {
  # Example configuration for Agent Alias
  name = "example-agent_alias"

  # Common attributes
  tags = {
    Name        = "example-agent_alias"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Agent Collaborator

```hcl
resource "aws_bedrockagent_agent_collaborator" "example" {
  # Example configuration for Agent Collaborator
  name = "example-agent_collaborator"

  # Common attributes
  tags = {
    Name        = "example-agent_collaborator"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Agent Knowledge Base Association

```hcl
resource "aws_bedrockagent_agent_knowledge_base_association" "example" {
  # Example configuration for Agent Knowledge Base Association
  name = "example-agent_knowledge_base_association"

  # Common attributes
  tags = {
    Name        = "example-agent_knowledge_base_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Data Source

```hcl
resource "aws_bedrockagent_data_source" "example" {
  # Example configuration for Data Source
  name = "example-data_source"

  # Common attributes
  tags = {
    Name        = "example-data_source"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Knowledge Base

```hcl
resource "aws_bedrockagent_knowledge_base" "example" {
  # Example configuration for Knowledge Base
  name = "example-knowledge_base"

  # Common attributes
  tags = {
    Name        = "example-knowledge_base"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## budgets

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Budget | aws_budgets_budget | SDK |


### Examples


#### Budget

```hcl
resource "aws_budgets_budget" "example" {
  # Example configuration for Budget
  name = "example-budget"

  # Common attributes
  tags = {
    Name        = "example-budget"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## ce

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Anomaly Monitor | aws_ce_anomaly_monitor | SDK |
| Anomaly Subscription | aws_ce_anomaly_subscription | SDK |
| Cost Allocation Tag | aws_ce_cost_allocation_tag | SDK |
| Cost Category | aws_ce_cost_category | SDK |


### Examples


#### Anomaly Monitor

```hcl
resource "aws_ce_anomaly_monitor" "example" {
  # Example configuration for Anomaly Monitor
  name = "example-anomaly_monitor"

  # Common attributes
  tags = {
    Name        = "example-anomaly_monitor"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Anomaly Subscription

```hcl
resource "aws_ce_anomaly_subscription" "example" {
  # Example configuration for Anomaly Subscription
  name = "example-anomaly_subscription"

  # Common attributes
  tags = {
    Name        = "example-anomaly_subscription"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cost Allocation Tag

```hcl
resource "aws_ce_cost_allocation_tag" "example" {
  # Example configuration for Cost Allocation Tag
  name = "example-cost_allocation_tag"

  # Common attributes
  tags = {
    Name        = "example-cost_allocation_tag"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cost Category

```hcl
resource "aws_ce_cost_category" "example" {
  # Example configuration for Cost Category
  name = "example-cost_category"

  # Common attributes
  tags = {
    Name        = "example-cost_category"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## chatbot

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Slack Channel Configuration | N/A | Framework |
| Teams Channel Configuration | N/A | Framework |


### Examples


#### Slack Channel Configuration

```hcl
resource "aws_chatbot_slack_channel_configuration" "example" {
  # Example configuration for Slack Channel Configuration
  name = "example-slack_channel_configuration"

  # Common attributes
  tags = {
    Name        = "example-slack_channel_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Teams Channel Configuration

```hcl
resource "aws_chatbot_teams_channel_configuration" "example" {
  # Example configuration for Teams Channel Configuration
  name = "example-teams_channel_configuration"

  # Common attributes
  tags = {
    Name        = "example-teams_channel_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## chime

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Voice Connector | aws_chime_voice_connector | SDK |


### Examples


#### Voice Connector

```hcl
resource "aws_chime_voice_connector" "example" {
  # Example configuration for Voice Connector
  name = "example-voice_connector"

  # Common attributes
  tags = {
    Name        = "example-voice_connector"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## chimesdkmediapipelines

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Media Insights Pipeline Configuration | aws_chimesdkmediapipelines_media_insights_pipeline_configuration | SDK |


### Examples


#### Media Insights Pipeline Configuration

```hcl
resource "aws_chimesdkmediapipelines_media_insights_pipeline_configuration" "example" {
  # Example configuration for Media Insights Pipeline Configuration
  name = "example-media_insights_pipeline_configuration"

  # Common attributes
  tags = {
    Name        = "example-media_insights_pipeline_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## chimesdkvoice

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Sip Media Application | aws_chimesdkvoice_sip_media_application | SDK |
| Sip Rule | aws_chimesdkvoice_sip_rule | SDK |
| Voice Profile Domain | aws_chimesdkvoice_voice_profile_domain | SDK |


### Examples


#### Sip Media Application

```hcl
resource "aws_chimesdkvoice_sip_media_application" "example" {
  # Example configuration for Sip Media Application
  name = "example-sip_media_application"

  # Common attributes
  tags = {
    Name        = "example-sip_media_application"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Sip Rule

```hcl
resource "aws_chimesdkvoice_sip_rule" "example" {
  # Example configuration for Sip Rule
  name = "example-sip_rule"

  # Common attributes
  tags = {
    Name        = "example-sip_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Voice Profile Domain

```hcl
resource "aws_chimesdkvoice_voice_profile_domain" "example" {
  # Example configuration for Voice Profile Domain
  name = "example-voice_profile_domain"

  # Common attributes
  tags = {
    Name        = "example-voice_profile_domain"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## cleanrooms

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Membership | N/A | Framework |


### Examples


#### Membership

```hcl
resource "aws_cleanrooms_membership" "example" {
  # Example configuration for Membership
  name = "example-membership"

  # Common attributes
  tags = {
    Name        = "example-membership"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## cloud9

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Environment EC2 | aws_cloud9_environment_ec2 | SDK |
| Environment Membership | aws_cloud9_environment_membership | SDK |


### Examples


#### Environment EC2

```hcl
resource "aws_cloud9_environment_ec2" "example" {
  # Example configuration for Environment EC2
  name = "example-environment_ec2"

  # Common attributes
  tags = {
    Name        = "example-environment_ec2"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Environment Membership

```hcl
resource "aws_cloud9_environment_membership" "example" {
  # Example configuration for Environment Membership
  name = "example-environment_membership"

  # Common attributes
  tags = {
    Name        = "example-environment_membership"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## cloudcontrol

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Resource | aws_cloudcontrolapi_resource | SDK |


### Examples


#### Resource

```hcl
resource "aws_cloudcontrolapi_resource" "example" {
  # Example configuration for Resource
  name = "example-resource"

  # Common attributes
  tags = {
    Name        = "example-resource"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## cloudformation

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Stack | aws_cloudformation_stack | SDK |
| Stack Instances | aws_cloudformation_stack_instances | SDK |
| Stack Set | aws_cloudformation_stack_set | SDK |
| Stack Set Instance | aws_cloudformation_stack_set_instance | SDK |
| Type | aws_cloudformation_type | SDK |


### Examples


#### Stack

```hcl
resource "aws_cloudformation_stack" "example" {
  # Example configuration for Stack
  name = "example-stack"

  # Common attributes
  tags = {
    Name        = "example-stack"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Stack Instances

```hcl
resource "aws_cloudformation_stack_instances" "example" {
  # Example configuration for Stack Instances
  name = "example-stack_instances"

  # Common attributes
  tags = {
    Name        = "example-stack_instances"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Stack Set

```hcl
resource "aws_cloudformation_stack_set" "example" {
  # Example configuration for Stack Set
  name = "example-stack_set"

  # Common attributes
  tags = {
    Name        = "example-stack_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Stack Set Instance

```hcl
resource "aws_cloudformation_stack_set_instance" "example" {
  # Example configuration for Stack Set Instance
  name = "example-stack_set_instance"

  # Common attributes
  tags = {
    Name        = "example-stack_set_instance"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Type

```hcl
resource "aws_cloudformation_type" "example" {
  # Example configuration for Type
  name = "example-type"

  # Common attributes
  tags = {
    Name        = "example-type"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## cloudfront

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Cache Policy | aws_cloudfront_cache_policy | SDK |
| Continuous Deployment Policy | N/A | Framework |
| Distribution | aws_cloudfront_distribution | SDK |
| Field-level Encryption Config | aws_cloudfront_field_level_encryption_config | SDK |
| Field-level Encryption Profile | aws_cloudfront_field_level_encryption_profile | SDK |
| Function | aws_cloudfront_function | SDK |
| Key Group | aws_cloudfront_key_group | SDK |
| Key Value Store | N/A | Framework |
| Monitoring Subscription | aws_cloudfront_monitoring_subscription | SDK |
| Origin Access Control | aws_cloudfront_origin_access_control | SDK |
| Origin Access Identity | aws_cloudfront_origin_access_identity | SDK |
| Origin Request Policy | aws_cloudfront_origin_request_policy | SDK |
| Public Key | aws_cloudfront_public_key | SDK |
| Real-time Log Config | aws_cloudfront_realtime_log_config | SDK |
| Response Headers Policy | aws_cloudfront_response_headers_policy | SDK |
| VPC Origin | N/A | Framework |


### Examples


#### Cache Policy

```hcl
resource "aws_cloudfront_cache_policy" "example" {
  # Example configuration for Cache Policy
  name = "example-cache_policy"

  # Common attributes
  tags = {
    Name        = "example-cache_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Continuous Deployment Policy

```hcl
resource "aws_cloudfront_continuous_deployment_policy" "example" {
  # Example configuration for Continuous Deployment Policy
  name = "example-continuous_deployment_policy"

  # Common attributes
  tags = {
    Name        = "example-continuous_deployment_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Distribution

```hcl
resource "aws_cloudfront_distribution" "example" {
  origin {
    domain_name = aws_s3_bucket.example.bucket_regional_domain_name
    origin_id   = "S3-example-bucket"
  }

  enabled             = true
  default_root_object = "index.html"

  default_cache_behavior {
    allowed_methods        = ["GET", "HEAD"]
    cached_methods         = ["GET", "HEAD"]
    target_origin_id       = "S3-example-bucket"
    viewer_protocol_policy = "redirect-to-https"

    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }
}
```


#### Field-level Encryption Config

```hcl
resource "aws_cloudfront_field_level_encryption_config" "example" {
  # Example configuration for Field-level Encryption Config
  name = "example-field-level_encryption_config"

  # Common attributes
  tags = {
    Name        = "example-field-level_encryption_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Field-level Encryption Profile

```hcl
resource "aws_cloudfront_field_level_encryption_profile" "example" {
  # Example configuration for Field-level Encryption Profile
  name = "example-field-level_encryption_profile"

  # Common attributes
  tags = {
    Name        = "example-field-level_encryption_profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Function

```hcl
resource "aws_cloudfront_function" "example" {
  # Example configuration for Function
  name = "example-function"

  # Common attributes
  tags = {
    Name        = "example-function"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Key Group

```hcl
resource "aws_cloudfront_key_group" "example" {
  # Example configuration for Key Group
  name = "example-key_group"

  # Common attributes
  tags = {
    Name        = "example-key_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Key Value Store

```hcl
resource "aws_cloudfront_key_value_store" "example" {
  # Example configuration for Key Value Store
  name = "example-key_value_store"

  # Common attributes
  tags = {
    Name        = "example-key_value_store"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Monitoring Subscription

```hcl
resource "aws_cloudfront_monitoring_subscription" "example" {
  # Example configuration for Monitoring Subscription
  name = "example-monitoring_subscription"

  # Common attributes
  tags = {
    Name        = "example-monitoring_subscription"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Origin Access Control

```hcl
resource "aws_cloudfront_origin_access_control" "example" {
  # Example configuration for Origin Access Control
  name = "example-origin_access_control"

  # Common attributes
  tags = {
    Name        = "example-origin_access_control"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Origin Access Identity

```hcl
resource "aws_cloudfront_origin_access_identity" "example" {
  # Example configuration for Origin Access Identity
  name = "example-origin_access_identity"

  # Common attributes
  tags = {
    Name        = "example-origin_access_identity"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Origin Request Policy

```hcl
resource "aws_cloudfront_origin_request_policy" "example" {
  # Example configuration for Origin Request Policy
  name = "example-origin_request_policy"

  # Common attributes
  tags = {
    Name        = "example-origin_request_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Public Key

```hcl
resource "aws_cloudfront_public_key" "example" {
  # Example configuration for Public Key
  name = "example-public_key"

  # Common attributes
  tags = {
    Name        = "example-public_key"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Real-time Log Config

```hcl
resource "aws_cloudfront_realtime_log_config" "example" {
  # Example configuration for Real-time Log Config
  name = "example-real-time_log_config"

  # Common attributes
  tags = {
    Name        = "example-real-time_log_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Response Headers Policy

```hcl
resource "aws_cloudfront_response_headers_policy" "example" {
  # Example configuration for Response Headers Policy
  name = "example-response_headers_policy"

  # Common attributes
  tags = {
    Name        = "example-response_headers_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Origin

```hcl
resource "aws_cloudfront_vpc_origin" "example" {
  # Example configuration for VPC Origin
  name = "example-vpc_origin"

  # Common attributes
  tags = {
    Name        = "example-vpc_origin"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## cloudfrontkeyvaluestore

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Key | N/A | Framework |


### Examples


#### Key

```hcl
resource "aws_cloudfrontkeyvaluestore_key" "example" {
  # Example configuration for Key
  name = "example-key"

  # Common attributes
  tags = {
    Name        = "example-key"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## cloudhsmv2

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Cluster | aws_cloudhsm_v2_cluster | SDK |
| HSM | aws_cloudhsm_v2_hsm | SDK |


### Examples


#### Cluster

```hcl
resource "aws_cloudhsm_v2_cluster" "example" {
  # Example configuration for Cluster
  name = "example-cluster"

  # Common attributes
  tags = {
    Name        = "example-cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### HSM

```hcl
resource "aws_cloudhsm_v2_hsm" "example" {
  # Example configuration for HSM
  name = "example-hsm"

  # Common attributes
  tags = {
    Name        = "example-hsm"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## cloudsearch

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Domain | aws_cloudsearch_domain | SDK |
| Domain Service Access Policy | aws_cloudsearch_domain_service_access_policy | SDK |


### Examples


#### Domain

```hcl
resource "aws_cloudsearch_domain" "example" {
  # Example configuration for Domain
  name = "example-domain"

  # Common attributes
  tags = {
    Name        = "example-domain"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain Service Access Policy

```hcl
resource "aws_cloudsearch_domain_service_access_policy" "example" {
  # Example configuration for Domain Service Access Policy
  name = "example-domain_service_access_policy"

  # Common attributes
  tags = {
    Name        = "example-domain_service_access_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## cloudtrail

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Event Data Store | aws_cloudtrail_event_data_store | SDK |
| Organization Delegated Admin Account | N/A | Framework |
| Trail | aws_cloudtrail | SDK |


### Examples


#### Event Data Store

```hcl
resource "aws_cloudtrail_event_data_store" "example" {
  # Example configuration for Event Data Store
  name = "example-event_data_store"

  # Common attributes
  tags = {
    Name        = "example-event_data_store"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Organization Delegated Admin Account

```hcl
resource "aws_cloudtrail_organization_delegated_admin_account" "example" {
  # Example configuration for Organization Delegated Admin Account
  name = "example-organization_delegated_admin_account"

  # Common attributes
  tags = {
    Name        = "example-organization_delegated_admin_account"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Trail

```hcl
resource "aws_cloudtrail" "example" {
  # Example configuration for Trail
  name = "example-trail"

  # Common attributes
  tags = {
    Name        = "example-trail"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## cloudwatch

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Composite Alarm | aws_cloudwatch_composite_alarm | SDK |
| Dashboard | aws_cloudwatch_dashboard | SDK |
| Metric Alarm | aws_cloudwatch_metric_alarm | SDK |
| Metric Stream | aws_cloudwatch_metric_stream | SDK |


### Examples


#### Composite Alarm

```hcl
resource "aws_cloudwatch_composite_alarm" "example" {
  # Example configuration for Composite Alarm
  name = "example-composite_alarm"

  # Common attributes
  tags = {
    Name        = "example-composite_alarm"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Dashboard

```hcl
resource "aws_cloudwatch_dashboard" "example" {
  # Example configuration for Dashboard
  name = "example-dashboard"

  # Common attributes
  tags = {
    Name        = "example-dashboard"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Metric Alarm

```hcl
resource "aws_cloudwatch_metric_alarm" "example" {
  # Example configuration for Metric Alarm
  name = "example-metric_alarm"

  # Common attributes
  tags = {
    Name        = "example-metric_alarm"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Metric Stream

```hcl
resource "aws_cloudwatch_metric_stream" "example" {
  # Example configuration for Metric Stream
  name = "example-metric_stream"

  # Common attributes
  tags = {
    Name        = "example-metric_stream"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## codeartifact

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Domain | aws_codeartifact_domain | SDK |
| Domain Permissions Policy | aws_codeartifact_domain_permissions_policy | SDK |
| Repository | aws_codeartifact_repository | SDK |
| Repository Permissions Policy | aws_codeartifact_repository_permissions_policy | SDK |


### Examples


#### Domain

```hcl
resource "aws_codeartifact_domain" "example" {
  # Example configuration for Domain
  name = "example-domain"

  # Common attributes
  tags = {
    Name        = "example-domain"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain Permissions Policy

```hcl
resource "aws_codeartifact_domain_permissions_policy" "example" {
  # Example configuration for Domain Permissions Policy
  name = "example-domain_permissions_policy"

  # Common attributes
  tags = {
    Name        = "example-domain_permissions_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Repository

```hcl
resource "aws_codeartifact_repository" "example" {
  # Example configuration for Repository
  name = "example-repository"

  # Common attributes
  tags = {
    Name        = "example-repository"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Repository Permissions Policy

```hcl
resource "aws_codeartifact_repository_permissions_policy" "example" {
  # Example configuration for Repository Permissions Policy
  name = "example-repository_permissions_policy"

  # Common attributes
  tags = {
    Name        = "example-repository_permissions_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## codebuild

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Fleet | aws_codebuild_fleet | SDK |
| Project | aws_codebuild_project | SDK |
| Report Group | aws_codebuild_report_group | SDK |
| Resource Policy | aws_codebuild_resource_policy | SDK |
| Source Credential | aws_codebuild_source_credential | SDK |
| Webhook | aws_codebuild_webhook | SDK |


### Examples


#### Fleet

```hcl
resource "aws_codebuild_fleet" "example" {
  # Example configuration for Fleet
  name = "example-fleet"

  # Common attributes
  tags = {
    Name        = "example-fleet"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Project

```hcl
resource "aws_codebuild_project" "example" {
  # Example configuration for Project
  name = "example-project"

  # Common attributes
  tags = {
    Name        = "example-project"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Report Group

```hcl
resource "aws_codebuild_report_group" "example" {
  # Example configuration for Report Group
  name = "example-report_group"

  # Common attributes
  tags = {
    Name        = "example-report_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource Policy

```hcl
resource "aws_codebuild_resource_policy" "example" {
  # Example configuration for Resource Policy
  name = "example-resource_policy"

  # Common attributes
  tags = {
    Name        = "example-resource_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Source Credential

```hcl
resource "aws_codebuild_source_credential" "example" {
  # Example configuration for Source Credential
  name = "example-source_credential"

  # Common attributes
  tags = {
    Name        = "example-source_credential"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Webhook

```hcl
resource "aws_codebuild_webhook" "example" {
  # Example configuration for Webhook
  name = "example-webhook"

  # Common attributes
  tags = {
    Name        = "example-webhook"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## codecatalyst

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| DevEnvironment | aws_codecatalyst_dev_environment | SDK |
| Project | aws_codecatalyst_project | SDK |
| Source Repository | aws_codecatalyst_source_repository | SDK |


### Examples


#### DevEnvironment

```hcl
resource "aws_codecatalyst_dev_environment" "example" {
  # Example configuration for DevEnvironment
  name = "example-devenvironment"

  # Common attributes
  tags = {
    Name        = "example-devenvironment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Project

```hcl
resource "aws_codecatalyst_project" "example" {
  # Example configuration for Project
  name = "example-project"

  # Common attributes
  tags = {
    Name        = "example-project"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Source Repository

```hcl
resource "aws_codecatalyst_source_repository" "example" {
  # Example configuration for Source Repository
  name = "example-source_repository"

  # Common attributes
  tags = {
    Name        = "example-source_repository"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## codecommit

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Approval Rule Template | aws_codecommit_approval_rule_template | SDK |
| Approval Rule Template Association | aws_codecommit_approval_rule_template_association | SDK |
| Repository | aws_codecommit_repository | SDK |
| Trigger | aws_codecommit_trigger | SDK |


### Examples


#### Approval Rule Template

```hcl
resource "aws_codecommit_approval_rule_template" "example" {
  # Example configuration for Approval Rule Template
  name = "example-approval_rule_template"

  # Common attributes
  tags = {
    Name        = "example-approval_rule_template"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Approval Rule Template Association

```hcl
resource "aws_codecommit_approval_rule_template_association" "example" {
  # Example configuration for Approval Rule Template Association
  name = "example-approval_rule_template_association"

  # Common attributes
  tags = {
    Name        = "example-approval_rule_template_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Repository

```hcl
resource "aws_codecommit_repository" "example" {
  # Example configuration for Repository
  name = "example-repository"

  # Common attributes
  tags = {
    Name        = "example-repository"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Trigger

```hcl
resource "aws_codecommit_trigger" "example" {
  # Example configuration for Trigger
  name = "example-trigger"

  # Common attributes
  tags = {
    Name        = "example-trigger"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## codeconnections

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Connection | N/A | Framework |
| Host | N/A | Framework |


### Examples


#### Connection

```hcl
resource "aws_codeconnections_connection" "example" {
  # Example configuration for Connection
  name = "example-connection"

  # Common attributes
  tags = {
    Name        = "example-connection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Host

```hcl
resource "aws_codeconnections_host" "example" {
  # Example configuration for Host
  name = "example-host"

  # Common attributes
  tags = {
    Name        = "example-host"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## codeguruprofiler

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Profiling Group | N/A | Framework |


### Examples


#### Profiling Group

```hcl
resource "aws_codeguruprofiler_profiling_group" "example" {
  # Example configuration for Profiling Group
  name = "example-profiling_group"

  # Common attributes
  tags = {
    Name        = "example-profiling_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## codegurureviewer

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Repository Association | aws_codegurureviewer_repository_association | SDK |


### Examples


#### Repository Association

```hcl
resource "aws_codegurureviewer_repository_association" "example" {
  # Example configuration for Repository Association
  name = "example-repository_association"

  # Common attributes
  tags = {
    Name        = "example-repository_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## codepipeline

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Custom Action Type | aws_codepipeline_custom_action_type | SDK |
| Pipeline | aws_codepipeline | SDK |
| Webhook | aws_codepipeline_webhook | SDK |


### Examples


#### Custom Action Type

```hcl
resource "aws_codepipeline_custom_action_type" "example" {
  # Example configuration for Custom Action Type
  name = "example-custom_action_type"

  # Common attributes
  tags = {
    Name        = "example-custom_action_type"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Pipeline

```hcl
resource "aws_codepipeline" "example" {
  # Example configuration for Pipeline
  name = "example-pipeline"

  # Common attributes
  tags = {
    Name        = "example-pipeline"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Webhook

```hcl
resource "aws_codepipeline_webhook" "example" {
  # Example configuration for Webhook
  name = "example-webhook"

  # Common attributes
  tags = {
    Name        = "example-webhook"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## codestarconnections

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Connection | aws_codestarconnections_connection | SDK |
| Host | aws_codestarconnections_host | SDK |


### Examples


#### Connection

```hcl
resource "aws_codestarconnections_connection" "example" {
  # Example configuration for Connection
  name = "example-connection"

  # Common attributes
  tags = {
    Name        = "example-connection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Host

```hcl
resource "aws_codestarconnections_host" "example" {
  # Example configuration for Host
  name = "example-host"

  # Common attributes
  tags = {
    Name        = "example-host"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## codestarnotifications

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Notification Rule | aws_codestarnotifications_notification_rule | SDK |


### Examples


#### Notification Rule

```hcl
resource "aws_codestarnotifications_notification_rule" "example" {
  # Example configuration for Notification Rule
  name = "example-notification_rule"

  # Common attributes
  tags = {
    Name        = "example-notification_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## cognitoidentity

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Pool | aws_cognito_identity_pool | SDK |
| Pool Roles Association | aws_cognito_identity_pool_roles_attachment | SDK |
| Provider Principal Tags | aws_cognito_identity_pool_provider_principal_tag | SDK |


### Examples


#### Pool

```hcl
resource "aws_cognito_identity_pool" "example" {
  # Example configuration for Pool
  name = "example-pool"

  # Common attributes
  tags = {
    Name        = "example-pool"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Pool Roles Association

```hcl
resource "aws_cognito_identity_pool_roles_attachment" "example" {
  # Example configuration for Pool Roles Association
  name = "example-pool_roles_association"

  # Common attributes
  tags = {
    Name        = "example-pool_roles_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Provider Principal Tags

```hcl
resource "aws_cognito_identity_pool_provider_principal_tag" "example" {
  # Example configuration for Provider Principal Tags
  name = "example-provider_principal_tags"

  # Common attributes
  tags = {
    Name        = "example-provider_principal_tags"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## cognitoidp

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Group User | aws_cognito_user_in_group | SDK |
| Identity Provider | aws_cognito_identity_provider | SDK |
| Managed User Pool Client | N/A | Framework |
| Resource Server | aws_cognito_resource_server | SDK |
| Risk Configuration | aws_cognito_risk_configuration | SDK |
| User | aws_cognito_user | SDK |
| User Group | aws_cognito_user_group | SDK |
| User Pool | aws_cognito_user_pool | SDK |
| User Pool Client | N/A | Framework |
| User Pool Domain | aws_cognito_user_pool_domain | SDK |
| User Pool UI Customization | aws_cognito_user_pool_ui_customization | SDK |


### Examples


#### Group User

```hcl
resource "aws_cognito_user_in_group" "example" {
  # Example configuration for Group User
  name = "example-group_user"

  # Common attributes
  tags = {
    Name        = "example-group_user"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Identity Provider

```hcl
resource "aws_cognito_identity_provider" "example" {
  # Example configuration for Identity Provider
  name = "example-identity_provider"

  # Common attributes
  tags = {
    Name        = "example-identity_provider"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Managed User Pool Client

```hcl
resource "aws_cognitoidp_managed_user_pool_client" "example" {
  # Example configuration for Managed User Pool Client
  name = "example-managed_user_pool_client"

  # Common attributes
  tags = {
    Name        = "example-managed_user_pool_client"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource Server

```hcl
resource "aws_cognito_resource_server" "example" {
  # Example configuration for Resource Server
  name = "example-resource_server"

  # Common attributes
  tags = {
    Name        = "example-resource_server"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Risk Configuration

```hcl
resource "aws_cognito_risk_configuration" "example" {
  # Example configuration for Risk Configuration
  name = "example-risk_configuration"

  # Common attributes
  tags = {
    Name        = "example-risk_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User

```hcl
resource "aws_cognito_user" "example" {
  # Example configuration for User
  name = "example-user"

  # Common attributes
  tags = {
    Name        = "example-user"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User Group

```hcl
resource "aws_cognito_user_group" "example" {
  # Example configuration for User Group
  name = "example-user_group"

  # Common attributes
  tags = {
    Name        = "example-user_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User Pool

```hcl
resource "aws_cognito_user_pool" "example" {
  # Example configuration for User Pool
  name = "example-user_pool"

  # Common attributes
  tags = {
    Name        = "example-user_pool"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User Pool Client

```hcl
resource "aws_cognitoidp_user_pool_client" "example" {
  # Example configuration for User Pool Client
  name = "example-user_pool_client"

  # Common attributes
  tags = {
    Name        = "example-user_pool_client"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User Pool Domain

```hcl
resource "aws_cognito_user_pool_domain" "example" {
  # Example configuration for User Pool Domain
  name = "example-user_pool_domain"

  # Common attributes
  tags = {
    Name        = "example-user_pool_domain"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User Pool UI Customization

```hcl
resource "aws_cognito_user_pool_ui_customization" "example" {
  # Example configuration for User Pool UI Customization
  name = "example-user_pool_ui_customization"

  # Common attributes
  tags = {
    Name        = "example-user_pool_ui_customization"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## comprehend

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Document Classifier | aws_comprehend_document_classifier | SDK |
| Entity Recognizer | aws_comprehend_entity_recognizer | SDK |


### Examples


#### Document Classifier

```hcl
resource "aws_comprehend_document_classifier" "example" {
  # Example configuration for Document Classifier
  name = "example-document_classifier"

  # Common attributes
  tags = {
    Name        = "example-document_classifier"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Entity Recognizer

```hcl
resource "aws_comprehend_entity_recognizer" "example" {
  # Example configuration for Entity Recognizer
  name = "example-entity_recognizer"

  # Common attributes
  tags = {
    Name        = "example-entity_recognizer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## computeoptimizer

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Enrollment Status | N/A | Framework |
| Recommendation Preferences | N/A | Framework |


### Examples


#### Enrollment Status

```hcl
resource "aws_computeoptimizer_enrollment_status" "example" {
  # Example configuration for Enrollment Status
  name = "example-enrollment_status"

  # Common attributes
  tags = {
    Name        = "example-enrollment_status"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Recommendation Preferences

```hcl
resource "aws_computeoptimizer_recommendation_preferences" "example" {
  # Example configuration for Recommendation Preferences
  name = "example-recommendation_preferences"

  # Common attributes
  tags = {
    Name        = "example-recommendation_preferences"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## configservice

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Aggregate Authorization | aws_config_aggregate_authorization | SDK |
| Config Rule | aws_config_config_rule | SDK |
| Configuration Aggregator | aws_config_configuration_aggregator | SDK |
| Configuration Recorder | aws_config_configuration_recorder | SDK |
| Configuration Recorder Status | aws_config_configuration_recorder_status | SDK |
| Conformance Pack | aws_config_conformance_pack | SDK |
| Delivery Channel | aws_config_delivery_channel | SDK |
| Organization Conformance Pack | aws_config_organization_conformance_pack | SDK |
| Organization Custom Policy Rule | aws_config_organization_custom_policy_rule | SDK |
| Organization Custom Rule | aws_config_organization_custom_rule | SDK |
| Organization Managed Rule | aws_config_organization_managed_rule | SDK |
| Remediation Configuration | aws_config_remediation_configuration | SDK |
| Retention Configuration | N/A | Framework |


### Examples


#### Aggregate Authorization

```hcl
resource "aws_config_aggregate_authorization" "example" {
  # Example configuration for Aggregate Authorization
  name = "example-aggregate_authorization"

  # Common attributes
  tags = {
    Name        = "example-aggregate_authorization"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Config Rule

```hcl
resource "aws_config_config_rule" "example" {
  # Example configuration for Config Rule
  name = "example-config_rule"

  # Common attributes
  tags = {
    Name        = "example-config_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Configuration Aggregator

```hcl
resource "aws_config_configuration_aggregator" "example" {
  # Example configuration for Configuration Aggregator
  name = "example-configuration_aggregator"

  # Common attributes
  tags = {
    Name        = "example-configuration_aggregator"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Configuration Recorder

```hcl
resource "aws_config_configuration_recorder" "example" {
  # Example configuration for Configuration Recorder
  name = "example-configuration_recorder"

  # Common attributes
  tags = {
    Name        = "example-configuration_recorder"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Configuration Recorder Status

```hcl
resource "aws_config_configuration_recorder_status" "example" {
  # Example configuration for Configuration Recorder Status
  name = "example-configuration_recorder_status"

  # Common attributes
  tags = {
    Name        = "example-configuration_recorder_status"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Conformance Pack

```hcl
resource "aws_config_conformance_pack" "example" {
  # Example configuration for Conformance Pack
  name = "example-conformance_pack"

  # Common attributes
  tags = {
    Name        = "example-conformance_pack"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Delivery Channel

```hcl
resource "aws_config_delivery_channel" "example" {
  # Example configuration for Delivery Channel
  name = "example-delivery_channel"

  # Common attributes
  tags = {
    Name        = "example-delivery_channel"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Organization Conformance Pack

```hcl
resource "aws_config_organization_conformance_pack" "example" {
  # Example configuration for Organization Conformance Pack
  name = "example-organization_conformance_pack"

  # Common attributes
  tags = {
    Name        = "example-organization_conformance_pack"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Organization Custom Policy Rule

```hcl
resource "aws_config_organization_custom_policy_rule" "example" {
  # Example configuration for Organization Custom Policy Rule
  name = "example-organization_custom_policy_rule"

  # Common attributes
  tags = {
    Name        = "example-organization_custom_policy_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Organization Custom Rule

```hcl
resource "aws_config_organization_custom_rule" "example" {
  # Example configuration for Organization Custom Rule
  name = "example-organization_custom_rule"

  # Common attributes
  tags = {
    Name        = "example-organization_custom_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Organization Managed Rule

```hcl
resource "aws_config_organization_managed_rule" "example" {
  # Example configuration for Organization Managed Rule
  name = "example-organization_managed_rule"

  # Common attributes
  tags = {
    Name        = "example-organization_managed_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Remediation Configuration

```hcl
resource "aws_config_remediation_configuration" "example" {
  # Example configuration for Remediation Configuration
  name = "example-remediation_configuration"

  # Common attributes
  tags = {
    Name        = "example-remediation_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Retention Configuration

```hcl
resource "aws_configservice_retention_configuration" "example" {
  # Example configuration for Retention Configuration
  name = "example-retention_configuration"

  # Common attributes
  tags = {
    Name        = "example-retention_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## connect

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Bot Association | aws_connect_bot_association | SDK |
| Contact Flow | aws_connect_contact_flow | SDK |
| Contact Flow Module | aws_connect_contact_flow_module | SDK |
| Hours Of Operation | aws_connect_hours_of_operation | SDK |
| Instance | aws_connect_instance | SDK |
| Instance Storage Config | aws_connect_instance_storage_config | SDK |
| Lambda Function Association | aws_connect_lambda_function_association | SDK |
| Phone Number | aws_connect_phone_number | SDK |
| Queue | aws_connect_queue | SDK |
| Quick Connect | aws_connect_quick_connect | SDK |
| Routing Profile | aws_connect_routing_profile | SDK |
| Security Profile | aws_connect_security_profile | SDK |
| User | aws_connect_user | SDK |
| User Hierarchy Group | aws_connect_user_hierarchy_group | SDK |
| User Hierarchy Structure | aws_connect_user_hierarchy_structure | SDK |
| Vocabulary | aws_connect_vocabulary | SDK |


### Examples


#### Bot Association

```hcl
resource "aws_connect_bot_association" "example" {
  # Example configuration for Bot Association
  name = "example-bot_association"

  # Common attributes
  tags = {
    Name        = "example-bot_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Contact Flow

```hcl
resource "aws_connect_contact_flow" "example" {
  # Example configuration for Contact Flow
  name = "example-contact_flow"

  # Common attributes
  tags = {
    Name        = "example-contact_flow"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Contact Flow Module

```hcl
resource "aws_connect_contact_flow_module" "example" {
  # Example configuration for Contact Flow Module
  name = "example-contact_flow_module"

  # Common attributes
  tags = {
    Name        = "example-contact_flow_module"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Hours Of Operation

```hcl
resource "aws_connect_hours_of_operation" "example" {
  # Example configuration for Hours Of Operation
  name = "example-hours_of_operation"

  # Common attributes
  tags = {
    Name        = "example-hours_of_operation"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Instance

```hcl
resource "aws_connect_instance" "example" {
  # Example configuration for Instance
  name = "example-instance"

  # Common attributes
  tags = {
    Name        = "example-instance"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Instance Storage Config

```hcl
resource "aws_connect_instance_storage_config" "example" {
  # Example configuration for Instance Storage Config
  name = "example-instance_storage_config"

  # Common attributes
  tags = {
    Name        = "example-instance_storage_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Lambda Function Association

```hcl
resource "aws_connect_lambda_function_association" "example" {
  # Example configuration for Lambda Function Association
  name = "example-lambda_function_association"

  # Common attributes
  tags = {
    Name        = "example-lambda_function_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Phone Number

```hcl
resource "aws_connect_phone_number" "example" {
  # Example configuration for Phone Number
  name = "example-phone_number"

  # Common attributes
  tags = {
    Name        = "example-phone_number"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Queue

```hcl
resource "aws_connect_queue" "example" {
  # Example configuration for Queue
  name = "example-queue"

  # Common attributes
  tags = {
    Name        = "example-queue"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Quick Connect

```hcl
resource "aws_connect_quick_connect" "example" {
  # Example configuration for Quick Connect
  name = "example-quick_connect"

  # Common attributes
  tags = {
    Name        = "example-quick_connect"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Routing Profile

```hcl
resource "aws_connect_routing_profile" "example" {
  # Example configuration for Routing Profile
  name = "example-routing_profile"

  # Common attributes
  tags = {
    Name        = "example-routing_profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Security Profile

```hcl
resource "aws_connect_security_profile" "example" {
  # Example configuration for Security Profile
  name = "example-security_profile"

  # Common attributes
  tags = {
    Name        = "example-security_profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User

```hcl
resource "aws_connect_user" "example" {
  # Example configuration for User
  name = "example-user"

  # Common attributes
  tags = {
    Name        = "example-user"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User Hierarchy Group

```hcl
resource "aws_connect_user_hierarchy_group" "example" {
  # Example configuration for User Hierarchy Group
  name = "example-user_hierarchy_group"

  # Common attributes
  tags = {
    Name        = "example-user_hierarchy_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User Hierarchy Structure

```hcl
resource "aws_connect_user_hierarchy_structure" "example" {
  # Example configuration for User Hierarchy Structure
  name = "example-user_hierarchy_structure"

  # Common attributes
  tags = {
    Name        = "example-user_hierarchy_structure"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Vocabulary

```hcl
resource "aws_connect_vocabulary" "example" {
  # Example configuration for Vocabulary
  name = "example-vocabulary"

  # Common attributes
  tags = {
    Name        = "example-vocabulary"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## controltower

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Control | aws_controltower_control | SDK |
| Landing Zone | aws_controltower_landing_zone | SDK |


### Examples


#### Control

```hcl
resource "aws_controltower_control" "example" {
  # Example configuration for Control
  name = "example-control"

  # Common attributes
  tags = {
    Name        = "example-control"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Landing Zone

```hcl
resource "aws_controltower_landing_zone" "example" {
  # Example configuration for Landing Zone
  name = "example-landing_zone"

  # Common attributes
  tags = {
    Name        = "example-landing_zone"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## costoptimizationhub

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Enrollment Status | N/A | Framework |
| Preferences | N/A | Framework |


### Examples


#### Enrollment Status

```hcl
resource "aws_costoptimizationhub_enrollment_status" "example" {
  # Example configuration for Enrollment Status
  name = "example-enrollment_status"

  # Common attributes
  tags = {
    Name        = "example-enrollment_status"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Preferences

```hcl
resource "aws_costoptimizationhub_preferences" "example" {
  # Example configuration for Preferences
  name = "example-preferences"

  # Common attributes
  tags = {
    Name        = "example-preferences"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## cur

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Report Definition | aws_cur_report_definition | SDK |


### Examples


#### Report Definition

```hcl
resource "aws_cur_report_definition" "example" {
  # Example configuration for Report Definition
  name = "example-report_definition"

  # Common attributes
  tags = {
    Name        = "example-report_definition"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## dataexchange

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Data Set | aws_dataexchange_data_set | SDK |
| Revision | aws_dataexchange_revision | SDK |


### Examples


#### Data Set

```hcl
resource "aws_dataexchange_data_set" "example" {
  # Example configuration for Data Set
  name = "example-data_set"

  # Common attributes
  tags = {
    Name        = "example-data_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Revision

```hcl
resource "aws_dataexchange_revision" "example" {
  # Example configuration for Revision
  name = "example-revision"

  # Common attributes
  tags = {
    Name        = "example-revision"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## datapipeline

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Pipeline | aws_datapipeline_pipeline | SDK |


### Examples


#### Pipeline

```hcl
resource "aws_datapipeline_pipeline" "example" {
  # Example configuration for Pipeline
  name = "example-pipeline"

  # Common attributes
  tags = {
    Name        = "example-pipeline"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## datasync

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Agent | aws_datasync_agent | SDK |
| Location EFS | aws_datasync_location_efs | SDK |
| Location FSx for Lustre File System | aws_datasync_location_fsx_lustre_file_system | SDK |
| Location FSx for NetApp ONTAP File System | aws_datasync_location_fsx_ontap_file_system | SDK |
| Location FSx for OpenZFS File System | aws_datasync_location_fsx_openzfs_file_system | SDK |
| Location FSx for Windows File Server File System | aws_datasync_location_fsx_windows_file_system | SDK |
| Location HDFS | aws_datasync_location_hdfs | SDK |
| Location Microsoft Azure Blob Storage | aws_datasync_location_azure_blob | SDK |
| Location NFS | aws_datasync_location_nfs | SDK |
| Location Object Storage | aws_datasync_location_object_storage | SDK |
| Location S3 | aws_datasync_location_s3 | SDK |
| Location SMB | aws_datasync_location_smb | SDK |
| Task | aws_datasync_task | SDK |


### Examples


#### Agent

```hcl
resource "aws_datasync_agent" "example" {
  # Example configuration for Agent
  name = "example-agent"

  # Common attributes
  tags = {
    Name        = "example-agent"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Location EFS

```hcl
resource "aws_datasync_location_efs" "example" {
  # Example configuration for Location EFS
  name = "example-location_efs"

  # Common attributes
  tags = {
    Name        = "example-location_efs"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Location FSx for Lustre File System

```hcl
resource "aws_datasync_location_fsx_lustre_file_system" "example" {
  # Example configuration for Location FSx for Lustre File System
  name = "example-location_fsx_for_lustre_file_system"

  # Common attributes
  tags = {
    Name        = "example-location_fsx_for_lustre_file_system"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Location FSx for NetApp ONTAP File System

```hcl
resource "aws_datasync_location_fsx_ontap_file_system" "example" {
  # Example configuration for Location FSx for NetApp ONTAP File System
  name = "example-location_fsx_for_netapp_ontap_file_system"

  # Common attributes
  tags = {
    Name        = "example-location_fsx_for_netapp_ontap_file_system"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Location FSx for OpenZFS File System

```hcl
resource "aws_datasync_location_fsx_openzfs_file_system" "example" {
  # Example configuration for Location FSx for OpenZFS File System
  name = "example-location_fsx_for_openzfs_file_system"

  # Common attributes
  tags = {
    Name        = "example-location_fsx_for_openzfs_file_system"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Location FSx for Windows File Server File System

```hcl
resource "aws_datasync_location_fsx_windows_file_system" "example" {
  # Example configuration for Location FSx for Windows File Server File System
  name = "example-location_fsx_for_windows_file_server_file_system"

  # Common attributes
  tags = {
    Name        = "example-location_fsx_for_windows_file_server_file_system"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Location HDFS

```hcl
resource "aws_datasync_location_hdfs" "example" {
  # Example configuration for Location HDFS
  name = "example-location_hdfs"

  # Common attributes
  tags = {
    Name        = "example-location_hdfs"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Location Microsoft Azure Blob Storage

```hcl
resource "aws_datasync_location_azure_blob" "example" {
  # Example configuration for Location Microsoft Azure Blob Storage
  name = "example-location_microsoft_azure_blob_storage"

  # Common attributes
  tags = {
    Name        = "example-location_microsoft_azure_blob_storage"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Location NFS

```hcl
resource "aws_datasync_location_nfs" "example" {
  # Example configuration for Location NFS
  name = "example-location_nfs"

  # Common attributes
  tags = {
    Name        = "example-location_nfs"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Location Object Storage

```hcl
resource "aws_datasync_location_object_storage" "example" {
  # Example configuration for Location Object Storage
  name = "example-location_object_storage"

  # Common attributes
  tags = {
    Name        = "example-location_object_storage"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Location S3

```hcl
resource "aws_datasync_location_s3" "example" {
  # Example configuration for Location S3
  name = "example-location_s3"

  # Common attributes
  tags = {
    Name        = "example-location_s3"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Location SMB

```hcl
resource "aws_datasync_location_smb" "example" {
  # Example configuration for Location SMB
  name = "example-location_smb"

  # Common attributes
  tags = {
    Name        = "example-location_smb"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Task

```hcl
resource "aws_datasync_task" "example" {
  # Example configuration for Task
  name = "example-task"

  # Common attributes
  tags = {
    Name        = "example-task"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## datazone

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Asset Type | N/A | Framework |
| Domain | N/A | Framework |
| Environment | N/A | Framework |
| Environment Blueprint Configuration | N/A | Framework |
| Environment Profile | N/A | Framework |
| Form Type | N/A | Framework |
| Glossary | N/A | Framework |
| Glossary Term | N/A | Framework |
| Project | N/A | Framework |
| User Profile | N/A | Framework |


### Examples


#### Asset Type

```hcl
resource "aws_datazone_asset_type" "example" {
  # Example configuration for Asset Type
  name = "example-asset_type"

  # Common attributes
  tags = {
    Name        = "example-asset_type"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain

```hcl
resource "aws_datazone_domain" "example" {
  # Example configuration for Domain
  name = "example-domain"

  # Common attributes
  tags = {
    Name        = "example-domain"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Environment

```hcl
resource "aws_datazone_environment" "example" {
  # Example configuration for Environment
  name = "example-environment"

  # Common attributes
  tags = {
    Name        = "example-environment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Environment Blueprint Configuration

```hcl
resource "aws_datazone_environment_blueprint_configuration" "example" {
  # Example configuration for Environment Blueprint Configuration
  name = "example-environment_blueprint_configuration"

  # Common attributes
  tags = {
    Name        = "example-environment_blueprint_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Environment Profile

```hcl
resource "aws_datazone_environment_profile" "example" {
  # Example configuration for Environment Profile
  name = "example-environment_profile"

  # Common attributes
  tags = {
    Name        = "example-environment_profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Form Type

```hcl
resource "aws_datazone_form_type" "example" {
  # Example configuration for Form Type
  name = "example-form_type"

  # Common attributes
  tags = {
    Name        = "example-form_type"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Glossary

```hcl
resource "aws_datazone_glossary" "example" {
  # Example configuration for Glossary
  name = "example-glossary"

  # Common attributes
  tags = {
    Name        = "example-glossary"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Glossary Term

```hcl
resource "aws_datazone_glossary_term" "example" {
  # Example configuration for Glossary Term
  name = "example-glossary_term"

  # Common attributes
  tags = {
    Name        = "example-glossary_term"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Project

```hcl
resource "aws_datazone_project" "example" {
  # Example configuration for Project
  name = "example-project"

  # Common attributes
  tags = {
    Name        = "example-project"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User Profile

```hcl
resource "aws_datazone_user_profile" "example" {
  # Example configuration for User Profile
  name = "example-user_profile"

  # Common attributes
  tags = {
    Name        = "example-user_profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## dax

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Cluster | aws_dax_cluster | SDK |


### Examples


#### Cluster

```hcl
resource "aws_dax_cluster" "example" {
  # Example configuration for Cluster
  name = "example-cluster"

  # Common attributes
  tags = {
    Name        = "example-cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## deploy

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| App | aws_codedeploy_app | SDK |
| Deployment Config | aws_codedeploy_deployment_config | SDK |
| Deployment Group | aws_codedeploy_deployment_group | SDK |


### Examples


#### App

```hcl
resource "aws_codedeploy_app" "example" {
  # Example configuration for App
  name = "example-app"

  # Common attributes
  tags = {
    Name        = "example-app"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Deployment Config

```hcl
resource "aws_codedeploy_deployment_config" "example" {
  # Example configuration for Deployment Config
  name = "example-deployment_config"

  # Common attributes
  tags = {
    Name        = "example-deployment_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Deployment Group

```hcl
resource "aws_codedeploy_deployment_group" "example" {
  # Example configuration for Deployment Group
  name = "example-deployment_group"

  # Common attributes
  tags = {
    Name        = "example-deployment_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## detective

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Graph | aws_detective_graph | SDK |


### Examples


#### Graph

```hcl
resource "aws_detective_graph" "example" {
  # Example configuration for Graph
  name = "example-graph"

  # Common attributes
  tags = {
    Name        = "example-graph"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## devicefarm

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Device Pool | aws_devicefarm_device_pool | SDK |
| Instance Profile | aws_devicefarm_instance_profile | SDK |
| Network Profile | aws_devicefarm_network_profile | SDK |
| Project | aws_devicefarm_project | SDK |
| Test Grid Project | aws_devicefarm_test_grid_project | SDK |
| Upload | aws_devicefarm_upload | SDK |


### Examples


#### Device Pool

```hcl
resource "aws_devicefarm_device_pool" "example" {
  # Example configuration for Device Pool
  name = "example-device_pool"

  # Common attributes
  tags = {
    Name        = "example-device_pool"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Instance Profile

```hcl
resource "aws_devicefarm_instance_profile" "example" {
  # Example configuration for Instance Profile
  name = "example-instance_profile"

  # Common attributes
  tags = {
    Name        = "example-instance_profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Network Profile

```hcl
resource "aws_devicefarm_network_profile" "example" {
  # Example configuration for Network Profile
  name = "example-network_profile"

  # Common attributes
  tags = {
    Name        = "example-network_profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Project

```hcl
resource "aws_devicefarm_project" "example" {
  # Example configuration for Project
  name = "example-project"

  # Common attributes
  tags = {
    Name        = "example-project"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Test Grid Project

```hcl
resource "aws_devicefarm_test_grid_project" "example" {
  # Example configuration for Test Grid Project
  name = "example-test_grid_project"

  # Common attributes
  tags = {
    Name        = "example-test_grid_project"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Upload

```hcl
resource "aws_devicefarm_upload" "example" {
  # Example configuration for Upload
  name = "example-upload"

  # Common attributes
  tags = {
    Name        = "example-upload"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## devopsguru

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Event Sources Config | N/A | Framework |
| Notification Channel | N/A | Framework |
| Resource Collection | N/A | Framework |
| Service Integration | N/A | Framework |


### Examples


#### Event Sources Config

```hcl
resource "aws_devopsguru_event_sources_config" "example" {
  # Example configuration for Event Sources Config
  name = "example-event_sources_config"

  # Common attributes
  tags = {
    Name        = "example-event_sources_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Notification Channel

```hcl
resource "aws_devopsguru_notification_channel" "example" {
  # Example configuration for Notification Channel
  name = "example-notification_channel"

  # Common attributes
  tags = {
    Name        = "example-notification_channel"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource Collection

```hcl
resource "aws_devopsguru_resource_collection" "example" {
  # Example configuration for Resource Collection
  name = "example-resource_collection"

  # Common attributes
  tags = {
    Name        = "example-resource_collection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Service Integration

```hcl
resource "aws_devopsguru_service_integration" "example" {
  # Example configuration for Service Integration
  name = "example-service_integration"

  # Common attributes
  tags = {
    Name        = "example-service_integration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## directconnect

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| BGP Peer | aws_dx_bgp_peer | SDK |
| Connection | aws_dx_connection | SDK |
| Connection Confirmation | aws_dx_connection_confirmation | SDK |
| Connection LAG Association | aws_dx_connection_association | SDK |
| Gateway | aws_dx_gateway | SDK |
| Gateway Association | aws_dx_gateway_association | SDK |
| Gateway Association Proposal | aws_dx_gateway_association_proposal | SDK |
| Hosted Connection | aws_dx_hosted_connection | SDK |
| Hosted Private Virtual Interface | aws_dx_hosted_private_virtual_interface | SDK |
| Hosted Private Virtual Interface Accepter | aws_dx_hosted_private_virtual_interface_accepter | SDK |
| Hosted Public Virtual Interface | aws_dx_hosted_public_virtual_interface | SDK |
| Hosted Public Virtual Interface Accepter | aws_dx_hosted_public_virtual_interface_accepter | SDK |
| Hosted Transit Virtual Interface | aws_dx_hosted_transit_virtual_interface | SDK |
| Hosted Transit Virtual Interface Accepter | aws_dx_hosted_transit_virtual_interface_accepter | SDK |
| LAG | aws_dx_lag | SDK |
| MACSec Key Association | aws_dx_macsec_key_association | SDK |
| Private Virtual Interface | aws_dx_private_virtual_interface | SDK |
| Public Virtual Interface | aws_dx_public_virtual_interface | SDK |
| Transit Virtual Interface | aws_dx_transit_virtual_interface | SDK |


### Examples


#### BGP Peer

```hcl
resource "aws_dx_bgp_peer" "example" {
  # Example configuration for BGP Peer
  name = "example-bgp_peer"

  # Common attributes
  tags = {
    Name        = "example-bgp_peer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Connection

```hcl
resource "aws_dx_connection" "example" {
  # Example configuration for Connection
  name = "example-connection"

  # Common attributes
  tags = {
    Name        = "example-connection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Connection Confirmation

```hcl
resource "aws_dx_connection_confirmation" "example" {
  # Example configuration for Connection Confirmation
  name = "example-connection_confirmation"

  # Common attributes
  tags = {
    Name        = "example-connection_confirmation"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Connection LAG Association

```hcl
resource "aws_dx_connection_association" "example" {
  # Example configuration for Connection LAG Association
  name = "example-connection_lag_association"

  # Common attributes
  tags = {
    Name        = "example-connection_lag_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Gateway

```hcl
resource "aws_dx_gateway" "example" {
  # Example configuration for Gateway
  name = "example-gateway"

  # Common attributes
  tags = {
    Name        = "example-gateway"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Gateway Association

```hcl
resource "aws_dx_gateway_association" "example" {
  # Example configuration for Gateway Association
  name = "example-gateway_association"

  # Common attributes
  tags = {
    Name        = "example-gateway_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Gateway Association Proposal

```hcl
resource "aws_dx_gateway_association_proposal" "example" {
  # Example configuration for Gateway Association Proposal
  name = "example-gateway_association_proposal"

  # Common attributes
  tags = {
    Name        = "example-gateway_association_proposal"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Hosted Connection

```hcl
resource "aws_dx_hosted_connection" "example" {
  # Example configuration for Hosted Connection
  name = "example-hosted_connection"

  # Common attributes
  tags = {
    Name        = "example-hosted_connection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Hosted Private Virtual Interface

```hcl
resource "aws_dx_hosted_private_virtual_interface" "example" {
  # Example configuration for Hosted Private Virtual Interface
  name = "example-hosted_private_virtual_interface"

  # Common attributes
  tags = {
    Name        = "example-hosted_private_virtual_interface"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Hosted Private Virtual Interface Accepter

```hcl
resource "aws_dx_hosted_private_virtual_interface_accepter" "example" {
  # Example configuration for Hosted Private Virtual Interface Accepter
  name = "example-hosted_private_virtual_interface_accepter"

  # Common attributes
  tags = {
    Name        = "example-hosted_private_virtual_interface_accepter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Hosted Public Virtual Interface

```hcl
resource "aws_dx_hosted_public_virtual_interface" "example" {
  # Example configuration for Hosted Public Virtual Interface
  name = "example-hosted_public_virtual_interface"

  # Common attributes
  tags = {
    Name        = "example-hosted_public_virtual_interface"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Hosted Public Virtual Interface Accepter

```hcl
resource "aws_dx_hosted_public_virtual_interface_accepter" "example" {
  # Example configuration for Hosted Public Virtual Interface Accepter
  name = "example-hosted_public_virtual_interface_accepter"

  # Common attributes
  tags = {
    Name        = "example-hosted_public_virtual_interface_accepter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Hosted Transit Virtual Interface

```hcl
resource "aws_dx_hosted_transit_virtual_interface" "example" {
  # Example configuration for Hosted Transit Virtual Interface
  name = "example-hosted_transit_virtual_interface"

  # Common attributes
  tags = {
    Name        = "example-hosted_transit_virtual_interface"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Hosted Transit Virtual Interface Accepter

```hcl
resource "aws_dx_hosted_transit_virtual_interface_accepter" "example" {
  # Example configuration for Hosted Transit Virtual Interface Accepter
  name = "example-hosted_transit_virtual_interface_accepter"

  # Common attributes
  tags = {
    Name        = "example-hosted_transit_virtual_interface_accepter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### LAG

```hcl
resource "aws_dx_lag" "example" {
  # Example configuration for LAG
  name = "example-lag"

  # Common attributes
  tags = {
    Name        = "example-lag"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### MACSec Key Association

```hcl
resource "aws_dx_macsec_key_association" "example" {
  # Example configuration for MACSec Key Association
  name = "example-macsec_key_association"

  # Common attributes
  tags = {
    Name        = "example-macsec_key_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Private Virtual Interface

```hcl
resource "aws_dx_private_virtual_interface" "example" {
  # Example configuration for Private Virtual Interface
  name = "example-private_virtual_interface"

  # Common attributes
  tags = {
    Name        = "example-private_virtual_interface"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Public Virtual Interface

```hcl
resource "aws_dx_public_virtual_interface" "example" {
  # Example configuration for Public Virtual Interface
  name = "example-public_virtual_interface"

  # Common attributes
  tags = {
    Name        = "example-public_virtual_interface"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Virtual Interface

```hcl
resource "aws_dx_transit_virtual_interface" "example" {
  # Example configuration for Transit Virtual Interface
  name = "example-transit_virtual_interface"

  # Common attributes
  tags = {
    Name        = "example-transit_virtual_interface"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## dlm

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Lifecycle Policy | aws_dlm_lifecycle_policy | SDK |


### Examples


#### Lifecycle Policy

```hcl
resource "aws_dlm_lifecycle_policy" "example" {
  # Example configuration for Lifecycle Policy
  name = "example-lifecycle_policy"

  # Common attributes
  tags = {
    Name        = "example-lifecycle_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## dms

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Certificate | aws_dms_certificate | SDK |
| Endpoint | aws_dms_endpoint | SDK |
| Event Subscription | aws_dms_event_subscription | SDK |
| Replication Config | aws_dms_replication_config | SDK |
| Replication Instance | aws_dms_replication_instance | SDK |
| Replication Subnet Group | aws_dms_replication_subnet_group | SDK |
| Replication Task | aws_dms_replication_task | SDK |
| S3 Endpoint | aws_dms_s3_endpoint | SDK |


### Examples


#### Certificate

```hcl
resource "aws_dms_certificate" "example" {
  # Example configuration for Certificate
  name = "example-certificate"

  # Common attributes
  tags = {
    Name        = "example-certificate"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Endpoint

```hcl
resource "aws_dms_endpoint" "example" {
  # Example configuration for Endpoint
  name = "example-endpoint"

  # Common attributes
  tags = {
    Name        = "example-endpoint"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Event Subscription

```hcl
resource "aws_dms_event_subscription" "example" {
  # Example configuration for Event Subscription
  name = "example-event_subscription"

  # Common attributes
  tags = {
    Name        = "example-event_subscription"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Replication Config

```hcl
resource "aws_dms_replication_config" "example" {
  # Example configuration for Replication Config
  name = "example-replication_config"

  # Common attributes
  tags = {
    Name        = "example-replication_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Replication Instance

```hcl
resource "aws_dms_replication_instance" "example" {
  # Example configuration for Replication Instance
  name = "example-replication_instance"

  # Common attributes
  tags = {
    Name        = "example-replication_instance"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Replication Subnet Group

```hcl
resource "aws_dms_replication_subnet_group" "example" {
  # Example configuration for Replication Subnet Group
  name = "example-replication_subnet_group"

  # Common attributes
  tags = {
    Name        = "example-replication_subnet_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Replication Task

```hcl
resource "aws_dms_replication_task" "example" {
  # Example configuration for Replication Task
  name = "example-replication_task"

  # Common attributes
  tags = {
    Name        = "example-replication_task"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### S3 Endpoint

```hcl
resource "aws_dms_s3_endpoint" "example" {
  # Example configuration for S3 Endpoint
  name = "example-s3_endpoint"

  # Common attributes
  tags = {
    Name        = "example-s3_endpoint"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## docdb

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Cluster | aws_docdb_cluster | SDK |
| Cluster Instance | aws_docdb_cluster_instance | SDK |
| Cluster Parameter Group | aws_docdb_cluster_parameter_group | SDK |
| Event Subscription | aws_docdb_event_subscription | SDK |
| Subnet Group | aws_docdb_subnet_group | SDK |


### Examples


#### Cluster

```hcl
resource "aws_docdb_cluster" "example" {
  # Example configuration for Cluster
  name = "example-cluster"

  # Common attributes
  tags = {
    Name        = "example-cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster Instance

```hcl
resource "aws_docdb_cluster_instance" "example" {
  # Example configuration for Cluster Instance
  name = "example-cluster_instance"

  # Common attributes
  tags = {
    Name        = "example-cluster_instance"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster Parameter Group

```hcl
resource "aws_docdb_cluster_parameter_group" "example" {
  # Example configuration for Cluster Parameter Group
  name = "example-cluster_parameter_group"

  # Common attributes
  tags = {
    Name        = "example-cluster_parameter_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Event Subscription

```hcl
resource "aws_docdb_event_subscription" "example" {
  # Example configuration for Event Subscription
  name = "example-event_subscription"

  # Common attributes
  tags = {
    Name        = "example-event_subscription"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Subnet Group

```hcl
resource "aws_docdb_subnet_group" "example" {
  # Example configuration for Subnet Group
  name = "example-subnet_group"

  # Common attributes
  tags = {
    Name        = "example-subnet_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## docdbelastic

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Cluster | N/A | Framework |


### Examples


#### Cluster

```hcl
resource "aws_docdbelastic_cluster" "example" {
  # Example configuration for Cluster
  name = "example-cluster"

  # Common attributes
  tags = {
    Name        = "example-cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## drs

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Replication Configuration Template | N/A | Framework |


### Examples


#### Replication Configuration Template

```hcl
resource "aws_drs_replication_configuration_template" "example" {
  # Example configuration for Replication Configuration Template
  name = "example-replication_configuration_template"

  # Common attributes
  tags = {
    Name        = "example-replication_configuration_template"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## ds

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Conditional Forwarder | aws_directory_service_conditional_forwarder | SDK |
| Directory | aws_directory_service_directory | SDK |
| Log Subscription | aws_directory_service_log_subscription | SDK |
| RADIUS Settings | aws_directory_service_radius_settings | SDK |
| Region | aws_directory_service_region | SDK |
| Shared Directory | aws_directory_service_shared_directory | SDK |
| Shared Directory Accepter | aws_directory_service_shared_directory_accepter | SDK |
| Trust | N/A | Framework |


### Examples


#### Conditional Forwarder

```hcl
resource "aws_directory_service_conditional_forwarder" "example" {
  # Example configuration for Conditional Forwarder
  name = "example-conditional_forwarder"

  # Common attributes
  tags = {
    Name        = "example-conditional_forwarder"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Directory

```hcl
resource "aws_directory_service_directory" "example" {
  # Example configuration for Directory
  name = "example-directory"

  # Common attributes
  tags = {
    Name        = "example-directory"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Log Subscription

```hcl
resource "aws_directory_service_log_subscription" "example" {
  # Example configuration for Log Subscription
  name = "example-log_subscription"

  # Common attributes
  tags = {
    Name        = "example-log_subscription"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### RADIUS Settings

```hcl
resource "aws_directory_service_radius_settings" "example" {
  # Example configuration for RADIUS Settings
  name = "example-radius_settings"

  # Common attributes
  tags = {
    Name        = "example-radius_settings"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Region

```hcl
resource "aws_directory_service_region" "example" {
  # Example configuration for Region
  name = "example-region"

  # Common attributes
  tags = {
    Name        = "example-region"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Shared Directory

```hcl
resource "aws_directory_service_shared_directory" "example" {
  # Example configuration for Shared Directory
  name = "example-shared_directory"

  # Common attributes
  tags = {
    Name        = "example-shared_directory"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Shared Directory Accepter

```hcl
resource "aws_directory_service_shared_directory_accepter" "example" {
  # Example configuration for Shared Directory Accepter
  name = "example-shared_directory_accepter"

  # Common attributes
  tags = {
    Name        = "example-shared_directory_accepter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Trust

```hcl
resource "aws_ds_trust" "example" {
  # Example configuration for Trust
  name = "example-trust"

  # Common attributes
  tags = {
    Name        = "example-trust"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## dynamodb

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Contributor Insights | aws_dynamodb_contributor_insights | SDK |
| DynamoDB Resource Tag | aws_dynamodb_tag | SDK |
| Global Table | aws_dynamodb_global_table | SDK |
| Kinesis Streaming Destination | aws_dynamodb_kinesis_streaming_destination | SDK |
| Resource Policy | N/A | Framework |
| Table | aws_dynamodb_table | SDK |
| Table Export | aws_dynamodb_table_export | SDK |
| Table Item | aws_dynamodb_table_item | SDK |
| Table Replica | aws_dynamodb_table_replica | SDK |


### Examples


#### Contributor Insights

```hcl
resource "aws_dynamodb_contributor_insights" "example" {
  # Example configuration for Contributor Insights
  name = "example-contributor_insights"

  # Common attributes
  tags = {
    Name        = "example-contributor_insights"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### DynamoDB Resource Tag

```hcl
resource "aws_dynamodb_tag" "example" {
  # Example configuration for DynamoDB Resource Tag
  name = "example-dynamodb_resource_tag"

  # Common attributes
  tags = {
    Name        = "example-dynamodb_resource_tag"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Global Table

```hcl
resource "aws_dynamodb_global_table" "example" {
  # Example configuration for Global Table
  name = "example-global_table"

  # Common attributes
  tags = {
    Name        = "example-global_table"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Kinesis Streaming Destination

```hcl
resource "aws_dynamodb_kinesis_streaming_destination" "example" {
  # Example configuration for Kinesis Streaming Destination
  name = "example-kinesis_streaming_destination"

  # Common attributes
  tags = {
    Name        = "example-kinesis_streaming_destination"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource Policy

```hcl
resource "aws_dynamodb_resource_policy" "example" {
  # Example configuration for Resource Policy
  name = "example-resource_policy"

  # Common attributes
  tags = {
    Name        = "example-resource_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Table

```hcl
resource "aws_dynamodb_table" "example" {
  name           = "example-table"
  billing_mode   = "PROVISIONED"
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "id"

  attribute {
    name = "id"
    type = "S"
  }

  tags = {
    Name = "example-table"
  }
}
```


#### Table Export

```hcl
resource "aws_dynamodb_table_export" "example" {
  # Example configuration for Table Export
  name = "example-table_export"

  # Common attributes
  tags = {
    Name        = "example-table_export"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Table Item

```hcl
resource "aws_dynamodb_table_item" "example" {
  # Example configuration for Table Item
  name = "example-table_item"

  # Common attributes
  tags = {
    Name        = "example-table_item"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Table Replica

```hcl
resource "aws_dynamodb_table_replica" "example" {
  # Example configuration for Table Replica
  name = "example-table_replica"

  # Common attributes
  tags = {
    Name        = "example-table_replica"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## ec2

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| AMI | aws_ami_from_instance | SDK |
| AMI Launch Permission | aws_ami_launch_permission | SDK |
| Availability Zone Group | aws_ec2_availability_zone_group | SDK |
| Capacity Block Reservation | N/A | Framework |
| Capacity Reservation | aws_ec2_capacity_reservation | SDK |
| Carrier Gateway | aws_ec2_carrier_gateway | SDK |
| Client VPN Authorization Rule | aws_ec2_client_vpn_authorization_rule | SDK |
| Client VPN Endpoint | aws_ec2_client_vpn_endpoint | SDK |
| Client VPN Network Association | aws_ec2_client_vpn_network_association | SDK |
| Client VPN Route | aws_ec2_client_vpn_route | SDK |
| Customer Gateway | aws_customer_gateway | SDK |
| DHCP Options | aws_vpc_dhcp_options | SDK |
| Default VPC | aws_default_vpc | SDK |
| EBS Default KMS Key | aws_ebs_default_kms_key | SDK |
| EBS Encryption By Default | aws_ebs_encryption_by_default | SDK |
| EBS Fast Snapshot Restore | N/A | Framework |
| EBS Snapshot | aws_ebs_snapshot | SDK |
| EBS Snapshot Block Public Access | aws_ebs_snapshot_block_public_access | SDK |
| EBS Snapshot Copy | aws_ebs_snapshot_copy | SDK |
| EBS Snapshot CreateVolume Permission | aws_snapshot_create_volume_permission | SDK |
| EBS Snapshot Import | aws_ebs_snapshot_import | SDK |
| EBS Volume | aws_ebs_volume | SDK |
| EBS Volume Attachment | aws_volume_attachment | SDK |
| EC2 Resource Tag | aws_ec2_tag | SDK |
| EIP | aws_eip | SDK |
| EIP Association | aws_eip_association | SDK |
| EIP Domain Name | N/A | Framework |
| Egress-Only Internet Gateway | aws_egress_only_internet_gateway | SDK |
| Endpoint Service Allowed Principal | aws_vpc_endpoint_service_allowed_principal | SDK |
| Fleet | aws_ec2_fleet | SDK |
| Flow Log | aws_flow_log | SDK |
| Host | aws_ec2_host | SDK |
| IPAM | aws_vpc_ipam | SDK |
| IPAM Organization Admin Account | aws_vpc_ipam_organization_admin_account | SDK |
| IPAM Pool | aws_vpc_ipam_pool | SDK |
| IPAM Pool CIDR | aws_vpc_ipam_pool_cidr | SDK |
| IPAM Pool CIDR Allocation | aws_vpc_ipam_pool_cidr_allocation | SDK |
| IPAM Preview Next CIDR | aws_vpc_ipam_preview_next_cidr | SDK |
| IPAM Resource Discovery | aws_vpc_ipam_resource_discovery | SDK |
| IPAM Resource Discovery Association | aws_vpc_ipam_resource_discovery_association | SDK |
| IPAM Scope | aws_vpc_ipam_scope | SDK |
| Image Block Public Access | aws_ec2_image_block_public_access | SDK |
| Instance | aws_instance | SDK |
| Instance Connect Endpoint | N/A | Framework |
| Instance Metadata Defaults | N/A | Framework |
| Instance State | aws_ec2_instance_state | SDK |
| Internet Gateway | aws_internet_gateway | SDK |
| Internet Gateway Attachment | aws_internet_gateway_attachment | SDK |
| Key Pair | aws_key_pair | SDK |
| Launch Template | aws_launch_template | SDK |
| Local Gateway Route Table VPC Association | aws_ec2_local_gateway_route_table_vpc_association | SDK |
| Main Route Table Association | aws_main_route_table_association | SDK |
| Managed Prefix List | aws_ec2_managed_prefix_list | SDK |
| Managed Prefix List Entry | aws_ec2_managed_prefix_list_entry | SDK |
| NAT Gateway | aws_nat_gateway | SDK |
| Network ACL | aws_network_acl | SDK |
| Network ACL Association | aws_network_acl_association | SDK |
| Network ACL Rule | aws_network_acl_rule | SDK |
| Network Insights Analysis | aws_ec2_network_insights_analysis | SDK |
| Network Insights Path | aws_ec2_network_insights_path | SDK |
| Network Interface | aws_network_interface | SDK |
| Network Interface Attachment | aws_network_interface_attachment | SDK |
| Network Interface SG Attachement | aws_network_interface_sg_attachment | SDK |
| Placement Group | aws_placement_group | SDK |
| Route | aws_route | SDK |
| Route Table | aws_route_table | SDK |
| Route Table Association | aws_route_table_association | SDK |
| Security Group | aws_security_group | SDK |
| Security Group Egress Rule | N/A | Framework |
| Security Group Ingress Rule | N/A | Framework |
| Security Group Rule | aws_security_group_rule | SDK |
| Security Group VPC Association | N/A | Framework |
| Serial Console Access | aws_ec2_serial_console_access | SDK |
| Spot Datafeed Subscription | aws_spot_datafeed_subscription | SDK |
| Spot Fleet Request | aws_spot_fleet_request | SDK |
| Spot Instance Request | aws_spot_instance_request | SDK |
| Subnet | aws_subnet | SDK |
| Subnet CIDR Reservation | aws_ec2_subnet_cidr_reservation | SDK |
| Traffic Mirror Filter | aws_ec2_traffic_mirror_filter | SDK |
| Traffic Mirror Filter Rule | aws_ec2_traffic_mirror_filter_rule | SDK |
| Traffic Mirror Session | aws_ec2_traffic_mirror_session | SDK |
| Traffic Mirror Target | aws_ec2_traffic_mirror_target | SDK |
| Transit Gateway | aws_ec2_transit_gateway | SDK |
| Transit Gateway Connect | aws_ec2_transit_gateway_connect | SDK |
| Transit Gateway Connect Peer | aws_ec2_transit_gateway_connect_peer | SDK |
| Transit Gateway Default Route Table Association | N/A | Framework |
| Transit Gateway Default Route Table Propagation | N/A | Framework |
| Transit Gateway Multicast Domain | aws_ec2_transit_gateway_multicast_domain | SDK |
| Transit Gateway Multicast Domain Association | aws_ec2_transit_gateway_multicast_domain_association | SDK |
| Transit Gateway Multicast Group Member | aws_ec2_transit_gateway_multicast_group_member | SDK |
| Transit Gateway Multicast Group Source | aws_ec2_transit_gateway_multicast_group_source | SDK |
| Transit Gateway Peering Attachment | aws_ec2_transit_gateway_peering_attachment | SDK |
| Transit Gateway Peering Attachment Accepter | aws_ec2_transit_gateway_peering_attachment_accepter | SDK |
| Transit Gateway Policy Table | aws_ec2_transit_gateway_policy_table | SDK |
| Transit Gateway Policy Table Association | aws_ec2_transit_gateway_policy_table_association | SDK |
| Transit Gateway Prefix List Reference | aws_ec2_transit_gateway_prefix_list_reference | SDK |
| Transit Gateway Route | aws_ec2_transit_gateway_route | SDK |
| Transit Gateway Route Table | aws_ec2_transit_gateway_route_table | SDK |
| Transit Gateway Route Table Association | aws_ec2_transit_gateway_route_table_association | SDK |
| Transit Gateway Route Table Propagation | aws_ec2_transit_gateway_route_table_propagation | SDK |
| Transit Gateway VPC Attachment | aws_ec2_transit_gateway_vpc_attachment | SDK |
| Transit Gateway VPC Attachment Accepter | aws_ec2_transit_gateway_vpc_attachment_accepter | SDK |
| VPC | aws_vpc | SDK |
| VPC Block Public Access Exclusion | N/A | Framework |
| VPC Block Public Access Options | N/A | Framework |
| VPC DHCP Options Association | aws_vpc_dhcp_options_association | SDK |
| VPC Endpoint | aws_vpc_endpoint | SDK |
| VPC Endpoint Connection Accepter | aws_vpc_endpoint_connection_accepter | SDK |
| VPC Endpoint Connection Notification | aws_vpc_endpoint_connection_notification | SDK |
| VPC Endpoint Private DNS | N/A | Framework |
| VPC Endpoint Route Table Association | aws_vpc_endpoint_route_table_association | SDK |
| VPC Endpoint Security Group Association | aws_vpc_endpoint_security_group_association | SDK |
| VPC Endpoint Service | aws_vpc_endpoint_service | SDK |
| VPC Endpoint Service Private DNS Verification | N/A | Framework |
| VPC Endpoint Subnet Association | aws_vpc_endpoint_subnet_association | SDK |
| VPC IPV4 CIDR Block Association | aws_vpc_ipv4_cidr_block_association | SDK |
| VPC IPV6 CIDR Block Association | aws_vpc_ipv6_cidr_block_association | SDK |
| VPC Network Performance Metric Subscription | aws_vpc_network_performance_metric_subscription | SDK |
| VPC Peering Connection | aws_vpc_peering_connection_accepter | SDK |
| VPC Peering Connection Options | aws_vpc_peering_connection_options | SDK |
| VPN Connection | aws_vpn_connection | SDK |
| VPN Connection Route | aws_vpn_connection_route | SDK |
| VPN Gateway | aws_vpn_gateway | SDK |
| VPN Gateway Attachment | aws_vpn_gateway_attachment | SDK |
| VPN Gateway Route Propagation | aws_vpn_gateway_route_propagation | SDK |
| Verified Access Endpoint | aws_verifiedaccess_endpoint | SDK |
| Verified Access Group | aws_verifiedaccess_group | SDK |
| Verified Access Instance | aws_verifiedaccess_instance | SDK |
| Verified Access Instance Logging Configuration | aws_verifiedaccess_instance_logging_configuration | SDK |
| Verified Access Instance Trust Provider Attachment | aws_verifiedaccess_instance_trust_provider_attachment | SDK |
| Verified Access Trust Provider | aws_verifiedaccess_trust_provider | SDK |


### Examples


#### AMI

```hcl
resource "aws_ami_from_instance" "example" {
  # Example configuration for AMI
  name = "example-ami"

  # Common attributes
  tags = {
    Name        = "example-ami"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### AMI Launch Permission

```hcl
resource "aws_ami_launch_permission" "example" {
  # Example configuration for AMI Launch Permission
  name = "example-ami_launch_permission"

  # Common attributes
  tags = {
    Name        = "example-ami_launch_permission"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Availability Zone Group

```hcl
resource "aws_ec2_availability_zone_group" "example" {
  # Example configuration for Availability Zone Group
  name = "example-availability_zone_group"

  # Common attributes
  tags = {
    Name        = "example-availability_zone_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Capacity Block Reservation

```hcl
resource "aws_ec2_capacity_block_reservation" "example" {
  # Example configuration for Capacity Block Reservation
  name = "example-capacity_block_reservation"

  # Common attributes
  tags = {
    Name        = "example-capacity_block_reservation"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Capacity Reservation

```hcl
resource "aws_ec2_capacity_reservation" "example" {
  # Example configuration for Capacity Reservation
  name = "example-capacity_reservation"

  # Common attributes
  tags = {
    Name        = "example-capacity_reservation"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Carrier Gateway

```hcl
resource "aws_ec2_carrier_gateway" "example" {
  # Example configuration for Carrier Gateway
  name = "example-carrier_gateway"

  # Common attributes
  tags = {
    Name        = "example-carrier_gateway"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Client VPN Authorization Rule

```hcl
resource "aws_ec2_client_vpn_authorization_rule" "example" {
  # Example configuration for Client VPN Authorization Rule
  name = "example-client_vpn_authorization_rule"

  # Common attributes
  tags = {
    Name        = "example-client_vpn_authorization_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Client VPN Endpoint

```hcl
resource "aws_ec2_client_vpn_endpoint" "example" {
  # Example configuration for Client VPN Endpoint
  name = "example-client_vpn_endpoint"

  # Common attributes
  tags = {
    Name        = "example-client_vpn_endpoint"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Client VPN Network Association

```hcl
resource "aws_ec2_client_vpn_network_association" "example" {
  # Example configuration for Client VPN Network Association
  name = "example-client_vpn_network_association"

  # Common attributes
  tags = {
    Name        = "example-client_vpn_network_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Client VPN Route

```hcl
resource "aws_ec2_client_vpn_route" "example" {
  # Example configuration for Client VPN Route
  name = "example-client_vpn_route"

  # Common attributes
  tags = {
    Name        = "example-client_vpn_route"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Customer Gateway

```hcl
resource "aws_customer_gateway" "example" {
  # Example configuration for Customer Gateway
  name = "example-customer_gateway"

  # Common attributes
  tags = {
    Name        = "example-customer_gateway"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### DHCP Options

```hcl
resource "aws_vpc_dhcp_options" "example" {
  # Example configuration for DHCP Options
  name = "example-dhcp_options"

  # Common attributes
  tags = {
    Name        = "example-dhcp_options"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Default VPC

```hcl
resource "aws_default_vpc" "example" {
  # Example configuration for Default VPC
  name = "example-default_vpc"

  # Common attributes
  tags = {
    Name        = "example-default_vpc"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### EBS Default KMS Key

```hcl
resource "aws_ebs_default_kms_key" "example" {
  # Example configuration for EBS Default KMS Key
  name = "example-ebs_default_kms_key"

  # Common attributes
  tags = {
    Name        = "example-ebs_default_kms_key"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### EBS Encryption By Default

```hcl
resource "aws_ebs_encryption_by_default" "example" {
  # Example configuration for EBS Encryption By Default
  name = "example-ebs_encryption_by_default"

  # Common attributes
  tags = {
    Name        = "example-ebs_encryption_by_default"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### EBS Fast Snapshot Restore

```hcl
resource "aws_ec2_ebs_fast_snapshot_restore" "example" {
  # Example configuration for EBS Fast Snapshot Restore
  name = "example-ebs_fast_snapshot_restore"

  # Common attributes
  tags = {
    Name        = "example-ebs_fast_snapshot_restore"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### EBS Snapshot

```hcl
resource "aws_ebs_snapshot" "example" {
  # Example configuration for EBS Snapshot
  name = "example-ebs_snapshot"

  # Common attributes
  tags = {
    Name        = "example-ebs_snapshot"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### EBS Snapshot Block Public Access

```hcl
resource "aws_ebs_snapshot_block_public_access" "example" {
  # Example configuration for EBS Snapshot Block Public Access
  name = "example-ebs_snapshot_block_public_access"

  # Common attributes
  tags = {
    Name        = "example-ebs_snapshot_block_public_access"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### EBS Snapshot Copy

```hcl
resource "aws_ebs_snapshot_copy" "example" {
  # Example configuration for EBS Snapshot Copy
  name = "example-ebs_snapshot_copy"

  # Common attributes
  tags = {
    Name        = "example-ebs_snapshot_copy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### EBS Snapshot CreateVolume Permission

```hcl
resource "aws_snapshot_create_volume_permission" "example" {
  # Example configuration for EBS Snapshot CreateVolume Permission
  name = "example-ebs_snapshot_createvolume_permission"

  # Common attributes
  tags = {
    Name        = "example-ebs_snapshot_createvolume_permission"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### EBS Snapshot Import

```hcl
resource "aws_ebs_snapshot_import" "example" {
  # Example configuration for EBS Snapshot Import
  name = "example-ebs_snapshot_import"

  # Common attributes
  tags = {
    Name        = "example-ebs_snapshot_import"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### EBS Volume

```hcl
resource "aws_ebs_volume" "example" {
  # Example configuration for EBS Volume
  name = "example-ebs_volume"

  # Common attributes
  tags = {
    Name        = "example-ebs_volume"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### EBS Volume Attachment

```hcl
resource "aws_volume_attachment" "example" {
  # Example configuration for EBS Volume Attachment
  name = "example-ebs_volume_attachment"

  # Common attributes
  tags = {
    Name        = "example-ebs_volume_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### EC2 Resource Tag

```hcl
resource "aws_ec2_tag" "example" {
  # Example configuration for EC2 Resource Tag
  name = "example-ec2_resource_tag"

  # Common attributes
  tags = {
    Name        = "example-ec2_resource_tag"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### EIP

```hcl
resource "aws_eip" "example" {
  # Example configuration for EIP
  name = "example-eip"

  # Common attributes
  tags = {
    Name        = "example-eip"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### EIP Association

```hcl
resource "aws_eip_association" "example" {
  # Example configuration for EIP Association
  name = "example-eip_association"

  # Common attributes
  tags = {
    Name        = "example-eip_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### EIP Domain Name

```hcl
resource "aws_ec2_eip_domain_name" "example" {
  # Example configuration for EIP Domain Name
  name = "example-eip_domain_name"

  # Common attributes
  tags = {
    Name        = "example-eip_domain_name"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Egress-Only Internet Gateway

```hcl
resource "aws_egress_only_internet_gateway" "example" {
  # Example configuration for Egress-Only Internet Gateway
  name = "example-egress-only_internet_gateway"

  # Common attributes
  tags = {
    Name        = "example-egress-only_internet_gateway"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Endpoint Service Allowed Principal

```hcl
resource "aws_vpc_endpoint_service_allowed_principal" "example" {
  # Example configuration for Endpoint Service Allowed Principal
  name = "example-endpoint_service_allowed_principal"

  # Common attributes
  tags = {
    Name        = "example-endpoint_service_allowed_principal"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Fleet

```hcl
resource "aws_ec2_fleet" "example" {
  # Example configuration for Fleet
  name = "example-fleet"

  # Common attributes
  tags = {
    Name        = "example-fleet"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Flow Log

```hcl
resource "aws_flow_log" "example" {
  # Example configuration for Flow Log
  name = "example-flow_log"

  # Common attributes
  tags = {
    Name        = "example-flow_log"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Host

```hcl
resource "aws_ec2_host" "example" {
  # Example configuration for Host
  name = "example-host"

  # Common attributes
  tags = {
    Name        = "example-host"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### IPAM

```hcl
resource "aws_vpc_ipam" "example" {
  # Example configuration for IPAM
  name = "example-ipam"

  # Common attributes
  tags = {
    Name        = "example-ipam"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### IPAM Organization Admin Account

```hcl
resource "aws_vpc_ipam_organization_admin_account" "example" {
  # Example configuration for IPAM Organization Admin Account
  name = "example-ipam_organization_admin_account"

  # Common attributes
  tags = {
    Name        = "example-ipam_organization_admin_account"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### IPAM Pool

```hcl
resource "aws_vpc_ipam_pool" "example" {
  # Example configuration for IPAM Pool
  name = "example-ipam_pool"

  # Common attributes
  tags = {
    Name        = "example-ipam_pool"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### IPAM Pool CIDR

```hcl
resource "aws_vpc_ipam_pool_cidr" "example" {
  # Example configuration for IPAM Pool CIDR
  name = "example-ipam_pool_cidr"

  # Common attributes
  tags = {
    Name        = "example-ipam_pool_cidr"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### IPAM Pool CIDR Allocation

```hcl
resource "aws_vpc_ipam_pool_cidr_allocation" "example" {
  # Example configuration for IPAM Pool CIDR Allocation
  name = "example-ipam_pool_cidr_allocation"

  # Common attributes
  tags = {
    Name        = "example-ipam_pool_cidr_allocation"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### IPAM Preview Next CIDR

```hcl
resource "aws_vpc_ipam_preview_next_cidr" "example" {
  # Example configuration for IPAM Preview Next CIDR
  name = "example-ipam_preview_next_cidr"

  # Common attributes
  tags = {
    Name        = "example-ipam_preview_next_cidr"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### IPAM Resource Discovery

```hcl
resource "aws_vpc_ipam_resource_discovery" "example" {
  # Example configuration for IPAM Resource Discovery
  name = "example-ipam_resource_discovery"

  # Common attributes
  tags = {
    Name        = "example-ipam_resource_discovery"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### IPAM Resource Discovery Association

```hcl
resource "aws_vpc_ipam_resource_discovery_association" "example" {
  # Example configuration for IPAM Resource Discovery Association
  name = "example-ipam_resource_discovery_association"

  # Common attributes
  tags = {
    Name        = "example-ipam_resource_discovery_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### IPAM Scope

```hcl
resource "aws_vpc_ipam_scope" "example" {
  # Example configuration for IPAM Scope
  name = "example-ipam_scope"

  # Common attributes
  tags = {
    Name        = "example-ipam_scope"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Image Block Public Access

```hcl
resource "aws_ec2_image_block_public_access" "example" {
  # Example configuration for Image Block Public Access
  name = "example-image_block_public_access"

  # Common attributes
  tags = {
    Name        = "example-image_block_public_access"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Instance

```hcl
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "example-instance"
  }
}
```


#### Instance Connect Endpoint

```hcl
resource "aws_ec2_instance_connect_endpoint" "example" {
  # Example configuration for Instance Connect Endpoint
  name = "example-instance_connect_endpoint"

  # Common attributes
  tags = {
    Name        = "example-instance_connect_endpoint"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Instance Metadata Defaults

```hcl
resource "aws_ec2_instance_metadata_defaults" "example" {
  # Example configuration for Instance Metadata Defaults
  name = "example-instance_metadata_defaults"

  # Common attributes
  tags = {
    Name        = "example-instance_metadata_defaults"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Instance State

```hcl
resource "aws_ec2_instance_state" "example" {
  # Example configuration for Instance State
  name = "example-instance_state"

  # Common attributes
  tags = {
    Name        = "example-instance_state"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Internet Gateway

```hcl
resource "aws_internet_gateway" "example" {
  # Example configuration for Internet Gateway
  name = "example-internet_gateway"

  # Common attributes
  tags = {
    Name        = "example-internet_gateway"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Internet Gateway Attachment

```hcl
resource "aws_internet_gateway_attachment" "example" {
  # Example configuration for Internet Gateway Attachment
  name = "example-internet_gateway_attachment"

  # Common attributes
  tags = {
    Name        = "example-internet_gateway_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Key Pair

```hcl
resource "aws_key_pair" "example" {
  # Example configuration for Key Pair
  name = "example-key_pair"

  # Common attributes
  tags = {
    Name        = "example-key_pair"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Launch Template

```hcl
resource "aws_launch_template" "example" {
  # Example configuration for Launch Template
  name = "example-launch_template"

  # Common attributes
  tags = {
    Name        = "example-launch_template"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Local Gateway Route Table VPC Association

```hcl
resource "aws_ec2_local_gateway_route_table_vpc_association" "example" {
  # Example configuration for Local Gateway Route Table VPC Association
  name = "example-local_gateway_route_table_vpc_association"

  # Common attributes
  tags = {
    Name        = "example-local_gateway_route_table_vpc_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Main Route Table Association

```hcl
resource "aws_main_route_table_association" "example" {
  # Example configuration for Main Route Table Association
  name = "example-main_route_table_association"

  # Common attributes
  tags = {
    Name        = "example-main_route_table_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Managed Prefix List

```hcl
resource "aws_ec2_managed_prefix_list" "example" {
  # Example configuration for Managed Prefix List
  name = "example-managed_prefix_list"

  # Common attributes
  tags = {
    Name        = "example-managed_prefix_list"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Managed Prefix List Entry

```hcl
resource "aws_ec2_managed_prefix_list_entry" "example" {
  # Example configuration for Managed Prefix List Entry
  name = "example-managed_prefix_list_entry"

  # Common attributes
  tags = {
    Name        = "example-managed_prefix_list_entry"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### NAT Gateway

```hcl
resource "aws_nat_gateway" "example" {
  # Example configuration for NAT Gateway
  name = "example-nat_gateway"

  # Common attributes
  tags = {
    Name        = "example-nat_gateway"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Network ACL

```hcl
resource "aws_network_acl" "example" {
  # Example configuration for Network ACL
  name = "example-network_acl"

  # Common attributes
  tags = {
    Name        = "example-network_acl"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Network ACL Association

```hcl
resource "aws_network_acl_association" "example" {
  # Example configuration for Network ACL Association
  name = "example-network_acl_association"

  # Common attributes
  tags = {
    Name        = "example-network_acl_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Network ACL Rule

```hcl
resource "aws_network_acl_rule" "example" {
  # Example configuration for Network ACL Rule
  name = "example-network_acl_rule"

  # Common attributes
  tags = {
    Name        = "example-network_acl_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Network Insights Analysis

```hcl
resource "aws_ec2_network_insights_analysis" "example" {
  # Example configuration for Network Insights Analysis
  name = "example-network_insights_analysis"

  # Common attributes
  tags = {
    Name        = "example-network_insights_analysis"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Network Insights Path

```hcl
resource "aws_ec2_network_insights_path" "example" {
  # Example configuration for Network Insights Path
  name = "example-network_insights_path"

  # Common attributes
  tags = {
    Name        = "example-network_insights_path"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Network Interface

```hcl
resource "aws_network_interface" "example" {
  # Example configuration for Network Interface
  name = "example-network_interface"

  # Common attributes
  tags = {
    Name        = "example-network_interface"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Network Interface Attachment

```hcl
resource "aws_network_interface_attachment" "example" {
  # Example configuration for Network Interface Attachment
  name = "example-network_interface_attachment"

  # Common attributes
  tags = {
    Name        = "example-network_interface_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Network Interface SG Attachement

```hcl
resource "aws_network_interface_sg_attachment" "example" {
  # Example configuration for Network Interface SG Attachement
  name = "example-network_interface_sg_attachement"

  # Common attributes
  tags = {
    Name        = "example-network_interface_sg_attachement"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Placement Group

```hcl
resource "aws_placement_group" "example" {
  # Example configuration for Placement Group
  name = "example-placement_group"

  # Common attributes
  tags = {
    Name        = "example-placement_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Route

```hcl
resource "aws_route" "example" {
  # Example configuration for Route
  name = "example-route"

  # Common attributes
  tags = {
    Name        = "example-route"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Route Table

```hcl
resource "aws_route_table" "example" {
  # Example configuration for Route Table
  name = "example-route_table"

  # Common attributes
  tags = {
    Name        = "example-route_table"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Route Table Association

```hcl
resource "aws_route_table_association" "example" {
  # Example configuration for Route Table Association
  name = "example-route_table_association"

  # Common attributes
  tags = {
    Name        = "example-route_table_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Security Group

```hcl
resource "aws_security_group" "example" {
  name        = "example-security-group"
  description = "Example security group"
  vpc_id      = aws_vpc.example.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```


#### Security Group Egress Rule

```hcl
resource "aws_ec2_security_group_egress_rule" "example" {
  # Example configuration for Security Group Egress Rule
  name = "example-security_group_egress_rule"

  # Common attributes
  tags = {
    Name        = "example-security_group_egress_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Security Group Ingress Rule

```hcl
resource "aws_ec2_security_group_ingress_rule" "example" {
  # Example configuration for Security Group Ingress Rule
  name = "example-security_group_ingress_rule"

  # Common attributes
  tags = {
    Name        = "example-security_group_ingress_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Security Group Rule

```hcl
resource "aws_security_group_rule" "example" {
  # Example configuration for Security Group Rule
  name = "example-security_group_rule"

  # Common attributes
  tags = {
    Name        = "example-security_group_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Security Group VPC Association

```hcl
resource "aws_ec2_security_group_vpc_association" "example" {
  # Example configuration for Security Group VPC Association
  name = "example-security_group_vpc_association"

  # Common attributes
  tags = {
    Name        = "example-security_group_vpc_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Serial Console Access

```hcl
resource "aws_ec2_serial_console_access" "example" {
  # Example configuration for Serial Console Access
  name = "example-serial_console_access"

  # Common attributes
  tags = {
    Name        = "example-serial_console_access"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Spot Datafeed Subscription

```hcl
resource "aws_spot_datafeed_subscription" "example" {
  # Example configuration for Spot Datafeed Subscription
  name = "example-spot_datafeed_subscription"

  # Common attributes
  tags = {
    Name        = "example-spot_datafeed_subscription"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Spot Fleet Request

```hcl
resource "aws_spot_fleet_request" "example" {
  # Example configuration for Spot Fleet Request
  name = "example-spot_fleet_request"

  # Common attributes
  tags = {
    Name        = "example-spot_fleet_request"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Spot Instance Request

```hcl
resource "aws_spot_instance_request" "example" {
  # Example configuration for Spot Instance Request
  name = "example-spot_instance_request"

  # Common attributes
  tags = {
    Name        = "example-spot_instance_request"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Subnet

```hcl
resource "aws_subnet" "example" {
  vpc_id            = aws_vpc.example.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-west-2a"

  tags = {
    Name = "example-subnet"
  }
}
```


#### Subnet CIDR Reservation

```hcl
resource "aws_ec2_subnet_cidr_reservation" "example" {
  # Example configuration for Subnet CIDR Reservation
  name = "example-subnet_cidr_reservation"

  # Common attributes
  tags = {
    Name        = "example-subnet_cidr_reservation"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Traffic Mirror Filter

```hcl
resource "aws_ec2_traffic_mirror_filter" "example" {
  # Example configuration for Traffic Mirror Filter
  name = "example-traffic_mirror_filter"

  # Common attributes
  tags = {
    Name        = "example-traffic_mirror_filter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Traffic Mirror Filter Rule

```hcl
resource "aws_ec2_traffic_mirror_filter_rule" "example" {
  # Example configuration for Traffic Mirror Filter Rule
  name = "example-traffic_mirror_filter_rule"

  # Common attributes
  tags = {
    Name        = "example-traffic_mirror_filter_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Traffic Mirror Session

```hcl
resource "aws_ec2_traffic_mirror_session" "example" {
  # Example configuration for Traffic Mirror Session
  name = "example-traffic_mirror_session"

  # Common attributes
  tags = {
    Name        = "example-traffic_mirror_session"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Traffic Mirror Target

```hcl
resource "aws_ec2_traffic_mirror_target" "example" {
  # Example configuration for Traffic Mirror Target
  name = "example-traffic_mirror_target"

  # Common attributes
  tags = {
    Name        = "example-traffic_mirror_target"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway

```hcl
resource "aws_ec2_transit_gateway" "example" {
  # Example configuration for Transit Gateway
  name = "example-transit_gateway"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Connect

```hcl
resource "aws_ec2_transit_gateway_connect" "example" {
  # Example configuration for Transit Gateway Connect
  name = "example-transit_gateway_connect"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_connect"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Connect Peer

```hcl
resource "aws_ec2_transit_gateway_connect_peer" "example" {
  # Example configuration for Transit Gateway Connect Peer
  name = "example-transit_gateway_connect_peer"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_connect_peer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Default Route Table Association

```hcl
resource "aws_ec2_transit_gateway_default_route_table_association" "example" {
  # Example configuration for Transit Gateway Default Route Table Association
  name = "example-transit_gateway_default_route_table_association"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_default_route_table_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Default Route Table Propagation

```hcl
resource "aws_ec2_transit_gateway_default_route_table_propagation" "example" {
  # Example configuration for Transit Gateway Default Route Table Propagation
  name = "example-transit_gateway_default_route_table_propagation"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_default_route_table_propagation"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Multicast Domain

```hcl
resource "aws_ec2_transit_gateway_multicast_domain" "example" {
  # Example configuration for Transit Gateway Multicast Domain
  name = "example-transit_gateway_multicast_domain"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_multicast_domain"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Multicast Domain Association

```hcl
resource "aws_ec2_transit_gateway_multicast_domain_association" "example" {
  # Example configuration for Transit Gateway Multicast Domain Association
  name = "example-transit_gateway_multicast_domain_association"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_multicast_domain_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Multicast Group Member

```hcl
resource "aws_ec2_transit_gateway_multicast_group_member" "example" {
  # Example configuration for Transit Gateway Multicast Group Member
  name = "example-transit_gateway_multicast_group_member"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_multicast_group_member"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Multicast Group Source

```hcl
resource "aws_ec2_transit_gateway_multicast_group_source" "example" {
  # Example configuration for Transit Gateway Multicast Group Source
  name = "example-transit_gateway_multicast_group_source"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_multicast_group_source"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Peering Attachment

```hcl
resource "aws_ec2_transit_gateway_peering_attachment" "example" {
  # Example configuration for Transit Gateway Peering Attachment
  name = "example-transit_gateway_peering_attachment"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_peering_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Peering Attachment Accepter

```hcl
resource "aws_ec2_transit_gateway_peering_attachment_accepter" "example" {
  # Example configuration for Transit Gateway Peering Attachment Accepter
  name = "example-transit_gateway_peering_attachment_accepter"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_peering_attachment_accepter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Policy Table

```hcl
resource "aws_ec2_transit_gateway_policy_table" "example" {
  # Example configuration for Transit Gateway Policy Table
  name = "example-transit_gateway_policy_table"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_policy_table"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Policy Table Association

```hcl
resource "aws_ec2_transit_gateway_policy_table_association" "example" {
  # Example configuration for Transit Gateway Policy Table Association
  name = "example-transit_gateway_policy_table_association"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_policy_table_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Prefix List Reference

```hcl
resource "aws_ec2_transit_gateway_prefix_list_reference" "example" {
  # Example configuration for Transit Gateway Prefix List Reference
  name = "example-transit_gateway_prefix_list_reference"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_prefix_list_reference"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Route

```hcl
resource "aws_ec2_transit_gateway_route" "example" {
  # Example configuration for Transit Gateway Route
  name = "example-transit_gateway_route"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_route"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Route Table

```hcl
resource "aws_ec2_transit_gateway_route_table" "example" {
  # Example configuration for Transit Gateway Route Table
  name = "example-transit_gateway_route_table"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_route_table"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Route Table Association

```hcl
resource "aws_ec2_transit_gateway_route_table_association" "example" {
  # Example configuration for Transit Gateway Route Table Association
  name = "example-transit_gateway_route_table_association"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_route_table_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Route Table Propagation

```hcl
resource "aws_ec2_transit_gateway_route_table_propagation" "example" {
  # Example configuration for Transit Gateway Route Table Propagation
  name = "example-transit_gateway_route_table_propagation"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_route_table_propagation"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway VPC Attachment

```hcl
resource "aws_ec2_transit_gateway_vpc_attachment" "example" {
  # Example configuration for Transit Gateway VPC Attachment
  name = "example-transit_gateway_vpc_attachment"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_vpc_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway VPC Attachment Accepter

```hcl
resource "aws_ec2_transit_gateway_vpc_attachment_accepter" "example" {
  # Example configuration for Transit Gateway VPC Attachment Accepter
  name = "example-transit_gateway_vpc_attachment_accepter"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_vpc_attachment_accepter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC

```hcl
resource "aws_vpc" "example" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "example-vpc"
  }
}
```


#### VPC Block Public Access Exclusion

```hcl
resource "aws_ec2_vpc_block_public_access_exclusion" "example" {
  # Example configuration for VPC Block Public Access Exclusion
  name = "example-vpc_block_public_access_exclusion"

  # Common attributes
  tags = {
    Name        = "example-vpc_block_public_access_exclusion"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Block Public Access Options

```hcl
resource "aws_ec2_vpc_block_public_access_options" "example" {
  # Example configuration for VPC Block Public Access Options
  name = "example-vpc_block_public_access_options"

  # Common attributes
  tags = {
    Name        = "example-vpc_block_public_access_options"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC DHCP Options Association

```hcl
resource "aws_vpc_dhcp_options_association" "example" {
  # Example configuration for VPC DHCP Options Association
  name = "example-vpc_dhcp_options_association"

  # Common attributes
  tags = {
    Name        = "example-vpc_dhcp_options_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Endpoint

```hcl
resource "aws_vpc_endpoint" "example" {
  # Example configuration for VPC Endpoint
  name = "example-vpc_endpoint"

  # Common attributes
  tags = {
    Name        = "example-vpc_endpoint"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Endpoint Connection Accepter

```hcl
resource "aws_vpc_endpoint_connection_accepter" "example" {
  # Example configuration for VPC Endpoint Connection Accepter
  name = "example-vpc_endpoint_connection_accepter"

  # Common attributes
  tags = {
    Name        = "example-vpc_endpoint_connection_accepter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Endpoint Connection Notification

```hcl
resource "aws_vpc_endpoint_connection_notification" "example" {
  # Example configuration for VPC Endpoint Connection Notification
  name = "example-vpc_endpoint_connection_notification"

  # Common attributes
  tags = {
    Name        = "example-vpc_endpoint_connection_notification"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Endpoint Private DNS

```hcl
resource "aws_ec2_vpc_endpoint_private_dns" "example" {
  # Example configuration for VPC Endpoint Private DNS
  name = "example-vpc_endpoint_private_dns"

  # Common attributes
  tags = {
    Name        = "example-vpc_endpoint_private_dns"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Endpoint Route Table Association

```hcl
resource "aws_vpc_endpoint_route_table_association" "example" {
  # Example configuration for VPC Endpoint Route Table Association
  name = "example-vpc_endpoint_route_table_association"

  # Common attributes
  tags = {
    Name        = "example-vpc_endpoint_route_table_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Endpoint Security Group Association

```hcl
resource "aws_vpc_endpoint_security_group_association" "example" {
  # Example configuration for VPC Endpoint Security Group Association
  name = "example-vpc_endpoint_security_group_association"

  # Common attributes
  tags = {
    Name        = "example-vpc_endpoint_security_group_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Endpoint Service

```hcl
resource "aws_vpc_endpoint_service" "example" {
  # Example configuration for VPC Endpoint Service
  name = "example-vpc_endpoint_service"

  # Common attributes
  tags = {
    Name        = "example-vpc_endpoint_service"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Endpoint Service Private DNS Verification

```hcl
resource "aws_ec2_vpc_endpoint_service_private_dns_verification" "example" {
  # Example configuration for VPC Endpoint Service Private DNS Verification
  name = "example-vpc_endpoint_service_private_dns_verification"

  # Common attributes
  tags = {
    Name        = "example-vpc_endpoint_service_private_dns_verification"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Endpoint Subnet Association

```hcl
resource "aws_vpc_endpoint_subnet_association" "example" {
  # Example configuration for VPC Endpoint Subnet Association
  name = "example-vpc_endpoint_subnet_association"

  # Common attributes
  tags = {
    Name        = "example-vpc_endpoint_subnet_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC IPV4 CIDR Block Association

```hcl
resource "aws_vpc_ipv4_cidr_block_association" "example" {
  # Example configuration for VPC IPV4 CIDR Block Association
  name = "example-vpc_ipv4_cidr_block_association"

  # Common attributes
  tags = {
    Name        = "example-vpc_ipv4_cidr_block_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC IPV6 CIDR Block Association

```hcl
resource "aws_vpc_ipv6_cidr_block_association" "example" {
  # Example configuration for VPC IPV6 CIDR Block Association
  name = "example-vpc_ipv6_cidr_block_association"

  # Common attributes
  tags = {
    Name        = "example-vpc_ipv6_cidr_block_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Network Performance Metric Subscription

```hcl
resource "aws_vpc_network_performance_metric_subscription" "example" {
  # Example configuration for VPC Network Performance Metric Subscription
  name = "example-vpc_network_performance_metric_subscription"

  # Common attributes
  tags = {
    Name        = "example-vpc_network_performance_metric_subscription"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Peering Connection

```hcl
resource "aws_vpc_peering_connection_accepter" "example" {
  # Example configuration for VPC Peering Connection
  name = "example-vpc_peering_connection"

  # Common attributes
  tags = {
    Name        = "example-vpc_peering_connection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Peering Connection Options

```hcl
resource "aws_vpc_peering_connection_options" "example" {
  # Example configuration for VPC Peering Connection Options
  name = "example-vpc_peering_connection_options"

  # Common attributes
  tags = {
    Name        = "example-vpc_peering_connection_options"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPN Connection

```hcl
resource "aws_vpn_connection" "example" {
  # Example configuration for VPN Connection
  name = "example-vpn_connection"

  # Common attributes
  tags = {
    Name        = "example-vpn_connection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPN Connection Route

```hcl
resource "aws_vpn_connection_route" "example" {
  # Example configuration for VPN Connection Route
  name = "example-vpn_connection_route"

  # Common attributes
  tags = {
    Name        = "example-vpn_connection_route"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPN Gateway

```hcl
resource "aws_vpn_gateway" "example" {
  # Example configuration for VPN Gateway
  name = "example-vpn_gateway"

  # Common attributes
  tags = {
    Name        = "example-vpn_gateway"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPN Gateway Attachment

```hcl
resource "aws_vpn_gateway_attachment" "example" {
  # Example configuration for VPN Gateway Attachment
  name = "example-vpn_gateway_attachment"

  # Common attributes
  tags = {
    Name        = "example-vpn_gateway_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPN Gateway Route Propagation

```hcl
resource "aws_vpn_gateway_route_propagation" "example" {
  # Example configuration for VPN Gateway Route Propagation
  name = "example-vpn_gateway_route_propagation"

  # Common attributes
  tags = {
    Name        = "example-vpn_gateway_route_propagation"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Verified Access Endpoint

```hcl
resource "aws_verifiedaccess_endpoint" "example" {
  # Example configuration for Verified Access Endpoint
  name = "example-verified_access_endpoint"

  # Common attributes
  tags = {
    Name        = "example-verified_access_endpoint"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Verified Access Group

```hcl
resource "aws_verifiedaccess_group" "example" {
  # Example configuration for Verified Access Group
  name = "example-verified_access_group"

  # Common attributes
  tags = {
    Name        = "example-verified_access_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Verified Access Instance

```hcl
resource "aws_verifiedaccess_instance" "example" {
  # Example configuration for Verified Access Instance
  name = "example-verified_access_instance"

  # Common attributes
  tags = {
    Name        = "example-verified_access_instance"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Verified Access Instance Logging Configuration

```hcl
resource "aws_verifiedaccess_instance_logging_configuration" "example" {
  # Example configuration for Verified Access Instance Logging Configuration
  name = "example-verified_access_instance_logging_configuration"

  # Common attributes
  tags = {
    Name        = "example-verified_access_instance_logging_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Verified Access Instance Trust Provider Attachment

```hcl
resource "aws_verifiedaccess_instance_trust_provider_attachment" "example" {
  # Example configuration for Verified Access Instance Trust Provider Attachment
  name = "example-verified_access_instance_trust_provider_attachment"

  # Common attributes
  tags = {
    Name        = "example-verified_access_instance_trust_provider_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Verified Access Trust Provider

```hcl
resource "aws_verifiedaccess_trust_provider" "example" {
  # Example configuration for Verified Access Trust Provider
  name = "example-verified_access_trust_provider"

  # Common attributes
  tags = {
    Name        = "example-verified_access_trust_provider"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## ecr

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Account Setting | N/A | Framework |
| Lifecycle Policy | aws_ecr_lifecycle_policy | SDK |
| Pull Through Cache Rule | aws_ecr_pull_through_cache_rule | SDK |
| Registry Policy | aws_ecr_registry_policy | SDK |
| Registry Scanning Configuration | aws_ecr_registry_scanning_configuration | SDK |
| Replication Configuration | aws_ecr_replication_configuration | SDK |
| Repository | aws_ecr_repository | SDK |
| Repository Creation Template | aws_ecr_repository_creation_template | SDK |
| Repsitory Policy | aws_ecr_repository_policy | SDK |


### Examples


#### Account Setting

```hcl
resource "aws_ecr_account_setting" "example" {
  # Example configuration for Account Setting
  name = "example-account_setting"

  # Common attributes
  tags = {
    Name        = "example-account_setting"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Lifecycle Policy

```hcl
resource "aws_ecr_lifecycle_policy" "example" {
  # Example configuration for Lifecycle Policy
  name = "example-lifecycle_policy"

  # Common attributes
  tags = {
    Name        = "example-lifecycle_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Pull Through Cache Rule

```hcl
resource "aws_ecr_pull_through_cache_rule" "example" {
  # Example configuration for Pull Through Cache Rule
  name = "example-pull_through_cache_rule"

  # Common attributes
  tags = {
    Name        = "example-pull_through_cache_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Registry Policy

```hcl
resource "aws_ecr_registry_policy" "example" {
  # Example configuration for Registry Policy
  name = "example-registry_policy"

  # Common attributes
  tags = {
    Name        = "example-registry_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Registry Scanning Configuration

```hcl
resource "aws_ecr_registry_scanning_configuration" "example" {
  # Example configuration for Registry Scanning Configuration
  name = "example-registry_scanning_configuration"

  # Common attributes
  tags = {
    Name        = "example-registry_scanning_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Replication Configuration

```hcl
resource "aws_ecr_replication_configuration" "example" {
  # Example configuration for Replication Configuration
  name = "example-replication_configuration"

  # Common attributes
  tags = {
    Name        = "example-replication_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Repository

```hcl
resource "aws_ecr_repository" "example" {
  # Example configuration for Repository
  name = "example-repository"

  # Common attributes
  tags = {
    Name        = "example-repository"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Repository Creation Template

```hcl
resource "aws_ecr_repository_creation_template" "example" {
  # Example configuration for Repository Creation Template
  name = "example-repository_creation_template"

  # Common attributes
  tags = {
    Name        = "example-repository_creation_template"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Repsitory Policy

```hcl
resource "aws_ecr_repository_policy" "example" {
  # Example configuration for Repsitory Policy
  name = "example-repsitory_policy"

  # Common attributes
  tags = {
    Name        = "example-repsitory_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## ecrpublic

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Repository | aws_ecrpublic_repository | SDK |


### Examples


#### Repository

```hcl
resource "aws_ecrpublic_repository" "example" {
  # Example configuration for Repository
  name = "example-repository"

  # Common attributes
  tags = {
    Name        = "example-repository"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## ecs

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Account Setting Default | aws_ecs_account_setting_default | SDK |
| Capacity Provider | aws_ecs_capacity_provider | SDK |
| Cluster | aws_ecs_cluster | SDK |
| Cluster Capacity Providers | aws_ecs_cluster_capacity_providers | SDK |
| ECS Resource Tag | aws_ecs_tag | SDK |
| Service | aws_ecs_service | SDK |
| Task Definition | aws_ecs_task_definition | SDK |
| Task Set | aws_ecs_task_set | SDK |


### Examples


#### Account Setting Default

```hcl
resource "aws_ecs_account_setting_default" "example" {
  # Example configuration for Account Setting Default
  name = "example-account_setting_default"

  # Common attributes
  tags = {
    Name        = "example-account_setting_default"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Capacity Provider

```hcl
resource "aws_ecs_capacity_provider" "example" {
  # Example configuration for Capacity Provider
  name = "example-capacity_provider"

  # Common attributes
  tags = {
    Name        = "example-capacity_provider"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster

```hcl
resource "aws_ecs_cluster" "example" {
  name = "example-cluster"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}
```


#### Cluster Capacity Providers

```hcl
resource "aws_ecs_cluster_capacity_providers" "example" {
  # Example configuration for Cluster Capacity Providers
  name = "example-cluster_capacity_providers"

  # Common attributes
  tags = {
    Name        = "example-cluster_capacity_providers"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### ECS Resource Tag

```hcl
resource "aws_ecs_tag" "example" {
  # Example configuration for ECS Resource Tag
  name = "example-ecs_resource_tag"

  # Common attributes
  tags = {
    Name        = "example-ecs_resource_tag"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Service

```hcl
resource "aws_ecs_service" "example" {
  name            = "example-service"
  cluster         = aws_ecs_cluster.example.id
  task_definition = aws_ecs_task_definition.example.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = [aws_subnet.example.id]
    security_groups  = [aws_security_group.example.id]
    assign_public_ip = true
  }
}
```


#### Task Definition

```hcl
resource "aws_ecs_task_definition" "example" {
  family                   = "example-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  execution_role_arn       = aws_iam_role.example.arn

  container_definitions = jsonencode([
    {
      name      = "example-container"
      image     = "nginx:latest"
      essential = true
      portMappings = [
        {
          containerPort = 80
          hostPort      = 80
        }
      ]
    }
  ])
}
```


#### Task Set

```hcl
resource "aws_ecs_task_set" "example" {
  # Example configuration for Task Set
  name = "example-task_set"

  # Common attributes
  tags = {
    Name        = "example-task_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## efs

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Access Point | aws_efs_access_point | SDK |
| Backup Policy | aws_efs_backup_policy | SDK |
| File System | aws_efs_file_system | SDK |
| File System Policy | aws_efs_file_system_policy | SDK |
| Mount Target | aws_efs_mount_target | SDK |
| Replication Configuration | aws_efs_replication_configuration | SDK |


### Examples


#### Access Point

```hcl
resource "aws_efs_access_point" "example" {
  # Example configuration for Access Point
  name = "example-access_point"

  # Common attributes
  tags = {
    Name        = "example-access_point"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Backup Policy

```hcl
resource "aws_efs_backup_policy" "example" {
  # Example configuration for Backup Policy
  name = "example-backup_policy"

  # Common attributes
  tags = {
    Name        = "example-backup_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### File System

```hcl
resource "aws_efs_file_system" "example" {
  # Example configuration for File System
  name = "example-file_system"

  # Common attributes
  tags = {
    Name        = "example-file_system"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### File System Policy

```hcl
resource "aws_efs_file_system_policy" "example" {
  # Example configuration for File System Policy
  name = "example-file_system_policy"

  # Common attributes
  tags = {
    Name        = "example-file_system_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Mount Target

```hcl
resource "aws_efs_mount_target" "example" {
  # Example configuration for Mount Target
  name = "example-mount_target"

  # Common attributes
  tags = {
    Name        = "example-mount_target"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Replication Configuration

```hcl
resource "aws_efs_replication_configuration" "example" {
  # Example configuration for Replication Configuration
  name = "example-replication_configuration"

  # Common attributes
  tags = {
    Name        = "example-replication_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## eks

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Access Entry | aws_eks_access_entry | SDK |
| Access Policy Association | aws_eks_access_policy_association | SDK |
| Add-On | aws_eks_addon | SDK |
| Cluster | aws_eks_cluster | SDK |
| Fargate Profile | aws_eks_fargate_profile | SDK |
| Identity Provider Config | aws_eks_identity_provider_config | SDK |
| Node Group | aws_eks_node_group | SDK |
| Pod Identity Association | N/A | Framework |


### Examples


#### Access Entry

```hcl
resource "aws_eks_access_entry" "example" {
  # Example configuration for Access Entry
  name = "example-access_entry"

  # Common attributes
  tags = {
    Name        = "example-access_entry"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Access Policy Association

```hcl
resource "aws_eks_access_policy_association" "example" {
  # Example configuration for Access Policy Association
  name = "example-access_policy_association"

  # Common attributes
  tags = {
    Name        = "example-access_policy_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Add-On

```hcl
resource "aws_eks_addon" "example" {
  # Example configuration for Add-On
  name = "example-add-on"

  # Common attributes
  tags = {
    Name        = "example-add-on"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster

```hcl
resource "aws_eks_cluster" "example" {
  # Example configuration for Cluster
  name = "example-cluster"

  # Common attributes
  tags = {
    Name        = "example-cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Fargate Profile

```hcl
resource "aws_eks_fargate_profile" "example" {
  # Example configuration for Fargate Profile
  name = "example-fargate_profile"

  # Common attributes
  tags = {
    Name        = "example-fargate_profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Identity Provider Config

```hcl
resource "aws_eks_identity_provider_config" "example" {
  # Example configuration for Identity Provider Config
  name = "example-identity_provider_config"

  # Common attributes
  tags = {
    Name        = "example-identity_provider_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Node Group

```hcl
resource "aws_eks_node_group" "example" {
  # Example configuration for Node Group
  name = "example-node_group"

  # Common attributes
  tags = {
    Name        = "example-node_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Pod Identity Association

```hcl
resource "aws_eks_pod_identity_association" "example" {
  # Example configuration for Pod Identity Association
  name = "example-pod_identity_association"

  # Common attributes
  tags = {
    Name        = "example-pod_identity_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## elasticache

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Cluster | aws_elasticache_cluster | SDK |
| Global Replication Group | aws_elasticache_global_replication_group | SDK |
| Parameter Group | aws_elasticache_parameter_group | SDK |
| Replication Group | aws_elasticache_replication_group | SDK |
| Serverless Cache | N/A | Framework |
| Subnet Group | aws_elasticache_subnet_group | SDK |
| User | aws_elasticache_user | SDK |
| User Group | aws_elasticache_user_group | SDK |
| User Group Association | aws_elasticache_user_group_association | SDK |


### Examples


#### Cluster

```hcl
resource "aws_elasticache_cluster" "example" {
  # Example configuration for Cluster
  name = "example-cluster"

  # Common attributes
  tags = {
    Name        = "example-cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Global Replication Group

```hcl
resource "aws_elasticache_global_replication_group" "example" {
  # Example configuration for Global Replication Group
  name = "example-global_replication_group"

  # Common attributes
  tags = {
    Name        = "example-global_replication_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Parameter Group

```hcl
resource "aws_elasticache_parameter_group" "example" {
  # Example configuration for Parameter Group
  name = "example-parameter_group"

  # Common attributes
  tags = {
    Name        = "example-parameter_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Replication Group

```hcl
resource "aws_elasticache_replication_group" "example" {
  # Example configuration for Replication Group
  name = "example-replication_group"

  # Common attributes
  tags = {
    Name        = "example-replication_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Serverless Cache

```hcl
resource "aws_elasticache_serverless_cache" "example" {
  # Example configuration for Serverless Cache
  name = "example-serverless_cache"

  # Common attributes
  tags = {
    Name        = "example-serverless_cache"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Subnet Group

```hcl
resource "aws_elasticache_subnet_group" "example" {
  # Example configuration for Subnet Group
  name = "example-subnet_group"

  # Common attributes
  tags = {
    Name        = "example-subnet_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User

```hcl
resource "aws_elasticache_user" "example" {
  # Example configuration for User
  name = "example-user"

  # Common attributes
  tags = {
    Name        = "example-user"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User Group

```hcl
resource "aws_elasticache_user_group" "example" {
  # Example configuration for User Group
  name = "example-user_group"

  # Common attributes
  tags = {
    Name        = "example-user_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User Group Association

```hcl
resource "aws_elasticache_user_group_association" "example" {
  # Example configuration for User Group Association
  name = "example-user_group_association"

  # Common attributes
  tags = {
    Name        = "example-user_group_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## elasticbeanstalk

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Application | aws_elastic_beanstalk_application | SDK |
| Application Version | aws_elastic_beanstalk_application_version | SDK |
| Configuration Template | aws_elastic_beanstalk_configuration_template | SDK |
| Environment | aws_elastic_beanstalk_environment | SDK |


### Examples


#### Application

```hcl
resource "aws_elastic_beanstalk_application" "example" {
  # Example configuration for Application
  name = "example-application"

  # Common attributes
  tags = {
    Name        = "example-application"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Application Version

```hcl
resource "aws_elastic_beanstalk_application_version" "example" {
  # Example configuration for Application Version
  name = "example-application_version"

  # Common attributes
  tags = {
    Name        = "example-application_version"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Configuration Template

```hcl
resource "aws_elastic_beanstalk_configuration_template" "example" {
  # Example configuration for Configuration Template
  name = "example-configuration_template"

  # Common attributes
  tags = {
    Name        = "example-configuration_template"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Environment

```hcl
resource "aws_elastic_beanstalk_environment" "example" {
  # Example configuration for Environment
  name = "example-environment"

  # Common attributes
  tags = {
    Name        = "example-environment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## elasticsearch

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Domain | aws_elasticsearch_domain | SDK |
| Domain Policy | aws_elasticsearch_domain_policy | SDK |
| Domain SAML Options | aws_elasticsearch_domain_saml_options | SDK |
| VPC Endpoint | aws_elasticsearch_vpc_endpoint | SDK |


### Examples


#### Domain

```hcl
resource "aws_elasticsearch_domain" "example" {
  # Example configuration for Domain
  name = "example-domain"

  # Common attributes
  tags = {
    Name        = "example-domain"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain Policy

```hcl
resource "aws_elasticsearch_domain_policy" "example" {
  # Example configuration for Domain Policy
  name = "example-domain_policy"

  # Common attributes
  tags = {
    Name        = "example-domain_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain SAML Options

```hcl
resource "aws_elasticsearch_domain_saml_options" "example" {
  # Example configuration for Domain SAML Options
  name = "example-domain_saml_options"

  # Common attributes
  tags = {
    Name        = "example-domain_saml_options"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Endpoint

```hcl
resource "aws_elasticsearch_vpc_endpoint" "example" {
  # Example configuration for VPC Endpoint
  name = "example-vpc_endpoint"

  # Common attributes
  tags = {
    Name        = "example-vpc_endpoint"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## elb

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| App Cookie Stickiness Policy | aws_app_cookie_stickiness_policy | SDK |
| Attachment | aws_elb_attachment | SDK |
| Backend Server Policy | aws_load_balancer_backend_server_policy | SDK |
| Classic Load Balancer | aws_elb | SDK |
| LB Cookie Stickiness Policy | aws_lb_cookie_stickiness_policy | SDK |
| Listener Policy | aws_load_balancer_listener_policy | SDK |
| Load Balancer Policy | aws_load_balancer_policy | SDK |
| Proxy Protocol Policy | aws_proxy_protocol_policy | SDK |
| SSL Negotiation Policy | aws_lb_ssl_negotiation_policy | SDK |


### Examples


#### App Cookie Stickiness Policy

```hcl
resource "aws_app_cookie_stickiness_policy" "example" {
  # Example configuration for App Cookie Stickiness Policy
  name = "example-app_cookie_stickiness_policy"

  # Common attributes
  tags = {
    Name        = "example-app_cookie_stickiness_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Attachment

```hcl
resource "aws_elb_attachment" "example" {
  # Example configuration for Attachment
  name = "example-attachment"

  # Common attributes
  tags = {
    Name        = "example-attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Backend Server Policy

```hcl
resource "aws_load_balancer_backend_server_policy" "example" {
  # Example configuration for Backend Server Policy
  name = "example-backend_server_policy"

  # Common attributes
  tags = {
    Name        = "example-backend_server_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Classic Load Balancer

```hcl
resource "aws_elb" "example" {
  # Example configuration for Classic Load Balancer
  name = "example-classic_load_balancer"

  # Common attributes
  tags = {
    Name        = "example-classic_load_balancer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### LB Cookie Stickiness Policy

```hcl
resource "aws_lb_cookie_stickiness_policy" "example" {
  # Example configuration for LB Cookie Stickiness Policy
  name = "example-lb_cookie_stickiness_policy"

  # Common attributes
  tags = {
    Name        = "example-lb_cookie_stickiness_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Listener Policy

```hcl
resource "aws_load_balancer_listener_policy" "example" {
  # Example configuration for Listener Policy
  name = "example-listener_policy"

  # Common attributes
  tags = {
    Name        = "example-listener_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Load Balancer Policy

```hcl
resource "aws_load_balancer_policy" "example" {
  # Example configuration for Load Balancer Policy
  name = "example-load_balancer_policy"

  # Common attributes
  tags = {
    Name        = "example-load_balancer_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Proxy Protocol Policy

```hcl
resource "aws_proxy_protocol_policy" "example" {
  # Example configuration for Proxy Protocol Policy
  name = "example-proxy_protocol_policy"

  # Common attributes
  tags = {
    Name        = "example-proxy_protocol_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### SSL Negotiation Policy

```hcl
resource "aws_lb_ssl_negotiation_policy" "example" {
  # Example configuration for SSL Negotiation Policy
  name = "example-ssl_negotiation_policy"

  # Common attributes
  tags = {
    Name        = "example-ssl_negotiation_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## elbv2

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Listener | aws_lb_listener | SDK |
| Listener Certificate | aws_lb_listener_certificate | SDK |
| Listener Rule | aws_lb_listener_rule | SDK |
| Load Balancer | aws_lb | SDK |
| Target Group | aws_lb_target_group | SDK |
| Target Group Attachment | aws_lb_target_group_attachment | SDK |
| Trust Store | aws_lb_trust_store | SDK |
| Trust Store Revocation | aws_lb_trust_store_revocation | SDK |


### Examples


#### Listener

```hcl
resource "aws_lb_listener" "example" {
  # Example configuration for Listener
  name = "example-listener"

  # Common attributes
  tags = {
    Name        = "example-listener"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Listener Certificate

```hcl
resource "aws_lb_listener_certificate" "example" {
  # Example configuration for Listener Certificate
  name = "example-listener_certificate"

  # Common attributes
  tags = {
    Name        = "example-listener_certificate"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Listener Rule

```hcl
resource "aws_lb_listener_rule" "example" {
  # Example configuration for Listener Rule
  name = "example-listener_rule"

  # Common attributes
  tags = {
    Name        = "example-listener_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Load Balancer

```hcl
resource "aws_lb" "example" {
  name               = "example-lb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.example.id]
  subnets            = [aws_subnet.example.id]
}
```


#### Target Group

```hcl
resource "aws_lb_target_group" "example" {
  # Example configuration for Target Group
  name = "example-target_group"

  # Common attributes
  tags = {
    Name        = "example-target_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Target Group Attachment

```hcl
resource "aws_lb_target_group_attachment" "example" {
  # Example configuration for Target Group Attachment
  name = "example-target_group_attachment"

  # Common attributes
  tags = {
    Name        = "example-target_group_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Trust Store

```hcl
resource "aws_lb_trust_store" "example" {
  # Example configuration for Trust Store
  name = "example-trust_store"

  # Common attributes
  tags = {
    Name        = "example-trust_store"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Trust Store Revocation

```hcl
resource "aws_lb_trust_store_revocation" "example" {
  # Example configuration for Trust Store Revocation
  name = "example-trust_store_revocation"

  # Common attributes
  tags = {
    Name        = "example-trust_store_revocation"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## emr

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Block Public Access Configuration | aws_emr_block_public_access_configuration | SDK |
| Cluster | aws_emr_cluster | SDK |
| Instance Fleet | aws_emr_instance_fleet | SDK |
| Instance Group | aws_emr_instance_group | SDK |
| Managed Scaling Policy | aws_emr_managed_scaling_policy | SDK |
| Security Configuration | aws_emr_security_configuration | SDK |
| Studio | aws_emr_studio | SDK |
| Studio Session Mapping | aws_emr_studio_session_mapping | SDK |


### Examples


#### Block Public Access Configuration

```hcl
resource "aws_emr_block_public_access_configuration" "example" {
  # Example configuration for Block Public Access Configuration
  name = "example-block_public_access_configuration"

  # Common attributes
  tags = {
    Name        = "example-block_public_access_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster

```hcl
resource "aws_emr_cluster" "example" {
  # Example configuration for Cluster
  name = "example-cluster"

  # Common attributes
  tags = {
    Name        = "example-cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Instance Fleet

```hcl
resource "aws_emr_instance_fleet" "example" {
  # Example configuration for Instance Fleet
  name = "example-instance_fleet"

  # Common attributes
  tags = {
    Name        = "example-instance_fleet"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Instance Group

```hcl
resource "aws_emr_instance_group" "example" {
  # Example configuration for Instance Group
  name = "example-instance_group"

  # Common attributes
  tags = {
    Name        = "example-instance_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Managed Scaling Policy

```hcl
resource "aws_emr_managed_scaling_policy" "example" {
  # Example configuration for Managed Scaling Policy
  name = "example-managed_scaling_policy"

  # Common attributes
  tags = {
    Name        = "example-managed_scaling_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Security Configuration

```hcl
resource "aws_emr_security_configuration" "example" {
  # Example configuration for Security Configuration
  name = "example-security_configuration"

  # Common attributes
  tags = {
    Name        = "example-security_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Studio

```hcl
resource "aws_emr_studio" "example" {
  # Example configuration for Studio
  name = "example-studio"

  # Common attributes
  tags = {
    Name        = "example-studio"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Studio Session Mapping

```hcl
resource "aws_emr_studio_session_mapping" "example" {
  # Example configuration for Studio Session Mapping
  name = "example-studio_session_mapping"

  # Common attributes
  tags = {
    Name        = "example-studio_session_mapping"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## emrcontainers

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Job Template | aws_emrcontainers_job_template | SDK |
| Virtual Cluster | aws_emrcontainers_virtual_cluster | SDK |


### Examples


#### Job Template

```hcl
resource "aws_emrcontainers_job_template" "example" {
  # Example configuration for Job Template
  name = "example-job_template"

  # Common attributes
  tags = {
    Name        = "example-job_template"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Virtual Cluster

```hcl
resource "aws_emrcontainers_virtual_cluster" "example" {
  # Example configuration for Virtual Cluster
  name = "example-virtual_cluster"

  # Common attributes
  tags = {
    Name        = "example-virtual_cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## emrserverless

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Application | aws_emrserverless_application | SDK |


### Examples


#### Application

```hcl
resource "aws_emrserverless_application" "example" {
  # Example configuration for Application
  name = "example-application"

  # Common attributes
  tags = {
    Name        = "example-application"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## events

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| API Destination | aws_cloudwatch_event_api_destination | SDK |
| Archive | aws_cloudwatch_event_archive | SDK |
| Connection | aws_cloudwatch_event_connection | SDK |
| Event Bus | aws_cloudwatch_event_bus | SDK |
| Event Bus Policy | aws_cloudwatch_event_bus_policy | SDK |
| Global Endpoint | aws_cloudwatch_event_endpoint | SDK |
| Permission | aws_cloudwatch_event_permission | SDK |
| Rule | aws_cloudwatch_event_rule | SDK |
| Target | aws_cloudwatch_event_target | SDK |


### Examples


#### API Destination

```hcl
resource "aws_cloudwatch_event_api_destination" "example" {
  # Example configuration for API Destination
  name = "example-api_destination"

  # Common attributes
  tags = {
    Name        = "example-api_destination"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Archive

```hcl
resource "aws_cloudwatch_event_archive" "example" {
  # Example configuration for Archive
  name = "example-archive"

  # Common attributes
  tags = {
    Name        = "example-archive"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Connection

```hcl
resource "aws_cloudwatch_event_connection" "example" {
  # Example configuration for Connection
  name = "example-connection"

  # Common attributes
  tags = {
    Name        = "example-connection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Event Bus

```hcl
resource "aws_cloudwatch_event_bus" "example" {
  # Example configuration for Event Bus
  name = "example-event_bus"

  # Common attributes
  tags = {
    Name        = "example-event_bus"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Event Bus Policy

```hcl
resource "aws_cloudwatch_event_bus_policy" "example" {
  # Example configuration for Event Bus Policy
  name = "example-event_bus_policy"

  # Common attributes
  tags = {
    Name        = "example-event_bus_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Global Endpoint

```hcl
resource "aws_cloudwatch_event_endpoint" "example" {
  # Example configuration for Global Endpoint
  name = "example-global_endpoint"

  # Common attributes
  tags = {
    Name        = "example-global_endpoint"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Permission

```hcl
resource "aws_cloudwatch_event_permission" "example" {
  # Example configuration for Permission
  name = "example-permission"

  # Common attributes
  tags = {
    Name        = "example-permission"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Rule

```hcl
resource "aws_cloudwatch_event_rule" "example" {
  # Example configuration for Rule
  name = "example-rule"

  # Common attributes
  tags = {
    Name        = "example-rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Target

```hcl
resource "aws_cloudwatch_event_target" "example" {
  # Example configuration for Target
  name = "example-target"

  # Common attributes
  tags = {
    Name        = "example-target"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## evidently

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Feature | aws_evidently_feature | SDK |
| Launch | aws_evidently_launch | SDK |
| Project | aws_evidently_project | SDK |
| Segment | aws_evidently_segment | SDK |


### Examples


#### Feature

```hcl
resource "aws_evidently_feature" "example" {
  # Example configuration for Feature
  name = "example-feature"

  # Common attributes
  tags = {
    Name        = "example-feature"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Launch

```hcl
resource "aws_evidently_launch" "example" {
  # Example configuration for Launch
  name = "example-launch"

  # Common attributes
  tags = {
    Name        = "example-launch"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Project

```hcl
resource "aws_evidently_project" "example" {
  # Example configuration for Project
  name = "example-project"

  # Common attributes
  tags = {
    Name        = "example-project"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Segment

```hcl
resource "aws_evidently_segment" "example" {
  # Example configuration for Segment
  name = "example-segment"

  # Common attributes
  tags = {
    Name        = "example-segment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## finspace

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Kx Cluster | aws_finspace_kx_cluster | SDK |
| Kx Database | aws_finspace_kx_database | SDK |
| Kx Dataview | aws_finspace_kx_dataview | SDK |
| Kx Environment | aws_finspace_kx_environment | SDK |
| Kx Scaling Group | aws_finspace_kx_scaling_group | SDK |
| Kx User | aws_finspace_kx_user | SDK |
| Kx Volume | aws_finspace_kx_volume | SDK |


### Examples


#### Kx Cluster

```hcl
resource "aws_finspace_kx_cluster" "example" {
  # Example configuration for Kx Cluster
  name = "example-kx_cluster"

  # Common attributes
  tags = {
    Name        = "example-kx_cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Kx Database

```hcl
resource "aws_finspace_kx_database" "example" {
  # Example configuration for Kx Database
  name = "example-kx_database"

  # Common attributes
  tags = {
    Name        = "example-kx_database"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Kx Dataview

```hcl
resource "aws_finspace_kx_dataview" "example" {
  # Example configuration for Kx Dataview
  name = "example-kx_dataview"

  # Common attributes
  tags = {
    Name        = "example-kx_dataview"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Kx Environment

```hcl
resource "aws_finspace_kx_environment" "example" {
  # Example configuration for Kx Environment
  name = "example-kx_environment"

  # Common attributes
  tags = {
    Name        = "example-kx_environment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Kx Scaling Group

```hcl
resource "aws_finspace_kx_scaling_group" "example" {
  # Example configuration for Kx Scaling Group
  name = "example-kx_scaling_group"

  # Common attributes
  tags = {
    Name        = "example-kx_scaling_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Kx User

```hcl
resource "aws_finspace_kx_user" "example" {
  # Example configuration for Kx User
  name = "example-kx_user"

  # Common attributes
  tags = {
    Name        = "example-kx_user"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Kx Volume

```hcl
resource "aws_finspace_kx_volume" "example" {
  # Example configuration for Kx Volume
  name = "example-kx_volume"

  # Common attributes
  tags = {
    Name        = "example-kx_volume"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## firehose

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Delivery Stream | aws_kinesis_firehose_delivery_stream | SDK |


### Examples


#### Delivery Stream

```hcl
resource "aws_kinesis_firehose_delivery_stream" "example" {
  # Example configuration for Delivery Stream
  name = "example-delivery_stream"

  # Common attributes
  tags = {
    Name        = "example-delivery_stream"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## fis

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Experiment Template | aws_fis_experiment_template | SDK |


### Examples


#### Experiment Template

```hcl
resource "aws_fis_experiment_template" "example" {
  # Example configuration for Experiment Template
  name = "example-experiment_template"

  # Common attributes
  tags = {
    Name        = "example-experiment_template"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## fms

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Admin Account | aws_fms_admin_account | SDK |
| Policy | aws_fms_policy | SDK |
| Resource Set | N/A | Framework |


### Examples


#### Admin Account

```hcl
resource "aws_fms_admin_account" "example" {
  # Example configuration for Admin Account
  name = "example-admin_account"

  # Common attributes
  tags = {
    Name        = "example-admin_account"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Policy

```hcl
resource "aws_fms_policy" "example" {
  # Example configuration for Policy
  name = "example-policy"

  # Common attributes
  tags = {
    Name        = "example-policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource Set

```hcl
resource "aws_fms_resource_set" "example" {
  # Example configuration for Resource Set
  name = "example-resource_set"

  # Common attributes
  tags = {
    Name        = "example-resource_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## fsx

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Backup | aws_fsx_backup | SDK |
| Data Repository Association | aws_fsx_data_repository_association | SDK |
| File Cache | aws_fsx_file_cache | SDK |
| Lustre File System | aws_fsx_lustre_file_system | SDK |
| ONTAP File System | aws_fsx_ontap_file_system | SDK |
| ONTAP Storage Virtual Machine | aws_fsx_ontap_storage_virtual_machine | SDK |
| ONTAP Volume | aws_fsx_ontap_volume | SDK |
| OpenZFS File System | aws_fsx_openzfs_file_system | SDK |
| OpenZFS Snapshot | aws_fsx_openzfs_snapshot | SDK |
| OpenZFS Volume | aws_fsx_openzfs_volume | SDK |
| Windows File System | aws_fsx_windows_file_system | SDK |


### Examples


#### Backup

```hcl
resource "aws_fsx_backup" "example" {
  # Example configuration for Backup
  name = "example-backup"

  # Common attributes
  tags = {
    Name        = "example-backup"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Data Repository Association

```hcl
resource "aws_fsx_data_repository_association" "example" {
  # Example configuration for Data Repository Association
  name = "example-data_repository_association"

  # Common attributes
  tags = {
    Name        = "example-data_repository_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### File Cache

```hcl
resource "aws_fsx_file_cache" "example" {
  # Example configuration for File Cache
  name = "example-file_cache"

  # Common attributes
  tags = {
    Name        = "example-file_cache"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Lustre File System

```hcl
resource "aws_fsx_lustre_file_system" "example" {
  # Example configuration for Lustre File System
  name = "example-lustre_file_system"

  # Common attributes
  tags = {
    Name        = "example-lustre_file_system"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### ONTAP File System

```hcl
resource "aws_fsx_ontap_file_system" "example" {
  # Example configuration for ONTAP File System
  name = "example-ontap_file_system"

  # Common attributes
  tags = {
    Name        = "example-ontap_file_system"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### ONTAP Storage Virtual Machine

```hcl
resource "aws_fsx_ontap_storage_virtual_machine" "example" {
  # Example configuration for ONTAP Storage Virtual Machine
  name = "example-ontap_storage_virtual_machine"

  # Common attributes
  tags = {
    Name        = "example-ontap_storage_virtual_machine"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### ONTAP Volume

```hcl
resource "aws_fsx_ontap_volume" "example" {
  # Example configuration for ONTAP Volume
  name = "example-ontap_volume"

  # Common attributes
  tags = {
    Name        = "example-ontap_volume"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### OpenZFS File System

```hcl
resource "aws_fsx_openzfs_file_system" "example" {
  # Example configuration for OpenZFS File System
  name = "example-openzfs_file_system"

  # Common attributes
  tags = {
    Name        = "example-openzfs_file_system"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### OpenZFS Snapshot

```hcl
resource "aws_fsx_openzfs_snapshot" "example" {
  # Example configuration for OpenZFS Snapshot
  name = "example-openzfs_snapshot"

  # Common attributes
  tags = {
    Name        = "example-openzfs_snapshot"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### OpenZFS Volume

```hcl
resource "aws_fsx_openzfs_volume" "example" {
  # Example configuration for OpenZFS Volume
  name = "example-openzfs_volume"

  # Common attributes
  tags = {
    Name        = "example-openzfs_volume"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Windows File System

```hcl
resource "aws_fsx_windows_file_system" "example" {
  # Example configuration for Windows File System
  name = "example-windows_file_system"

  # Common attributes
  tags = {
    Name        = "example-windows_file_system"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## gamelift

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Alias | aws_gamelift_alias | SDK |
| Build | aws_gamelift_build | SDK |
| Fleet | aws_gamelift_fleet | SDK |
| Game Server Group | aws_gamelift_game_server_group | SDK |
| Game Session Queue | aws_gamelift_game_session_queue | SDK |
| Script | aws_gamelift_script | SDK |


### Examples


#### Alias

```hcl
resource "aws_gamelift_alias" "example" {
  # Example configuration for Alias
  name = "example-alias"

  # Common attributes
  tags = {
    Name        = "example-alias"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Build

```hcl
resource "aws_gamelift_build" "example" {
  # Example configuration for Build
  name = "example-build"

  # Common attributes
  tags = {
    Name        = "example-build"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Fleet

```hcl
resource "aws_gamelift_fleet" "example" {
  # Example configuration for Fleet
  name = "example-fleet"

  # Common attributes
  tags = {
    Name        = "example-fleet"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Game Server Group

```hcl
resource "aws_gamelift_game_server_group" "example" {
  # Example configuration for Game Server Group
  name = "example-game_server_group"

  # Common attributes
  tags = {
    Name        = "example-game_server_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Game Session Queue

```hcl
resource "aws_gamelift_game_session_queue" "example" {
  # Example configuration for Game Session Queue
  name = "example-game_session_queue"

  # Common attributes
  tags = {
    Name        = "example-game_session_queue"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Script

```hcl
resource "aws_gamelift_script" "example" {
  # Example configuration for Script
  name = "example-script"

  # Common attributes
  tags = {
    Name        = "example-script"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## glacier

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Vault | aws_glacier_vault | SDK |


### Examples


#### Vault

```hcl
resource "aws_glacier_vault" "example" {
  # Example configuration for Vault
  name = "example-vault"

  # Common attributes
  tags = {
    Name        = "example-vault"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## globalaccelerator

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Accelerator | aws_globalaccelerator_accelerator | SDK |
| Cross-account Attachment | N/A | Framework |
| Custom Routing Accelerator | aws_globalaccelerator_custom_routing_accelerator | SDK |
| Custom Routing Endpoint Group | aws_globalaccelerator_custom_routing_endpoint_group | SDK |
| Custom Routing Listener | aws_globalaccelerator_custom_routing_listener | SDK |
| Endpoint Group | aws_globalaccelerator_endpoint_group | SDK |
| Listener | aws_globalaccelerator_listener | SDK |


### Examples


#### Accelerator

```hcl
resource "aws_globalaccelerator_accelerator" "example" {
  # Example configuration for Accelerator
  name = "example-accelerator"

  # Common attributes
  tags = {
    Name        = "example-accelerator"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cross-account Attachment

```hcl
resource "aws_globalaccelerator_cross-account_attachment" "example" {
  # Example configuration for Cross-account Attachment
  name = "example-cross-account_attachment"

  # Common attributes
  tags = {
    Name        = "example-cross-account_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Custom Routing Accelerator

```hcl
resource "aws_globalaccelerator_custom_routing_accelerator" "example" {
  # Example configuration for Custom Routing Accelerator
  name = "example-custom_routing_accelerator"

  # Common attributes
  tags = {
    Name        = "example-custom_routing_accelerator"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Custom Routing Endpoint Group

```hcl
resource "aws_globalaccelerator_custom_routing_endpoint_group" "example" {
  # Example configuration for Custom Routing Endpoint Group
  name = "example-custom_routing_endpoint_group"

  # Common attributes
  tags = {
    Name        = "example-custom_routing_endpoint_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Custom Routing Listener

```hcl
resource "aws_globalaccelerator_custom_routing_listener" "example" {
  # Example configuration for Custom Routing Listener
  name = "example-custom_routing_listener"

  # Common attributes
  tags = {
    Name        = "example-custom_routing_listener"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Endpoint Group

```hcl
resource "aws_globalaccelerator_endpoint_group" "example" {
  # Example configuration for Endpoint Group
  name = "example-endpoint_group"

  # Common attributes
  tags = {
    Name        = "example-endpoint_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Listener

```hcl
resource "aws_globalaccelerator_listener" "example" {
  # Example configuration for Listener
  name = "example-listener"

  # Common attributes
  tags = {
    Name        = "example-listener"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## glue

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Catalog Table Optimizer | N/A | Framework |
| Connection | aws_glue_connection | SDK |
| Crawler | aws_glue_crawler | SDK |
| Data Quality Ruleset | aws_glue_data_quality_ruleset | SDK |
| Database | aws_glue_catalog_database | SDK |
| Dev Endpoint | aws_glue_dev_endpoint | SDK |
| Job | aws_glue_job | SDK |
| ML Transform | aws_glue_ml_transform | SDK |
| Registry | aws_glue_registry | SDK |
| Schema | aws_glue_schema | SDK |
| Trigger | aws_glue_trigger | SDK |
| Workflow | aws_glue_workflow | SDK |


### Examples


#### Catalog Table Optimizer

```hcl
resource "aws_glue_catalog_table_optimizer" "example" {
  # Example configuration for Catalog Table Optimizer
  name = "example-catalog_table_optimizer"

  # Common attributes
  tags = {
    Name        = "example-catalog_table_optimizer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Connection

```hcl
resource "aws_glue_connection" "example" {
  # Example configuration for Connection
  name = "example-connection"

  # Common attributes
  tags = {
    Name        = "example-connection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Crawler

```hcl
resource "aws_glue_crawler" "example" {
  # Example configuration for Crawler
  name = "example-crawler"

  # Common attributes
  tags = {
    Name        = "example-crawler"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Data Quality Ruleset

```hcl
resource "aws_glue_data_quality_ruleset" "example" {
  # Example configuration for Data Quality Ruleset
  name = "example-data_quality_ruleset"

  # Common attributes
  tags = {
    Name        = "example-data_quality_ruleset"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Database

```hcl
resource "aws_glue_catalog_database" "example" {
  # Example configuration for Database
  name = "example-database"

  # Common attributes
  tags = {
    Name        = "example-database"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Dev Endpoint

```hcl
resource "aws_glue_dev_endpoint" "example" {
  # Example configuration for Dev Endpoint
  name = "example-dev_endpoint"

  # Common attributes
  tags = {
    Name        = "example-dev_endpoint"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Job

```hcl
resource "aws_glue_job" "example" {
  # Example configuration for Job
  name = "example-job"

  # Common attributes
  tags = {
    Name        = "example-job"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### ML Transform

```hcl
resource "aws_glue_ml_transform" "example" {
  # Example configuration for ML Transform
  name = "example-ml_transform"

  # Common attributes
  tags = {
    Name        = "example-ml_transform"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Registry

```hcl
resource "aws_glue_registry" "example" {
  # Example configuration for Registry
  name = "example-registry"

  # Common attributes
  tags = {
    Name        = "example-registry"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Schema

```hcl
resource "aws_glue_schema" "example" {
  # Example configuration for Schema
  name = "example-schema"

  # Common attributes
  tags = {
    Name        = "example-schema"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Trigger

```hcl
resource "aws_glue_trigger" "example" {
  # Example configuration for Trigger
  name = "example-trigger"

  # Common attributes
  tags = {
    Name        = "example-trigger"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Workflow

```hcl
resource "aws_glue_workflow" "example" {
  # Example configuration for Workflow
  name = "example-workflow"

  # Common attributes
  tags = {
    Name        = "example-workflow"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## grafana

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Grafana Workspace SAML Configuration | aws_grafana_workspace_saml_configuration | SDK |
| License Association | aws_grafana_license_association | SDK |
| Workspace | aws_grafana_workspace | SDK |
| Workspace API Key | aws_grafana_workspace_api_key | SDK |
| Workspace Role Association | aws_grafana_role_association | SDK |
| Workspace Service Account | N/A | Framework |
| Workspace Service Account Token | N/A | Framework |


### Examples


#### Grafana Workspace SAML Configuration

```hcl
resource "aws_grafana_workspace_saml_configuration" "example" {
  # Example configuration for Grafana Workspace SAML Configuration
  name = "example-grafana_workspace_saml_configuration"

  # Common attributes
  tags = {
    Name        = "example-grafana_workspace_saml_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### License Association

```hcl
resource "aws_grafana_license_association" "example" {
  # Example configuration for License Association
  name = "example-license_association"

  # Common attributes
  tags = {
    Name        = "example-license_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Workspace

```hcl
resource "aws_grafana_workspace" "example" {
  # Example configuration for Workspace
  name = "example-workspace"

  # Common attributes
  tags = {
    Name        = "example-workspace"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Workspace API Key

```hcl
resource "aws_grafana_workspace_api_key" "example" {
  # Example configuration for Workspace API Key
  name = "example-workspace_api_key"

  # Common attributes
  tags = {
    Name        = "example-workspace_api_key"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Workspace Role Association

```hcl
resource "aws_grafana_role_association" "example" {
  # Example configuration for Workspace Role Association
  name = "example-workspace_role_association"

  # Common attributes
  tags = {
    Name        = "example-workspace_role_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Workspace Service Account

```hcl
resource "aws_grafana_workspace_service_account" "example" {
  # Example configuration for Workspace Service Account
  name = "example-workspace_service_account"

  # Common attributes
  tags = {
    Name        = "example-workspace_service_account"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Workspace Service Account Token

```hcl
resource "aws_grafana_workspace_service_account_token" "example" {
  # Example configuration for Workspace Service Account Token
  name = "example-workspace_service_account_token"

  # Common attributes
  tags = {
    Name        = "example-workspace_service_account_token"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## guardduty

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Detector | aws_guardduty_detector | SDK |
| Detector Feature | aws_guardduty_detector_feature | SDK |
| Filter | aws_guardduty_filter | SDK |
| IP Set | aws_guardduty_ipset | SDK |
| Invite Accepter | aws_guardduty_invite_accepter | SDK |
| Malware Protection Plan | N/A | Framework |
| Organization Configuration | aws_guardduty_organization_configuration | SDK |
| Organization Configuration Feature | aws_guardduty_organization_configuration_feature | SDK |
| Threat Intel Set | aws_guardduty_threatintelset | SDK |


### Examples


#### Detector

```hcl
resource "aws_guardduty_detector" "example" {
  # Example configuration for Detector
  name = "example-detector"

  # Common attributes
  tags = {
    Name        = "example-detector"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Detector Feature

```hcl
resource "aws_guardduty_detector_feature" "example" {
  # Example configuration for Detector Feature
  name = "example-detector_feature"

  # Common attributes
  tags = {
    Name        = "example-detector_feature"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Filter

```hcl
resource "aws_guardduty_filter" "example" {
  # Example configuration for Filter
  name = "example-filter"

  # Common attributes
  tags = {
    Name        = "example-filter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### IP Set

```hcl
resource "aws_guardduty_ipset" "example" {
  # Example configuration for IP Set
  name = "example-ip_set"

  # Common attributes
  tags = {
    Name        = "example-ip_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Invite Accepter

```hcl
resource "aws_guardduty_invite_accepter" "example" {
  # Example configuration for Invite Accepter
  name = "example-invite_accepter"

  # Common attributes
  tags = {
    Name        = "example-invite_accepter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Malware Protection Plan

```hcl
resource "aws_guardduty_malware_protection_plan" "example" {
  # Example configuration for Malware Protection Plan
  name = "example-malware_protection_plan"

  # Common attributes
  tags = {
    Name        = "example-malware_protection_plan"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Organization Configuration

```hcl
resource "aws_guardduty_organization_configuration" "example" {
  # Example configuration for Organization Configuration
  name = "example-organization_configuration"

  # Common attributes
  tags = {
    Name        = "example-organization_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Organization Configuration Feature

```hcl
resource "aws_guardduty_organization_configuration_feature" "example" {
  # Example configuration for Organization Configuration Feature
  name = "example-organization_configuration_feature"

  # Common attributes
  tags = {
    Name        = "example-organization_configuration_feature"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Threat Intel Set

```hcl
resource "aws_guardduty_threatintelset" "example" {
  # Example configuration for Threat Intel Set
  name = "example-threat_intel_set"

  # Common attributes
  tags = {
    Name        = "example-threat_intel_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## iam

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Access Key | aws_iam_access_key | SDK |
| Account Alias | aws_iam_account_alias | SDK |
| Account Password Policy | aws_iam_account_password_policy | SDK |
| Group | aws_iam_group | SDK |
| Group Membership | aws_iam_group_membership | SDK |
| Group Policies Exclusive | N/A | Framework |
| Group Policy | aws_iam_group_policy | SDK |
| Group Policy Attachment | aws_iam_group_policy_attachment | SDK |
| Group Policy Attachments Exclusive | N/A | Framework |
| Instance Profile | aws_iam_instance_profile | SDK |
| OIDC Provider | aws_iam_openid_connect_provider | SDK |
| Organizations Features | N/A | Framework |
| Policy | aws_iam_policy | SDK |
| Policy Attachment | aws_iam_policy_attachment | SDK |
| Role | aws_iam_role | SDK |
| Role Policies Exclusive | N/A | Framework |
| Role Policy | aws_iam_role_policy | SDK |
| Role Policy Attachment | aws_iam_role_policy_attachment | SDK |
| Role Policy Attachments Exclusive | N/A | Framework |
| SAML Provider | aws_iam_saml_provider | SDK |
| Security Token Service Preferences | aws_iam_security_token_service_preferences | SDK |
| Server Certificate | aws_iam_server_certificate | SDK |
| Service Linked Role | aws_iam_service_linked_role | SDK |
| Service Specific Credential | aws_iam_service_specific_credential | SDK |
| Signing Certificate | aws_iam_signing_certificate | SDK |
| User | aws_iam_user | SDK |
| User Group Membership | aws_iam_user_group_membership | SDK |
| User Login Profile | aws_iam_user_login_profile | SDK |
| User Policies Exclusive | N/A | Framework |
| User Policy | aws_iam_user_policy | SDK |
| User Policy Attachment | aws_iam_user_policy_attachment | SDK |
| User Policy Attachments Exclusive | N/A | Framework |
| User SSH Key | aws_iam_user_ssh_key | SDK |
| Virtual MFA Device | aws_iam_virtual_mfa_device | SDK |


### Examples


#### Access Key

```hcl
resource "aws_iam_access_key" "example" {
  # Example configuration for Access Key
  name = "example-access_key"

  # Common attributes
  tags = {
    Name        = "example-access_key"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Account Alias

```hcl
resource "aws_iam_account_alias" "example" {
  # Example configuration for Account Alias
  name = "example-account_alias"

  # Common attributes
  tags = {
    Name        = "example-account_alias"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Account Password Policy

```hcl
resource "aws_iam_account_password_policy" "example" {
  # Example configuration for Account Password Policy
  name = "example-account_password_policy"

  # Common attributes
  tags = {
    Name        = "example-account_password_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Group

```hcl
resource "aws_iam_group" "example" {
  # Example configuration for Group
  name = "example-group"

  # Common attributes
  tags = {
    Name        = "example-group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Group Membership

```hcl
resource "aws_iam_group_membership" "example" {
  # Example configuration for Group Membership
  name = "example-group_membership"

  # Common attributes
  tags = {
    Name        = "example-group_membership"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Group Policies Exclusive

```hcl
resource "aws_iam_group_policies_exclusive" "example" {
  # Example configuration for Group Policies Exclusive
  name = "example-group_policies_exclusive"

  # Common attributes
  tags = {
    Name        = "example-group_policies_exclusive"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Group Policy

```hcl
resource "aws_iam_group_policy" "example" {
  # Example configuration for Group Policy
  name = "example-group_policy"

  # Common attributes
  tags = {
    Name        = "example-group_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Group Policy Attachment

```hcl
resource "aws_iam_group_policy_attachment" "example" {
  # Example configuration for Group Policy Attachment
  name = "example-group_policy_attachment"

  # Common attributes
  tags = {
    Name        = "example-group_policy_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Group Policy Attachments Exclusive

```hcl
resource "aws_iam_group_policy_attachments_exclusive" "example" {
  # Example configuration for Group Policy Attachments Exclusive
  name = "example-group_policy_attachments_exclusive"

  # Common attributes
  tags = {
    Name        = "example-group_policy_attachments_exclusive"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Instance Profile

```hcl
resource "aws_iam_instance_profile" "example" {
  # Example configuration for Instance Profile
  name = "example-instance_profile"

  # Common attributes
  tags = {
    Name        = "example-instance_profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### OIDC Provider

```hcl
resource "aws_iam_openid_connect_provider" "example" {
  # Example configuration for OIDC Provider
  name = "example-oidc_provider"

  # Common attributes
  tags = {
    Name        = "example-oidc_provider"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Organizations Features

```hcl
resource "aws_iam_organizations_features" "example" {
  # Example configuration for Organizations Features
  name = "example-organizations_features"

  # Common attributes
  tags = {
    Name        = "example-organizations_features"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Policy

```hcl
resource "aws_iam_policy" "example" {
  name        = "example-policy"
  description = "Example policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "ec2:Describe*",
        ]
        Effect   = "Allow"
        Resource = "*"
      }
    ]
  })
}
```


#### Policy Attachment

```hcl
resource "aws_iam_policy_attachment" "example" {
  # Example configuration for Policy Attachment
  name = "example-policy_attachment"

  # Common attributes
  tags = {
    Name        = "example-policy_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Role

```hcl
resource "aws_iam_role" "example" {
  name = "example-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      }
    ]
  })
}
```


#### Role Policies Exclusive

```hcl
resource "aws_iam_role_policies_exclusive" "example" {
  # Example configuration for Role Policies Exclusive
  name = "example-role_policies_exclusive"

  # Common attributes
  tags = {
    Name        = "example-role_policies_exclusive"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Role Policy

```hcl
resource "aws_iam_role_policy" "example" {
  # Example configuration for Role Policy
  name = "example-role_policy"

  # Common attributes
  tags = {
    Name        = "example-role_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Role Policy Attachment

```hcl
resource "aws_iam_role_policy_attachment" "example" {
  # Example configuration for Role Policy Attachment
  name = "example-role_policy_attachment"

  # Common attributes
  tags = {
    Name        = "example-role_policy_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Role Policy Attachments Exclusive

```hcl
resource "aws_iam_role_policy_attachments_exclusive" "example" {
  # Example configuration for Role Policy Attachments Exclusive
  name = "example-role_policy_attachments_exclusive"

  # Common attributes
  tags = {
    Name        = "example-role_policy_attachments_exclusive"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### SAML Provider

```hcl
resource "aws_iam_saml_provider" "example" {
  # Example configuration for SAML Provider
  name = "example-saml_provider"

  # Common attributes
  tags = {
    Name        = "example-saml_provider"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Security Token Service Preferences

```hcl
resource "aws_iam_security_token_service_preferences" "example" {
  # Example configuration for Security Token Service Preferences
  name = "example-security_token_service_preferences"

  # Common attributes
  tags = {
    Name        = "example-security_token_service_preferences"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Server Certificate

```hcl
resource "aws_iam_server_certificate" "example" {
  # Example configuration for Server Certificate
  name = "example-server_certificate"

  # Common attributes
  tags = {
    Name        = "example-server_certificate"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Service Linked Role

```hcl
resource "aws_iam_service_linked_role" "example" {
  # Example configuration for Service Linked Role
  name = "example-service_linked_role"

  # Common attributes
  tags = {
    Name        = "example-service_linked_role"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Service Specific Credential

```hcl
resource "aws_iam_service_specific_credential" "example" {
  # Example configuration for Service Specific Credential
  name = "example-service_specific_credential"

  # Common attributes
  tags = {
    Name        = "example-service_specific_credential"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Signing Certificate

```hcl
resource "aws_iam_signing_certificate" "example" {
  # Example configuration for Signing Certificate
  name = "example-signing_certificate"

  # Common attributes
  tags = {
    Name        = "example-signing_certificate"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User

```hcl
resource "aws_iam_user" "example" {
  # Example configuration for User
  name = "example-user"

  # Common attributes
  tags = {
    Name        = "example-user"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User Group Membership

```hcl
resource "aws_iam_user_group_membership" "example" {
  # Example configuration for User Group Membership
  name = "example-user_group_membership"

  # Common attributes
  tags = {
    Name        = "example-user_group_membership"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User Login Profile

```hcl
resource "aws_iam_user_login_profile" "example" {
  # Example configuration for User Login Profile
  name = "example-user_login_profile"

  # Common attributes
  tags = {
    Name        = "example-user_login_profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User Policies Exclusive

```hcl
resource "aws_iam_user_policies_exclusive" "example" {
  # Example configuration for User Policies Exclusive
  name = "example-user_policies_exclusive"

  # Common attributes
  tags = {
    Name        = "example-user_policies_exclusive"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User Policy

```hcl
resource "aws_iam_user_policy" "example" {
  # Example configuration for User Policy
  name = "example-user_policy"

  # Common attributes
  tags = {
    Name        = "example-user_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User Policy Attachment

```hcl
resource "aws_iam_user_policy_attachment" "example" {
  # Example configuration for User Policy Attachment
  name = "example-user_policy_attachment"

  # Common attributes
  tags = {
    Name        = "example-user_policy_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User Policy Attachments Exclusive

```hcl
resource "aws_iam_user_policy_attachments_exclusive" "example" {
  # Example configuration for User Policy Attachments Exclusive
  name = "example-user_policy_attachments_exclusive"

  # Common attributes
  tags = {
    Name        = "example-user_policy_attachments_exclusive"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User SSH Key

```hcl
resource "aws_iam_user_ssh_key" "example" {
  # Example configuration for User SSH Key
  name = "example-user_ssh_key"

  # Common attributes
  tags = {
    Name        = "example-user_ssh_key"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Virtual MFA Device

```hcl
resource "aws_iam_virtual_mfa_device" "example" {
  # Example configuration for Virtual MFA Device
  name = "example-virtual_mfa_device"

  # Common attributes
  tags = {
    Name        = "example-virtual_mfa_device"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## identitystore

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Group | aws_identitystore_group | SDK |
| Group Membership | aws_identitystore_group_membership | SDK |
| User | aws_identitystore_user | SDK |


### Examples


#### Group

```hcl
resource "aws_identitystore_group" "example" {
  # Example configuration for Group
  name = "example-group"

  # Common attributes
  tags = {
    Name        = "example-group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Group Membership

```hcl
resource "aws_identitystore_group_membership" "example" {
  # Example configuration for Group Membership
  name = "example-group_membership"

  # Common attributes
  tags = {
    Name        = "example-group_membership"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User

```hcl
resource "aws_identitystore_user" "example" {
  # Example configuration for User
  name = "example-user"

  # Common attributes
  tags = {
    Name        = "example-user"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## imagebuilder

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Component | aws_imagebuilder_component | SDK |
| Container Recipe | aws_imagebuilder_container_recipe | SDK |
| Distribution Configuration | aws_imagebuilder_distribution_configuration | SDK |
| Image | aws_imagebuilder_image | SDK |
| Image Pipeline | aws_imagebuilder_image_pipeline | SDK |
| Image Recipe | aws_imagebuilder_image_recipe | SDK |
| Infrastructure Configuration | aws_imagebuilder_infrastructure_configuration | SDK |
| Lifecycle Policy | N/A | Framework |
| Workflow | aws_imagebuilder_workflow | SDK |


### Examples


#### Component

```hcl
resource "aws_imagebuilder_component" "example" {
  # Example configuration for Component
  name = "example-component"

  # Common attributes
  tags = {
    Name        = "example-component"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Container Recipe

```hcl
resource "aws_imagebuilder_container_recipe" "example" {
  # Example configuration for Container Recipe
  name = "example-container_recipe"

  # Common attributes
  tags = {
    Name        = "example-container_recipe"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Distribution Configuration

```hcl
resource "aws_imagebuilder_distribution_configuration" "example" {
  # Example configuration for Distribution Configuration
  name = "example-distribution_configuration"

  # Common attributes
  tags = {
    Name        = "example-distribution_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Image

```hcl
resource "aws_imagebuilder_image" "example" {
  # Example configuration for Image
  name = "example-image"

  # Common attributes
  tags = {
    Name        = "example-image"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Image Pipeline

```hcl
resource "aws_imagebuilder_image_pipeline" "example" {
  # Example configuration for Image Pipeline
  name = "example-image_pipeline"

  # Common attributes
  tags = {
    Name        = "example-image_pipeline"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Image Recipe

```hcl
resource "aws_imagebuilder_image_recipe" "example" {
  # Example configuration for Image Recipe
  name = "example-image_recipe"

  # Common attributes
  tags = {
    Name        = "example-image_recipe"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Infrastructure Configuration

```hcl
resource "aws_imagebuilder_infrastructure_configuration" "example" {
  # Example configuration for Infrastructure Configuration
  name = "example-infrastructure_configuration"

  # Common attributes
  tags = {
    Name        = "example-infrastructure_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Lifecycle Policy

```hcl
resource "aws_imagebuilder_lifecycle_policy" "example" {
  # Example configuration for Lifecycle Policy
  name = "example-lifecycle_policy"

  # Common attributes
  tags = {
    Name        = "example-lifecycle_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Workflow

```hcl
resource "aws_imagebuilder_workflow" "example" {
  # Example configuration for Workflow
  name = "example-workflow"

  # Common attributes
  tags = {
    Name        = "example-workflow"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## inspector

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Assessment Template | aws_inspector_assessment_template | SDK |


### Examples


#### Assessment Template

```hcl
resource "aws_inspector_assessment_template" "example" {
  # Example configuration for Assessment Template
  name = "example-assessment_template"

  # Common attributes
  tags = {
    Name        = "example-assessment_template"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## inspector2

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Delegated Admin Account | aws_inspector2_delegated_admin_account | SDK |
| Member Association | aws_inspector2_member_association | SDK |
| Organization Configuration | aws_inspector2_organization_configuration | SDK |


### Examples


#### Delegated Admin Account

```hcl
resource "aws_inspector2_delegated_admin_account" "example" {
  # Example configuration for Delegated Admin Account
  name = "example-delegated_admin_account"

  # Common attributes
  tags = {
    Name        = "example-delegated_admin_account"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Member Association

```hcl
resource "aws_inspector2_member_association" "example" {
  # Example configuration for Member Association
  name = "example-member_association"

  # Common attributes
  tags = {
    Name        = "example-member_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Organization Configuration

```hcl
resource "aws_inspector2_organization_configuration" "example" {
  # Example configuration for Organization Configuration
  name = "example-organization_configuration"

  # Common attributes
  tags = {
    Name        = "example-organization_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## internetmonitor

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Monitor | aws_internetmonitor_monitor | SDK |


### Examples


#### Monitor

```hcl
resource "aws_internetmonitor_monitor" "example" {
  # Example configuration for Monitor
  name = "example-monitor"

  # Common attributes
  tags = {
    Name        = "example-monitor"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## iot

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Authorizer | aws_iot_authorizer | SDK |
| Billing Group | N/A | Framework |
| CA Certificate | aws_iot_ca_certificate | SDK |
| Certificate | aws_iot_certificate | SDK |
| Domain Configuration | aws_iot_domain_configuration | SDK |
| Event Configurations | aws_iot_event_configurations | SDK |
| Indexing Configuration | aws_iot_indexing_configuration | SDK |
| Logging Options | aws_iot_logging_options | SDK |
| Policy | aws_iot_policy | SDK |
| Provisioning Template | aws_iot_provisioning_template | SDK |
| Role Alias | aws_iot_role_alias | SDK |
| Thing | aws_iot_thing | SDK |
| Thing Group | aws_iot_thing_group | SDK |
| Thing Group Membership | aws_iot_thing_group_membership | SDK |
| Thing Principal Attachment | aws_iot_thing_principal_attachment | SDK |
| Thing Type | aws_iot_thing_type | SDK |
| Topic Rule | aws_iot_topic_rule | SDK |
| Topic Rule Destination | aws_iot_topic_rule_destination | SDK |


### Examples


#### Authorizer

```hcl
resource "aws_iot_authorizer" "example" {
  # Example configuration for Authorizer
  name = "example-authorizer"

  # Common attributes
  tags = {
    Name        = "example-authorizer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Billing Group

```hcl
resource "aws_iot_billing_group" "example" {
  # Example configuration for Billing Group
  name = "example-billing_group"

  # Common attributes
  tags = {
    Name        = "example-billing_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### CA Certificate

```hcl
resource "aws_iot_ca_certificate" "example" {
  # Example configuration for CA Certificate
  name = "example-ca_certificate"

  # Common attributes
  tags = {
    Name        = "example-ca_certificate"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Certificate

```hcl
resource "aws_iot_certificate" "example" {
  # Example configuration for Certificate
  name = "example-certificate"

  # Common attributes
  tags = {
    Name        = "example-certificate"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain Configuration

```hcl
resource "aws_iot_domain_configuration" "example" {
  # Example configuration for Domain Configuration
  name = "example-domain_configuration"

  # Common attributes
  tags = {
    Name        = "example-domain_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Event Configurations

```hcl
resource "aws_iot_event_configurations" "example" {
  # Example configuration for Event Configurations
  name = "example-event_configurations"

  # Common attributes
  tags = {
    Name        = "example-event_configurations"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Indexing Configuration

```hcl
resource "aws_iot_indexing_configuration" "example" {
  # Example configuration for Indexing Configuration
  name = "example-indexing_configuration"

  # Common attributes
  tags = {
    Name        = "example-indexing_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Logging Options

```hcl
resource "aws_iot_logging_options" "example" {
  # Example configuration for Logging Options
  name = "example-logging_options"

  # Common attributes
  tags = {
    Name        = "example-logging_options"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Policy

```hcl
resource "aws_iot_policy" "example" {
  # Example configuration for Policy
  name = "example-policy"

  # Common attributes
  tags = {
    Name        = "example-policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Provisioning Template

```hcl
resource "aws_iot_provisioning_template" "example" {
  # Example configuration for Provisioning Template
  name = "example-provisioning_template"

  # Common attributes
  tags = {
    Name        = "example-provisioning_template"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Role Alias

```hcl
resource "aws_iot_role_alias" "example" {
  # Example configuration for Role Alias
  name = "example-role_alias"

  # Common attributes
  tags = {
    Name        = "example-role_alias"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Thing

```hcl
resource "aws_iot_thing" "example" {
  # Example configuration for Thing
  name = "example-thing"

  # Common attributes
  tags = {
    Name        = "example-thing"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Thing Group

```hcl
resource "aws_iot_thing_group" "example" {
  # Example configuration for Thing Group
  name = "example-thing_group"

  # Common attributes
  tags = {
    Name        = "example-thing_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Thing Group Membership

```hcl
resource "aws_iot_thing_group_membership" "example" {
  # Example configuration for Thing Group Membership
  name = "example-thing_group_membership"

  # Common attributes
  tags = {
    Name        = "example-thing_group_membership"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Thing Principal Attachment

```hcl
resource "aws_iot_thing_principal_attachment" "example" {
  # Example configuration for Thing Principal Attachment
  name = "example-thing_principal_attachment"

  # Common attributes
  tags = {
    Name        = "example-thing_principal_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Thing Type

```hcl
resource "aws_iot_thing_type" "example" {
  # Example configuration for Thing Type
  name = "example-thing_type"

  # Common attributes
  tags = {
    Name        = "example-thing_type"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Topic Rule

```hcl
resource "aws_iot_topic_rule" "example" {
  # Example configuration for Topic Rule
  name = "example-topic_rule"

  # Common attributes
  tags = {
    Name        = "example-topic_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Topic Rule Destination

```hcl
resource "aws_iot_topic_rule_destination" "example" {
  # Example configuration for Topic Rule Destination
  name = "example-topic_rule_destination"

  # Common attributes
  tags = {
    Name        = "example-topic_rule_destination"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## ivs

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Channel | aws_ivs_channel | SDK |
| Playback Key Pair | aws_ivs_playback_key_pair | SDK |
| Recording Configuration | aws_ivs_recording_configuration | SDK |


### Examples


#### Channel

```hcl
resource "aws_ivs_channel" "example" {
  # Example configuration for Channel
  name = "example-channel"

  # Common attributes
  tags = {
    Name        = "example-channel"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Playback Key Pair

```hcl
resource "aws_ivs_playback_key_pair" "example" {
  # Example configuration for Playback Key Pair
  name = "example-playback_key_pair"

  # Common attributes
  tags = {
    Name        = "example-playback_key_pair"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Recording Configuration

```hcl
resource "aws_ivs_recording_configuration" "example" {
  # Example configuration for Recording Configuration
  name = "example-recording_configuration"

  # Common attributes
  tags = {
    Name        = "example-recording_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## ivschat

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Logging Configuration | aws_ivschat_logging_configuration | SDK |
| Room | aws_ivschat_room | SDK |


### Examples


#### Logging Configuration

```hcl
resource "aws_ivschat_logging_configuration" "example" {
  # Example configuration for Logging Configuration
  name = "example-logging_configuration"

  # Common attributes
  tags = {
    Name        = "example-logging_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Room

```hcl
resource "aws_ivschat_room" "example" {
  # Example configuration for Room
  name = "example-room"

  # Common attributes
  tags = {
    Name        = "example-room"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## kafka

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Cluster | aws_msk_cluster | SDK |
| Cluster Policy | aws_msk_cluster_policy | SDK |
| Configuration | aws_msk_configuration | SDK |
| Replicator | aws_msk_replicator | SDK |
| SCRAM Secret Association | aws_msk_scram_secret_association | SDK |
| Serverless Cluster | aws_msk_serverless_cluster | SDK |
| Single SCRAM Secret Association | N/A | Framework |
| VPC Connection | aws_msk_vpc_connection | SDK |


### Examples


#### Cluster

```hcl
resource "aws_msk_cluster" "example" {
  # Example configuration for Cluster
  name = "example-cluster"

  # Common attributes
  tags = {
    Name        = "example-cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster Policy

```hcl
resource "aws_msk_cluster_policy" "example" {
  # Example configuration for Cluster Policy
  name = "example-cluster_policy"

  # Common attributes
  tags = {
    Name        = "example-cluster_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Configuration

```hcl
resource "aws_msk_configuration" "example" {
  # Example configuration for Configuration
  name = "example-configuration"

  # Common attributes
  tags = {
    Name        = "example-configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Replicator

```hcl
resource "aws_msk_replicator" "example" {
  # Example configuration for Replicator
  name = "example-replicator"

  # Common attributes
  tags = {
    Name        = "example-replicator"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### SCRAM Secret Association

```hcl
resource "aws_msk_scram_secret_association" "example" {
  # Example configuration for SCRAM Secret Association
  name = "example-scram_secret_association"

  # Common attributes
  tags = {
    Name        = "example-scram_secret_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Serverless Cluster

```hcl
resource "aws_msk_serverless_cluster" "example" {
  # Example configuration for Serverless Cluster
  name = "example-serverless_cluster"

  # Common attributes
  tags = {
    Name        = "example-serverless_cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Single SCRAM Secret Association

```hcl
resource "aws_kafka_single_scram_secret_association" "example" {
  # Example configuration for Single SCRAM Secret Association
  name = "example-single_scram_secret_association"

  # Common attributes
  tags = {
    Name        = "example-single_scram_secret_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Connection

```hcl
resource "aws_msk_vpc_connection" "example" {
  # Example configuration for VPC Connection
  name = "example-vpc_connection"

  # Common attributes
  tags = {
    Name        = "example-vpc_connection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## kafkaconnect

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Connector | aws_mskconnect_connector | SDK |
| Custom Plugin | aws_mskconnect_custom_plugin | SDK |
| Worker Configuration | aws_mskconnect_worker_configuration | SDK |


### Examples


#### Connector

```hcl
resource "aws_mskconnect_connector" "example" {
  # Example configuration for Connector
  name = "example-connector"

  # Common attributes
  tags = {
    Name        = "example-connector"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Custom Plugin

```hcl
resource "aws_mskconnect_custom_plugin" "example" {
  # Example configuration for Custom Plugin
  name = "example-custom_plugin"

  # Common attributes
  tags = {
    Name        = "example-custom_plugin"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Worker Configuration

```hcl
resource "aws_mskconnect_worker_configuration" "example" {
  # Example configuration for Worker Configuration
  name = "example-worker_configuration"

  # Common attributes
  tags = {
    Name        = "example-worker_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## kendra

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Data Source | aws_kendra_data_source | SDK |
| FAQ | aws_kendra_faq | SDK |
| Index | aws_kendra_index | SDK |
| Query Suggestions Block List | aws_kendra_query_suggestions_block_list | SDK |
| Thesaurus | aws_kendra_thesaurus | SDK |


### Examples


#### Data Source

```hcl
resource "aws_kendra_data_source" "example" {
  # Example configuration for Data Source
  name = "example-data_source"

  # Common attributes
  tags = {
    Name        = "example-data_source"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### FAQ

```hcl
resource "aws_kendra_faq" "example" {
  # Example configuration for FAQ
  name = "example-faq"

  # Common attributes
  tags = {
    Name        = "example-faq"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Index

```hcl
resource "aws_kendra_index" "example" {
  # Example configuration for Index
  name = "example-index"

  # Common attributes
  tags = {
    Name        = "example-index"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Query Suggestions Block List

```hcl
resource "aws_kendra_query_suggestions_block_list" "example" {
  # Example configuration for Query Suggestions Block List
  name = "example-query_suggestions_block_list"

  # Common attributes
  tags = {
    Name        = "example-query_suggestions_block_list"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Thesaurus

```hcl
resource "aws_kendra_thesaurus" "example" {
  # Example configuration for Thesaurus
  name = "example-thesaurus"

  # Common attributes
  tags = {
    Name        = "example-thesaurus"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## keyspaces

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Keyspace | aws_keyspaces_keyspace | SDK |
| Table | aws_keyspaces_table | SDK |


### Examples


#### Keyspace

```hcl
resource "aws_keyspaces_keyspace" "example" {
  # Example configuration for Keyspace
  name = "example-keyspace"

  # Common attributes
  tags = {
    Name        = "example-keyspace"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Table

```hcl
resource "aws_keyspaces_table" "example" {
  # Example configuration for Table
  name = "example-table"

  # Common attributes
  tags = {
    Name        = "example-table"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## kinesis

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Resource Policy | N/A | Framework |
| Stream | aws_kinesis_stream | SDK |
| Stream Consumer | aws_kinesis_stream_consumer | SDK |


### Examples


#### Resource Policy

```hcl
resource "aws_kinesis_resource_policy" "example" {
  # Example configuration for Resource Policy
  name = "example-resource_policy"

  # Common attributes
  tags = {
    Name        = "example-resource_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Stream

```hcl
resource "aws_kinesis_stream" "example" {
  # Example configuration for Stream
  name = "example-stream"

  # Common attributes
  tags = {
    Name        = "example-stream"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Stream Consumer

```hcl
resource "aws_kinesis_stream_consumer" "example" {
  # Example configuration for Stream Consumer
  name = "example-stream_consumer"

  # Common attributes
  tags = {
    Name        = "example-stream_consumer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## kinesisanalytics

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Application | aws_kinesis_analytics_application | SDK |


### Examples


#### Application

```hcl
resource "aws_kinesis_analytics_application" "example" {
  # Example configuration for Application
  name = "example-application"

  # Common attributes
  tags = {
    Name        = "example-application"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## kinesisanalyticsv2

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Application | aws_kinesisanalyticsv2_application | SDK |
| Application Snapshot | aws_kinesisanalyticsv2_application_snapshot | SDK |


### Examples


#### Application

```hcl
resource "aws_kinesisanalyticsv2_application" "example" {
  # Example configuration for Application
  name = "example-application"

  # Common attributes
  tags = {
    Name        = "example-application"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Application Snapshot

```hcl
resource "aws_kinesisanalyticsv2_application_snapshot" "example" {
  # Example configuration for Application Snapshot
  name = "example-application_snapshot"

  # Common attributes
  tags = {
    Name        = "example-application_snapshot"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## kinesisvideo

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Stream | aws_kinesis_video_stream | SDK |


### Examples


#### Stream

```hcl
resource "aws_kinesis_video_stream" "example" {
  # Example configuration for Stream
  name = "example-stream"

  # Common attributes
  tags = {
    Name        = "example-stream"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## kms

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Alias | aws_kms_alias | SDK |
| Ciphertext | aws_kms_ciphertext | SDK |
| Custom Key Store | aws_kms_custom_key_store | SDK |
| External Key | aws_kms_external_key | SDK |
| Grant | aws_kms_grant | SDK |
| Key | aws_kms_key | SDK |
| Key Policy | aws_kms_key_policy | SDK |
| Replica External Key | aws_kms_replica_external_key | SDK |
| Replica Key | aws_kms_replica_key | SDK |


### Examples


#### Alias

```hcl
resource "aws_kms_alias" "example" {
  # Example configuration for Alias
  name = "example-alias"

  # Common attributes
  tags = {
    Name        = "example-alias"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Ciphertext

```hcl
resource "aws_kms_ciphertext" "example" {
  # Example configuration for Ciphertext
  name = "example-ciphertext"

  # Common attributes
  tags = {
    Name        = "example-ciphertext"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Custom Key Store

```hcl
resource "aws_kms_custom_key_store" "example" {
  # Example configuration for Custom Key Store
  name = "example-custom_key_store"

  # Common attributes
  tags = {
    Name        = "example-custom_key_store"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### External Key

```hcl
resource "aws_kms_external_key" "example" {
  # Example configuration for External Key
  name = "example-external_key"

  # Common attributes
  tags = {
    Name        = "example-external_key"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Grant

```hcl
resource "aws_kms_grant" "example" {
  # Example configuration for Grant
  name = "example-grant"

  # Common attributes
  tags = {
    Name        = "example-grant"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Key

```hcl
resource "aws_kms_key" "example" {
  description             = "Example KMS key"
  deletion_window_in_days = 10
}
```


#### Key Policy

```hcl
resource "aws_kms_key_policy" "example" {
  # Example configuration for Key Policy
  name = "example-key_policy"

  # Common attributes
  tags = {
    Name        = "example-key_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Replica External Key

```hcl
resource "aws_kms_replica_external_key" "example" {
  # Example configuration for Replica External Key
  name = "example-replica_external_key"

  # Common attributes
  tags = {
    Name        = "example-replica_external_key"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Replica Key

```hcl
resource "aws_kms_replica_key" "example" {
  # Example configuration for Replica Key
  name = "example-replica_key"

  # Common attributes
  tags = {
    Name        = "example-replica_key"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## lakeformation

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Data Cells Filter | N/A | Framework |
| Resource | aws_lakeformation_resource | SDK |
| Resource LF Tag | N/A | Framework |


### Examples


#### Data Cells Filter

```hcl
resource "aws_lakeformation_data_cells_filter" "example" {
  # Example configuration for Data Cells Filter
  name = "example-data_cells_filter"

  # Common attributes
  tags = {
    Name        = "example-data_cells_filter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource

```hcl
resource "aws_lakeformation_resource" "example" {
  # Example configuration for Resource
  name = "example-resource"

  # Common attributes
  tags = {
    Name        = "example-resource"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource LF Tag

```hcl
resource "aws_lakeformation_resource_lf_tag" "example" {
  # Example configuration for Resource LF Tag
  name = "example-resource_lf_tag"

  # Common attributes
  tags = {
    Name        = "example-resource_lf_tag"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## lambda

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Alias | aws_lambda_alias | SDK |
| Code Signing Config | aws_lambda_code_signing_config | SDK |
| Event Source Mapping | aws_lambda_event_source_mapping | SDK |
| Function | aws_lambda_function | SDK |
| Function Event Invoke Config | aws_lambda_function_event_invoke_config | SDK |
| Function Recursion Config | N/A | Framework |
| Function URL | aws_lambda_function_url | SDK |
| Invocation | aws_lambda_invocation | SDK |
| Layer Version | aws_lambda_layer_version | SDK |
| Layer Version Permission | aws_lambda_layer_version_permission | SDK |
| Permission | aws_lambda_permission | SDK |
| Provisioned Concurrency Config | aws_lambda_provisioned_concurrency_config | SDK |
| Runtime Management Config | N/A | Framework |


### Examples


#### Alias

```hcl
resource "aws_lambda_alias" "example" {
  # Example configuration for Alias
  name = "example-alias"

  # Common attributes
  tags = {
    Name        = "example-alias"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Code Signing Config

```hcl
resource "aws_lambda_code_signing_config" "example" {
  # Example configuration for Code Signing Config
  name = "example-code_signing_config"

  # Common attributes
  tags = {
    Name        = "example-code_signing_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Event Source Mapping

```hcl
resource "aws_lambda_event_source_mapping" "example" {
  # Example configuration for Event Source Mapping
  name = "example-event_source_mapping"

  # Common attributes
  tags = {
    Name        = "example-event_source_mapping"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Function

```hcl
resource "aws_lambda_function" "example" {
  function_name = "example-function"
  role          = aws_iam_role.example.arn
  handler       = "index.handler"
  runtime       = "nodejs18.x"

  filename      = "lambda_function.zip"

  environment {
    variables = {
      ENV_VAR = "value"
    }
  }
}
```


#### Function Event Invoke Config

```hcl
resource "aws_lambda_function_event_invoke_config" "example" {
  # Example configuration for Function Event Invoke Config
  name = "example-function_event_invoke_config"

  # Common attributes
  tags = {
    Name        = "example-function_event_invoke_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Function Recursion Config

```hcl
resource "aws_lambda_function_recursion_config" "example" {
  # Example configuration for Function Recursion Config
  name = "example-function_recursion_config"

  # Common attributes
  tags = {
    Name        = "example-function_recursion_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Function URL

```hcl
resource "aws_lambda_function_url" "example" {
  # Example configuration for Function URL
  name = "example-function_url"

  # Common attributes
  tags = {
    Name        = "example-function_url"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Invocation

```hcl
resource "aws_lambda_invocation" "example" {
  # Example configuration for Invocation
  name = "example-invocation"

  # Common attributes
  tags = {
    Name        = "example-invocation"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Layer Version

```hcl
resource "aws_lambda_layer_version" "example" {
  # Example configuration for Layer Version
  name = "example-layer_version"

  # Common attributes
  tags = {
    Name        = "example-layer_version"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Layer Version Permission

```hcl
resource "aws_lambda_layer_version_permission" "example" {
  # Example configuration for Layer Version Permission
  name = "example-layer_version_permission"

  # Common attributes
  tags = {
    Name        = "example-layer_version_permission"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Permission

```hcl
resource "aws_lambda_permission" "example" {
  # Example configuration for Permission
  name = "example-permission"

  # Common attributes
  tags = {
    Name        = "example-permission"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Provisioned Concurrency Config

```hcl
resource "aws_lambda_provisioned_concurrency_config" "example" {
  # Example configuration for Provisioned Concurrency Config
  name = "example-provisioned_concurrency_config"

  # Common attributes
  tags = {
    Name        = "example-provisioned_concurrency_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Runtime Management Config

```hcl
resource "aws_lambda_runtime_management_config" "example" {
  # Example configuration for Runtime Management Config
  name = "example-runtime_management_config"

  # Common attributes
  tags = {
    Name        = "example-runtime_management_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## lexmodels

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Bot Alias | aws_lex_bot_alias | SDK |
| Intent | aws_lex_intent | SDK |
| Slot Type | aws_lex_slot_type | SDK |


### Examples


#### Bot Alias

```hcl
resource "aws_lex_bot_alias" "example" {
  # Example configuration for Bot Alias
  name = "example-bot_alias"

  # Common attributes
  tags = {
    Name        = "example-bot_alias"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Intent

```hcl
resource "aws_lex_intent" "example" {
  # Example configuration for Intent
  name = "example-intent"

  # Common attributes
  tags = {
    Name        = "example-intent"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Slot Type

```hcl
resource "aws_lex_slot_type" "example" {
  # Example configuration for Slot Type
  name = "example-slot_type"

  # Common attributes
  tags = {
    Name        = "example-slot_type"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## lexv2models

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Bot | N/A | Framework |
| Bot Locale | N/A | Framework |
| Bot Version | N/A | Framework |
| Intent | N/A | Framework |
| Slot | N/A | Framework |
| Slot Type | N/A | Framework |


### Examples


#### Bot

```hcl
resource "aws_lexv2models_bot" "example" {
  # Example configuration for Bot
  name = "example-bot"

  # Common attributes
  tags = {
    Name        = "example-bot"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bot Locale

```hcl
resource "aws_lexv2models_bot_locale" "example" {
  # Example configuration for Bot Locale
  name = "example-bot_locale"

  # Common attributes
  tags = {
    Name        = "example-bot_locale"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bot Version

```hcl
resource "aws_lexv2models_bot_version" "example" {
  # Example configuration for Bot Version
  name = "example-bot_version"

  # Common attributes
  tags = {
    Name        = "example-bot_version"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Intent

```hcl
resource "aws_lexv2models_intent" "example" {
  # Example configuration for Intent
  name = "example-intent"

  # Common attributes
  tags = {
    Name        = "example-intent"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Slot

```hcl
resource "aws_lexv2models_slot" "example" {
  # Example configuration for Slot
  name = "example-slot"

  # Common attributes
  tags = {
    Name        = "example-slot"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Slot Type

```hcl
resource "aws_lexv2models_slot_type" "example" {
  # Example configuration for Slot Type
  name = "example-slot_type"

  # Common attributes
  tags = {
    Name        = "example-slot_type"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## licensemanager

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Association | aws_licensemanager_association | SDK |
| Grant | aws_licensemanager_grant | SDK |
| Grant Accepter | aws_licensemanager_grant_accepter | SDK |
| License Configuration | aws_licensemanager_license_configuration | SDK |


### Examples


#### Association

```hcl
resource "aws_licensemanager_association" "example" {
  # Example configuration for Association
  name = "example-association"

  # Common attributes
  tags = {
    Name        = "example-association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Grant

```hcl
resource "aws_licensemanager_grant" "example" {
  # Example configuration for Grant
  name = "example-grant"

  # Common attributes
  tags = {
    Name        = "example-grant"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Grant Accepter

```hcl
resource "aws_licensemanager_grant_accepter" "example" {
  # Example configuration for Grant Accepter
  name = "example-grant_accepter"

  # Common attributes
  tags = {
    Name        = "example-grant_accepter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### License Configuration

```hcl
resource "aws_licensemanager_license_configuration" "example" {
  # Example configuration for License Configuration
  name = "example-license_configuration"

  # Common attributes
  tags = {
    Name        = "example-license_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## lightsail

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Bucket | aws_lightsail_bucket | SDK |
| Certificate | aws_lightsail_certificate | SDK |
| Container Service | aws_lightsail_container_service | SDK |
| Database | aws_lightsail_database | SDK |
| Disk | aws_lightsail_disk | SDK |
| Distribution | aws_lightsail_distribution | SDK |
| Instance | aws_lightsail_instance | SDK |
| KeyPair | aws_lightsail_key_pair | SDK |
| LB | aws_lightsail_lb | SDK |


### Examples


#### Bucket

```hcl
resource "aws_lightsail_bucket" "example" {
  # Example configuration for Bucket
  name = "example-bucket"

  # Common attributes
  tags = {
    Name        = "example-bucket"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Certificate

```hcl
resource "aws_lightsail_certificate" "example" {
  # Example configuration for Certificate
  name = "example-certificate"

  # Common attributes
  tags = {
    Name        = "example-certificate"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Container Service

```hcl
resource "aws_lightsail_container_service" "example" {
  # Example configuration for Container Service
  name = "example-container_service"

  # Common attributes
  tags = {
    Name        = "example-container_service"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Database

```hcl
resource "aws_lightsail_database" "example" {
  # Example configuration for Database
  name = "example-database"

  # Common attributes
  tags = {
    Name        = "example-database"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Disk

```hcl
resource "aws_lightsail_disk" "example" {
  # Example configuration for Disk
  name = "example-disk"

  # Common attributes
  tags = {
    Name        = "example-disk"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Distribution

```hcl
resource "aws_lightsail_distribution" "example" {
  # Example configuration for Distribution
  name = "example-distribution"

  # Common attributes
  tags = {
    Name        = "example-distribution"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Instance

```hcl
resource "aws_lightsail_instance" "example" {
  # Example configuration for Instance
  name = "example-instance"

  # Common attributes
  tags = {
    Name        = "example-instance"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### KeyPair

```hcl
resource "aws_lightsail_key_pair" "example" {
  # Example configuration for KeyPair
  name = "example-keypair"

  # Common attributes
  tags = {
    Name        = "example-keypair"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### LB

```hcl
resource "aws_lightsail_lb" "example" {
  # Example configuration for LB
  name = "example-lb"

  # Common attributes
  tags = {
    Name        = "example-lb"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## location

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Geofence Collection | aws_location_geofence_collection | SDK |
| Map | aws_location_place_index | SDK |
| Route Calculator | aws_location_tracker | SDK |


### Examples


#### Geofence Collection

```hcl
resource "aws_location_geofence_collection" "example" {
  # Example configuration for Geofence Collection
  name = "example-geofence_collection"

  # Common attributes
  tags = {
    Name        = "example-geofence_collection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Map

```hcl
resource "aws_location_place_index" "example" {
  # Example configuration for Map
  name = "example-map"

  # Common attributes
  tags = {
    Name        = "example-map"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Route Calculator

```hcl
resource "aws_location_tracker" "example" {
  # Example configuration for Route Calculator
  name = "example-route_calculator"

  # Common attributes
  tags = {
    Name        = "example-route_calculator"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## logs

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Account Policy | aws_cloudwatch_log_account_policy | SDK |
| Anomaly Detector | N/A | Framework |
| Data Protection Policy | aws_cloudwatch_log_data_protection_policy | SDK |
| Delivery | N/A | Framework |
| Delivery Destination | N/A | Framework |
| Delivery Destination Policy | N/A | Framework |
| Delivery Source | N/A | Framework |
| Destination | aws_cloudwatch_log_destination | SDK |
| Destination Policy | aws_cloudwatch_log_destination_policy | SDK |
| Index Policy | N/A | Framework |
| Log Group | aws_cloudwatch_log_group | SDK |
| Log Stream | aws_cloudwatch_log_stream | SDK |
| Metric Filter | aws_cloudwatch_log_metric_filter | SDK |
| Query Definition | aws_cloudwatch_query_definition | SDK |
| Resource Policy | aws_cloudwatch_log_resource_policy | SDK |
| Subscription Filter | aws_cloudwatch_log_subscription_filter | SDK |


### Examples


#### Account Policy

```hcl
resource "aws_cloudwatch_log_account_policy" "example" {
  # Example configuration for Account Policy
  name = "example-account_policy"

  # Common attributes
  tags = {
    Name        = "example-account_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Anomaly Detector

```hcl
resource "aws_logs_anomaly_detector" "example" {
  # Example configuration for Anomaly Detector
  name = "example-anomaly_detector"

  # Common attributes
  tags = {
    Name        = "example-anomaly_detector"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Data Protection Policy

```hcl
resource "aws_cloudwatch_log_data_protection_policy" "example" {
  # Example configuration for Data Protection Policy
  name = "example-data_protection_policy"

  # Common attributes
  tags = {
    Name        = "example-data_protection_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Delivery

```hcl
resource "aws_logs_delivery" "example" {
  # Example configuration for Delivery
  name = "example-delivery"

  # Common attributes
  tags = {
    Name        = "example-delivery"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Delivery Destination

```hcl
resource "aws_logs_delivery_destination" "example" {
  # Example configuration for Delivery Destination
  name = "example-delivery_destination"

  # Common attributes
  tags = {
    Name        = "example-delivery_destination"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Delivery Destination Policy

```hcl
resource "aws_logs_delivery_destination_policy" "example" {
  # Example configuration for Delivery Destination Policy
  name = "example-delivery_destination_policy"

  # Common attributes
  tags = {
    Name        = "example-delivery_destination_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Delivery Source

```hcl
resource "aws_logs_delivery_source" "example" {
  # Example configuration for Delivery Source
  name = "example-delivery_source"

  # Common attributes
  tags = {
    Name        = "example-delivery_source"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Destination

```hcl
resource "aws_cloudwatch_log_destination" "example" {
  # Example configuration for Destination
  name = "example-destination"

  # Common attributes
  tags = {
    Name        = "example-destination"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Destination Policy

```hcl
resource "aws_cloudwatch_log_destination_policy" "example" {
  # Example configuration for Destination Policy
  name = "example-destination_policy"

  # Common attributes
  tags = {
    Name        = "example-destination_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Index Policy

```hcl
resource "aws_logs_index_policy" "example" {
  # Example configuration for Index Policy
  name = "example-index_policy"

  # Common attributes
  tags = {
    Name        = "example-index_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Log Group

```hcl
resource "aws_cloudwatch_log_group" "example" {
  name              = "/aws/example/log-group"
  retention_in_days = 14
}
```


#### Log Stream

```hcl
resource "aws_cloudwatch_log_stream" "example" {
  # Example configuration for Log Stream
  name = "example-log_stream"

  # Common attributes
  tags = {
    Name        = "example-log_stream"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Metric Filter

```hcl
resource "aws_cloudwatch_log_metric_filter" "example" {
  # Example configuration for Metric Filter
  name = "example-metric_filter"

  # Common attributes
  tags = {
    Name        = "example-metric_filter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Query Definition

```hcl
resource "aws_cloudwatch_query_definition" "example" {
  # Example configuration for Query Definition
  name = "example-query_definition"

  # Common attributes
  tags = {
    Name        = "example-query_definition"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource Policy

```hcl
resource "aws_cloudwatch_log_resource_policy" "example" {
  # Example configuration for Resource Policy
  name = "example-resource_policy"

  # Common attributes
  tags = {
    Name        = "example-resource_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Subscription Filter

```hcl
resource "aws_cloudwatch_log_subscription_filter" "example" {
  # Example configuration for Subscription Filter
  name = "example-subscription_filter"

  # Common attributes
  tags = {
    Name        = "example-subscription_filter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## m2

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Application | N/A | Framework |
| Deployment | N/A | Framework |
| Environment | N/A | Framework |


### Examples


#### Application

```hcl
resource "aws_m2_application" "example" {
  # Example configuration for Application
  name = "example-application"

  # Common attributes
  tags = {
    Name        = "example-application"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Deployment

```hcl
resource "aws_m2_deployment" "example" {
  # Example configuration for Deployment
  name = "example-deployment"

  # Common attributes
  tags = {
    Name        = "example-deployment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Environment

```hcl
resource "aws_m2_environment" "example" {
  # Example configuration for Environment
  name = "example-environment"

  # Common attributes
  tags = {
    Name        = "example-environment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## macie2

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Account | aws_macie2_account | SDK |
| Classification Export Configuration | aws_macie2_classification_export_configuration | SDK |
| Classification Job | aws_macie2_classification_job | SDK |
| Custom Data Identifier | aws_macie2_custom_data_identifier | SDK |
| Findings Filter | aws_macie2_findings_filter | SDK |
| Invitation Accepter | aws_macie2_invitation_accepter | SDK |
| Member | aws_macie2_member | SDK |
| Organization Admin Account | aws_macie2_organization_admin_account | SDK |


### Examples


#### Account

```hcl
resource "aws_macie2_account" "example" {
  # Example configuration for Account
  name = "example-account"

  # Common attributes
  tags = {
    Name        = "example-account"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Classification Export Configuration

```hcl
resource "aws_macie2_classification_export_configuration" "example" {
  # Example configuration for Classification Export Configuration
  name = "example-classification_export_configuration"

  # Common attributes
  tags = {
    Name        = "example-classification_export_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Classification Job

```hcl
resource "aws_macie2_classification_job" "example" {
  # Example configuration for Classification Job
  name = "example-classification_job"

  # Common attributes
  tags = {
    Name        = "example-classification_job"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Custom Data Identifier

```hcl
resource "aws_macie2_custom_data_identifier" "example" {
  # Example configuration for Custom Data Identifier
  name = "example-custom_data_identifier"

  # Common attributes
  tags = {
    Name        = "example-custom_data_identifier"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Findings Filter

```hcl
resource "aws_macie2_findings_filter" "example" {
  # Example configuration for Findings Filter
  name = "example-findings_filter"

  # Common attributes
  tags = {
    Name        = "example-findings_filter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Invitation Accepter

```hcl
resource "aws_macie2_invitation_accepter" "example" {
  # Example configuration for Invitation Accepter
  name = "example-invitation_accepter"

  # Common attributes
  tags = {
    Name        = "example-invitation_accepter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Member

```hcl
resource "aws_macie2_member" "example" {
  # Example configuration for Member
  name = "example-member"

  # Common attributes
  tags = {
    Name        = "example-member"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Organization Admin Account

```hcl
resource "aws_macie2_organization_admin_account" "example" {
  # Example configuration for Organization Admin Account
  name = "example-organization_admin_account"

  # Common attributes
  tags = {
    Name        = "example-organization_admin_account"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## mediaconvert

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Queue | aws_media_convert_queue | SDK |


### Examples


#### Queue

```hcl
resource "aws_media_convert_queue" "example" {
  # Example configuration for Queue
  name = "example-queue"

  # Common attributes
  tags = {
    Name        = "example-queue"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## medialive

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Channel | aws_medialive_channel | SDK |
| Input | aws_medialive_input | SDK |
| Input Security Group | aws_medialive_input_security_group | SDK |
| Multiplex | aws_medialive_multiplex | SDK |


### Examples


#### Channel

```hcl
resource "aws_medialive_channel" "example" {
  # Example configuration for Channel
  name = "example-channel"

  # Common attributes
  tags = {
    Name        = "example-channel"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Input

```hcl
resource "aws_medialive_input" "example" {
  # Example configuration for Input
  name = "example-input"

  # Common attributes
  tags = {
    Name        = "example-input"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Input Security Group

```hcl
resource "aws_medialive_input_security_group" "example" {
  # Example configuration for Input Security Group
  name = "example-input_security_group"

  # Common attributes
  tags = {
    Name        = "example-input_security_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Multiplex

```hcl
resource "aws_medialive_multiplex" "example" {
  # Example configuration for Multiplex
  name = "example-multiplex"

  # Common attributes
  tags = {
    Name        = "example-multiplex"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## mediapackage

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Channel | aws_media_package_channel | SDK |


### Examples


#### Channel

```hcl
resource "aws_media_package_channel" "example" {
  # Example configuration for Channel
  name = "example-channel"

  # Common attributes
  tags = {
    Name        = "example-channel"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## mediapackagev2

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Channel Group | N/A | Framework |


### Examples


#### Channel Group

```hcl
resource "aws_mediapackagev2_channel_group" "example" {
  # Example configuration for Channel Group
  name = "example-channel_group"

  # Common attributes
  tags = {
    Name        = "example-channel_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## mediastore

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Container | aws_media_store_container | SDK |


### Examples


#### Container

```hcl
resource "aws_media_store_container" "example" {
  # Example configuration for Container
  name = "example-container"

  # Common attributes
  tags = {
    Name        = "example-container"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## memorydb

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| ACL | aws_memorydb_acl | SDK |
| Cluster | aws_memorydb_cluster | SDK |
| Multi Region Cluster | N/A | Framework |
| Parameter Group | aws_memorydb_parameter_group | SDK |
| Snapshot | aws_memorydb_snapshot | SDK |
| Subnet Group | aws_memorydb_subnet_group | SDK |
| User | aws_memorydb_user | SDK |


### Examples


#### ACL

```hcl
resource "aws_memorydb_acl" "example" {
  # Example configuration for ACL
  name = "example-acl"

  # Common attributes
  tags = {
    Name        = "example-acl"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster

```hcl
resource "aws_memorydb_cluster" "example" {
  # Example configuration for Cluster
  name = "example-cluster"

  # Common attributes
  tags = {
    Name        = "example-cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Multi Region Cluster

```hcl
resource "aws_memorydb_multi_region_cluster" "example" {
  # Example configuration for Multi Region Cluster
  name = "example-multi_region_cluster"

  # Common attributes
  tags = {
    Name        = "example-multi_region_cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Parameter Group

```hcl
resource "aws_memorydb_parameter_group" "example" {
  # Example configuration for Parameter Group
  name = "example-parameter_group"

  # Common attributes
  tags = {
    Name        = "example-parameter_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Snapshot

```hcl
resource "aws_memorydb_snapshot" "example" {
  # Example configuration for Snapshot
  name = "example-snapshot"

  # Common attributes
  tags = {
    Name        = "example-snapshot"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Subnet Group

```hcl
resource "aws_memorydb_subnet_group" "example" {
  # Example configuration for Subnet Group
  name = "example-subnet_group"

  # Common attributes
  tags = {
    Name        = "example-subnet_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User

```hcl
resource "aws_memorydb_user" "example" {
  # Example configuration for User
  name = "example-user"

  # Common attributes
  tags = {
    Name        = "example-user"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## mq

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Broker | aws_mq_broker | SDK |
| Configuration | aws_mq_configuration | SDK |


### Examples


#### Broker

```hcl
resource "aws_mq_broker" "example" {
  # Example configuration for Broker
  name = "example-broker"

  # Common attributes
  tags = {
    Name        = "example-broker"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Configuration

```hcl
resource "aws_mq_configuration" "example" {
  # Example configuration for Configuration
  name = "example-configuration"

  # Common attributes
  tags = {
    Name        = "example-configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## mwaa

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Environment | aws_mwaa_environment | SDK |


### Examples


#### Environment

```hcl
resource "aws_mwaa_environment" "example" {
  # Example configuration for Environment
  name = "example-environment"

  # Common attributes
  tags = {
    Name        = "example-environment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## neptune

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Cluster | aws_neptune_cluster | SDK |
| Cluster Endpoint | aws_neptune_cluster_endpoint | SDK |
| Cluster Instance | aws_neptune_cluster_instance | SDK |
| Cluster Parameter Group | aws_neptune_cluster_parameter_group | SDK |
| Cluster Snapshot | aws_neptune_cluster_snapshot | SDK |
| Event Subscription | aws_neptune_event_subscription | SDK |
| Global Cluster | aws_neptune_global_cluster | SDK |
| Parameter Group | aws_neptune_parameter_group | SDK |
| Subnet Group | aws_neptune_subnet_group | SDK |


### Examples


#### Cluster

```hcl
resource "aws_neptune_cluster" "example" {
  # Example configuration for Cluster
  name = "example-cluster"

  # Common attributes
  tags = {
    Name        = "example-cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster Endpoint

```hcl
resource "aws_neptune_cluster_endpoint" "example" {
  # Example configuration for Cluster Endpoint
  name = "example-cluster_endpoint"

  # Common attributes
  tags = {
    Name        = "example-cluster_endpoint"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster Instance

```hcl
resource "aws_neptune_cluster_instance" "example" {
  # Example configuration for Cluster Instance
  name = "example-cluster_instance"

  # Common attributes
  tags = {
    Name        = "example-cluster_instance"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster Parameter Group

```hcl
resource "aws_neptune_cluster_parameter_group" "example" {
  # Example configuration for Cluster Parameter Group
  name = "example-cluster_parameter_group"

  # Common attributes
  tags = {
    Name        = "example-cluster_parameter_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster Snapshot

```hcl
resource "aws_neptune_cluster_snapshot" "example" {
  # Example configuration for Cluster Snapshot
  name = "example-cluster_snapshot"

  # Common attributes
  tags = {
    Name        = "example-cluster_snapshot"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Event Subscription

```hcl
resource "aws_neptune_event_subscription" "example" {
  # Example configuration for Event Subscription
  name = "example-event_subscription"

  # Common attributes
  tags = {
    Name        = "example-event_subscription"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Global Cluster

```hcl
resource "aws_neptune_global_cluster" "example" {
  # Example configuration for Global Cluster
  name = "example-global_cluster"

  # Common attributes
  tags = {
    Name        = "example-global_cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Parameter Group

```hcl
resource "aws_neptune_parameter_group" "example" {
  # Example configuration for Parameter Group
  name = "example-parameter_group"

  # Common attributes
  tags = {
    Name        = "example-parameter_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Subnet Group

```hcl
resource "aws_neptune_subnet_group" "example" {
  # Example configuration for Subnet Group
  name = "example-subnet_group"

  # Common attributes
  tags = {
    Name        = "example-subnet_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## networkfirewall

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Firewall | aws_networkfirewall_firewall | SDK |
| Firewall Policy | aws_networkfirewall_firewall_policy | SDK |
| Logging Configuration | aws_networkfirewall_logging_configuration | SDK |
| Resource Policy | aws_networkfirewall_resource_policy | SDK |
| Rule Group | aws_networkfirewall_rule_group | SDK |
| TLS Inspection Configuration | N/A | Framework |


### Examples


#### Firewall

```hcl
resource "aws_networkfirewall_firewall" "example" {
  # Example configuration for Firewall
  name = "example-firewall"

  # Common attributes
  tags = {
    Name        = "example-firewall"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Firewall Policy

```hcl
resource "aws_networkfirewall_firewall_policy" "example" {
  # Example configuration for Firewall Policy
  name = "example-firewall_policy"

  # Common attributes
  tags = {
    Name        = "example-firewall_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Logging Configuration

```hcl
resource "aws_networkfirewall_logging_configuration" "example" {
  # Example configuration for Logging Configuration
  name = "example-logging_configuration"

  # Common attributes
  tags = {
    Name        = "example-logging_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource Policy

```hcl
resource "aws_networkfirewall_resource_policy" "example" {
  # Example configuration for Resource Policy
  name = "example-resource_policy"

  # Common attributes
  tags = {
    Name        = "example-resource_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Rule Group

```hcl
resource "aws_networkfirewall_rule_group" "example" {
  # Example configuration for Rule Group
  name = "example-rule_group"

  # Common attributes
  tags = {
    Name        = "example-rule_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### TLS Inspection Configuration

```hcl
resource "aws_networkfirewall_tls_inspection_configuration" "example" {
  # Example configuration for TLS Inspection Configuration
  name = "example-tls_inspection_configuration"

  # Common attributes
  tags = {
    Name        = "example-tls_inspection_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## networkmanager

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Attachment Accepter | aws_networkmanager_attachment_accepter | SDK |
| Connect Attachment | aws_networkmanager_connect_attachment | SDK |
| Connect Peer | aws_networkmanager_connect_peer | SDK |
| Connection | aws_networkmanager_connection | SDK |
| Core Network | aws_networkmanager_core_network | SDK |
| Core Network Policy Attachment | aws_networkmanager_core_network_policy_attachment | SDK |
| Customer Gateway Association | aws_networkmanager_customer_gateway_association | SDK |
| Device | aws_networkmanager_device | SDK |
| Direct Connect Gateway Attachment | N/A | Framework |
| Global Network | aws_networkmanager_global_network | SDK |
| Link | aws_networkmanager_link | SDK |
| Link Association | aws_networkmanager_link_association | SDK |
| Site | aws_networkmanager_site | SDK |
| Site To Site VPN Attachment | aws_networkmanager_site_to_site_vpn_attachment | SDK |
| Transit Gateway Connect Peer Association | aws_networkmanager_transit_gateway_connect_peer_association | SDK |
| Transit Gateway Peering | aws_networkmanager_transit_gateway_peering | SDK |
| Transit Gateway Registration | aws_networkmanager_transit_gateway_registration | SDK |
| Transit Gateway Route Table Attachment | aws_networkmanager_transit_gateway_route_table_attachment | SDK |
| VPC Attachment | aws_networkmanager_vpc_attachment | SDK |


### Examples


#### Attachment Accepter

```hcl
resource "aws_networkmanager_attachment_accepter" "example" {
  # Example configuration for Attachment Accepter
  name = "example-attachment_accepter"

  # Common attributes
  tags = {
    Name        = "example-attachment_accepter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Connect Attachment

```hcl
resource "aws_networkmanager_connect_attachment" "example" {
  # Example configuration for Connect Attachment
  name = "example-connect_attachment"

  # Common attributes
  tags = {
    Name        = "example-connect_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Connect Peer

```hcl
resource "aws_networkmanager_connect_peer" "example" {
  # Example configuration for Connect Peer
  name = "example-connect_peer"

  # Common attributes
  tags = {
    Name        = "example-connect_peer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Connection

```hcl
resource "aws_networkmanager_connection" "example" {
  # Example configuration for Connection
  name = "example-connection"

  # Common attributes
  tags = {
    Name        = "example-connection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Core Network

```hcl
resource "aws_networkmanager_core_network" "example" {
  # Example configuration for Core Network
  name = "example-core_network"

  # Common attributes
  tags = {
    Name        = "example-core_network"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Core Network Policy Attachment

```hcl
resource "aws_networkmanager_core_network_policy_attachment" "example" {
  # Example configuration for Core Network Policy Attachment
  name = "example-core_network_policy_attachment"

  # Common attributes
  tags = {
    Name        = "example-core_network_policy_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Customer Gateway Association

```hcl
resource "aws_networkmanager_customer_gateway_association" "example" {
  # Example configuration for Customer Gateway Association
  name = "example-customer_gateway_association"

  # Common attributes
  tags = {
    Name        = "example-customer_gateway_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Device

```hcl
resource "aws_networkmanager_device" "example" {
  # Example configuration for Device
  name = "example-device"

  # Common attributes
  tags = {
    Name        = "example-device"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Direct Connect Gateway Attachment

```hcl
resource "aws_networkmanager_direct_connect_gateway_attachment" "example" {
  # Example configuration for Direct Connect Gateway Attachment
  name = "example-direct_connect_gateway_attachment"

  # Common attributes
  tags = {
    Name        = "example-direct_connect_gateway_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Global Network

```hcl
resource "aws_networkmanager_global_network" "example" {
  # Example configuration for Global Network
  name = "example-global_network"

  # Common attributes
  tags = {
    Name        = "example-global_network"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Link

```hcl
resource "aws_networkmanager_link" "example" {
  # Example configuration for Link
  name = "example-link"

  # Common attributes
  tags = {
    Name        = "example-link"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Link Association

```hcl
resource "aws_networkmanager_link_association" "example" {
  # Example configuration for Link Association
  name = "example-link_association"

  # Common attributes
  tags = {
    Name        = "example-link_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Site

```hcl
resource "aws_networkmanager_site" "example" {
  # Example configuration for Site
  name = "example-site"

  # Common attributes
  tags = {
    Name        = "example-site"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Site To Site VPN Attachment

```hcl
resource "aws_networkmanager_site_to_site_vpn_attachment" "example" {
  # Example configuration for Site To Site VPN Attachment
  name = "example-site_to_site_vpn_attachment"

  # Common attributes
  tags = {
    Name        = "example-site_to_site_vpn_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Connect Peer Association

```hcl
resource "aws_networkmanager_transit_gateway_connect_peer_association" "example" {
  # Example configuration for Transit Gateway Connect Peer Association
  name = "example-transit_gateway_connect_peer_association"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_connect_peer_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Peering

```hcl
resource "aws_networkmanager_transit_gateway_peering" "example" {
  # Example configuration for Transit Gateway Peering
  name = "example-transit_gateway_peering"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_peering"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Registration

```hcl
resource "aws_networkmanager_transit_gateway_registration" "example" {
  # Example configuration for Transit Gateway Registration
  name = "example-transit_gateway_registration"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_registration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transit Gateway Route Table Attachment

```hcl
resource "aws_networkmanager_transit_gateway_route_table_attachment" "example" {
  # Example configuration for Transit Gateway Route Table Attachment
  name = "example-transit_gateway_route_table_attachment"

  # Common attributes
  tags = {
    Name        = "example-transit_gateway_route_table_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Attachment

```hcl
resource "aws_networkmanager_vpc_attachment" "example" {
  # Example configuration for VPC Attachment
  name = "example-vpc_attachment"

  # Common attributes
  tags = {
    Name        = "example-vpc_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## networkmonitor

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Monitor | N/A | Framework |
| Probe | N/A | Framework |


### Examples


#### Monitor

```hcl
resource "aws_networkmonitor_monitor" "example" {
  # Example configuration for Monitor
  name = "example-monitor"

  # Common attributes
  tags = {
    Name        = "example-monitor"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Probe

```hcl
resource "aws_networkmonitor_probe" "example" {
  # Example configuration for Probe
  name = "example-probe"

  # Common attributes
  tags = {
    Name        = "example-probe"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## oam

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Link | aws_oam_link | SDK |
| Sink | aws_oam_sink | SDK |


### Examples


#### Link

```hcl
resource "aws_oam_link" "example" {
  # Example configuration for Link
  name = "example-link"

  # Common attributes
  tags = {
    Name        = "example-link"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Sink

```hcl
resource "aws_oam_sink" "example" {
  # Example configuration for Sink
  name = "example-sink"

  # Common attributes
  tags = {
    Name        = "example-sink"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## opensearch

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Authorize VPC Endpoint Access | N/A | Framework |
| Domain | aws_opensearch_domain | SDK |
| Domain Policy | aws_opensearch_domain_policy | SDK |
| Domain SAML Options | aws_opensearch_domain_saml_options | SDK |
| Inbound Connection Accepter | aws_opensearch_inbound_connection_accepter | SDK |
| Outbound Connection | aws_opensearch_outbound_connection | SDK |
| Package | aws_opensearch_package | SDK |
| Package Association | aws_opensearch_package_association | SDK |
| VPC Endpoint | aws_opensearch_vpc_endpoint | SDK |


### Examples


#### Authorize VPC Endpoint Access

```hcl
resource "aws_opensearch_authorize_vpc_endpoint_access" "example" {
  # Example configuration for Authorize VPC Endpoint Access
  name = "example-authorize_vpc_endpoint_access"

  # Common attributes
  tags = {
    Name        = "example-authorize_vpc_endpoint_access"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain

```hcl
resource "aws_opensearch_domain" "example" {
  # Example configuration for Domain
  name = "example-domain"

  # Common attributes
  tags = {
    Name        = "example-domain"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain Policy

```hcl
resource "aws_opensearch_domain_policy" "example" {
  # Example configuration for Domain Policy
  name = "example-domain_policy"

  # Common attributes
  tags = {
    Name        = "example-domain_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain SAML Options

```hcl
resource "aws_opensearch_domain_saml_options" "example" {
  # Example configuration for Domain SAML Options
  name = "example-domain_saml_options"

  # Common attributes
  tags = {
    Name        = "example-domain_saml_options"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Inbound Connection Accepter

```hcl
resource "aws_opensearch_inbound_connection_accepter" "example" {
  # Example configuration for Inbound Connection Accepter
  name = "example-inbound_connection_accepter"

  # Common attributes
  tags = {
    Name        = "example-inbound_connection_accepter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Outbound Connection

```hcl
resource "aws_opensearch_outbound_connection" "example" {
  # Example configuration for Outbound Connection
  name = "example-outbound_connection"

  # Common attributes
  tags = {
    Name        = "example-outbound_connection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Package

```hcl
resource "aws_opensearch_package" "example" {
  # Example configuration for Package
  name = "example-package"

  # Common attributes
  tags = {
    Name        = "example-package"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Package Association

```hcl
resource "aws_opensearch_package_association" "example" {
  # Example configuration for Package Association
  name = "example-package_association"

  # Common attributes
  tags = {
    Name        = "example-package_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Endpoint

```hcl
resource "aws_opensearch_vpc_endpoint" "example" {
  # Example configuration for VPC Endpoint
  name = "example-vpc_endpoint"

  # Common attributes
  tags = {
    Name        = "example-vpc_endpoint"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## opensearchserverless

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Access Policy | N/A | Framework |
| Collection | N/A | Framework |
| Lifecycle Policy | N/A | Framework |
| Security Config | N/A | Framework |
| Security Policy | N/A | Framework |
| VPC Endpoint | N/A | Framework |


### Examples


#### Access Policy

```hcl
resource "aws_opensearchserverless_access_policy" "example" {
  # Example configuration for Access Policy
  name = "example-access_policy"

  # Common attributes
  tags = {
    Name        = "example-access_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Collection

```hcl
resource "aws_opensearchserverless_collection" "example" {
  # Example configuration for Collection
  name = "example-collection"

  # Common attributes
  tags = {
    Name        = "example-collection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Lifecycle Policy

```hcl
resource "aws_opensearchserverless_lifecycle_policy" "example" {
  # Example configuration for Lifecycle Policy
  name = "example-lifecycle_policy"

  # Common attributes
  tags = {
    Name        = "example-lifecycle_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Security Config

```hcl
resource "aws_opensearchserverless_security_config" "example" {
  # Example configuration for Security Config
  name = "example-security_config"

  # Common attributes
  tags = {
    Name        = "example-security_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Security Policy

```hcl
resource "aws_opensearchserverless_security_policy" "example" {
  # Example configuration for Security Policy
  name = "example-security_policy"

  # Common attributes
  tags = {
    Name        = "example-security_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Endpoint

```hcl
resource "aws_opensearchserverless_vpc_endpoint" "example" {
  # Example configuration for VPC Endpoint
  name = "example-vpc_endpoint"

  # Common attributes
  tags = {
    Name        = "example-vpc_endpoint"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## opsworks

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Application | aws_opsworks_application | SDK |
| Custom Layer | aws_opsworks_custom_layer | SDK |
| ECS Cluster Layer | aws_opsworks_ecs_cluster_layer | SDK |
| Ganglia Layer | aws_opsworks_ganglia_layer | SDK |
| HAProxy Layer | aws_opsworks_haproxy_layer | SDK |
| Instance | aws_opsworks_instance | SDK |
| Java App Layer | aws_opsworks_java_app_layer | SDK |
| Memcached Layer | aws_opsworks_memcached_layer | SDK |
| MySQL Layer | aws_opsworks_mysql_layer | SDK |
| NodeJS App Layer | aws_opsworks_nodejs_app_layer | SDK |
| PHP App Layer | aws_opsworks_php_app_layer | SDK |
| Permission | aws_opsworks_permission | SDK |
| Profile | aws_opsworks_user_profile | SDK |
| RDS DB Instance | aws_opsworks_rds_db_instance | SDK |
| Rails App Layer | aws_opsworks_rails_app_layer | SDK |
| Stack | aws_opsworks_stack | SDK |
| Static Web Layer | aws_opsworks_static_web_layer | SDK |


### Examples


#### Application

```hcl
resource "aws_opsworks_application" "example" {
  # Example configuration for Application
  name = "example-application"

  # Common attributes
  tags = {
    Name        = "example-application"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Custom Layer

```hcl
resource "aws_opsworks_custom_layer" "example" {
  # Example configuration for Custom Layer
  name = "example-custom_layer"

  # Common attributes
  tags = {
    Name        = "example-custom_layer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### ECS Cluster Layer

```hcl
resource "aws_opsworks_ecs_cluster_layer" "example" {
  # Example configuration for ECS Cluster Layer
  name = "example-ecs_cluster_layer"

  # Common attributes
  tags = {
    Name        = "example-ecs_cluster_layer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Ganglia Layer

```hcl
resource "aws_opsworks_ganglia_layer" "example" {
  # Example configuration for Ganglia Layer
  name = "example-ganglia_layer"

  # Common attributes
  tags = {
    Name        = "example-ganglia_layer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### HAProxy Layer

```hcl
resource "aws_opsworks_haproxy_layer" "example" {
  # Example configuration for HAProxy Layer
  name = "example-haproxy_layer"

  # Common attributes
  tags = {
    Name        = "example-haproxy_layer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Instance

```hcl
resource "aws_opsworks_instance" "example" {
  # Example configuration for Instance
  name = "example-instance"

  # Common attributes
  tags = {
    Name        = "example-instance"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Java App Layer

```hcl
resource "aws_opsworks_java_app_layer" "example" {
  # Example configuration for Java App Layer
  name = "example-java_app_layer"

  # Common attributes
  tags = {
    Name        = "example-java_app_layer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Memcached Layer

```hcl
resource "aws_opsworks_memcached_layer" "example" {
  # Example configuration for Memcached Layer
  name = "example-memcached_layer"

  # Common attributes
  tags = {
    Name        = "example-memcached_layer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### MySQL Layer

```hcl
resource "aws_opsworks_mysql_layer" "example" {
  # Example configuration for MySQL Layer
  name = "example-mysql_layer"

  # Common attributes
  tags = {
    Name        = "example-mysql_layer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### NodeJS App Layer

```hcl
resource "aws_opsworks_nodejs_app_layer" "example" {
  # Example configuration for NodeJS App Layer
  name = "example-nodejs_app_layer"

  # Common attributes
  tags = {
    Name        = "example-nodejs_app_layer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### PHP App Layer

```hcl
resource "aws_opsworks_php_app_layer" "example" {
  # Example configuration for PHP App Layer
  name = "example-php_app_layer"

  # Common attributes
  tags = {
    Name        = "example-php_app_layer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Permission

```hcl
resource "aws_opsworks_permission" "example" {
  # Example configuration for Permission
  name = "example-permission"

  # Common attributes
  tags = {
    Name        = "example-permission"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Profile

```hcl
resource "aws_opsworks_user_profile" "example" {
  # Example configuration for Profile
  name = "example-profile"

  # Common attributes
  tags = {
    Name        = "example-profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### RDS DB Instance

```hcl
resource "aws_opsworks_rds_db_instance" "example" {
  # Example configuration for RDS DB Instance
  name = "example-rds_db_instance"

  # Common attributes
  tags = {
    Name        = "example-rds_db_instance"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Rails App Layer

```hcl
resource "aws_opsworks_rails_app_layer" "example" {
  # Example configuration for Rails App Layer
  name = "example-rails_app_layer"

  # Common attributes
  tags = {
    Name        = "example-rails_app_layer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Stack

```hcl
resource "aws_opsworks_stack" "example" {
  # Example configuration for Stack
  name = "example-stack"

  # Common attributes
  tags = {
    Name        = "example-stack"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Static Web Layer

```hcl
resource "aws_opsworks_static_web_layer" "example" {
  # Example configuration for Static Web Layer
  name = "example-static_web_layer"

  # Common attributes
  tags = {
    Name        = "example-static_web_layer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## organizations

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Account | aws_organizations_account | SDK |
| Delegated Administrator | aws_organizations_delegated_administrator | SDK |
| Organization | aws_organizations_organization | SDK |
| Organizational Unit | aws_organizations_organizational_unit | SDK |
| Policy | aws_organizations_policy | SDK |
| Policy Attachment | aws_organizations_policy_attachment | SDK |
| Resource Policy | aws_organizations_resource_policy | SDK |


### Examples


#### Account

```hcl
resource "aws_organizations_account" "example" {
  # Example configuration for Account
  name = "example-account"

  # Common attributes
  tags = {
    Name        = "example-account"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Delegated Administrator

```hcl
resource "aws_organizations_delegated_administrator" "example" {
  # Example configuration for Delegated Administrator
  name = "example-delegated_administrator"

  # Common attributes
  tags = {
    Name        = "example-delegated_administrator"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Organization

```hcl
resource "aws_organizations_organization" "example" {
  # Example configuration for Organization
  name = "example-organization"

  # Common attributes
  tags = {
    Name        = "example-organization"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Organizational Unit

```hcl
resource "aws_organizations_organizational_unit" "example" {
  # Example configuration for Organizational Unit
  name = "example-organizational_unit"

  # Common attributes
  tags = {
    Name        = "example-organizational_unit"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Policy

```hcl
resource "aws_organizations_policy" "example" {
  # Example configuration for Policy
  name = "example-policy"

  # Common attributes
  tags = {
    Name        = "example-policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Policy Attachment

```hcl
resource "aws_organizations_policy_attachment" "example" {
  # Example configuration for Policy Attachment
  name = "example-policy_attachment"

  # Common attributes
  tags = {
    Name        = "example-policy_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource Policy

```hcl
resource "aws_organizations_resource_policy" "example" {
  # Example configuration for Resource Policy
  name = "example-resource_policy"

  # Common attributes
  tags = {
    Name        = "example-resource_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## osis

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Pipeline | N/A | Framework |


### Examples


#### Pipeline

```hcl
resource "aws_osis_pipeline" "example" {
  # Example configuration for Pipeline
  name = "example-pipeline"

  # Common attributes
  tags = {
    Name        = "example-pipeline"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## paymentcryptography

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Key | N/A | Framework |
| Key Alias | N/A | Framework |


### Examples


#### Key

```hcl
resource "aws_paymentcryptography_key" "example" {
  # Example configuration for Key
  name = "example-key"

  # Common attributes
  tags = {
    Name        = "example-key"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Key Alias

```hcl
resource "aws_paymentcryptography_key_alias" "example" {
  # Example configuration for Key Alias
  name = "example-key_alias"

  # Common attributes
  tags = {
    Name        = "example-key_alias"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## pinpoint

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| ADM Channel | aws_pinpoint_adm_channel | SDK |
| APNS Channel | aws_pinpoint_apns_channel | SDK |
| APNS Sandbox Channel | aws_pinpoint_apns_sandbox_channel | SDK |
| APNS VoIP Channel | aws_pinpoint_apns_voip_channel | SDK |
| APNS VoIP Sandbox Channel | aws_pinpoint_apns_voip_sandbox_channel | SDK |
| App | aws_pinpoint_app | SDK |
| Baidu Channel | aws_pinpoint_baidu_channel | SDK |
| Email Channel | aws_pinpoint_email_channel | SDK |
| Email Template | N/A | Framework |
| Event Stream | aws_pinpoint_event_stream | SDK |
| GCM Channel | aws_pinpoint_gcm_channel | SDK |
| SMS Channel | aws_pinpoint_sms_channel | SDK |


### Examples


#### ADM Channel

```hcl
resource "aws_pinpoint_adm_channel" "example" {
  # Example configuration for ADM Channel
  name = "example-adm_channel"

  # Common attributes
  tags = {
    Name        = "example-adm_channel"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### APNS Channel

```hcl
resource "aws_pinpoint_apns_channel" "example" {
  # Example configuration for APNS Channel
  name = "example-apns_channel"

  # Common attributes
  tags = {
    Name        = "example-apns_channel"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### APNS Sandbox Channel

```hcl
resource "aws_pinpoint_apns_sandbox_channel" "example" {
  # Example configuration for APNS Sandbox Channel
  name = "example-apns_sandbox_channel"

  # Common attributes
  tags = {
    Name        = "example-apns_sandbox_channel"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### APNS VoIP Channel

```hcl
resource "aws_pinpoint_apns_voip_channel" "example" {
  # Example configuration for APNS VoIP Channel
  name = "example-apns_voip_channel"

  # Common attributes
  tags = {
    Name        = "example-apns_voip_channel"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### APNS VoIP Sandbox Channel

```hcl
resource "aws_pinpoint_apns_voip_sandbox_channel" "example" {
  # Example configuration for APNS VoIP Sandbox Channel
  name = "example-apns_voip_sandbox_channel"

  # Common attributes
  tags = {
    Name        = "example-apns_voip_sandbox_channel"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### App

```hcl
resource "aws_pinpoint_app" "example" {
  # Example configuration for App
  name = "example-app"

  # Common attributes
  tags = {
    Name        = "example-app"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Baidu Channel

```hcl
resource "aws_pinpoint_baidu_channel" "example" {
  # Example configuration for Baidu Channel
  name = "example-baidu_channel"

  # Common attributes
  tags = {
    Name        = "example-baidu_channel"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Email Channel

```hcl
resource "aws_pinpoint_email_channel" "example" {
  # Example configuration for Email Channel
  name = "example-email_channel"

  # Common attributes
  tags = {
    Name        = "example-email_channel"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Email Template

```hcl
resource "aws_pinpoint_email_template" "example" {
  # Example configuration for Email Template
  name = "example-email_template"

  # Common attributes
  tags = {
    Name        = "example-email_template"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Event Stream

```hcl
resource "aws_pinpoint_event_stream" "example" {
  # Example configuration for Event Stream
  name = "example-event_stream"

  # Common attributes
  tags = {
    Name        = "example-event_stream"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### GCM Channel

```hcl
resource "aws_pinpoint_gcm_channel" "example" {
  # Example configuration for GCM Channel
  name = "example-gcm_channel"

  # Common attributes
  tags = {
    Name        = "example-gcm_channel"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### SMS Channel

```hcl
resource "aws_pinpoint_sms_channel" "example" {
  # Example configuration for SMS Channel
  name = "example-sms_channel"

  # Common attributes
  tags = {
    Name        = "example-sms_channel"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## pinpointsmsvoicev2

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Configuration Set | N/A | Framework |
| Opt-out List | N/A | Framework |
| Phone Number | N/A | Framework |


### Examples


#### Configuration Set

```hcl
resource "aws_pinpointsmsvoicev2_configuration_set" "example" {
  # Example configuration for Configuration Set
  name = "example-configuration_set"

  # Common attributes
  tags = {
    Name        = "example-configuration_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Opt-out List

```hcl
resource "aws_pinpointsmsvoicev2_opt-out_list" "example" {
  # Example configuration for Opt-out List
  name = "example-opt-out_list"

  # Common attributes
  tags = {
    Name        = "example-opt-out_list"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Phone Number

```hcl
resource "aws_pinpointsmsvoicev2_phone_number" "example" {
  # Example configuration for Phone Number
  name = "example-phone_number"

  # Common attributes
  tags = {
    Name        = "example-phone_number"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## pipes

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Pipe | aws_pipes_pipe | SDK |


### Examples


#### Pipe

```hcl
resource "aws_pipes_pipe" "example" {
  # Example configuration for Pipe
  name = "example-pipe"

  # Common attributes
  tags = {
    Name        = "example-pipe"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## qldb

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Ledger | aws_qldb_ledger | SDK |
| Stream | aws_qldb_stream | SDK |


### Examples


#### Ledger

```hcl
resource "aws_qldb_ledger" "example" {
  # Example configuration for Ledger
  name = "example-ledger"

  # Common attributes
  tags = {
    Name        = "example-ledger"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Stream

```hcl
resource "aws_qldb_stream" "example" {
  # Example configuration for Stream
  name = "example-stream"

  # Common attributes
  tags = {
    Name        = "example-stream"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## quicksight

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Account Subscription | aws_quicksight_account_subscription | SDK |
| Analysis | aws_quicksight_analysis | SDK |
| Dashboard | aws_quicksight_dashboard | SDK |
| Data Set | aws_quicksight_data_set | SDK |
| Data Source | aws_quicksight_data_source | SDK |
| Folder | aws_quicksight_folder | SDK |
| Folder Membership | N/A | Framework |
| Group | aws_quicksight_group | SDK |
| Group Membership | aws_quicksight_group_membership | SDK |
| IAM Policy Assignment | N/A | Framework |
| Ingestion | N/A | Framework |
| Namespace | N/A | Framework |
| Refresh Schedule | N/A | Framework |
| Template | aws_quicksight_template | SDK |
| Template Alias | N/A | Framework |
| Theme | aws_quicksight_theme | SDK |
| User | aws_quicksight_user | SDK |
| VPC Connection | N/A | Framework |


### Examples


#### Account Subscription

```hcl
resource "aws_quicksight_account_subscription" "example" {
  # Example configuration for Account Subscription
  name = "example-account_subscription"

  # Common attributes
  tags = {
    Name        = "example-account_subscription"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Analysis

```hcl
resource "aws_quicksight_analysis" "example" {
  # Example configuration for Analysis
  name = "example-analysis"

  # Common attributes
  tags = {
    Name        = "example-analysis"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Dashboard

```hcl
resource "aws_quicksight_dashboard" "example" {
  # Example configuration for Dashboard
  name = "example-dashboard"

  # Common attributes
  tags = {
    Name        = "example-dashboard"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Data Set

```hcl
resource "aws_quicksight_data_set" "example" {
  # Example configuration for Data Set
  name = "example-data_set"

  # Common attributes
  tags = {
    Name        = "example-data_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Data Source

```hcl
resource "aws_quicksight_data_source" "example" {
  # Example configuration for Data Source
  name = "example-data_source"

  # Common attributes
  tags = {
    Name        = "example-data_source"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Folder

```hcl
resource "aws_quicksight_folder" "example" {
  # Example configuration for Folder
  name = "example-folder"

  # Common attributes
  tags = {
    Name        = "example-folder"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Folder Membership

```hcl
resource "aws_quicksight_folder_membership" "example" {
  # Example configuration for Folder Membership
  name = "example-folder_membership"

  # Common attributes
  tags = {
    Name        = "example-folder_membership"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Group

```hcl
resource "aws_quicksight_group" "example" {
  # Example configuration for Group
  name = "example-group"

  # Common attributes
  tags = {
    Name        = "example-group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Group Membership

```hcl
resource "aws_quicksight_group_membership" "example" {
  # Example configuration for Group Membership
  name = "example-group_membership"

  # Common attributes
  tags = {
    Name        = "example-group_membership"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### IAM Policy Assignment

```hcl
resource "aws_quicksight_iam_policy_assignment" "example" {
  # Example configuration for IAM Policy Assignment
  name = "example-iam_policy_assignment"

  # Common attributes
  tags = {
    Name        = "example-iam_policy_assignment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Ingestion

```hcl
resource "aws_quicksight_ingestion" "example" {
  # Example configuration for Ingestion
  name = "example-ingestion"

  # Common attributes
  tags = {
    Name        = "example-ingestion"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Namespace

```hcl
resource "aws_quicksight_namespace" "example" {
  # Example configuration for Namespace
  name = "example-namespace"

  # Common attributes
  tags = {
    Name        = "example-namespace"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Refresh Schedule

```hcl
resource "aws_quicksight_refresh_schedule" "example" {
  # Example configuration for Refresh Schedule
  name = "example-refresh_schedule"

  # Common attributes
  tags = {
    Name        = "example-refresh_schedule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Template

```hcl
resource "aws_quicksight_template" "example" {
  # Example configuration for Template
  name = "example-template"

  # Common attributes
  tags = {
    Name        = "example-template"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Template Alias

```hcl
resource "aws_quicksight_template_alias" "example" {
  # Example configuration for Template Alias
  name = "example-template_alias"

  # Common attributes
  tags = {
    Name        = "example-template_alias"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Theme

```hcl
resource "aws_quicksight_theme" "example" {
  # Example configuration for Theme
  name = "example-theme"

  # Common attributes
  tags = {
    Name        = "example-theme"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User

```hcl
resource "aws_quicksight_user" "example" {
  # Example configuration for User
  name = "example-user"

  # Common attributes
  tags = {
    Name        = "example-user"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Connection

```hcl
resource "aws_quicksight_vpc_connection" "example" {
  # Example configuration for VPC Connection
  name = "example-vpc_connection"

  # Common attributes
  tags = {
    Name        = "example-vpc_connection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## ram

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Principal Association | aws_ram_principal_association | SDK |
| Resource Association | aws_ram_resource_association | SDK |
| Resource Share | aws_ram_resource_share | SDK |
| Resource Share Accepter | aws_ram_resource_share_accepter | SDK |
| Sharing With Organization | aws_ram_sharing_with_organization | SDK |


### Examples


#### Principal Association

```hcl
resource "aws_ram_principal_association" "example" {
  # Example configuration for Principal Association
  name = "example-principal_association"

  # Common attributes
  tags = {
    Name        = "example-principal_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource Association

```hcl
resource "aws_ram_resource_association" "example" {
  # Example configuration for Resource Association
  name = "example-resource_association"

  # Common attributes
  tags = {
    Name        = "example-resource_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource Share

```hcl
resource "aws_ram_resource_share" "example" {
  # Example configuration for Resource Share
  name = "example-resource_share"

  # Common attributes
  tags = {
    Name        = "example-resource_share"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource Share Accepter

```hcl
resource "aws_ram_resource_share_accepter" "example" {
  # Example configuration for Resource Share Accepter
  name = "example-resource_share_accepter"

  # Common attributes
  tags = {
    Name        = "example-resource_share_accepter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Sharing With Organization

```hcl
resource "aws_ram_sharing_with_organization" "example" {
  # Example configuration for Sharing With Organization
  name = "example-sharing_with_organization"

  # Common attributes
  tags = {
    Name        = "example-sharing_with_organization"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## rbin

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Rule | aws_rbin_rule | SDK |


### Examples


#### Rule

```hcl
resource "aws_rbin_rule" "example" {
  # Example configuration for Rule
  name = "example-rule"

  # Common attributes
  tags = {
    Name        = "example-rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## rds

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Cluster | aws_rds_cluster | SDK |
| Cluster Activity Stream | aws_rds_cluster_activity_stream | SDK |
| Cluster Endpoint | aws_rds_cluster_endpoint | SDK |
| Cluster IAM Role Association | aws_rds_cluster_role_association | SDK |
| Cluster Instance | aws_rds_cluster_instance | SDK |
| Cluster Parameter Group | aws_rds_cluster_parameter_group | SDK |
| Cluster Snapshot Copy | N/A | Framework |
| Custom DB Engine Version | aws_rds_custom_db_engine_version | SDK |
| DB Cluster Snapshot | aws_db_cluster_snapshot | SDK |
| DB Instance | aws_db_instance | SDK |
| DB Instance IAM Role Association | aws_db_instance_role_association | SDK |
| DB Option Group | aws_db_option_group | SDK |
| DB Parameter Group | aws_db_parameter_group | SDK |
| DB Proxy | aws_db_proxy | SDK |
| DB Proxy Default Target Group | aws_db_proxy_default_target_group | SDK |
| DB Proxy Endpoint | aws_db_proxy_endpoint | SDK |
| DB Proxy Target | aws_db_proxy_target | SDK |
| DB Snapshot | aws_db_snapshot | SDK |
| DB Snapshot Copy | aws_db_snapshot_copy | SDK |
| DB Subnet Group | aws_db_subnet_group | SDK |
| Default Certificate | aws_rds_certificate | SDK |
| Event Subscription | aws_db_event_subscription | SDK |
| Global Cluster | aws_rds_global_cluster | SDK |
| Instance Automated Backups Replication | aws_db_instance_automated_backups_replication | SDK |
| Instance State | N/A | Framework |
| Integration | N/A | Framework |
| Reserved Instance | aws_rds_reserved_instance | SDK |


### Examples


#### Cluster

```hcl
resource "aws_rds_cluster" "example" {
  # Example configuration for Cluster
  name = "example-cluster"

  # Common attributes
  tags = {
    Name        = "example-cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster Activity Stream

```hcl
resource "aws_rds_cluster_activity_stream" "example" {
  # Example configuration for Cluster Activity Stream
  name = "example-cluster_activity_stream"

  # Common attributes
  tags = {
    Name        = "example-cluster_activity_stream"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster Endpoint

```hcl
resource "aws_rds_cluster_endpoint" "example" {
  # Example configuration for Cluster Endpoint
  name = "example-cluster_endpoint"

  # Common attributes
  tags = {
    Name        = "example-cluster_endpoint"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster IAM Role Association

```hcl
resource "aws_rds_cluster_role_association" "example" {
  # Example configuration for Cluster IAM Role Association
  name = "example-cluster_iam_role_association"

  # Common attributes
  tags = {
    Name        = "example-cluster_iam_role_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster Instance

```hcl
resource "aws_rds_cluster_instance" "example" {
  # Example configuration for Cluster Instance
  name = "example-cluster_instance"

  # Common attributes
  tags = {
    Name        = "example-cluster_instance"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster Parameter Group

```hcl
resource "aws_rds_cluster_parameter_group" "example" {
  # Example configuration for Cluster Parameter Group
  name = "example-cluster_parameter_group"

  # Common attributes
  tags = {
    Name        = "example-cluster_parameter_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster Snapshot Copy

```hcl
resource "aws_rds_cluster_snapshot_copy" "example" {
  # Example configuration for Cluster Snapshot Copy
  name = "example-cluster_snapshot_copy"

  # Common attributes
  tags = {
    Name        = "example-cluster_snapshot_copy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Custom DB Engine Version

```hcl
resource "aws_rds_custom_db_engine_version" "example" {
  # Example configuration for Custom DB Engine Version
  name = "example-custom_db_engine_version"

  # Common attributes
  tags = {
    Name        = "example-custom_db_engine_version"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### DB Cluster Snapshot

```hcl
resource "aws_db_cluster_snapshot" "example" {
  # Example configuration for DB Cluster Snapshot
  name = "example-db_cluster_snapshot"

  # Common attributes
  tags = {
    Name        = "example-db_cluster_snapshot"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### DB Instance

```hcl
resource "aws_db_instance" "example" {
  allocated_storage    = 10
  db_name              = "example"
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.t3.micro"
  username             = "admin"
  password             = "password"
  parameter_group_name = "default.mysql5.7"
  skip_final_snapshot  = true
}
```


#### DB Instance IAM Role Association

```hcl
resource "aws_db_instance_role_association" "example" {
  # Example configuration for DB Instance IAM Role Association
  name = "example-db_instance_iam_role_association"

  # Common attributes
  tags = {
    Name        = "example-db_instance_iam_role_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### DB Option Group

```hcl
resource "aws_db_option_group" "example" {
  # Example configuration for DB Option Group
  name = "example-db_option_group"

  # Common attributes
  tags = {
    Name        = "example-db_option_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### DB Parameter Group

```hcl
resource "aws_db_parameter_group" "example" {
  # Example configuration for DB Parameter Group
  name = "example-db_parameter_group"

  # Common attributes
  tags = {
    Name        = "example-db_parameter_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### DB Proxy

```hcl
resource "aws_db_proxy" "example" {
  # Example configuration for DB Proxy
  name = "example-db_proxy"

  # Common attributes
  tags = {
    Name        = "example-db_proxy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### DB Proxy Default Target Group

```hcl
resource "aws_db_proxy_default_target_group" "example" {
  # Example configuration for DB Proxy Default Target Group
  name = "example-db_proxy_default_target_group"

  # Common attributes
  tags = {
    Name        = "example-db_proxy_default_target_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### DB Proxy Endpoint

```hcl
resource "aws_db_proxy_endpoint" "example" {
  # Example configuration for DB Proxy Endpoint
  name = "example-db_proxy_endpoint"

  # Common attributes
  tags = {
    Name        = "example-db_proxy_endpoint"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### DB Proxy Target

```hcl
resource "aws_db_proxy_target" "example" {
  # Example configuration for DB Proxy Target
  name = "example-db_proxy_target"

  # Common attributes
  tags = {
    Name        = "example-db_proxy_target"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### DB Snapshot

```hcl
resource "aws_db_snapshot" "example" {
  # Example configuration for DB Snapshot
  name = "example-db_snapshot"

  # Common attributes
  tags = {
    Name        = "example-db_snapshot"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### DB Snapshot Copy

```hcl
resource "aws_db_snapshot_copy" "example" {
  # Example configuration for DB Snapshot Copy
  name = "example-db_snapshot_copy"

  # Common attributes
  tags = {
    Name        = "example-db_snapshot_copy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### DB Subnet Group

```hcl
resource "aws_db_subnet_group" "example" {
  # Example configuration for DB Subnet Group
  name = "example-db_subnet_group"

  # Common attributes
  tags = {
    Name        = "example-db_subnet_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Default Certificate

```hcl
resource "aws_rds_certificate" "example" {
  # Example configuration for Default Certificate
  name = "example-default_certificate"

  # Common attributes
  tags = {
    Name        = "example-default_certificate"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Event Subscription

```hcl
resource "aws_db_event_subscription" "example" {
  # Example configuration for Event Subscription
  name = "example-event_subscription"

  # Common attributes
  tags = {
    Name        = "example-event_subscription"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Global Cluster

```hcl
resource "aws_rds_global_cluster" "example" {
  # Example configuration for Global Cluster
  name = "example-global_cluster"

  # Common attributes
  tags = {
    Name        = "example-global_cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Instance Automated Backups Replication

```hcl
resource "aws_db_instance_automated_backups_replication" "example" {
  # Example configuration for Instance Automated Backups Replication
  name = "example-instance_automated_backups_replication"

  # Common attributes
  tags = {
    Name        = "example-instance_automated_backups_replication"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Instance State

```hcl
resource "aws_rds_instance_state" "example" {
  # Example configuration for Instance State
  name = "example-instance_state"

  # Common attributes
  tags = {
    Name        = "example-instance_state"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Integration

```hcl
resource "aws_rds_integration" "example" {
  # Example configuration for Integration
  name = "example-integration"

  # Common attributes
  tags = {
    Name        = "example-integration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Reserved Instance

```hcl
resource "aws_rds_reserved_instance" "example" {
  # Example configuration for Reserved Instance
  name = "example-reserved_instance"

  # Common attributes
  tags = {
    Name        = "example-reserved_instance"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## redshift

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Authentication Profile | aws_redshift_authentication_profile | SDK |
| Cluster | aws_redshift_cluster | SDK |
| Cluster IAM Roles | aws_redshift_cluster_iam_roles | SDK |
| Cluster Snapshot | aws_redshift_cluster_snapshot | SDK |
| Data Share Authorization | N/A | Framework |
| Data Share Consumer Association | N/A | Framework |
| Endpoint Access | aws_redshift_endpoint_access | SDK |
| Endpoint Authorization | aws_redshift_endpoint_authorization | SDK |
| Event Subscription | aws_redshift_event_subscription | SDK |
| HSM Client Certificate | aws_redshift_hsm_client_certificate | SDK |
| HSM Configuration | aws_redshift_hsm_configuration | SDK |
| Logging | N/A | Framework |
| Parameter Group | aws_redshift_parameter_group | SDK |
| Partner | aws_redshift_partner | SDK |
| Resource Policy | aws_redshift_resource_policy | SDK |
| Scheduled Action | aws_redshift_scheduled_action | SDK |
| Snapshot Copy | N/A | Framework |
| Snapshot Copy Grant | aws_redshift_snapshot_copy_grant | SDK |
| Snapshot Schedule | aws_redshift_snapshot_schedule | SDK |
| Snapshot Schedule Association | aws_redshift_snapshot_schedule_association | SDK |
| Subnet Group | aws_redshift_subnet_group | SDK |
| Usage Limit | aws_redshift_usage_limit | SDK |


### Examples


#### Authentication Profile

```hcl
resource "aws_redshift_authentication_profile" "example" {
  # Example configuration for Authentication Profile
  name = "example-authentication_profile"

  # Common attributes
  tags = {
    Name        = "example-authentication_profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster

```hcl
resource "aws_redshift_cluster" "example" {
  # Example configuration for Cluster
  name = "example-cluster"

  # Common attributes
  tags = {
    Name        = "example-cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster IAM Roles

```hcl
resource "aws_redshift_cluster_iam_roles" "example" {
  # Example configuration for Cluster IAM Roles
  name = "example-cluster_iam_roles"

  # Common attributes
  tags = {
    Name        = "example-cluster_iam_roles"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cluster Snapshot

```hcl
resource "aws_redshift_cluster_snapshot" "example" {
  # Example configuration for Cluster Snapshot
  name = "example-cluster_snapshot"

  # Common attributes
  tags = {
    Name        = "example-cluster_snapshot"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Data Share Authorization

```hcl
resource "aws_redshift_data_share_authorization" "example" {
  # Example configuration for Data Share Authorization
  name = "example-data_share_authorization"

  # Common attributes
  tags = {
    Name        = "example-data_share_authorization"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Data Share Consumer Association

```hcl
resource "aws_redshift_data_share_consumer_association" "example" {
  # Example configuration for Data Share Consumer Association
  name = "example-data_share_consumer_association"

  # Common attributes
  tags = {
    Name        = "example-data_share_consumer_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Endpoint Access

```hcl
resource "aws_redshift_endpoint_access" "example" {
  # Example configuration for Endpoint Access
  name = "example-endpoint_access"

  # Common attributes
  tags = {
    Name        = "example-endpoint_access"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Endpoint Authorization

```hcl
resource "aws_redshift_endpoint_authorization" "example" {
  # Example configuration for Endpoint Authorization
  name = "example-endpoint_authorization"

  # Common attributes
  tags = {
    Name        = "example-endpoint_authorization"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Event Subscription

```hcl
resource "aws_redshift_event_subscription" "example" {
  # Example configuration for Event Subscription
  name = "example-event_subscription"

  # Common attributes
  tags = {
    Name        = "example-event_subscription"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### HSM Client Certificate

```hcl
resource "aws_redshift_hsm_client_certificate" "example" {
  # Example configuration for HSM Client Certificate
  name = "example-hsm_client_certificate"

  # Common attributes
  tags = {
    Name        = "example-hsm_client_certificate"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### HSM Configuration

```hcl
resource "aws_redshift_hsm_configuration" "example" {
  # Example configuration for HSM Configuration
  name = "example-hsm_configuration"

  # Common attributes
  tags = {
    Name        = "example-hsm_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Logging

```hcl
resource "aws_redshift_logging" "example" {
  # Example configuration for Logging
  name = "example-logging"

  # Common attributes
  tags = {
    Name        = "example-logging"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Parameter Group

```hcl
resource "aws_redshift_parameter_group" "example" {
  # Example configuration for Parameter Group
  name = "example-parameter_group"

  # Common attributes
  tags = {
    Name        = "example-parameter_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Partner

```hcl
resource "aws_redshift_partner" "example" {
  # Example configuration for Partner
  name = "example-partner"

  # Common attributes
  tags = {
    Name        = "example-partner"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource Policy

```hcl
resource "aws_redshift_resource_policy" "example" {
  # Example configuration for Resource Policy
  name = "example-resource_policy"

  # Common attributes
  tags = {
    Name        = "example-resource_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Scheduled Action

```hcl
resource "aws_redshift_scheduled_action" "example" {
  # Example configuration for Scheduled Action
  name = "example-scheduled_action"

  # Common attributes
  tags = {
    Name        = "example-scheduled_action"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Snapshot Copy

```hcl
resource "aws_redshift_snapshot_copy" "example" {
  # Example configuration for Snapshot Copy
  name = "example-snapshot_copy"

  # Common attributes
  tags = {
    Name        = "example-snapshot_copy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Snapshot Copy Grant

```hcl
resource "aws_redshift_snapshot_copy_grant" "example" {
  # Example configuration for Snapshot Copy Grant
  name = "example-snapshot_copy_grant"

  # Common attributes
  tags = {
    Name        = "example-snapshot_copy_grant"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Snapshot Schedule

```hcl
resource "aws_redshift_snapshot_schedule" "example" {
  # Example configuration for Snapshot Schedule
  name = "example-snapshot_schedule"

  # Common attributes
  tags = {
    Name        = "example-snapshot_schedule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Snapshot Schedule Association

```hcl
resource "aws_redshift_snapshot_schedule_association" "example" {
  # Example configuration for Snapshot Schedule Association
  name = "example-snapshot_schedule_association"

  # Common attributes
  tags = {
    Name        = "example-snapshot_schedule_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Subnet Group

```hcl
resource "aws_redshift_subnet_group" "example" {
  # Example configuration for Subnet Group
  name = "example-subnet_group"

  # Common attributes
  tags = {
    Name        = "example-subnet_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Usage Limit

```hcl
resource "aws_redshift_usage_limit" "example" {
  # Example configuration for Usage Limit
  name = "example-usage_limit"

  # Common attributes
  tags = {
    Name        = "example-usage_limit"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## redshiftserverless

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Custom Domain Association | N/A | Framework |
| Endpoint Access | aws_redshiftserverless_endpoint_access | SDK |
| Namespace | aws_redshiftserverless_namespace | SDK |
| Resource Policy | aws_redshiftserverless_resource_policy | SDK |
| Snapshot | aws_redshiftserverless_snapshot | SDK |
| Usage Limit | aws_redshiftserverless_usage_limit | SDK |
| Workgroup | aws_redshiftserverless_workgroup | SDK |


### Examples


#### Custom Domain Association

```hcl
resource "aws_redshiftserverless_custom_domain_association" "example" {
  # Example configuration for Custom Domain Association
  name = "example-custom_domain_association"

  # Common attributes
  tags = {
    Name        = "example-custom_domain_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Endpoint Access

```hcl
resource "aws_redshiftserverless_endpoint_access" "example" {
  # Example configuration for Endpoint Access
  name = "example-endpoint_access"

  # Common attributes
  tags = {
    Name        = "example-endpoint_access"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Namespace

```hcl
resource "aws_redshiftserverless_namespace" "example" {
  # Example configuration for Namespace
  name = "example-namespace"

  # Common attributes
  tags = {
    Name        = "example-namespace"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource Policy

```hcl
resource "aws_redshiftserverless_resource_policy" "example" {
  # Example configuration for Resource Policy
  name = "example-resource_policy"

  # Common attributes
  tags = {
    Name        = "example-resource_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Snapshot

```hcl
resource "aws_redshiftserverless_snapshot" "example" {
  # Example configuration for Snapshot
  name = "example-snapshot"

  # Common attributes
  tags = {
    Name        = "example-snapshot"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Usage Limit

```hcl
resource "aws_redshiftserverless_usage_limit" "example" {
  # Example configuration for Usage Limit
  name = "example-usage_limit"

  # Common attributes
  tags = {
    Name        = "example-usage_limit"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Workgroup

```hcl
resource "aws_redshiftserverless_workgroup" "example" {
  # Example configuration for Workgroup
  name = "example-workgroup"

  # Common attributes
  tags = {
    Name        = "example-workgroup"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## rekognition

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Collection | N/A | Framework |
| Project | N/A | Framework |
| Stream Processor | N/A | Framework |


### Examples


#### Collection

```hcl
resource "aws_rekognition_collection" "example" {
  # Example configuration for Collection
  name = "example-collection"

  # Common attributes
  tags = {
    Name        = "example-collection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Project

```hcl
resource "aws_rekognition_project" "example" {
  # Example configuration for Project
  name = "example-project"

  # Common attributes
  tags = {
    Name        = "example-project"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Stream Processor

```hcl
resource "aws_rekognition_stream_processor" "example" {
  # Example configuration for Stream Processor
  name = "example-stream_processor"

  # Common attributes
  tags = {
    Name        = "example-stream_processor"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## resiliencehub

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Resiliency Policy | N/A | Framework |


### Examples


#### Resiliency Policy

```hcl
resource "aws_resiliencehub_resiliency_policy" "example" {
  # Example configuration for Resiliency Policy
  name = "example-resiliency_policy"

  # Common attributes
  tags = {
    Name        = "example-resiliency_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## resourceexplorer2

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Index | N/A | Framework |
| View | N/A | Framework |


### Examples


#### Index

```hcl
resource "aws_resourceexplorer2_index" "example" {
  # Example configuration for Index
  name = "example-index"

  # Common attributes
  tags = {
    Name        = "example-index"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### View

```hcl
resource "aws_resourceexplorer2_view" "example" {
  # Example configuration for View
  name = "example-view"

  # Common attributes
  tags = {
    Name        = "example-view"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## resourcegroups

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Group | aws_resourcegroups_group | SDK |
| Resource | aws_resourcegroups_resource | SDK |


### Examples


#### Group

```hcl
resource "aws_resourcegroups_group" "example" {
  # Example configuration for Group
  name = "example-group"

  # Common attributes
  tags = {
    Name        = "example-group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource

```hcl
resource "aws_resourcegroups_resource" "example" {
  # Example configuration for Resource
  name = "example-resource"

  # Common attributes
  tags = {
    Name        = "example-resource"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## rolesanywhere

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Profile | aws_rolesanywhere_profile | SDK |
| Trust Anchor | aws_rolesanywhere_trust_anchor | SDK |


### Examples


#### Profile

```hcl
resource "aws_rolesanywhere_profile" "example" {
  # Example configuration for Profile
  name = "example-profile"

  # Common attributes
  tags = {
    Name        = "example-profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Trust Anchor

```hcl
resource "aws_rolesanywhere_trust_anchor" "example" {
  # Example configuration for Trust Anchor
  name = "example-trust_anchor"

  # Common attributes
  tags = {
    Name        = "example-trust_anchor"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## route53

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| CIDR Collection | N/A | Framework |
| CIDR Location | N/A | Framework |
| Health Check | aws_route53_health_check | SDK |
| Hosted Zone | aws_route53_zone | SDK |
| Hosted Zone DNSSEC | aws_route53_hosted_zone_dnssec | SDK |
| Key Signing Key | aws_route53_key_signing_key | SDK |
| Query Logging Config | aws_route53_query_log | SDK |
| Record | aws_route53_record | SDK |
| Reusable Delegation Set | aws_route53_delegation_set | SDK |
| Traffic Policy | aws_route53_traffic_policy | SDK |
| Traffic Policy Instance | aws_route53_traffic_policy_instance | SDK |
| VPC Association Authorization | aws_route53_vpc_association_authorization | SDK |
| Zone Association | aws_route53_zone_association | SDK |


### Examples


#### CIDR Collection

```hcl
resource "aws_route53_cidr_collection" "example" {
  # Example configuration for CIDR Collection
  name = "example-cidr_collection"

  # Common attributes
  tags = {
    Name        = "example-cidr_collection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### CIDR Location

```hcl
resource "aws_route53_cidr_location" "example" {
  # Example configuration for CIDR Location
  name = "example-cidr_location"

  # Common attributes
  tags = {
    Name        = "example-cidr_location"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Health Check

```hcl
resource "aws_route53_health_check" "example" {
  # Example configuration for Health Check
  name = "example-health_check"

  # Common attributes
  tags = {
    Name        = "example-health_check"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Hosted Zone

```hcl
resource "aws_route53_zone" "example" {
  name = "example.com"
}
```


#### Hosted Zone DNSSEC

```hcl
resource "aws_route53_hosted_zone_dnssec" "example" {
  # Example configuration for Hosted Zone DNSSEC
  name = "example-hosted_zone_dnssec"

  # Common attributes
  tags = {
    Name        = "example-hosted_zone_dnssec"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Key Signing Key

```hcl
resource "aws_route53_key_signing_key" "example" {
  # Example configuration for Key Signing Key
  name = "example-key_signing_key"

  # Common attributes
  tags = {
    Name        = "example-key_signing_key"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Query Logging Config

```hcl
resource "aws_route53_query_log" "example" {
  # Example configuration for Query Logging Config
  name = "example-query_logging_config"

  # Common attributes
  tags = {
    Name        = "example-query_logging_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Record

```hcl
resource "aws_route53_record" "example" {
  zone_id = aws_route53_zone.example.zone_id
  name    = "www.example.com"
  type    = "A"
  ttl     = 300
  records = ["10.0.0.1"]
}
```


#### Reusable Delegation Set

```hcl
resource "aws_route53_delegation_set" "example" {
  # Example configuration for Reusable Delegation Set
  name = "example-reusable_delegation_set"

  # Common attributes
  tags = {
    Name        = "example-reusable_delegation_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Traffic Policy

```hcl
resource "aws_route53_traffic_policy" "example" {
  # Example configuration for Traffic Policy
  name = "example-traffic_policy"

  # Common attributes
  tags = {
    Name        = "example-traffic_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Traffic Policy Instance

```hcl
resource "aws_route53_traffic_policy_instance" "example" {
  # Example configuration for Traffic Policy Instance
  name = "example-traffic_policy_instance"

  # Common attributes
  tags = {
    Name        = "example-traffic_policy_instance"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### VPC Association Authorization

```hcl
resource "aws_route53_vpc_association_authorization" "example" {
  # Example configuration for VPC Association Authorization
  name = "example-vpc_association_authorization"

  # Common attributes
  tags = {
    Name        = "example-vpc_association_authorization"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Zone Association

```hcl
resource "aws_route53_zone_association" "example" {
  # Example configuration for Zone Association
  name = "example-zone_association"

  # Common attributes
  tags = {
    Name        = "example-zone_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## route53domains

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Delegation Signer Record | N/A | Framework |
| Registered Domain | aws_route53domains_registered_domain | SDK |


### Examples


#### Delegation Signer Record

```hcl
resource "aws_route53domains_delegation_signer_record" "example" {
  # Example configuration for Delegation Signer Record
  name = "example-delegation_signer_record"

  # Common attributes
  tags = {
    Name        = "example-delegation_signer_record"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Registered Domain

```hcl
resource "aws_route53domains_registered_domain" "example" {
  # Example configuration for Registered Domain
  name = "example-registered_domain"

  # Common attributes
  tags = {
    Name        = "example-registered_domain"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## route53profiles

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Association | N/A | Framework |
| Profile | N/A | Framework |
| ResourceAssociation | N/A | Framework |


### Examples


#### Association

```hcl
resource "aws_route53profiles_association" "example" {
  # Example configuration for Association
  name = "example-association"

  # Common attributes
  tags = {
    Name        = "example-association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Profile

```hcl
resource "aws_route53profiles_profile" "example" {
  # Example configuration for Profile
  name = "example-profile"

  # Common attributes
  tags = {
    Name        = "example-profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### ResourceAssociation

```hcl
resource "aws_route53profiles_resourceassociation" "example" {
  # Example configuration for ResourceAssociation
  name = "example-resourceassociation"

  # Common attributes
  tags = {
    Name        = "example-resourceassociation"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## route53recoverycontrolconfig

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Cluster | aws_route53recoverycontrolconfig_cluster | SDK |
| Control Panel | aws_route53recoverycontrolconfig_control_panel | SDK |
| Routing Control | aws_route53recoverycontrolconfig_routing_control | SDK |
| Safety Rule | aws_route53recoverycontrolconfig_safety_rule | SDK |


### Examples


#### Cluster

```hcl
resource "aws_route53recoverycontrolconfig_cluster" "example" {
  # Example configuration for Cluster
  name = "example-cluster"

  # Common attributes
  tags = {
    Name        = "example-cluster"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Control Panel

```hcl
resource "aws_route53recoverycontrolconfig_control_panel" "example" {
  # Example configuration for Control Panel
  name = "example-control_panel"

  # Common attributes
  tags = {
    Name        = "example-control_panel"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Routing Control

```hcl
resource "aws_route53recoverycontrolconfig_routing_control" "example" {
  # Example configuration for Routing Control
  name = "example-routing_control"

  # Common attributes
  tags = {
    Name        = "example-routing_control"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Safety Rule

```hcl
resource "aws_route53recoverycontrolconfig_safety_rule" "example" {
  # Example configuration for Safety Rule
  name = "example-safety_rule"

  # Common attributes
  tags = {
    Name        = "example-safety_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## route53recoveryreadiness

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Cell | aws_route53recoveryreadiness_cell | SDK |
| Readiness Check | aws_route53recoveryreadiness_readiness_check | SDK |
| Recovery Group | aws_route53recoveryreadiness_recovery_group | SDK |
| Resource Set | aws_route53recoveryreadiness_resource_set | SDK |


### Examples


#### Cell

```hcl
resource "aws_route53recoveryreadiness_cell" "example" {
  # Example configuration for Cell
  name = "example-cell"

  # Common attributes
  tags = {
    Name        = "example-cell"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Readiness Check

```hcl
resource "aws_route53recoveryreadiness_readiness_check" "example" {
  # Example configuration for Readiness Check
  name = "example-readiness_check"

  # Common attributes
  tags = {
    Name        = "example-readiness_check"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Recovery Group

```hcl
resource "aws_route53recoveryreadiness_recovery_group" "example" {
  # Example configuration for Recovery Group
  name = "example-recovery_group"

  # Common attributes
  tags = {
    Name        = "example-recovery_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource Set

```hcl
resource "aws_route53recoveryreadiness_resource_set" "example" {
  # Example configuration for Resource Set
  name = "example-resource_set"

  # Common attributes
  tags = {
    Name        = "example-resource_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## route53resolver

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Config | aws_route53_resolver_config | SDK |
| DNSSEC Config | aws_route53_resolver_dnssec_config | SDK |
| Endpoint | aws_route53_resolver_endpoint | SDK |
| Firewall Config | aws_route53_resolver_firewall_config | SDK |
| Firewall Domain List | aws_route53_resolver_firewall_domain_list | SDK |
| Firewall Rule | aws_route53_resolver_firewall_rule | SDK |
| Firewall Rule Group | aws_route53_resolver_firewall_rule_group | SDK |
| Firewall Rule Group Association | aws_route53_resolver_firewall_rule_group_association | SDK |
| Query Log Config | aws_route53_resolver_query_log_config | SDK |
| Query Log Config Association | aws_route53_resolver_query_log_config_association | SDK |
| Rule | aws_route53_resolver_rule | SDK |
| Rule Association | aws_route53_resolver_rule_association | SDK |


### Examples


#### Config

```hcl
resource "aws_route53_resolver_config" "example" {
  # Example configuration for Config
  name = "example-config"

  # Common attributes
  tags = {
    Name        = "example-config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### DNSSEC Config

```hcl
resource "aws_route53_resolver_dnssec_config" "example" {
  # Example configuration for DNSSEC Config
  name = "example-dnssec_config"

  # Common attributes
  tags = {
    Name        = "example-dnssec_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Endpoint

```hcl
resource "aws_route53_resolver_endpoint" "example" {
  # Example configuration for Endpoint
  name = "example-endpoint"

  # Common attributes
  tags = {
    Name        = "example-endpoint"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Firewall Config

```hcl
resource "aws_route53_resolver_firewall_config" "example" {
  # Example configuration for Firewall Config
  name = "example-firewall_config"

  # Common attributes
  tags = {
    Name        = "example-firewall_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Firewall Domain List

```hcl
resource "aws_route53_resolver_firewall_domain_list" "example" {
  # Example configuration for Firewall Domain List
  name = "example-firewall_domain_list"

  # Common attributes
  tags = {
    Name        = "example-firewall_domain_list"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Firewall Rule

```hcl
resource "aws_route53_resolver_firewall_rule" "example" {
  # Example configuration for Firewall Rule
  name = "example-firewall_rule"

  # Common attributes
  tags = {
    Name        = "example-firewall_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Firewall Rule Group

```hcl
resource "aws_route53_resolver_firewall_rule_group" "example" {
  # Example configuration for Firewall Rule Group
  name = "example-firewall_rule_group"

  # Common attributes
  tags = {
    Name        = "example-firewall_rule_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Firewall Rule Group Association

```hcl
resource "aws_route53_resolver_firewall_rule_group_association" "example" {
  # Example configuration for Firewall Rule Group Association
  name = "example-firewall_rule_group_association"

  # Common attributes
  tags = {
    Name        = "example-firewall_rule_group_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Query Log Config

```hcl
resource "aws_route53_resolver_query_log_config" "example" {
  # Example configuration for Query Log Config
  name = "example-query_log_config"

  # Common attributes
  tags = {
    Name        = "example-query_log_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Query Log Config Association

```hcl
resource "aws_route53_resolver_query_log_config_association" "example" {
  # Example configuration for Query Log Config Association
  name = "example-query_log_config_association"

  # Common attributes
  tags = {
    Name        = "example-query_log_config_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Rule

```hcl
resource "aws_route53_resolver_rule" "example" {
  # Example configuration for Rule
  name = "example-rule"

  # Common attributes
  tags = {
    Name        = "example-rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Rule Association

```hcl
resource "aws_route53_resolver_rule_association" "example" {
  # Example configuration for Rule Association
  name = "example-rule_association"

  # Common attributes
  tags = {
    Name        = "example-rule_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## rum

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| App Monitor | aws_rum_app_monitor | SDK |
| Metrics Destination | aws_rum_metrics_destination | SDK |


### Examples


#### App Monitor

```hcl
resource "aws_rum_app_monitor" "example" {
  # Example configuration for App Monitor
  name = "example-app_monitor"

  # Common attributes
  tags = {
    Name        = "example-app_monitor"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Metrics Destination

```hcl
resource "aws_rum_metrics_destination" "example" {
  # Example configuration for Metrics Destination
  name = "example-metrics_destination"

  # Common attributes
  tags = {
    Name        = "example-metrics_destination"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## s3

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Bucket | aws_s3_bucket | SDK |
| Bucket ACL | aws_s3_bucket_acl | SDK |
| Bucket Accelerate Configuration | aws_s3_bucket_accelerate_configuration | SDK |
| Bucket Analytics Configuration | aws_s3_bucket_analytics_configuration | SDK |
| Bucket CORS Configuration | aws_s3_bucket_cors_configuration | SDK |
| Bucket Intelligent-Tiering Configuration | aws_s3_bucket_intelligent_tiering_configuration | SDK |
| Bucket Inventory | aws_s3_bucket_inventory | SDK |
| Bucket Lifecycle Configuration | aws_s3_bucket_lifecycle_configuration | SDK |
| Bucket Logging | aws_s3_bucket_logging | SDK |
| Bucket Metric | aws_s3_bucket_metric | SDK |
| Bucket Notification | aws_s3_bucket_notification | SDK |
| Bucket Object | aws_s3_bucket_object | SDK |
| Bucket Object Lock Configuration | aws_s3_bucket_object_lock_configuration | SDK |
| Bucket Ownership Controls | aws_s3_bucket_ownership_controls | SDK |
| Bucket Policy | aws_s3_bucket_policy | SDK |
| Bucket Public Access Block | aws_s3_bucket_public_access_block | SDK |
| Bucket Replication Configuration | aws_s3_bucket_replication_configuration | SDK |
| Bucket Request Payment Configuration | aws_s3_bucket_request_payment_configuration | SDK |
| Bucket Server-side Encryption Configuration | aws_s3_bucket_server_side_encryption_configuration | SDK |
| Bucket Versioning | aws_s3_bucket_versioning | SDK |
| Bucket Website Configuration | aws_s3_bucket_website_configuration | SDK |
| Directory Bucket | N/A | Framework |
| Object | aws_s3_object | SDK |
| Object Copy | aws_s3_object_copy | SDK |


### Examples


#### Bucket

```hcl
resource "aws_s3_bucket" "example" {
  bucket = "example-bucket-name"

  tags = {
    Name = "example-bucket"
  }
}
```


#### Bucket ACL

```hcl
resource "aws_s3_bucket_acl" "example" {
  # Example configuration for Bucket ACL
  name = "example-bucket_acl"

  # Common attributes
  tags = {
    Name        = "example-bucket_acl"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket Accelerate Configuration

```hcl
resource "aws_s3_bucket_accelerate_configuration" "example" {
  # Example configuration for Bucket Accelerate Configuration
  name = "example-bucket_accelerate_configuration"

  # Common attributes
  tags = {
    Name        = "example-bucket_accelerate_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket Analytics Configuration

```hcl
resource "aws_s3_bucket_analytics_configuration" "example" {
  # Example configuration for Bucket Analytics Configuration
  name = "example-bucket_analytics_configuration"

  # Common attributes
  tags = {
    Name        = "example-bucket_analytics_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket CORS Configuration

```hcl
resource "aws_s3_bucket_cors_configuration" "example" {
  # Example configuration for Bucket CORS Configuration
  name = "example-bucket_cors_configuration"

  # Common attributes
  tags = {
    Name        = "example-bucket_cors_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket Intelligent-Tiering Configuration

```hcl
resource "aws_s3_bucket_intelligent_tiering_configuration" "example" {
  # Example configuration for Bucket Intelligent-Tiering Configuration
  name = "example-bucket_intelligent-tiering_configuration"

  # Common attributes
  tags = {
    Name        = "example-bucket_intelligent-tiering_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket Inventory

```hcl
resource "aws_s3_bucket_inventory" "example" {
  # Example configuration for Bucket Inventory
  name = "example-bucket_inventory"

  # Common attributes
  tags = {
    Name        = "example-bucket_inventory"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket Lifecycle Configuration

```hcl
resource "aws_s3_bucket_lifecycle_configuration" "example" {
  # Example configuration for Bucket Lifecycle Configuration
  name = "example-bucket_lifecycle_configuration"

  # Common attributes
  tags = {
    Name        = "example-bucket_lifecycle_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket Logging

```hcl
resource "aws_s3_bucket_logging" "example" {
  # Example configuration for Bucket Logging
  name = "example-bucket_logging"

  # Common attributes
  tags = {
    Name        = "example-bucket_logging"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket Metric

```hcl
resource "aws_s3_bucket_metric" "example" {
  # Example configuration for Bucket Metric
  name = "example-bucket_metric"

  # Common attributes
  tags = {
    Name        = "example-bucket_metric"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket Notification

```hcl
resource "aws_s3_bucket_notification" "example" {
  # Example configuration for Bucket Notification
  name = "example-bucket_notification"

  # Common attributes
  tags = {
    Name        = "example-bucket_notification"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket Object

```hcl
resource "aws_s3_bucket_object" "example" {
  # Example configuration for Bucket Object
  name = "example-bucket_object"

  # Common attributes
  tags = {
    Name        = "example-bucket_object"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket Object Lock Configuration

```hcl
resource "aws_s3_bucket_object_lock_configuration" "example" {
  # Example configuration for Bucket Object Lock Configuration
  name = "example-bucket_object_lock_configuration"

  # Common attributes
  tags = {
    Name        = "example-bucket_object_lock_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket Ownership Controls

```hcl
resource "aws_s3_bucket_ownership_controls" "example" {
  # Example configuration for Bucket Ownership Controls
  name = "example-bucket_ownership_controls"

  # Common attributes
  tags = {
    Name        = "example-bucket_ownership_controls"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket Policy

```hcl
resource "aws_s3_bucket_policy" "example" {
  # Example configuration for Bucket Policy
  name = "example-bucket_policy"

  # Common attributes
  tags = {
    Name        = "example-bucket_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket Public Access Block

```hcl
resource "aws_s3_bucket_public_access_block" "example" {
  # Example configuration for Bucket Public Access Block
  name = "example-bucket_public_access_block"

  # Common attributes
  tags = {
    Name        = "example-bucket_public_access_block"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket Replication Configuration

```hcl
resource "aws_s3_bucket_replication_configuration" "example" {
  # Example configuration for Bucket Replication Configuration
  name = "example-bucket_replication_configuration"

  # Common attributes
  tags = {
    Name        = "example-bucket_replication_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket Request Payment Configuration

```hcl
resource "aws_s3_bucket_request_payment_configuration" "example" {
  # Example configuration for Bucket Request Payment Configuration
  name = "example-bucket_request_payment_configuration"

  # Common attributes
  tags = {
    Name        = "example-bucket_request_payment_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket Server-side Encryption Configuration

```hcl
resource "aws_s3_bucket_server_side_encryption_configuration" "example" {
  # Example configuration for Bucket Server-side Encryption Configuration
  name = "example-bucket_server-side_encryption_configuration"

  # Common attributes
  tags = {
    Name        = "example-bucket_server-side_encryption_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket Versioning

```hcl
resource "aws_s3_bucket_versioning" "example" {
  # Example configuration for Bucket Versioning
  name = "example-bucket_versioning"

  # Common attributes
  tags = {
    Name        = "example-bucket_versioning"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket Website Configuration

```hcl
resource "aws_s3_bucket_website_configuration" "example" {
  # Example configuration for Bucket Website Configuration
  name = "example-bucket_website_configuration"

  # Common attributes
  tags = {
    Name        = "example-bucket_website_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Directory Bucket

```hcl
resource "aws_s3_directory_bucket" "example" {
  # Example configuration for Directory Bucket
  name = "example-directory_bucket"

  # Common attributes
  tags = {
    Name        = "example-directory_bucket"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Object

```hcl
resource "aws_s3_object" "example" {
  # Example configuration for Object
  name = "example-object"

  # Common attributes
  tags = {
    Name        = "example-object"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Object Copy

```hcl
resource "aws_s3_object_copy" "example" {
  # Example configuration for Object Copy
  name = "example-object_copy"

  # Common attributes
  tags = {
    Name        = "example-object_copy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## s3control

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Access Grant | N/A | Framework |
| Access Grants Instance | N/A | Framework |
| Access Grants Instance Resource Policy | N/A | Framework |
| Access Grants Location | N/A | Framework |
| Account Public Access Block | aws_s3_account_public_access_block | SDK |
| Bucket | aws_s3control_bucket | SDK |
| Storage Lens Configuration | aws_s3control_storage_lens_configuration | SDK |


### Examples


#### Access Grant

```hcl
resource "aws_s3control_access_grant" "example" {
  # Example configuration for Access Grant
  name = "example-access_grant"

  # Common attributes
  tags = {
    Name        = "example-access_grant"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Access Grants Instance

```hcl
resource "aws_s3control_access_grants_instance" "example" {
  # Example configuration for Access Grants Instance
  name = "example-access_grants_instance"

  # Common attributes
  tags = {
    Name        = "example-access_grants_instance"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Access Grants Instance Resource Policy

```hcl
resource "aws_s3control_access_grants_instance_resource_policy" "example" {
  # Example configuration for Access Grants Instance Resource Policy
  name = "example-access_grants_instance_resource_policy"

  # Common attributes
  tags = {
    Name        = "example-access_grants_instance_resource_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Access Grants Location

```hcl
resource "aws_s3control_access_grants_location" "example" {
  # Example configuration for Access Grants Location
  name = "example-access_grants_location"

  # Common attributes
  tags = {
    Name        = "example-access_grants_location"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Account Public Access Block

```hcl
resource "aws_s3_account_public_access_block" "example" {
  # Example configuration for Account Public Access Block
  name = "example-account_public_access_block"

  # Common attributes
  tags = {
    Name        = "example-account_public_access_block"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Bucket

```hcl
resource "aws_s3control_bucket" "example" {
  # Example configuration for Bucket
  name = "example-bucket"

  # Common attributes
  tags = {
    Name        = "example-bucket"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Storage Lens Configuration

```hcl
resource "aws_s3control_storage_lens_configuration" "example" {
  # Example configuration for Storage Lens Configuration
  name = "example-storage_lens_configuration"

  # Common attributes
  tags = {
    Name        = "example-storage_lens_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## s3outposts

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Endpoint | aws_s3outposts_endpoint | SDK |


### Examples


#### Endpoint

```hcl
resource "aws_s3outposts_endpoint" "example" {
  # Example configuration for Endpoint
  name = "example-endpoint"

  # Common attributes
  tags = {
    Name        = "example-endpoint"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## s3tables

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Namespace | N/A | Framework |
| Table | N/A | Framework |
| Table Bucket | N/A | Framework |
| Table Bucket Policy | N/A | Framework |
| Table Policy | N/A | Framework |


### Examples


#### Namespace

```hcl
resource "aws_s3tables_namespace" "example" {
  # Example configuration for Namespace
  name = "example-namespace"

  # Common attributes
  tags = {
    Name        = "example-namespace"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Table

```hcl
resource "aws_s3tables_table" "example" {
  # Example configuration for Table
  name = "example-table"

  # Common attributes
  tags = {
    Name        = "example-table"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Table Bucket

```hcl
resource "aws_s3tables_table_bucket" "example" {
  # Example configuration for Table Bucket
  name = "example-table_bucket"

  # Common attributes
  tags = {
    Name        = "example-table_bucket"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Table Bucket Policy

```hcl
resource "aws_s3tables_table_bucket_policy" "example" {
  # Example configuration for Table Bucket Policy
  name = "example-table_bucket_policy"

  # Common attributes
  tags = {
    Name        = "example-table_bucket_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Table Policy

```hcl
resource "aws_s3tables_table_policy" "example" {
  # Example configuration for Table Policy
  name = "example-table_policy"

  # Common attributes
  tags = {
    Name        = "example-table_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## sagemaker

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| App | aws_sagemaker_app | SDK |
| App Image Config | aws_sagemaker_app_image_config | SDK |
| Code Repository | aws_sagemaker_code_repository | SDK |
| Data Quality Job Definition | aws_sagemaker_data_quality_job_definition | SDK |
| Device | aws_sagemaker_device | SDK |
| Device Fleet | aws_sagemaker_device_fleet | SDK |
| Domain | aws_sagemaker_domain | SDK |
| Endpoint | aws_sagemaker_endpoint | SDK |
| Endpoint Configuration | aws_sagemaker_endpoint_configuration | SDK |
| Feature Group | aws_sagemaker_feature_group | SDK |
| Flow Definition | aws_sagemaker_flow_definition | SDK |
| Hub | aws_sagemaker_hub | SDK |
| Human Task UI | aws_sagemaker_human_task_ui | SDK |
| Image | aws_sagemaker_image | SDK |
| Image Version | aws_sagemaker_image_version | SDK |
| Mlflow Tracking Server | aws_sagemaker_mlflow_tracking_server | SDK |
| Model | aws_sagemaker_model | SDK |
| Model Package Group | aws_sagemaker_model_package_group | SDK |
| Model Package Group Policy | aws_sagemaker_model_package_group_policy | SDK |
| Monitoring Schedule | aws_sagemaker_monitoring_schedule | SDK |
| Notebook Instance | aws_sagemaker_notebook_instance | SDK |
| Notebook Instance Lifecycle Configuration | aws_sagemaker_notebook_instance_lifecycle_configuration | SDK |
| Pipeline | aws_sagemaker_pipeline | SDK |
| Project | aws_sagemaker_project | SDK |
| Servicecatalog Portfolio Status | aws_sagemaker_servicecatalog_portfolio_status | SDK |
| Space | aws_sagemaker_space | SDK |
| Studio Lifecycle Config | aws_sagemaker_studio_lifecycle_config | SDK |
| User Profile | aws_sagemaker_user_profile | SDK |
| Workforce | aws_sagemaker_workforce | SDK |
| Workteam | aws_sagemaker_workteam | SDK |


### Examples


#### App

```hcl
resource "aws_sagemaker_app" "example" {
  # Example configuration for App
  name = "example-app"

  # Common attributes
  tags = {
    Name        = "example-app"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### App Image Config

```hcl
resource "aws_sagemaker_app_image_config" "example" {
  # Example configuration for App Image Config
  name = "example-app_image_config"

  # Common attributes
  tags = {
    Name        = "example-app_image_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Code Repository

```hcl
resource "aws_sagemaker_code_repository" "example" {
  # Example configuration for Code Repository
  name = "example-code_repository"

  # Common attributes
  tags = {
    Name        = "example-code_repository"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Data Quality Job Definition

```hcl
resource "aws_sagemaker_data_quality_job_definition" "example" {
  # Example configuration for Data Quality Job Definition
  name = "example-data_quality_job_definition"

  # Common attributes
  tags = {
    Name        = "example-data_quality_job_definition"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Device

```hcl
resource "aws_sagemaker_device" "example" {
  # Example configuration for Device
  name = "example-device"

  # Common attributes
  tags = {
    Name        = "example-device"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Device Fleet

```hcl
resource "aws_sagemaker_device_fleet" "example" {
  # Example configuration for Device Fleet
  name = "example-device_fleet"

  # Common attributes
  tags = {
    Name        = "example-device_fleet"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain

```hcl
resource "aws_sagemaker_domain" "example" {
  # Example configuration for Domain
  name = "example-domain"

  # Common attributes
  tags = {
    Name        = "example-domain"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Endpoint

```hcl
resource "aws_sagemaker_endpoint" "example" {
  # Example configuration for Endpoint
  name = "example-endpoint"

  # Common attributes
  tags = {
    Name        = "example-endpoint"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Endpoint Configuration

```hcl
resource "aws_sagemaker_endpoint_configuration" "example" {
  # Example configuration for Endpoint Configuration
  name = "example-endpoint_configuration"

  # Common attributes
  tags = {
    Name        = "example-endpoint_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Feature Group

```hcl
resource "aws_sagemaker_feature_group" "example" {
  # Example configuration for Feature Group
  name = "example-feature_group"

  # Common attributes
  tags = {
    Name        = "example-feature_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Flow Definition

```hcl
resource "aws_sagemaker_flow_definition" "example" {
  # Example configuration for Flow Definition
  name = "example-flow_definition"

  # Common attributes
  tags = {
    Name        = "example-flow_definition"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Hub

```hcl
resource "aws_sagemaker_hub" "example" {
  # Example configuration for Hub
  name = "example-hub"

  # Common attributes
  tags = {
    Name        = "example-hub"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Human Task UI

```hcl
resource "aws_sagemaker_human_task_ui" "example" {
  # Example configuration for Human Task UI
  name = "example-human_task_ui"

  # Common attributes
  tags = {
    Name        = "example-human_task_ui"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Image

```hcl
resource "aws_sagemaker_image" "example" {
  # Example configuration for Image
  name = "example-image"

  # Common attributes
  tags = {
    Name        = "example-image"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Image Version

```hcl
resource "aws_sagemaker_image_version" "example" {
  # Example configuration for Image Version
  name = "example-image_version"

  # Common attributes
  tags = {
    Name        = "example-image_version"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Mlflow Tracking Server

```hcl
resource "aws_sagemaker_mlflow_tracking_server" "example" {
  # Example configuration for Mlflow Tracking Server
  name = "example-mlflow_tracking_server"

  # Common attributes
  tags = {
    Name        = "example-mlflow_tracking_server"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Model

```hcl
resource "aws_sagemaker_model" "example" {
  # Example configuration for Model
  name = "example-model"

  # Common attributes
  tags = {
    Name        = "example-model"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Model Package Group

```hcl
resource "aws_sagemaker_model_package_group" "example" {
  # Example configuration for Model Package Group
  name = "example-model_package_group"

  # Common attributes
  tags = {
    Name        = "example-model_package_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Model Package Group Policy

```hcl
resource "aws_sagemaker_model_package_group_policy" "example" {
  # Example configuration for Model Package Group Policy
  name = "example-model_package_group_policy"

  # Common attributes
  tags = {
    Name        = "example-model_package_group_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Monitoring Schedule

```hcl
resource "aws_sagemaker_monitoring_schedule" "example" {
  # Example configuration for Monitoring Schedule
  name = "example-monitoring_schedule"

  # Common attributes
  tags = {
    Name        = "example-monitoring_schedule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Notebook Instance

```hcl
resource "aws_sagemaker_notebook_instance" "example" {
  # Example configuration for Notebook Instance
  name = "example-notebook_instance"

  # Common attributes
  tags = {
    Name        = "example-notebook_instance"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Notebook Instance Lifecycle Configuration

```hcl
resource "aws_sagemaker_notebook_instance_lifecycle_configuration" "example" {
  # Example configuration for Notebook Instance Lifecycle Configuration
  name = "example-notebook_instance_lifecycle_configuration"

  # Common attributes
  tags = {
    Name        = "example-notebook_instance_lifecycle_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Pipeline

```hcl
resource "aws_sagemaker_pipeline" "example" {
  # Example configuration for Pipeline
  name = "example-pipeline"

  # Common attributes
  tags = {
    Name        = "example-pipeline"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Project

```hcl
resource "aws_sagemaker_project" "example" {
  # Example configuration for Project
  name = "example-project"

  # Common attributes
  tags = {
    Name        = "example-project"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Servicecatalog Portfolio Status

```hcl
resource "aws_sagemaker_servicecatalog_portfolio_status" "example" {
  # Example configuration for Servicecatalog Portfolio Status
  name = "example-servicecatalog_portfolio_status"

  # Common attributes
  tags = {
    Name        = "example-servicecatalog_portfolio_status"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Space

```hcl
resource "aws_sagemaker_space" "example" {
  # Example configuration for Space
  name = "example-space"

  # Common attributes
  tags = {
    Name        = "example-space"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Studio Lifecycle Config

```hcl
resource "aws_sagemaker_studio_lifecycle_config" "example" {
  # Example configuration for Studio Lifecycle Config
  name = "example-studio_lifecycle_config"

  # Common attributes
  tags = {
    Name        = "example-studio_lifecycle_config"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User Profile

```hcl
resource "aws_sagemaker_user_profile" "example" {
  # Example configuration for User Profile
  name = "example-user_profile"

  # Common attributes
  tags = {
    Name        = "example-user_profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Workforce

```hcl
resource "aws_sagemaker_workforce" "example" {
  # Example configuration for Workforce
  name = "example-workforce"

  # Common attributes
  tags = {
    Name        = "example-workforce"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Workteam

```hcl
resource "aws_sagemaker_workteam" "example" {
  # Example configuration for Workteam
  name = "example-workteam"

  # Common attributes
  tags = {
    Name        = "example-workteam"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## scheduler

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Schedule Group | aws_scheduler_schedule_group | SDK |


### Examples


#### Schedule Group

```hcl
resource "aws_scheduler_schedule_group" "example" {
  # Example configuration for Schedule Group
  name = "example-schedule_group"

  # Common attributes
  tags = {
    Name        = "example-schedule_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## schemas

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Discoverer | aws_schemas_discoverer | SDK |
| Registry | aws_schemas_registry | SDK |
| Registry Policy | aws_schemas_registry_policy | SDK |
| Schema | aws_schemas_schema | SDK |


### Examples


#### Discoverer

```hcl
resource "aws_schemas_discoverer" "example" {
  # Example configuration for Discoverer
  name = "example-discoverer"

  # Common attributes
  tags = {
    Name        = "example-discoverer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Registry

```hcl
resource "aws_schemas_registry" "example" {
  # Example configuration for Registry
  name = "example-registry"

  # Common attributes
  tags = {
    Name        = "example-registry"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Registry Policy

```hcl
resource "aws_schemas_registry_policy" "example" {
  # Example configuration for Registry Policy
  name = "example-registry_policy"

  # Common attributes
  tags = {
    Name        = "example-registry_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Schema

```hcl
resource "aws_schemas_schema" "example" {
  # Example configuration for Schema
  name = "example-schema"

  # Common attributes
  tags = {
    Name        = "example-schema"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## secretsmanager

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Secret | aws_secretsmanager_secret | SDK |
| Secret Policy | aws_secretsmanager_secret_policy | SDK |
| Secret Rotation | aws_secretsmanager_secret_rotation | SDK |
| Secret Version | aws_secretsmanager_secret_version | SDK |


### Examples


#### Secret

```hcl
resource "aws_secretsmanager_secret" "example" {
  # Example configuration for Secret
  name = "example-secret"

  # Common attributes
  tags = {
    Name        = "example-secret"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Secret Policy

```hcl
resource "aws_secretsmanager_secret_policy" "example" {
  # Example configuration for Secret Policy
  name = "example-secret_policy"

  # Common attributes
  tags = {
    Name        = "example-secret_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Secret Rotation

```hcl
resource "aws_secretsmanager_secret_rotation" "example" {
  # Example configuration for Secret Rotation
  name = "example-secret_rotation"

  # Common attributes
  tags = {
    Name        = "example-secret_rotation"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Secret Version

```hcl
resource "aws_secretsmanager_secret_version" "example" {
  # Example configuration for Secret Version
  name = "example-secret_version"

  # Common attributes
  tags = {
    Name        = "example-secret_version"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## securityhub

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Account | aws_securityhub_account | SDK |
| Action Target | aws_securityhub_action_target | SDK |
| Automation Rule | N/A | Framework |
| Configuration Policy | aws_securityhub_configuration_policy | SDK |
| Configuration Policy Association | aws_securityhub_configuration_policy_association | SDK |
| Finding Aggregator | aws_securityhub_finding_aggregator | SDK |
| Insight | aws_securityhub_insight | SDK |
| Invite Accepter | aws_securityhub_invite_accepter | SDK |
| Member | aws_securityhub_member | SDK |
| Organization Admin Account | aws_securityhub_organization_admin_account | SDK |
| Organization Configuration | aws_securityhub_organization_configuration | SDK |
| Product Subscription | aws_securityhub_product_subscription | SDK |
| Standards Control | aws_securityhub_standards_control | SDK |
| Standards Control Association | N/A | Framework |
| Standards Subscription | aws_securityhub_standards_subscription | SDK |


### Examples


#### Account

```hcl
resource "aws_securityhub_account" "example" {
  # Example configuration for Account
  name = "example-account"

  # Common attributes
  tags = {
    Name        = "example-account"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Action Target

```hcl
resource "aws_securityhub_action_target" "example" {
  # Example configuration for Action Target
  name = "example-action_target"

  # Common attributes
  tags = {
    Name        = "example-action_target"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Automation Rule

```hcl
resource "aws_securityhub_automation_rule" "example" {
  # Example configuration for Automation Rule
  name = "example-automation_rule"

  # Common attributes
  tags = {
    Name        = "example-automation_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Configuration Policy

```hcl
resource "aws_securityhub_configuration_policy" "example" {
  # Example configuration for Configuration Policy
  name = "example-configuration_policy"

  # Common attributes
  tags = {
    Name        = "example-configuration_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Configuration Policy Association

```hcl
resource "aws_securityhub_configuration_policy_association" "example" {
  # Example configuration for Configuration Policy Association
  name = "example-configuration_policy_association"

  # Common attributes
  tags = {
    Name        = "example-configuration_policy_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Finding Aggregator

```hcl
resource "aws_securityhub_finding_aggregator" "example" {
  # Example configuration for Finding Aggregator
  name = "example-finding_aggregator"

  # Common attributes
  tags = {
    Name        = "example-finding_aggregator"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Insight

```hcl
resource "aws_securityhub_insight" "example" {
  # Example configuration for Insight
  name = "example-insight"

  # Common attributes
  tags = {
    Name        = "example-insight"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Invite Accepter

```hcl
resource "aws_securityhub_invite_accepter" "example" {
  # Example configuration for Invite Accepter
  name = "example-invite_accepter"

  # Common attributes
  tags = {
    Name        = "example-invite_accepter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Member

```hcl
resource "aws_securityhub_member" "example" {
  # Example configuration for Member
  name = "example-member"

  # Common attributes
  tags = {
    Name        = "example-member"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Organization Admin Account

```hcl
resource "aws_securityhub_organization_admin_account" "example" {
  # Example configuration for Organization Admin Account
  name = "example-organization_admin_account"

  # Common attributes
  tags = {
    Name        = "example-organization_admin_account"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Organization Configuration

```hcl
resource "aws_securityhub_organization_configuration" "example" {
  # Example configuration for Organization Configuration
  name = "example-organization_configuration"

  # Common attributes
  tags = {
    Name        = "example-organization_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Product Subscription

```hcl
resource "aws_securityhub_product_subscription" "example" {
  # Example configuration for Product Subscription
  name = "example-product_subscription"

  # Common attributes
  tags = {
    Name        = "example-product_subscription"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Standards Control

```hcl
resource "aws_securityhub_standards_control" "example" {
  # Example configuration for Standards Control
  name = "example-standards_control"

  # Common attributes
  tags = {
    Name        = "example-standards_control"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Standards Control Association

```hcl
resource "aws_securityhub_standards_control_association" "example" {
  # Example configuration for Standards Control Association
  name = "example-standards_control_association"

  # Common attributes
  tags = {
    Name        = "example-standards_control_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Standards Subscription

```hcl
resource "aws_securityhub_standards_subscription" "example" {
  # Example configuration for Standards Subscription
  name = "example-standards_subscription"

  # Common attributes
  tags = {
    Name        = "example-standards_subscription"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## securitylake

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| AWS Log Source | N/A | Framework |
| Custom Log Source | N/A | Framework |
| Data Lake | N/A | Framework |
| Subscriber | N/A | Framework |
| Subscriber Notification | N/A | Framework |


### Examples


#### AWS Log Source

```hcl
resource "aws_securitylake_aws_log_source" "example" {
  # Example configuration for AWS Log Source
  name = "example-aws_log_source"

  # Common attributes
  tags = {
    Name        = "example-aws_log_source"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Custom Log Source

```hcl
resource "aws_securitylake_custom_log_source" "example" {
  # Example configuration for Custom Log Source
  name = "example-custom_log_source"

  # Common attributes
  tags = {
    Name        = "example-custom_log_source"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Data Lake

```hcl
resource "aws_securitylake_data_lake" "example" {
  # Example configuration for Data Lake
  name = "example-data_lake"

  # Common attributes
  tags = {
    Name        = "example-data_lake"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Subscriber

```hcl
resource "aws_securitylake_subscriber" "example" {
  # Example configuration for Subscriber
  name = "example-subscriber"

  # Common attributes
  tags = {
    Name        = "example-subscriber"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Subscriber Notification

```hcl
resource "aws_securitylake_subscriber_notification" "example" {
  # Example configuration for Subscriber Notification
  name = "example-subscriber_notification"

  # Common attributes
  tags = {
    Name        = "example-subscriber_notification"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## serverlessrepo

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| CloudFormation Stack | aws_serverlessapplicationrepository_cloudformation_stack | SDK |


### Examples


#### CloudFormation Stack

```hcl
resource "aws_serverlessapplicationrepository_cloudformation_stack" "example" {
  # Example configuration for CloudFormation Stack
  name = "example-cloudformation_stack"

  # Common attributes
  tags = {
    Name        = "example-cloudformation_stack"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## servicecatalog

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Budget Resource Association | aws_servicecatalog_budget_resource_association | SDK |
| Constraint | aws_servicecatalog_constraint | SDK |
| Organizations Access | aws_servicecatalog_organizations_access | SDK |
| Portfolio | aws_servicecatalog_portfolio | SDK |
| Portfolio Share | aws_servicecatalog_portfolio_share | SDK |
| Principal Portfolio Association | aws_servicecatalog_principal_portfolio_association | SDK |
| Product | aws_servicecatalog_product | SDK |
| Product Portfolio Association | aws_servicecatalog_product_portfolio_association | SDK |
| Provisioned Product | aws_servicecatalog_provisioned_product | SDK |
| Provisioning Artifact | aws_servicecatalog_provisioning_artifact | SDK |
| Service Action | aws_servicecatalog_service_action | SDK |
| Tag Option | aws_servicecatalog_tag_option | SDK |
| Tag Option Resource Association | aws_servicecatalog_tag_option_resource_association | SDK |


### Examples


#### Budget Resource Association

```hcl
resource "aws_servicecatalog_budget_resource_association" "example" {
  # Example configuration for Budget Resource Association
  name = "example-budget_resource_association"

  # Common attributes
  tags = {
    Name        = "example-budget_resource_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Constraint

```hcl
resource "aws_servicecatalog_constraint" "example" {
  # Example configuration for Constraint
  name = "example-constraint"

  # Common attributes
  tags = {
    Name        = "example-constraint"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Organizations Access

```hcl
resource "aws_servicecatalog_organizations_access" "example" {
  # Example configuration for Organizations Access
  name = "example-organizations_access"

  # Common attributes
  tags = {
    Name        = "example-organizations_access"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Portfolio

```hcl
resource "aws_servicecatalog_portfolio" "example" {
  # Example configuration for Portfolio
  name = "example-portfolio"

  # Common attributes
  tags = {
    Name        = "example-portfolio"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Portfolio Share

```hcl
resource "aws_servicecatalog_portfolio_share" "example" {
  # Example configuration for Portfolio Share
  name = "example-portfolio_share"

  # Common attributes
  tags = {
    Name        = "example-portfolio_share"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Principal Portfolio Association

```hcl
resource "aws_servicecatalog_principal_portfolio_association" "example" {
  # Example configuration for Principal Portfolio Association
  name = "example-principal_portfolio_association"

  # Common attributes
  tags = {
    Name        = "example-principal_portfolio_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Product

```hcl
resource "aws_servicecatalog_product" "example" {
  # Example configuration for Product
  name = "example-product"

  # Common attributes
  tags = {
    Name        = "example-product"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Product Portfolio Association

```hcl
resource "aws_servicecatalog_product_portfolio_association" "example" {
  # Example configuration for Product Portfolio Association
  name = "example-product_portfolio_association"

  # Common attributes
  tags = {
    Name        = "example-product_portfolio_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Provisioned Product

```hcl
resource "aws_servicecatalog_provisioned_product" "example" {
  # Example configuration for Provisioned Product
  name = "example-provisioned_product"

  # Common attributes
  tags = {
    Name        = "example-provisioned_product"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Provisioning Artifact

```hcl
resource "aws_servicecatalog_provisioning_artifact" "example" {
  # Example configuration for Provisioning Artifact
  name = "example-provisioning_artifact"

  # Common attributes
  tags = {
    Name        = "example-provisioning_artifact"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Service Action

```hcl
resource "aws_servicecatalog_service_action" "example" {
  # Example configuration for Service Action
  name = "example-service_action"

  # Common attributes
  tags = {
    Name        = "example-service_action"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Tag Option

```hcl
resource "aws_servicecatalog_tag_option" "example" {
  # Example configuration for Tag Option
  name = "example-tag_option"

  # Common attributes
  tags = {
    Name        = "example-tag_option"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Tag Option Resource Association

```hcl
resource "aws_servicecatalog_tag_option_resource_association" "example" {
  # Example configuration for Tag Option Resource Association
  name = "example-tag_option_resource_association"

  # Common attributes
  tags = {
    Name        = "example-tag_option_resource_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## servicecatalogappregistry

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Application | N/A | Framework |
| Attribute Group | N/A | Framework |
| Attribute Group Association | N/A | Framework |


### Examples


#### Application

```hcl
resource "aws_servicecatalogappregistry_application" "example" {
  # Example configuration for Application
  name = "example-application"

  # Common attributes
  tags = {
    Name        = "example-application"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Attribute Group

```hcl
resource "aws_servicecatalogappregistry_attribute_group" "example" {
  # Example configuration for Attribute Group
  name = "example-attribute_group"

  # Common attributes
  tags = {
    Name        = "example-attribute_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Attribute Group Association

```hcl
resource "aws_servicecatalogappregistry_attribute_group_association" "example" {
  # Example configuration for Attribute Group Association
  name = "example-attribute_group_association"

  # Common attributes
  tags = {
    Name        = "example-attribute_group_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## servicediscovery

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| HTTP Namespace | aws_service_discovery_http_namespace | SDK |
| Instance | aws_service_discovery_instance | SDK |
| Private DNS Namespace | aws_service_discovery_private_dns_namespace | SDK |
| Public DNS Namespace | aws_service_discovery_public_dns_namespace | SDK |
| Service | aws_service_discovery_service | SDK |


### Examples


#### HTTP Namespace

```hcl
resource "aws_service_discovery_http_namespace" "example" {
  # Example configuration for HTTP Namespace
  name = "example-http_namespace"

  # Common attributes
  tags = {
    Name        = "example-http_namespace"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Instance

```hcl
resource "aws_service_discovery_instance" "example" {
  # Example configuration for Instance
  name = "example-instance"

  # Common attributes
  tags = {
    Name        = "example-instance"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Private DNS Namespace

```hcl
resource "aws_service_discovery_private_dns_namespace" "example" {
  # Example configuration for Private DNS Namespace
  name = "example-private_dns_namespace"

  # Common attributes
  tags = {
    Name        = "example-private_dns_namespace"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Public DNS Namespace

```hcl
resource "aws_service_discovery_public_dns_namespace" "example" {
  # Example configuration for Public DNS Namespace
  name = "example-public_dns_namespace"

  # Common attributes
  tags = {
    Name        = "example-public_dns_namespace"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Service

```hcl
resource "aws_service_discovery_service" "example" {
  # Example configuration for Service
  name = "example-service"

  # Common attributes
  tags = {
    Name        = "example-service"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## servicequotas

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Template | N/A | Framework |
| Template Association | N/A | Framework |


### Examples


#### Template

```hcl
resource "aws_servicequotas_template" "example" {
  # Example configuration for Template
  name = "example-template"

  # Common attributes
  tags = {
    Name        = "example-template"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Template Association

```hcl
resource "aws_servicequotas_template_association" "example" {
  # Example configuration for Template Association
  name = "example-template_association"

  # Common attributes
  tags = {
    Name        = "example-template_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## ses

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Active Receipt Rule Set | aws_ses_active_receipt_rule_set | SDK |
| Configuration Set | aws_ses_configuration_set | SDK |
| Configuration Set Event Destination | aws_ses_event_destination | SDK |
| Domain DKIM | aws_ses_domain_dkim | SDK |
| Domain Identity | aws_ses_domain_identity | SDK |
| Domain Identity Verification | aws_ses_domain_identity_verification | SDK |
| Email Identity | aws_ses_email_identity | SDK |
| Identity Notification Topic | aws_ses_identity_notification_topic | SDK |
| Identity Policy | aws_ses_identity_policy | SDK |
| MAIL FROM Domain | aws_ses_domain_mail_from | SDK |
| Receipt Filter | aws_ses_receipt_filter | SDK |
| Receipt Rule | aws_ses_receipt_rule | SDK |
| Receipt Rule Set | aws_ses_receipt_rule_set | SDK |
| Template | aws_ses_template | SDK |


### Examples


#### Active Receipt Rule Set

```hcl
resource "aws_ses_active_receipt_rule_set" "example" {
  # Example configuration for Active Receipt Rule Set
  name = "example-active_receipt_rule_set"

  # Common attributes
  tags = {
    Name        = "example-active_receipt_rule_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Configuration Set

```hcl
resource "aws_ses_configuration_set" "example" {
  # Example configuration for Configuration Set
  name = "example-configuration_set"

  # Common attributes
  tags = {
    Name        = "example-configuration_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Configuration Set Event Destination

```hcl
resource "aws_ses_event_destination" "example" {
  # Example configuration for Configuration Set Event Destination
  name = "example-configuration_set_event_destination"

  # Common attributes
  tags = {
    Name        = "example-configuration_set_event_destination"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain DKIM

```hcl
resource "aws_ses_domain_dkim" "example" {
  # Example configuration for Domain DKIM
  name = "example-domain_dkim"

  # Common attributes
  tags = {
    Name        = "example-domain_dkim"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain Identity

```hcl
resource "aws_ses_domain_identity" "example" {
  # Example configuration for Domain Identity
  name = "example-domain_identity"

  # Common attributes
  tags = {
    Name        = "example-domain_identity"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Domain Identity Verification

```hcl
resource "aws_ses_domain_identity_verification" "example" {
  # Example configuration for Domain Identity Verification
  name = "example-domain_identity_verification"

  # Common attributes
  tags = {
    Name        = "example-domain_identity_verification"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Email Identity

```hcl
resource "aws_ses_email_identity" "example" {
  # Example configuration for Email Identity
  name = "example-email_identity"

  # Common attributes
  tags = {
    Name        = "example-email_identity"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Identity Notification Topic

```hcl
resource "aws_ses_identity_notification_topic" "example" {
  # Example configuration for Identity Notification Topic
  name = "example-identity_notification_topic"

  # Common attributes
  tags = {
    Name        = "example-identity_notification_topic"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Identity Policy

```hcl
resource "aws_ses_identity_policy" "example" {
  # Example configuration for Identity Policy
  name = "example-identity_policy"

  # Common attributes
  tags = {
    Name        = "example-identity_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### MAIL FROM Domain

```hcl
resource "aws_ses_domain_mail_from" "example" {
  # Example configuration for MAIL FROM Domain
  name = "example-mail_from_domain"

  # Common attributes
  tags = {
    Name        = "example-mail_from_domain"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Receipt Filter

```hcl
resource "aws_ses_receipt_filter" "example" {
  # Example configuration for Receipt Filter
  name = "example-receipt_filter"

  # Common attributes
  tags = {
    Name        = "example-receipt_filter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Receipt Rule

```hcl
resource "aws_ses_receipt_rule" "example" {
  # Example configuration for Receipt Rule
  name = "example-receipt_rule"

  # Common attributes
  tags = {
    Name        = "example-receipt_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Receipt Rule Set

```hcl
resource "aws_ses_receipt_rule_set" "example" {
  # Example configuration for Receipt Rule Set
  name = "example-receipt_rule_set"

  # Common attributes
  tags = {
    Name        = "example-receipt_rule_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Template

```hcl
resource "aws_ses_template" "example" {
  # Example configuration for Template
  name = "example-template"

  # Common attributes
  tags = {
    Name        = "example-template"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## sesv2

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Account Suppression Attributes | N/A | Framework |
| Account VDM Attributes | aws_sesv2_account_vdm_attributes | SDK |
| Configuration Set | aws_sesv2_configuration_set | SDK |
| Configuration Set Event Destination | aws_sesv2_configuration_set_event_destination | SDK |
| Contact List | aws_sesv2_contact_list | SDK |
| Dedicated IP Assignment | aws_sesv2_dedicated_ip_assignment | SDK |
| Dedicated IP Pool | aws_sesv2_dedicated_ip_pool | SDK |
| Email Identity | aws_sesv2_email_identity | SDK |
| Email Identity Feedback Attributes | aws_sesv2_email_identity_feedback_attributes | SDK |
| Email Identity Mail From Attributes | aws_sesv2_email_identity_mail_from_attributes | SDK |
| Email Identity Policy | aws_sesv2_email_identity_policy | SDK |


### Examples


#### Account Suppression Attributes

```hcl
resource "aws_sesv2_account_suppression_attributes" "example" {
  # Example configuration for Account Suppression Attributes
  name = "example-account_suppression_attributes"

  # Common attributes
  tags = {
    Name        = "example-account_suppression_attributes"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Account VDM Attributes

```hcl
resource "aws_sesv2_account_vdm_attributes" "example" {
  # Example configuration for Account VDM Attributes
  name = "example-account_vdm_attributes"

  # Common attributes
  tags = {
    Name        = "example-account_vdm_attributes"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Configuration Set

```hcl
resource "aws_sesv2_configuration_set" "example" {
  # Example configuration for Configuration Set
  name = "example-configuration_set"

  # Common attributes
  tags = {
    Name        = "example-configuration_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Configuration Set Event Destination

```hcl
resource "aws_sesv2_configuration_set_event_destination" "example" {
  # Example configuration for Configuration Set Event Destination
  name = "example-configuration_set_event_destination"

  # Common attributes
  tags = {
    Name        = "example-configuration_set_event_destination"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Contact List

```hcl
resource "aws_sesv2_contact_list" "example" {
  # Example configuration for Contact List
  name = "example-contact_list"

  # Common attributes
  tags = {
    Name        = "example-contact_list"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Dedicated IP Assignment

```hcl
resource "aws_sesv2_dedicated_ip_assignment" "example" {
  # Example configuration for Dedicated IP Assignment
  name = "example-dedicated_ip_assignment"

  # Common attributes
  tags = {
    Name        = "example-dedicated_ip_assignment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Dedicated IP Pool

```hcl
resource "aws_sesv2_dedicated_ip_pool" "example" {
  # Example configuration for Dedicated IP Pool
  name = "example-dedicated_ip_pool"

  # Common attributes
  tags = {
    Name        = "example-dedicated_ip_pool"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Email Identity

```hcl
resource "aws_sesv2_email_identity" "example" {
  # Example configuration for Email Identity
  name = "example-email_identity"

  # Common attributes
  tags = {
    Name        = "example-email_identity"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Email Identity Feedback Attributes

```hcl
resource "aws_sesv2_email_identity_feedback_attributes" "example" {
  # Example configuration for Email Identity Feedback Attributes
  name = "example-email_identity_feedback_attributes"

  # Common attributes
  tags = {
    Name        = "example-email_identity_feedback_attributes"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Email Identity Mail From Attributes

```hcl
resource "aws_sesv2_email_identity_mail_from_attributes" "example" {
  # Example configuration for Email Identity Mail From Attributes
  name = "example-email_identity_mail_from_attributes"

  # Common attributes
  tags = {
    Name        = "example-email_identity_mail_from_attributes"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Email Identity Policy

```hcl
resource "aws_sesv2_email_identity_policy" "example" {
  # Example configuration for Email Identity Policy
  name = "example-email_identity_policy"

  # Common attributes
  tags = {
    Name        = "example-email_identity_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## sfn

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Activity | aws_sfn_activity | SDK |
| Alias | aws_sfn_alias | SDK |
| State Machine | aws_sfn_state_machine | SDK |


### Examples


#### Activity

```hcl
resource "aws_sfn_activity" "example" {
  # Example configuration for Activity
  name = "example-activity"

  # Common attributes
  tags = {
    Name        = "example-activity"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Alias

```hcl
resource "aws_sfn_alias" "example" {
  # Example configuration for Alias
  name = "example-alias"

  # Common attributes
  tags = {
    Name        = "example-alias"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### State Machine

```hcl
resource "aws_sfn_state_machine" "example" {
  # Example configuration for State Machine
  name = "example-state_machine"

  # Common attributes
  tags = {
    Name        = "example-state_machine"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## shield

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Application Layer Automatic Response | N/A | Framework |
| DRT Log Bucket Association | N/A | Framework |
| DRT Role ARN Association | N/A | Framework |
| Proactive Engagement | N/A | Framework |
| Protection | aws_shield_protection | SDK |
| Protection Group | aws_shield_protection_group | SDK |
| Subscription | N/A | Framework |


### Examples


#### Application Layer Automatic Response

```hcl
resource "aws_shield_application_layer_automatic_response" "example" {
  # Example configuration for Application Layer Automatic Response
  name = "example-application_layer_automatic_response"

  # Common attributes
  tags = {
    Name        = "example-application_layer_automatic_response"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### DRT Log Bucket Association

```hcl
resource "aws_shield_drt_log_bucket_association" "example" {
  # Example configuration for DRT Log Bucket Association
  name = "example-drt_log_bucket_association"

  # Common attributes
  tags = {
    Name        = "example-drt_log_bucket_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### DRT Role ARN Association

```hcl
resource "aws_shield_drt_role_arn_association" "example" {
  # Example configuration for DRT Role ARN Association
  name = "example-drt_role_arn_association"

  # Common attributes
  tags = {
    Name        = "example-drt_role_arn_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Proactive Engagement

```hcl
resource "aws_shield_proactive_engagement" "example" {
  # Example configuration for Proactive Engagement
  name = "example-proactive_engagement"

  # Common attributes
  tags = {
    Name        = "example-proactive_engagement"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Protection

```hcl
resource "aws_shield_protection" "example" {
  # Example configuration for Protection
  name = "example-protection"

  # Common attributes
  tags = {
    Name        = "example-protection"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Protection Group

```hcl
resource "aws_shield_protection_group" "example" {
  # Example configuration for Protection Group
  name = "example-protection_group"

  # Common attributes
  tags = {
    Name        = "example-protection_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Subscription

```hcl
resource "aws_shield_subscription" "example" {
  # Example configuration for Subscription
  name = "example-subscription"

  # Common attributes
  tags = {
    Name        = "example-subscription"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## signer

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Signing Profile | aws_signer_signing_profile | SDK |


### Examples


#### Signing Profile

```hcl
resource "aws_signer_signing_profile" "example" {
  # Example configuration for Signing Profile
  name = "example-signing_profile"

  # Common attributes
  tags = {
    Name        = "example-signing_profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## sns

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Topic | aws_sns_topic | SDK |


### Examples


#### Topic

```hcl
resource "aws_sns_topic" "example" {
  name = "example-topic"
}
```



## sqs

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Queue | aws_sqs_queue | SDK |


### Examples


#### Queue

```hcl
resource "aws_sqs_queue" "example" {
  name                      = "example-queue"
  delay_seconds             = 90
  max_message_size          = 2048
  message_retention_seconds = 86400
  receive_wait_time_seconds = 10
}
```



## ssm

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Activation | aws_ssm_activation | SDK |
| Association | aws_ssm_association | SDK |
| Default Patch Baseline | aws_ssm_default_patch_baseline | SDK |
| Document | aws_ssm_document | SDK |
| Maintenance Window | aws_ssm_maintenance_window | SDK |
| Maintenance Window Target | aws_ssm_maintenance_window_target | SDK |
| Maintenance Window Task | aws_ssm_maintenance_window_task | SDK |
| Parameter | aws_ssm_parameter | SDK |
| Patch Baseline | aws_ssm_patch_baseline | SDK |
| Patch Group | aws_ssm_patch_group | SDK |
| Resource Data Sync | aws_ssm_resource_data_sync | SDK |
| Service Setting | aws_ssm_service_setting | SDK |


### Examples


#### Activation

```hcl
resource "aws_ssm_activation" "example" {
  # Example configuration for Activation
  name = "example-activation"

  # Common attributes
  tags = {
    Name        = "example-activation"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Association

```hcl
resource "aws_ssm_association" "example" {
  # Example configuration for Association
  name = "example-association"

  # Common attributes
  tags = {
    Name        = "example-association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Default Patch Baseline

```hcl
resource "aws_ssm_default_patch_baseline" "example" {
  # Example configuration for Default Patch Baseline
  name = "example-default_patch_baseline"

  # Common attributes
  tags = {
    Name        = "example-default_patch_baseline"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Document

```hcl
resource "aws_ssm_document" "example" {
  # Example configuration for Document
  name = "example-document"

  # Common attributes
  tags = {
    Name        = "example-document"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Maintenance Window

```hcl
resource "aws_ssm_maintenance_window" "example" {
  # Example configuration for Maintenance Window
  name = "example-maintenance_window"

  # Common attributes
  tags = {
    Name        = "example-maintenance_window"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Maintenance Window Target

```hcl
resource "aws_ssm_maintenance_window_target" "example" {
  # Example configuration for Maintenance Window Target
  name = "example-maintenance_window_target"

  # Common attributes
  tags = {
    Name        = "example-maintenance_window_target"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Maintenance Window Task

```hcl
resource "aws_ssm_maintenance_window_task" "example" {
  # Example configuration for Maintenance Window Task
  name = "example-maintenance_window_task"

  # Common attributes
  tags = {
    Name        = "example-maintenance_window_task"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Parameter

```hcl
resource "aws_ssm_parameter" "example" {
  # Example configuration for Parameter
  name = "example-parameter"

  # Common attributes
  tags = {
    Name        = "example-parameter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Patch Baseline

```hcl
resource "aws_ssm_patch_baseline" "example" {
  # Example configuration for Patch Baseline
  name = "example-patch_baseline"

  # Common attributes
  tags = {
    Name        = "example-patch_baseline"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Patch Group

```hcl
resource "aws_ssm_patch_group" "example" {
  # Example configuration for Patch Group
  name = "example-patch_group"

  # Common attributes
  tags = {
    Name        = "example-patch_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource Data Sync

```hcl
resource "aws_ssm_resource_data_sync" "example" {
  # Example configuration for Resource Data Sync
  name = "example-resource_data_sync"

  # Common attributes
  tags = {
    Name        = "example-resource_data_sync"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Service Setting

```hcl
resource "aws_ssm_service_setting" "example" {
  # Example configuration for Service Setting
  name = "example-service_setting"

  # Common attributes
  tags = {
    Name        = "example-service_setting"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## ssmcontacts

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Contact | aws_ssmcontacts_contact | SDK |
| Contact Channel | aws_ssmcontacts_contact_channel | SDK |
| Plan | aws_ssmcontacts_plan | SDK |
| Rotation | N/A | Framework |


### Examples


#### Contact

```hcl
resource "aws_ssmcontacts_contact" "example" {
  # Example configuration for Contact
  name = "example-contact"

  # Common attributes
  tags = {
    Name        = "example-contact"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Contact Channel

```hcl
resource "aws_ssmcontacts_contact_channel" "example" {
  # Example configuration for Contact Channel
  name = "example-contact_channel"

  # Common attributes
  tags = {
    Name        = "example-contact_channel"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Plan

```hcl
resource "aws_ssmcontacts_plan" "example" {
  # Example configuration for Plan
  name = "example-plan"

  # Common attributes
  tags = {
    Name        = "example-plan"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Rotation

```hcl
resource "aws_ssmcontacts_rotation" "example" {
  # Example configuration for Rotation
  name = "example-rotation"

  # Common attributes
  tags = {
    Name        = "example-rotation"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## ssmincidents

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Replication Set | aws_ssmincidents_replication_set | SDK |
| Response Plan | aws_ssmincidents_response_plan | SDK |


### Examples


#### Replication Set

```hcl
resource "aws_ssmincidents_replication_set" "example" {
  # Example configuration for Replication Set
  name = "example-replication_set"

  # Common attributes
  tags = {
    Name        = "example-replication_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Response Plan

```hcl
resource "aws_ssmincidents_response_plan" "example" {
  # Example configuration for Response Plan
  name = "example-response_plan"

  # Common attributes
  tags = {
    Name        = "example-response_plan"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## ssmquicksetup

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Configuration Manager | N/A | Framework |


### Examples


#### Configuration Manager

```hcl
resource "aws_ssmquicksetup_configuration_manager" "example" {
  # Example configuration for Configuration Manager
  name = "example-configuration_manager"

  # Common attributes
  tags = {
    Name        = "example-configuration_manager"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## ssoadmin

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Application | N/A | Framework |
| Application Access Scope | N/A | Framework |
| Application Assignment | N/A | Framework |
| Application Assignment Configuration | N/A | Framework |
| Permission Set | aws_ssoadmin_permission_set | SDK |
| Trusted Token Issuer | N/A | Framework |


### Examples


#### Application

```hcl
resource "aws_ssoadmin_application" "example" {
  # Example configuration for Application
  name = "example-application"

  # Common attributes
  tags = {
    Name        = "example-application"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Application Access Scope

```hcl
resource "aws_ssoadmin_application_access_scope" "example" {
  # Example configuration for Application Access Scope
  name = "example-application_access_scope"

  # Common attributes
  tags = {
    Name        = "example-application_access_scope"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Application Assignment

```hcl
resource "aws_ssoadmin_application_assignment" "example" {
  # Example configuration for Application Assignment
  name = "example-application_assignment"

  # Common attributes
  tags = {
    Name        = "example-application_assignment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Application Assignment Configuration

```hcl
resource "aws_ssoadmin_application_assignment_configuration" "example" {
  # Example configuration for Application Assignment Configuration
  name = "example-application_assignment_configuration"

  # Common attributes
  tags = {
    Name        = "example-application_assignment_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Permission Set

```hcl
resource "aws_ssoadmin_permission_set" "example" {
  # Example configuration for Permission Set
  name = "example-permission_set"

  # Common attributes
  tags = {
    Name        = "example-permission_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Trusted Token Issuer

```hcl
resource "aws_ssoadmin_trusted_token_issuer" "example" {
  # Example configuration for Trusted Token Issuer
  name = "example-trusted_token_issuer"

  # Common attributes
  tags = {
    Name        = "example-trusted_token_issuer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## storagegateway

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Cache | aws_storagegateway_cache | SDK |
| Cached iSCSI Volume | aws_storagegateway_cached_iscsi_volume | SDK |
| File System Association | aws_storagegateway_file_system_association | SDK |
| Gateway | aws_storagegateway_gateway | SDK |
| NFS File Share | aws_storagegateway_nfs_file_share | SDK |
| SMB File Share | aws_storagegateway_smb_file_share | SDK |
| Stored iSCSI Volume | aws_storagegateway_stored_iscsi_volume | SDK |
| Tape Pool | aws_storagegateway_tape_pool | SDK |
| Upload Buffer | aws_storagegateway_upload_buffer | SDK |
| Working Storage | aws_storagegateway_working_storage | SDK |


### Examples


#### Cache

```hcl
resource "aws_storagegateway_cache" "example" {
  # Example configuration for Cache
  name = "example-cache"

  # Common attributes
  tags = {
    Name        = "example-cache"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Cached iSCSI Volume

```hcl
resource "aws_storagegateway_cached_iscsi_volume" "example" {
  # Example configuration for Cached iSCSI Volume
  name = "example-cached_iscsi_volume"

  # Common attributes
  tags = {
    Name        = "example-cached_iscsi_volume"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### File System Association

```hcl
resource "aws_storagegateway_file_system_association" "example" {
  # Example configuration for File System Association
  name = "example-file_system_association"

  # Common attributes
  tags = {
    Name        = "example-file_system_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Gateway

```hcl
resource "aws_storagegateway_gateway" "example" {
  # Example configuration for Gateway
  name = "example-gateway"

  # Common attributes
  tags = {
    Name        = "example-gateway"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### NFS File Share

```hcl
resource "aws_storagegateway_nfs_file_share" "example" {
  # Example configuration for NFS File Share
  name = "example-nfs_file_share"

  # Common attributes
  tags = {
    Name        = "example-nfs_file_share"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### SMB File Share

```hcl
resource "aws_storagegateway_smb_file_share" "example" {
  # Example configuration for SMB File Share
  name = "example-smb_file_share"

  # Common attributes
  tags = {
    Name        = "example-smb_file_share"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Stored iSCSI Volume

```hcl
resource "aws_storagegateway_stored_iscsi_volume" "example" {
  # Example configuration for Stored iSCSI Volume
  name = "example-stored_iscsi_volume"

  # Common attributes
  tags = {
    Name        = "example-stored_iscsi_volume"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Tape Pool

```hcl
resource "aws_storagegateway_tape_pool" "example" {
  # Example configuration for Tape Pool
  name = "example-tape_pool"

  # Common attributes
  tags = {
    Name        = "example-tape_pool"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Upload Buffer

```hcl
resource "aws_storagegateway_upload_buffer" "example" {
  # Example configuration for Upload Buffer
  name = "example-upload_buffer"

  # Common attributes
  tags = {
    Name        = "example-upload_buffer"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Working Storage

```hcl
resource "aws_storagegateway_working_storage" "example" {
  # Example configuration for Working Storage
  name = "example-working_storage"

  # Common attributes
  tags = {
    Name        = "example-working_storage"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## swf

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Domain | aws_swf_domain | SDK |


### Examples


#### Domain

```hcl
resource "aws_swf_domain" "example" {
  # Example configuration for Domain
  name = "example-domain"

  # Common attributes
  tags = {
    Name        = "example-domain"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## synthetics

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Canary | aws_synthetics_canary | SDK |
| Group | aws_synthetics_group | SDK |
| Group Association | aws_synthetics_group_association | SDK |


### Examples


#### Canary

```hcl
resource "aws_synthetics_canary" "example" {
  # Example configuration for Canary
  name = "example-canary"

  # Common attributes
  tags = {
    Name        = "example-canary"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Group

```hcl
resource "aws_synthetics_group" "example" {
  # Example configuration for Group
  name = "example-group"

  # Common attributes
  tags = {
    Name        = "example-group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Group Association

```hcl
resource "aws_synthetics_group_association" "example" {
  # Example configuration for Group Association
  name = "example-group_association"

  # Common attributes
  tags = {
    Name        = "example-group_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## timestreaminfluxdb

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| DB Instance | N/A | Framework |


### Examples


#### DB Instance

```hcl
resource "aws_timestreaminfluxdb_db_instance" "example" {
  # Example configuration for DB Instance
  name = "example-db_instance"

  # Common attributes
  tags = {
    Name        = "example-db_instance"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## timestreamwrite

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Database | aws_timestreamwrite_database | SDK |
| Table | aws_timestreamwrite_table | SDK |


### Examples


#### Database

```hcl
resource "aws_timestreamwrite_database" "example" {
  # Example configuration for Database
  name = "example-database"

  # Common attributes
  tags = {
    Name        = "example-database"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Table

```hcl
resource "aws_timestreamwrite_table" "example" {
  # Example configuration for Table
  name = "example-table"

  # Common attributes
  tags = {
    Name        = "example-table"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## transcribe

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Language Model | aws_transcribe_language_model | SDK |
| Medical Vocabulary | aws_transcribe_medical_vocabulary | SDK |
| Vocabulary | aws_transcribe_vocabulary | SDK |
| Vocabulary Filter | aws_transcribe_vocabulary_filter | SDK |


### Examples


#### Language Model

```hcl
resource "aws_transcribe_language_model" "example" {
  # Example configuration for Language Model
  name = "example-language_model"

  # Common attributes
  tags = {
    Name        = "example-language_model"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Medical Vocabulary

```hcl
resource "aws_transcribe_medical_vocabulary" "example" {
  # Example configuration for Medical Vocabulary
  name = "example-medical_vocabulary"

  # Common attributes
  tags = {
    Name        = "example-medical_vocabulary"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Vocabulary

```hcl
resource "aws_transcribe_vocabulary" "example" {
  # Example configuration for Vocabulary
  name = "example-vocabulary"

  # Common attributes
  tags = {
    Name        = "example-vocabulary"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Vocabulary Filter

```hcl
resource "aws_transcribe_vocabulary_filter" "example" {
  # Example configuration for Vocabulary Filter
  name = "example-vocabulary_filter"

  # Common attributes
  tags = {
    Name        = "example-vocabulary_filter"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## transfer

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Access | aws_transfer_access | SDK |
| Agreement | aws_transfer_agreement | SDK |
| Certificate | aws_transfer_certificate | SDK |
| Connector | aws_transfer_connector | SDK |
| Profile | aws_transfer_profile | SDK |
| SSH Key | aws_transfer_ssh_key | SDK |
| Server | aws_transfer_server | SDK |
| Transfer Resource Tag | aws_transfer_tag | SDK |
| User | aws_transfer_user | SDK |
| Workflow | aws_transfer_workflow | SDK |


### Examples


#### Access

```hcl
resource "aws_transfer_access" "example" {
  # Example configuration for Access
  name = "example-access"

  # Common attributes
  tags = {
    Name        = "example-access"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Agreement

```hcl
resource "aws_transfer_agreement" "example" {
  # Example configuration for Agreement
  name = "example-agreement"

  # Common attributes
  tags = {
    Name        = "example-agreement"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Certificate

```hcl
resource "aws_transfer_certificate" "example" {
  # Example configuration for Certificate
  name = "example-certificate"

  # Common attributes
  tags = {
    Name        = "example-certificate"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Connector

```hcl
resource "aws_transfer_connector" "example" {
  # Example configuration for Connector
  name = "example-connector"

  # Common attributes
  tags = {
    Name        = "example-connector"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Profile

```hcl
resource "aws_transfer_profile" "example" {
  # Example configuration for Profile
  name = "example-profile"

  # Common attributes
  tags = {
    Name        = "example-profile"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### SSH Key

```hcl
resource "aws_transfer_ssh_key" "example" {
  # Example configuration for SSH Key
  name = "example-ssh_key"

  # Common attributes
  tags = {
    Name        = "example-ssh_key"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Server

```hcl
resource "aws_transfer_server" "example" {
  # Example configuration for Server
  name = "example-server"

  # Common attributes
  tags = {
    Name        = "example-server"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Transfer Resource Tag

```hcl
resource "aws_transfer_tag" "example" {
  # Example configuration for Transfer Resource Tag
  name = "example-transfer_resource_tag"

  # Common attributes
  tags = {
    Name        = "example-transfer_resource_tag"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### User

```hcl
resource "aws_transfer_user" "example" {
  # Example configuration for User
  name = "example-user"

  # Common attributes
  tags = {
    Name        = "example-user"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Workflow

```hcl
resource "aws_transfer_workflow" "example" {
  # Example configuration for Workflow
  name = "example-workflow"

  # Common attributes
  tags = {
    Name        = "example-workflow"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## verifiedpermissions

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Identity Source | N/A | Framework |
| Policy | N/A | Framework |
| Policy Store | N/A | Framework |
| Policy Template | N/A | Framework |
| Schema | N/A | Framework |


### Examples


#### Identity Source

```hcl
resource "aws_verifiedpermissions_identity_source" "example" {
  # Example configuration for Identity Source
  name = "example-identity_source"

  # Common attributes
  tags = {
    Name        = "example-identity_source"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Policy

```hcl
resource "aws_verifiedpermissions_policy" "example" {
  # Example configuration for Policy
  name = "example-policy"

  # Common attributes
  tags = {
    Name        = "example-policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Policy Store

```hcl
resource "aws_verifiedpermissions_policy_store" "example" {
  # Example configuration for Policy Store
  name = "example-policy_store"

  # Common attributes
  tags = {
    Name        = "example-policy_store"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Policy Template

```hcl
resource "aws_verifiedpermissions_policy_template" "example" {
  # Example configuration for Policy Template
  name = "example-policy_template"

  # Common attributes
  tags = {
    Name        = "example-policy_template"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Schema

```hcl
resource "aws_verifiedpermissions_schema" "example" {
  # Example configuration for Schema
  name = "example-schema"

  # Common attributes
  tags = {
    Name        = "example-schema"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## vpclattice

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Access Log Subscription | aws_vpclattice_access_log_subscription | SDK |
| Listener | aws_vpclattice_listener | SDK |
| Listener Rule | aws_vpclattice_listener_rule | SDK |
| Resource Gateway | N/A | Framework |
| Resource Policy | aws_vpclattice_resource_policy | SDK |
| Service | aws_vpclattice_service | SDK |
| Service Network | aws_vpclattice_service_network | SDK |
| Service Network Service Association | aws_vpclattice_service_network_service_association | SDK |
| Service Network VPC Association | aws_vpclattice_service_network_vpc_association | SDK |
| Target Group | aws_vpclattice_target_group | SDK |
| Target Group Attachment | aws_vpclattice_target_group_attachment | SDK |


### Examples


#### Access Log Subscription

```hcl
resource "aws_vpclattice_access_log_subscription" "example" {
  # Example configuration for Access Log Subscription
  name = "example-access_log_subscription"

  # Common attributes
  tags = {
    Name        = "example-access_log_subscription"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Listener

```hcl
resource "aws_vpclattice_listener" "example" {
  # Example configuration for Listener
  name = "example-listener"

  # Common attributes
  tags = {
    Name        = "example-listener"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Listener Rule

```hcl
resource "aws_vpclattice_listener_rule" "example" {
  # Example configuration for Listener Rule
  name = "example-listener_rule"

  # Common attributes
  tags = {
    Name        = "example-listener_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource Gateway

```hcl
resource "aws_vpclattice_resource_gateway" "example" {
  # Example configuration for Resource Gateway
  name = "example-resource_gateway"

  # Common attributes
  tags = {
    Name        = "example-resource_gateway"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Resource Policy

```hcl
resource "aws_vpclattice_resource_policy" "example" {
  # Example configuration for Resource Policy
  name = "example-resource_policy"

  # Common attributes
  tags = {
    Name        = "example-resource_policy"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Service

```hcl
resource "aws_vpclattice_service" "example" {
  # Example configuration for Service
  name = "example-service"

  # Common attributes
  tags = {
    Name        = "example-service"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Service Network

```hcl
resource "aws_vpclattice_service_network" "example" {
  # Example configuration for Service Network
  name = "example-service_network"

  # Common attributes
  tags = {
    Name        = "example-service_network"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Service Network Service Association

```hcl
resource "aws_vpclattice_service_network_service_association" "example" {
  # Example configuration for Service Network Service Association
  name = "example-service_network_service_association"

  # Common attributes
  tags = {
    Name        = "example-service_network_service_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Service Network VPC Association

```hcl
resource "aws_vpclattice_service_network_vpc_association" "example" {
  # Example configuration for Service Network VPC Association
  name = "example-service_network_vpc_association"

  # Common attributes
  tags = {
    Name        = "example-service_network_vpc_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Target Group

```hcl
resource "aws_vpclattice_target_group" "example" {
  # Example configuration for Target Group
  name = "example-target_group"

  # Common attributes
  tags = {
    Name        = "example-target_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Target Group Attachment

```hcl
resource "aws_vpclattice_target_group_attachment" "example" {
  # Example configuration for Target Group Attachment
  name = "example-target_group_attachment"

  # Common attributes
  tags = {
    Name        = "example-target_group_attachment"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## waf

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| ByteMatchSet | aws_waf_byte_match_set | SDK |
| GeoMatchSet | aws_waf_geo_match_set | SDK |
| IPSet | aws_waf_ipset | SDK |
| Rate Based Rule | aws_waf_rate_based_rule | SDK |
| Regex Match Set | aws_waf_regex_match_set | SDK |
| Regex Pattern Set | aws_waf_regex_pattern_set | SDK |
| Rule | aws_waf_rule | SDK |
| Rule Group | aws_waf_rule_group | SDK |
| Size Constraint Set | aws_waf_size_constraint_set | SDK |
| SqlInjectionMatchSet | aws_waf_sql_injection_match_set | SDK |
| Web ACL | aws_waf_web_acl | SDK |
| XSS Match Set | aws_waf_xss_match_set | SDK |


### Examples


#### ByteMatchSet

```hcl
resource "aws_waf_byte_match_set" "example" {
  # Example configuration for ByteMatchSet
  name = "example-bytematchset"

  # Common attributes
  tags = {
    Name        = "example-bytematchset"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### GeoMatchSet

```hcl
resource "aws_waf_geo_match_set" "example" {
  # Example configuration for GeoMatchSet
  name = "example-geomatchset"

  # Common attributes
  tags = {
    Name        = "example-geomatchset"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### IPSet

```hcl
resource "aws_waf_ipset" "example" {
  # Example configuration for IPSet
  name = "example-ipset"

  # Common attributes
  tags = {
    Name        = "example-ipset"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Rate Based Rule

```hcl
resource "aws_waf_rate_based_rule" "example" {
  # Example configuration for Rate Based Rule
  name = "example-rate_based_rule"

  # Common attributes
  tags = {
    Name        = "example-rate_based_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Regex Match Set

```hcl
resource "aws_waf_regex_match_set" "example" {
  # Example configuration for Regex Match Set
  name = "example-regex_match_set"

  # Common attributes
  tags = {
    Name        = "example-regex_match_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Regex Pattern Set

```hcl
resource "aws_waf_regex_pattern_set" "example" {
  # Example configuration for Regex Pattern Set
  name = "example-regex_pattern_set"

  # Common attributes
  tags = {
    Name        = "example-regex_pattern_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Rule

```hcl
resource "aws_waf_rule" "example" {
  # Example configuration for Rule
  name = "example-rule"

  # Common attributes
  tags = {
    Name        = "example-rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Rule Group

```hcl
resource "aws_waf_rule_group" "example" {
  # Example configuration for Rule Group
  name = "example-rule_group"

  # Common attributes
  tags = {
    Name        = "example-rule_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Size Constraint Set

```hcl
resource "aws_waf_size_constraint_set" "example" {
  # Example configuration for Size Constraint Set
  name = "example-size_constraint_set"

  # Common attributes
  tags = {
    Name        = "example-size_constraint_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### SqlInjectionMatchSet

```hcl
resource "aws_waf_sql_injection_match_set" "example" {
  # Example configuration for SqlInjectionMatchSet
  name = "example-sqlinjectionmatchset"

  # Common attributes
  tags = {
    Name        = "example-sqlinjectionmatchset"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Web ACL

```hcl
resource "aws_waf_web_acl" "example" {
  # Example configuration for Web ACL
  name = "example-web_acl"

  # Common attributes
  tags = {
    Name        = "example-web_acl"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### XSS Match Set

```hcl
resource "aws_waf_xss_match_set" "example" {
  # Example configuration for XSS Match Set
  name = "example-xss_match_set"

  # Common attributes
  tags = {
    Name        = "example-xss_match_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## wafregional

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Byte Match Set | aws_wafregional_byte_match_set | SDK |
| Geo Match Set | aws_wafregional_geo_match_set | SDK |
| IPSet | aws_wafregional_ipset | SDK |
| Rate Based Rule | aws_wafregional_rate_based_rule | SDK |
| Regex Match Set | aws_wafregional_regex_match_set | SDK |
| Regex Pattern Set | aws_wafregional_regex_pattern_set | SDK |
| Rule | aws_wafregional_rule | SDK |
| Rule Group | aws_wafregional_rule_group | SDK |
| SQL Injection Match Set | aws_wafregional_sql_injection_match_set | SDK |
| Size Constraint Set | aws_wafregional_size_constraint_set | SDK |
| Web ACL | aws_wafregional_web_acl | SDK |
| Web ACL Association | aws_wafregional_web_acl_association | SDK |
| XSS Match Set | aws_wafregional_xss_match_set | SDK |


### Examples


#### Byte Match Set

```hcl
resource "aws_wafregional_byte_match_set" "example" {
  # Example configuration for Byte Match Set
  name = "example-byte_match_set"

  # Common attributes
  tags = {
    Name        = "example-byte_match_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Geo Match Set

```hcl
resource "aws_wafregional_geo_match_set" "example" {
  # Example configuration for Geo Match Set
  name = "example-geo_match_set"

  # Common attributes
  tags = {
    Name        = "example-geo_match_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### IPSet

```hcl
resource "aws_wafregional_ipset" "example" {
  # Example configuration for IPSet
  name = "example-ipset"

  # Common attributes
  tags = {
    Name        = "example-ipset"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Rate Based Rule

```hcl
resource "aws_wafregional_rate_based_rule" "example" {
  # Example configuration for Rate Based Rule
  name = "example-rate_based_rule"

  # Common attributes
  tags = {
    Name        = "example-rate_based_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Regex Match Set

```hcl
resource "aws_wafregional_regex_match_set" "example" {
  # Example configuration for Regex Match Set
  name = "example-regex_match_set"

  # Common attributes
  tags = {
    Name        = "example-regex_match_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Regex Pattern Set

```hcl
resource "aws_wafregional_regex_pattern_set" "example" {
  # Example configuration for Regex Pattern Set
  name = "example-regex_pattern_set"

  # Common attributes
  tags = {
    Name        = "example-regex_pattern_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Rule

```hcl
resource "aws_wafregional_rule" "example" {
  # Example configuration for Rule
  name = "example-rule"

  # Common attributes
  tags = {
    Name        = "example-rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Rule Group

```hcl
resource "aws_wafregional_rule_group" "example" {
  # Example configuration for Rule Group
  name = "example-rule_group"

  # Common attributes
  tags = {
    Name        = "example-rule_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### SQL Injection Match Set

```hcl
resource "aws_wafregional_sql_injection_match_set" "example" {
  # Example configuration for SQL Injection Match Set
  name = "example-sql_injection_match_set"

  # Common attributes
  tags = {
    Name        = "example-sql_injection_match_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Size Constraint Set

```hcl
resource "aws_wafregional_size_constraint_set" "example" {
  # Example configuration for Size Constraint Set
  name = "example-size_constraint_set"

  # Common attributes
  tags = {
    Name        = "example-size_constraint_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Web ACL

```hcl
resource "aws_wafregional_web_acl" "example" {
  # Example configuration for Web ACL
  name = "example-web_acl"

  # Common attributes
  tags = {
    Name        = "example-web_acl"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Web ACL Association

```hcl
resource "aws_wafregional_web_acl_association" "example" {
  # Example configuration for Web ACL Association
  name = "example-web_acl_association"

  # Common attributes
  tags = {
    Name        = "example-web_acl_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### XSS Match Set

```hcl
resource "aws_wafregional_xss_match_set" "example" {
  # Example configuration for XSS Match Set
  name = "example-xss_match_set"

  # Common attributes
  tags = {
    Name        = "example-xss_match_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## wafv2

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| IP Set | aws_wafv2_ip_set | SDK |
| Regex Pattern Set | aws_wafv2_regex_pattern_set | SDK |
| Rule Group | aws_wafv2_rule_group | SDK |
| Web ACL | aws_wafv2_web_acl | SDK |
| Web ACL Association | aws_wafv2_web_acl_association | SDK |
| Web ACL Logging Configuration | aws_wafv2_web_acl_logging_configuration | SDK |


### Examples


#### IP Set

```hcl
resource "aws_wafv2_ip_set" "example" {
  # Example configuration for IP Set
  name = "example-ip_set"

  # Common attributes
  tags = {
    Name        = "example-ip_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Regex Pattern Set

```hcl
resource "aws_wafv2_regex_pattern_set" "example" {
  # Example configuration for Regex Pattern Set
  name = "example-regex_pattern_set"

  # Common attributes
  tags = {
    Name        = "example-regex_pattern_set"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Rule Group

```hcl
resource "aws_wafv2_rule_group" "example" {
  # Example configuration for Rule Group
  name = "example-rule_group"

  # Common attributes
  tags = {
    Name        = "example-rule_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Web ACL

```hcl
resource "aws_wafv2_web_acl" "example" {
  # Example configuration for Web ACL
  name = "example-web_acl"

  # Common attributes
  tags = {
    Name        = "example-web_acl"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Web ACL Association

```hcl
resource "aws_wafv2_web_acl_association" "example" {
  # Example configuration for Web ACL Association
  name = "example-web_acl_association"

  # Common attributes
  tags = {
    Name        = "example-web_acl_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Web ACL Logging Configuration

```hcl
resource "aws_wafv2_web_acl_logging_configuration" "example" {
  # Example configuration for Web ACL Logging Configuration
  name = "example-web_acl_logging_configuration"

  # Common attributes
  tags = {
    Name        = "example-web_acl_logging_configuration"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## worklink

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Fleet | aws_worklink_fleet | SDK |
| Website Certificate Authority Association | aws_worklink_website_certificate_authority_association | SDK |


### Examples


#### Fleet

```hcl
resource "aws_worklink_fleet" "example" {
  # Example configuration for Fleet
  name = "example-fleet"

  # Common attributes
  tags = {
    Name        = "example-fleet"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Website Certificate Authority Association

```hcl
resource "aws_worklink_website_certificate_authority_association" "example" {
  # Example configuration for Website Certificate Authority Association
  name = "example-website_certificate_authority_association"

  # Common attributes
  tags = {
    Name        = "example-website_certificate_authority_association"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## workspaces

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Connection Alias | N/A | Framework |
| Directory | aws_workspaces_directory | SDK |
| IP Group | aws_workspaces_ip_group | SDK |
| Workspace | aws_workspaces_workspace | SDK |


### Examples


#### Connection Alias

```hcl
resource "aws_workspaces_connection_alias" "example" {
  # Example configuration for Connection Alias
  name = "example-connection_alias"

  # Common attributes
  tags = {
    Name        = "example-connection_alias"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Directory

```hcl
resource "aws_workspaces_directory" "example" {
  # Example configuration for Directory
  name = "example-directory"

  # Common attributes
  tags = {
    Name        = "example-directory"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### IP Group

```hcl
resource "aws_workspaces_ip_group" "example" {
  # Example configuration for IP Group
  name = "example-ip_group"

  # Common attributes
  tags = {
    Name        = "example-ip_group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Workspace

```hcl
resource "aws_workspaces_workspace" "example" {
  # Example configuration for Workspace
  name = "example-workspace"

  # Common attributes
  tags = {
    Name        = "example-workspace"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



## xray

| Resource Name | Resource Type | Implementation |
|---------------|--------------|----------------|
| Group | aws_xray_group | SDK |
| Sampling Rule | aws_xray_sampling_rule | SDK |


### Examples


#### Group

```hcl
resource "aws_xray_group" "example" {
  # Example configuration for Group
  name = "example-group"

  # Common attributes
  tags = {
    Name        = "example-group"
    Environment = "dev"
    Terraform   = "true"
  }
}
```


#### Sampling Rule

```hcl
resource "aws_xray_sampling_rule" "example" {
  # Example configuration for Sampling Rule
  name = "example-sampling_rule"

  # Common attributes
  tags = {
    Name        = "example-sampling_rule"
    Environment = "dev"
    Terraform   = "true"
  }
}
```



