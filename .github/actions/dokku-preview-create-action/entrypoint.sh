#!/bin/sh
set -e

echo "Setting up SSH directory"
SSH_PATH="$HOME/.ssh"
mkdir -p "$SSH_PATH"
chmod 700 "$SSH_PATH"

echo "Saving SSH key"
echo "$PRIVATE_KEY" > "$SSH_PATH/deploy_key"
chmod 600 "$SSH_PATH/deploy_key"

GIT_SSH_COMMAND="ssh -p ${PORT-22} -i $SSH_PATH/deploy_key"
if [ -n "$HOST_KEY" ]; then
    echo "Adding hosts key to known_hosts"
    echo "$HOST_KEY" >> "$SSH_PATH/known_hosts"
    chmod 600 "$SSH_PATH/known_hosts"
else
    echo "Disabling host key checking"
    GIT_SSH_COMMAND="$GIT_SSH_COMMAND -o StrictHostKeyChecking=no"
fi

REF=$(echo $GITHUB_REF | sed -e 's/\//-/g')
APP_NAME="$PROJECT-$REF"

echo "Creating app $APP_NAME"

# create app
# TODO: handle creation based on pr status
$GIT_SSH_COMMAND dokku@$HOST "apps:create $APP_NAME" || true

# enable ssl
# TODO: only when PR/app is created
$GIT_SSH_COMMAND dokku@$HOST "letsencrypt $APP_NAME"

echo "The deploy is starting"

GIT_COMMAND="git push --force dokku@$HOST:$APP_NAME HEAD:refs/heads/master"

echo "GIT_SSH_COMMAND="$GIT_SSH_COMMAND" $GIT_COMMAND"
GIT_SSH_COMMAND="$GIT_SSH_COMMAND" $GIT_COMMAND

URL="https://$APP_NAME.app.etalab.studio"
echo "::set-output name=url::$URL"