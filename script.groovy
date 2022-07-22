def docker_deploy() {
  docker rm -f dogworld || true

  docker run -p 1234:1234 -d --name dogworld dogworld:latest
}

def echo_out(word) {
  echo "${word}"
}