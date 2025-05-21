#!/bin/sh

set -e

SECRETS_DIR=./secrets
PRIVATE_KEY_FILE="$SECRETS_DIR/private.pem"
PUBLIC_KEY_FILE="$SECRETS_DIR/public.pem"

# Create secrets directory if it doesn't exist
mkdir -p "$SECRETS_DIR"

# Write provided public key if available
if [ -n "$PUBLIC_KEY_CONTENT" ]; then
  echo "$PUBLIC_KEY_CONTENT" > "$PUBLIC_KEY_FILE"
  echo "Public key written to $PUBLIC_KEY_FILE"
fi

# Write provided private key if available
if [ -n "$PRIVATE_KEY_CONTENT" ]; then
  echo "$PRIVATE_KEY_CONTENT" > "$PRIVATE_KEY_FILE"
  echo "Private key written to $PRIVATE_KEY_FILE"
fi

# If either key is missing, generate both
if [ ! -f "$PRIVATE_KEY_FILE" ] || [ ! -f "$PUBLIC_KEY_FILE" ]; then
  echo "Generating new RSA key pair with openssl..."

  openssl genrsa -out "$PRIVATE_KEY_FILE" 2048
  openssl rsa -in "$PRIVATE_KEY_FILE" -pubout -out "$PUBLIC_KEY_FILE"

  echo "Generated private key at $PRIVATE_KEY_FILE"
  echo "Generated public key at $PUBLIC_KEY_FILE"
fi

# Execute CMD passed to the container (e.g., uvicorn ...)
exec "$@"
