"""

services:
  jellyfin:
    image: jellyfin/jellyfin:latest
    container_name: jellyfin
    environment:
      - PUID=1026
      - GUID=100
    network_mode: host
    volumes:
     - /volume1/docker/jellyfin/config:/config
     - /volume1/docker/jellyfin/cache:/cache
     - /volume1/media/Movie Collection/Movies
     - /volume1/media/Movie Collection/Kids Movies
     - /volume1/media/Movie Collection/Tv Shows
    restart: 'unless-stopped'
    ports:
     - 8073-8096 

"""