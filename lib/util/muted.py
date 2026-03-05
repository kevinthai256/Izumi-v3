import os
from datetime import datetime, timezone

import boto3
from botocore.exceptions import BotoCoreError, ClientError
from dotenv import load_dotenv

load_dotenv()


def _table():
    region = os.getenv("AWS_REGION", "us-east-1")
    table_name = os.getenv("MUTED_TABLE_NAME", "izumi-muted-users")
    dynamodb = boto3.resource("dynamodb", region_name=region)
    return dynamodb.Table(table_name)


def update_muted(guild_id: int, user_id: int) -> bool:
    table = _table()
    now = datetime.now(timezone.utc).isoformat()

    try:
        table.put_item(
            Item={
                "guild_id": str(guild_id),
                "user_id": str(user_id),
                "is_muted": True,
                "updated_at": now,
            }
        )
        return True
    except (BotoCoreError, ClientError):
        return False


def remove_muted(guild_id: int, user_id: int) -> bool:
    table = _table()
    now = datetime.now(timezone.utc).isoformat()

    try:
        # Keep an audit trail by marking unmuted instead of deleting.
        table.put_item(
            Item={
                "guild_id": str(guild_id),
                "user_id": str(user_id),
                "is_muted": False,
                "updated_at": now,
            }
        )
        return True
    except (BotoCoreError, ClientError):
        return False
