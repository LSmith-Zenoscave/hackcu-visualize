read -s -p "Enter password for encryption: " password
echo

tar cvf secrets.tar service-account.json
openssl aes-256-cbc -k "$password" -in secrets.tar -out secrets.tar.enc
rm secrets.tar
