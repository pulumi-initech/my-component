from typing import Optional, TypedDict
import pulumi_random as random
import pulumi


class MyComponentArgs(TypedDict):
    who: Optional[pulumi.Output[str]]

class MyComponent(pulumi.ComponentResource):
    greeting: pulumi.Output[str]

    def __init__(self, name: str, args: MyComponentArgs, opts: Optional[pulumi.ResourceOptions] = None):
        super().__init__("my-provider:index:MyComponent", name, {}, opts)

        who = args.get("who") or "Pulumipus"
        greeting_word= random.RandomShuffle(f"{name}-greeting", inputs=["Hello", "Konnichiwa", "Hola", "Bonjour"], result_count=1, opts=pulumi.ResourceOptions(parent=self))

        self.greeting = pulumi.Output.concat(greeting_word.results[0], ", ", who, "!")

        self.register_outputs({
            "greeting": self.greeting,
        })