# RedShift Reader

A script to quickly export tables from serverless RedShift workgroups with SSO access.

## Overview

The script is intended for use with serverless environments only and requires TEMP permissions for your role.

RedShift uses hyphens and quotation marks in its SQL queries, so the script parses the CLI arguments and adds the quotation marks automatically for ease of use.

The hardcoded limit of rows is 50, since the script is intended to give a quick overview of the table in question, and nothing more.

## Pre-requisites

1. AWS CLI with SSO configured.
2. Python 3.
3. TEMP (or higher) permission on the RedShift workgroup for the intended user/role.

## Usage

1. Run `aws configure sso` in the terminal and indicate the start URL, default region and account ID.
2. Run `aws sso login --profile <company>' in the terminal to initiate the work session, replacing <company> with the profile name provided in step 1.
3. Create CONSTANTS.py in the folder with the script and provide the following values:

```
PROFILE = "AWS SSO profile name"
REGION = "AWS region"

WORKGROUP_NAME = "RedShift workgroup name"
DATABASE = "RedShift database name"
DB_USER = "RedShift user"

NATIVE_DB = "RedShift native database name"
```

4. Launch the script with `python3 extract.py <schema>.<table>`, replacing <schema> and <table> with required names.

## Known Issues

Since this script is created for a specific purpose, the query structure is rigid, and the pattern of the database names is hardcoded.

## To-Do

1. Add an interface to flexibly type the database, schema and table names.
2. Add a way to prompt for the constants and create a CONSTANTS.py file automatically if it is missing.
3. Add settings for LIMIT query.
4. Add a feature to name the resulting files after the exported tables.
5. Add a way to choose the download location.
6. Add a loading indicator while RedShift is queried.