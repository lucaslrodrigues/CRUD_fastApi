# docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)
# Remove env
# docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)

# Remove all
docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q) && docker rmi $(docker images -a -q)
clear
# remover containers, imagens e networks
# docker system prune

# remover volumes
# docker system prune --all --force --volumes