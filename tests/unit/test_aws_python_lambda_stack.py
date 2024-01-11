import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_python_lambda.aws_python_lambda_stack import AwsPythonLambdaStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_python_lambda/aws_python_lambda_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsPythonLambdaStack(app, "aws-python-lambda")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
