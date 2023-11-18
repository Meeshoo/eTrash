variables {
  access_key="${env("AWS_ACCESS_KEY_ID")}"
  secret_key="${env("AWS_SECRET_ACCESS_KEY")}"
}

source "docker" "python" {
  image = "python"
  commit = true
  changes = [
    "ENV FOO bar",
    "WORKDIR /etrash",
    "CMD [\"eTrash.wsgi:application\", \"--bind\", \"0.0.0.0:80\"]",
    "ENTRYPOINT [\"gunicorn\"]"
  ]
}

build {
  sources = ["source.docker.python"]

  provisioner "shell" {
    inline = ["mkdir /etrash"]
  }

  provisioner "file" {
    source = "../"
    destination = "/etrash"
  }

  provisioner "shell" {
    inline = ["pip install -r /etrash/requirements.txt"]
  }

  post-processors {
    post-processor "docker-tag" {
      repository = "550661752655.dkr.ecr.eu-west-1.amazonaws.com/etrash-python"
      tags       = ["latest"]
    }

    post-processor "docker-push" {
      ecr_login = true
      aws_access_key = var.access_key
      aws_secret_key = var.secret_key
      login_server = "https://550661752655.dkr.ecr.eu-west-1.amazonaws.com/mitlan"
    }
  }
}
