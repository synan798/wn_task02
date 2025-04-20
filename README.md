# wn_task02
Task 2 of Assignment 2

docker network create my_socket_ipc_network

docker build -t my_ipc_server .
docker run -rm --network=my_socket_ipc_network --name ipc_server_dns_name my_ipc_server

docker build -t my_ipc_client .
docker run -rm --network=my_socket_ipc_network my_ipc_client
