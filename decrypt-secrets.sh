password=$1

openssl aes-256-cbc -k "$password" -in secrets.tar.enc -out secrets.tar -d
tar xvf secrets.tar