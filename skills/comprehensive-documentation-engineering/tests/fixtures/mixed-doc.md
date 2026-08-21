# Authentication

## Overview

Authentication in our system uses OAuth 2.0 because it provides delegated
authorization without sharing credentials. Historically we used API keys, but
they proved fragile for delegated access.

## Getting started

In this tutorial, we will build our first authenticated request. First, create
an API key. Now, notice that the response includes a `token` field.

## API reference

### POST /auth/token

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `grant_type` | string | yes | One of `client_credentials`, `authorization_code`. |
| `scope` | string | no | Space-separated scopes. |

Returns a `Token` object with `access_token` and `expires_at`.

## How to rotate a secret

To rotate your signing secret, run `auth rotate-secret` and update your
environment. If you use multiple regions, rotate each region in turn.
