#!/usr/bin/env python3

from aws_cdk import core

from cdk_state_machine.cdk_state_machine_stack import CdkStateMachineStack


app = core.App()
CdkStateMachineStack(app, "cdk-state-machine")

app.synth()
