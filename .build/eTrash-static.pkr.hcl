source "docker" "base_etrash" {
  image = "550661752655.dkr.ecr.eu-west-1.amazonaws.com/base-etrash"
  commit = true
  ecr_login = true
  login_server = "https://550661752655.dkr.ecr.eu-west-1.amazonaws.com/mitlan"
  changes = [
    "ENV FOO bar",
    "ENTRYPOINT [\"nginx\", \"-g\", \"daemon off;\"]"
  ]
}

build {
  sources = ["source.docker.base_etrash"]

  provisioner "shell" {
    inline = ["mkdir /etrash"]
  }

  provisioner "file" {
    source = "../static"
    destination = "/etrash"
  }

  post-processors {
    post-processor "docker-tag" {
      repository = "550661752655.dkr.ecr.eu-west-1.amazonaws.com/etrash-static"
      tags       = ["latest"]
    }

    post-processor "docker-push" {
      ecr_login = true
      login_server = "https://550661752655.dkr.ecr.eu-west-1.amazonaws.com/mitlan"
    }
  }
}
