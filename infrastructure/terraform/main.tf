resource "aws_s3_bucket" "mlops_demo_bucket" {
  bucket = "mlops-engineering-demo-882507341805"

  tags = {
    Name        = "MLOps Engineering Demo"
    Environment = "Learning"
    ManagedBy   = "Terraform"
  }
}