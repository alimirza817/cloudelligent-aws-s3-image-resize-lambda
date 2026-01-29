# Project: AWS S3 Image Resize & EOD Cleanup Lambda
## Overview

This project demonstrates an event-driven, serverless architecture using AWS Lambda and S3.

The solution consists of:

1. Image resize Lambda – Automatically resizes images uploaded to an S3 bucket and stores thumbnails in a separate bucket.

2. EOD cleanup Lambda – Empties the source bucket at the end of the day (cron-based via EventBridge) while keeping the thumbnails safe.

This task was implemented as part of my Cloudelligent internship to showcase serverless design, automation, and AWS best practices.

## Architecture Diagram
<img width="644" height="301" alt="image" src="https://github.com/user-attachments/assets/c1ff4a4f-cb31-4f12-a6e6-626c3cb16b53" />

## Features

* Event-driven: Resizing triggers automatically when new images are uploaded.

* Automated cleanup: Source bucket is cleared at EOD using a cron schedule.

* Least privilege IAM: Lambda functions only have permissions needed for S3 operations and logging.

* Safe testing: Cron was tested manually and deleted immediately after verification to prevent accidental data loss.

* Scalable: Handles multiple image formats (JPG, PNG) and can be extended to other S3 buckets.
## Project Structure
cloudelligent-aws-s3-image-resize-lambda/

├── lambda_resize_image/

│   └── lambda_function.py       # Resizes images and uploads thumbnails

├── lambda_cleanup/

│   └── lambda_function.py       # Deletes objects from source bucket

├── requirements.txt             # Dependencies (Pillow)

├── README.md                    # This file

## How it Works
### 1. Image Resize Lambda

* Trigger: S3 ObjectCreated event on image-upload-buckett1

* Process:

   1. Receives event with the uploaded image key

   2. Downloads the image from S3

   3. Resizes it to thumbnail size (e.g., 300x300)

   4. Uploads the thumbnail to image-resized-bucket-thumbnail

### 2. EOD Cleanup Lambda

* Trigger: EventBridge cron rule (e.g., every day at 23:59 UTC)

* Process:

  1. Lists all objects in the source bucket (image-upload-buckett1)

  2. Deletes them one by one

  3. Leaves thumbnail bucket untouched

* Safety: Cron rule was removed after testing to prevent accidental deletes.

## Screenshots
### 1. Image_Upload_Bucket1
   
   <img width="1363" height="495" alt="image" src="https://github.com/user-attachments/assets/01d8bb63-e100-443c-a861-1c0d8950c271" />
   
### 2. AWSImageResizeLamdaFunction
   <img width="1364" height="580" alt="image" src="https://github.com/user-attachments/assets/168b9dae-4579-43e7-840a-65fe2bcbb8a6" />
   
### 3. Image_Resized_Bucket_Thumbnail 
   <img width="1359" height="565" alt="image" src="https://github.com/user-attachments/assets/7352f8bc-3397-41d4-8431-2d9a62970a5d" />  
   
### 4. AWSCleanupObjectFunction_EventBridge_CronJob
   <img width="1359" height="626" alt="image" src="https://github.com/user-attachments/assets/a9514e6f-83b7-4ba2-885e-824ecdd196a0" />
   
### 5. CronJob_Scheduled_Test_Next_2Mints
   <img width="1363" height="644" alt="image" src="https://github.com/user-attachments/assets/eeea0bfc-af15-4037-a16a-dffd3c0bfb07" />
   
### 6. Object_Deleted
   <img width="1365" height="635" alt="image" src="https://github.com/user-attachments/assets/67a25f9f-ac21-49ce-9572-390fdb30c6a9" />
   
## Deployment Instructions

#### 1. Clone the repo
   * git clone https://github.com/alimirza817/cloudelligent-aws-s3-image-resize-lambda.git
   * cd cloudelligent-aws-s3-image-resize-lambda
#### 2. Install dependencies (for local testing)
   * pip install -r requirements.txt
#### 3. Upload Lambda functions via AWS Console or AWS CLI.
#### 4. Create triggers:
   * Resize Lambda: S3 → ObjectCreated
   * Cleanup Lambda: EventBridge → cron (optional, test carefully)
#### 5. IAM Roles:
   * Resize Lambda: S3 read/write to source and thumbnail buckets + CloudWatch logs
   * Cleanup Lambda: S3 delete only on source bucket + CloudWatch logs
#### 6. Test:
   * Upload image → thumbnail should appear
   * Cleanup Lambda can be run manually for safe testing
## Technologies Used
* AWS Lambda (Python 3.11)
* Amazon S3 (Source & Thumbnail Buckets)
* EventBridge (CloudWatch Events)
* Python Pillow for image processing
* CloudWatch Logs for monitoring
## Best Practices Highlighted
* Event-driven architecture
* Serverless design with minimal dependencies
* Least-privilege IAM
* Manual verification and safe deletion of cron jobs
* Clean GitHub repo with proper structure
## Future Enhancements
* Support multiple image sizes (small, medium, large)
* Add image format conversion (e.g., PNG → JPG)
* Integrate SNS notification for completed thumbnail processing
* Automate deployment using AWS SAM or CloudFormation
