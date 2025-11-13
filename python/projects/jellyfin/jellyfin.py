'''

services:
  jellyfin:
    image: jellyfin/jellyfin:latest
    container_name: jellyfin
    environment:
      - PUID = 1026
      - GUID = 100
      - JELLYFIN_PublishedServerUrl = http://...:8096/
    network_mode: host
    volumes:
     - /volume1/docker/jellyfin/config:/config:rw
     - /volume1/docker/jellyfin/cache:/cache:rw
     - /volume1/media/movies:/movies:rw
     - /volume1/media/kidsmovies:/kidsmovies:rw
     - /volume1/media/tvshows:/tvshows:rw
     - /volume1/media/kidstvshows:/kidstvshows:rw
     - /volume1/media/gym:/gym:rw
     - /volume1/media/docuseries:/docuseries:rw
     - /volume1/media/anon:/anon:rw
     - /volume1/media/miniseries:/miniseries:rw
     - /volume1/media/podcast:/podcast:rw
     - /volume1/media/music:/music:rw
    restart: 'unless-stopped'
    ports:
    # nas / container
     - 8073-8096 
     

'''