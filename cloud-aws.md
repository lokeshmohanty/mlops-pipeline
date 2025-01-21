# Setup a cloud server using AWS 

## Introduction

For continuous deployment, we need to automate the process of deploying our application on
a server. It is easy a very difficult task to manage your own server. That's why many
companies provide cloud services which provide you with a server without having to worry
about its availability, maintenance and security.


## Elastic Cloud Compute (EC2)

It is the default service provided by AWS for getting a server on the cloud.

Steps:

-   Go to EC2 and launch an instance.
-   Give a name to your instance and select the OS that you want to install on it.
-   Create a key-pair which you can use to login to your server using ssh.
-   Create a security group for managing the security (eg: which ip can access your server)
-   Select the configuration for the server (eg: storage).
-   Create the instance.

## Create a simple API

-   Log into your server through ssh (or browser). You can follow the steps under `Connect` tab under your `Instance`.
-   Install nodejs on the server.

```sh
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
    nvm install --lts
    nvm use --lts
```

-   Create a file named `index.js` for starting our api.

```nodejs
    const express = require('express');
    const app = express();
    
    app.listen(8000, () => console.log('Simple API running on port 8000'))
    
    app.get ('/', (req, res) => res.json('The api is up and running!'))
```

-   Install the dependencies and start the server

```sh
    npm init
    npm install express
    node index.js
```

## Other options within AWS

-   AWS lightsail
-   AWS lambda
-   ...

## Other Providers

-   [Google Cloud](https://cloud.google.com/free)
-   [Microsoft Azure](https://azure.microsoft.com/en-us/pricing/free-services)
-   [IBM Cloud](https://www.ibm.com/in-en/cloud)
-   [Digital Ocean](https://www.digitalocean.com/)
-   and many more ...

## Further Reading

-   [AWS cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2.html)
-   [AWS official tutorials](https://aws.amazon.com/getting-started/hands-on/?getting-started-all.sort-by=item.additionalFields.content-latest-publish-date&getting-started-all.sort-order=desc&awsf.getting-started-category=*all&awsf.getting-started-content-type=*all&awsm.page-getting-started-all=1)
