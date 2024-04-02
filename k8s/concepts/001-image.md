Define, Build and Modify Container Images
---

- Create custom nginx image

- Create image directory to contain files
  - `mkdir nginx-custom`
- Go to root of the image directory
  - `cd nginx-custom`
- Create [Dockerfile](../resources/nginx-custom/Dockerfile)
- Pull image on local
  - `docker pull nginx:latest`
- List local images
  - `docker images`
- Build docker image
  - `docker build -t nextgenadarsh/nginx .`
- Publish image
  - `docker push nextgenadarsh/nginx`

