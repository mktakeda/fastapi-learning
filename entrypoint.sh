#!/bin/sh

set -e

# Create secrets directory if it doesn't exist
mkdir -p ./secrets

# Write keys to files if content is provided
if [ -n "$PUBLIC_KEY_CONTENT" ]; then
  echo "$PUBLIC_KEY_CONTENT" > ./secrets/public.pem
  echo "Public key written to ./secrets/public.pem"
fi

if [ -n "$PRIVATE_KEY_CONTENT" ]; then
  echo "$PRIVATE_KEY_CONTENT" > ./secrets/private.pem
  echo "Private key written to ./secrets/private.pem"
fi

# Execute CMD passed to the container (uvicorn command)
exec "$@"
