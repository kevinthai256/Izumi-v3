<h1 align="center">
  <br>
  <a><img src="https://i.imgur.com/G16rGZA.png" alt="Izumi"</a>
  <br>
  Izumi Discord Bot
  <br>
</h1>

<h4 align="center">A modular Discord bot for moderation, fun, anime, and giveaway workflows.</h4>

# Izumi Bot

## Overview

Izumi is a Python-based Discord bot built around modular command cogs. It combines moderation, utility, anime, interaction, and giveaway commands in one service, with DynamoDB-backed persistence for mute state and Terraform-managed infrastructure.

## Features

- Moderation commands including mute/unmute, kick, ban, and message cleanup.
- Giveaway flow with create, reroll, and delete support.
- Anime- and media-focused commands, plus fun and interaction commands.
- Cog-based command loading from `lib/commands`.
- DynamoDB persistence for muted/unmuted status.
- Terraform configuration for DynamoDB deployment.

## Project Stack

- Language: Python 3
- Bot framework: `discord.py` / `discord`
- HTTP client utilities: `aiohttp`
- Persistence: AWS DynamoDB via `boto3`
- Infra as code: Terraform (AWS provider)
- Configuration: `.env` values via `python-dotenv`

## File Structure

```text
.
|-- main.py
|-- requirements.txt
|-- README.md
|-- lib/
|   |-- bot/
|   |   `-- __init__.py        # Bot class, event handling, status loop, errors
|   |-- commands/
|   |   |-- general.py
|   |   |-- mod.py             # Moderation commands + mute/unmute flow
|   |   |-- giveaway.py
|   |   |-- fun.py
|   |   |-- anime.py
|   |   |-- action.py
|   |   `-- image.py
|   `-- util/
|       |-- muted.py           # DynamoDB helpers for muted state
|       |-- functions.py
|       |-- cmd.py
|       |-- keep_alive.py
|       `-- ...                # API helpers, constants, utility modules
`-- terraform/
    |-- versions.tf
    |-- variables.tf
    |-- main.tf                # DynamoDB table definition
    `-- outputs.tf
```

## Run Locally

### 1) Prerequisites

- Python 3.10+ recommended
- `pip`
- AWS credentials with DynamoDB access (if using mute persistence)
- Terraform 1.5+ (for infrastructure provisioning)
- A Discord bot token from the Discord Developer Portal

### 2) Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3) Configure environment variables

Create a `.env` file in the project root:

```env
DISCORD_API_KEY=your_discord_bot_token

# Optional command integrations
KLIPY_API_KEY=your_klipy_api_key
GEMINI_API_KEY=your_gemini_api_key

# DynamoDB (mute tracking)
AWS_REGION=us-east-1
MUTED_TABLE_NAME=izumi-muted-users
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
# AWS_SESSION_TOKEN=optional_if_using_temporary_credentials
```

### 4) Provision DynamoDB with Terraform

```bash
cd terraform
terraform init
terraform apply \
  -var="aws_region=us-east-1" \
  -var="muted_table_name=izumi-muted-users"
cd ..
```

### 5) Start the bot

```bash
python3 main.py
```

## How the Architecture Works

- `main.py` initializes the Discord client and dynamically loads all command cogs from `lib/commands`.
- Each file in `lib/commands` defines a focused command group (mod, giveaway, anime, etc.).
- Shared helpers and API utilities live in `lib/util`.
- Mute/unmute state is written to DynamoDB in `lib/util/muted.py`.
- Terraform keeps the DynamoDB resource declarative and repeatable across environments.

## Why These Design Decisions

- Modular cogs reduce coupling and make new command categories easy to add.
- Utility modules centralize reusable logic, reducing duplicate code.
- DynamoDB provides a low-ops, scalable key-value store for moderation state.
- Terraform allows predictable infra changes, reviewable in version control.

## Opportunities for Improvement and Scale

- Prefer Discord timeout for mute enforcement if role-based behavior is not desired.
- Add automated tests (`pytest`) for command behavior and utility modules.
- Add CI checks for linting, tests, and Terraform validation on pull requests.
- Move blocking AWS calls to async-native clients (or robust task queue patterns) if throughput grows.
- Introduce structured logging, metrics, and alerting for production operations.
- Add config layering (dev/staging/prod) and secret management via AWS SSM/Secrets Manager.
- Add sharding and horizontal worker strategy for large multi-guild deployments.
