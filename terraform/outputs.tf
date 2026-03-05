output "muted_users_table_name" {
  description = "DynamoDB table name used by the bot."
  value       = aws_dynamodb_table.muted_users.name
}

output "muted_users_table_arn" {
  description = "DynamoDB table ARN for IAM policies."
  value       = aws_dynamodb_table.muted_users.arn
}
