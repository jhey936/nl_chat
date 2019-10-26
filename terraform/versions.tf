provider "google-beta" {
  credentials = file("account.json")
  project     = "hackathon"
  region      = "us-east1"
}

terraform {
  required_version = ">= 0.12"
}

