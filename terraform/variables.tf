variable "aws_region" {
  description = "AWS region for DynamoDB resources."
  type        = string
  default     = "us-east-1"
}

variable "muted_table_name" {
  description = "DynamoDB table name for tracking muted users."
  type        = string
  default     = "izumi-muted-users"
}

variable "environment" {
  description = "Environment label used for resource tags."
  type        = string
  default     = "prod"
}
