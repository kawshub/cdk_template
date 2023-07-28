#!/usr/bin/env python3
import aws_cdk as cdk
import yaml

from stacks.template_stack import TemplateStack

with open('configs/config.yaml', 'r') as yml:
    config = yaml.safe_load(yml)

app = cdk.App()

template_stack = TemplateStack(
    app,
    "TemplateStack",
    config=config,
    env=cdk.Environment(account=config['account']['account_id'], region=config['account']['region']),
    )

app.synth()
