from aws_cdk import (
    core,
    aws_stepfunctions as stepfunctions,
    aws_stepfunctions_tasks as tasks,
    aws_lambda as lambda_func
)


class CdkStateMachineStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        logging_lambda = lambda_func.Function(
            scope=self,
            id="logging_lambda",
            function_name="logging_lambda",
            handler="logging-lambda.main",
            runtime=lambda_func.Runtime.PYTHON_3_7,
            code=lambda_func.Code.from_asset("./code")
        )

        second_lambda = lambda_func.Function(
            scope=self,
            id="second_lambda",
            function_name="second_lambda",
            handler="second-lambda.main",
            runtime=lambda_func.Runtime.PYTHON_3_7,
            code=lambda_func.Code.from_asset("./code")
        )

        logging_lambda_task = tasks.InvokeFunction(logging_lambda)
        logging_step = stepfunctions.Task(
            scope=self,
            id="invoke_logging_function",
            task=logging_lambda_task)

        second_lambda_task = tasks.InvokeFunction(second_lambda)
        second_step = stepfunctions.Task(
            scope=self,
            id="invoke_second_function",
            task=second_lambda_task)

        definition = logging_step.next(second_step)

        stepfunctions.StateMachine(
            scope=self,
            id="state_machine",
            state_machine_name="state_machine",
            definition=definition,
        )

