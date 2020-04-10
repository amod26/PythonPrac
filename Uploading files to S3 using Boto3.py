#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3


# In[ ]:


s3 = boto3.client('s3') # connecting to s3
s3.upload_file('filename','bucketname','savefilenameas')

