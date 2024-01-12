from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_lambda_python_alpha as lambda_python,
    aws_iam as iam
)
import aws_cdk as cdk
from constructs import Construct

class AwsPythonLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Creating a common lambda role for all the lambdas
        lambda_role = self.create_basic_lambda_role()
        
        # Creating a demo lambda
        demo_lambda = self.create_lambda(
            lambda_name = "name_of_lambda",
            description = "Description of lambda",
            lambda_role = lambda_role,
            environmentvar={"ANY":"ANY"}
        )

        
    
    def create_lambda(self, lambda_name: str, description: str or None, lambda_role: iam.Role, environmentvar: dict or None) -> lambda_.Function or None:
        
        __doc__="""
            A method to create a lambda function. Provide {lambda_name} and {lambda_role} compulsory.
            
            Args:
                lambda_name (str): Name of the lambda (Compulsory)
                description (str): Description for the lambda.
                layers (list[lambda_.LayerVersion]): Array of layers we need to attach to the lambda.
                lambda_role (iam.Role): The Role for the lambda execution.
                environmentvar (dict): A dict containing all hte necessary environment vars for the lambda.
            Returns:
                lambda_.Funciton: Returns a instance of a lambda function
        """
        try:
            if self.string_validate(lambda_name):
                return None
            
            return lambda_python.PythonFunction(
                self,
                id= lambda_name,
                entry=f"src/{lambda_name}",
                description= description,
                function_name= f"{lambda_name}",
                index="index.py",
                handler= "handler",
                role=lambda_role,
                memory_size=128,
                architecture=lambda_.Architecture.ARM_64,
                timeout=cdk.Duration.seconds(240),
                runtime=lambda_.Runtime.PYTHON_3_10,
                retry_attempts= 1,
                environment=environmentvar,
            )
        except Exception as e:
            print(f"Error in creating lambda {e}")
            return None
        
    def string_validate(self, string: str) -> bool or None:
        
        __doc__ = """
            This function validates a string.

            Args:
                string (str): The string to be validated.

            Returns:
                bool: True if the string is None or empty, False otherwise.
        """
        try:
            if string is None or string == "":
                return True
            return False
        except Exception as e:
            return None
        
    def create_basic_lambda_role(self) -> iam.Role or None:
        
        __doc__="""
            A method to create a Lambda role.
                
            Returns:
                iam.Role : Returns a basic lambda role
                OR
                None
        """
        try:
            return iam.Role(
                self,
                f"lambdaExecutionRole",
                role_name=f"lambdaExecutionRoleStockScreener",
                assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
                managed_policies=[
                    iam.ManagedPolicy.from_aws_managed_policy_name(
                        "service-role/AWSLambdaBasicExecutionRole")
                ],
            )
        except Exception as e:
            print(e)
            return None