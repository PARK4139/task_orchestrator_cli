# network 
cd "$(dirname "$(realpath "$0")")"
sudo ./pk_ensure_wired_connection_1_set_as_124.sh

# remove container all
sudo run_container --rm-all

# remove docker image (old released version)
docker rmi mkrmkrmkrmkr:8004/a2z/no_image:0.0.3_dev
docker rmi a2z/no_image:0.0.3_dev

# pull docker image (new released version)
docker pull mkrmkrmkrmkr:8004/a2z/no_image:0.0.4_dev
docker image tag mkrmkrmkrmkr:8004/a2z/no_image:0.0.4_dev a2z/no_image:0.0.4_dev
