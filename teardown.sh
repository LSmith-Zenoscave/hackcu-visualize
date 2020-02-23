set -x

MY_INSTANCE_NAME="hackcu-visualize"
ZONE=us-central1-f

gcloud compute instances delete $MY_INSTANCE_NAME \
    --zone=$ZONE --delete-disks=all

gcloud compute firewall-rules delete default-allow-http-8080
