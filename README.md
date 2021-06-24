1. `aws s3 sync s3://some-s3-bucket-or-key C:/some-local-directory # use aws cli to sync folder from remote s3 bucket`
2. process photos
3. `aws s3 sync C:/resized-photos-directory s3://some-s3-bucket-or-key # use aws cli to sync folder from new photos directory`