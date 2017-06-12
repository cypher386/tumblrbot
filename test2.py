import pytumblr

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  'nNw1tynHGRTvbfjNtFypkmBkrIOKienmR9zCcGoxAJzWJndrNc',
  'z7CCAjPJ4CLCLHTNPo3stu4sjXJ0DfQCVAU9rHKPv4rGtdV5dO',
  'cvkYlSV6jwQSaoM1PWaCzBMgMeOjhDBy1iYVucXhLaY94pKRA7',
  'icS1b188l7j1SjhwBIsagRRmPJreD5wxrelFo6H5RfDoMCOSEi'
)

# Make the request
print client.submission('jessicastimeline.tumblr.com')[0]['id']
