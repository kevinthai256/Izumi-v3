provider "aws" {
  region = var.aws_region
}

resource "aws_dynamodb_table" "muted_users" {
  name         = var.muted_table_name
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "guild_id"
  range_key    = "user_id"

  attribute {
    name = "guild_id"
    type = "S"
  }

  attribute {
    name = "user_id"
    type = "S"
  }

  point_in_time_recovery {
    enabled = true
  }

  server_side_encryption {
    enabled = true
  }

  tags = {
    Name        = var.muted_table_name
    Environment = var.environment
    Service     = "izumi-bot"
  }
}
