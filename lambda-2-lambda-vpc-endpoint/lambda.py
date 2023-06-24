# Creat VPC Endpoint (Interface) for Lambda
# Select relevant Subnets and SGs for the Endpoint
# Just ensure the Endpoint is reachable from relevant Lambdas inside the Subnet
# During Test All Traffic was allowed for Subnet CIDR in the SG used
# The same SG was attached to both Lambda and Interface endpoint
# Private DNS Resolver (Outbound) has caused issues in another tests
# However, in this test there was no Private DNS Resolver/Forwarder
# The VPC Endpoint will publish a few DNS names which are to be used in the code when invoking the other lambda
# The following code invoke lambda l2 using the VPC endpoint DNS in endpoint_url
# boto3 is part of default lambda so extra module need not be loaded

import json
import boto3

c = boto3.client('lambda', endpoint_url='https://vpce-yyyyyyyyyyyyyyyyy-xxxxxx.lambda.us-east-1.vpce.amazonaws.com')

def lambda_handler(event, context):
    # TODO implement
    print("Triggered !!!")

    r = c.invoke(
        FunctionName = "arn:aws:lambda:us-east-1:1234567890:function:l2"
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

