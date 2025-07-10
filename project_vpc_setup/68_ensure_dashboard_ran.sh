cd "$(dirname "$(realpath "$0")")"
sudo ./pk_ensure_wired_connection_1_set_as_124.sh


# TBD
# remove previous version
# docker rmi mkrmkrmkrmkr:8004/a2z/aifw_dashboard_frontend:0.0.2_dev -f
# docker rmi mkrmkrmkrmkr:8004/a2z/aifw_dashboard_backend:0.0.2_dev -f


# modlule-type A -> both
# docker pull "mkrmkrmkrmkr:8004/a2z/aifw_dashboard_frontend:0.0.2_dev"
# docker pull "mkrmkrmkrmkr:8004/a2z/aifw_dashboard_backend:0.0.2_dev"

# module-type B -> only backend
docker pull "mkrmkrmkrmkr:8004/a2z/aifw_dashboard_backend:0.0.2_dev"

run_dashboard
