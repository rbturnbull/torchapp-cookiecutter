from pathlib import Path

from torch import nn

import fastapp as fa

from rich.console import Console
console = Console()

class {{ cookiecutter.app_name }}(fa.FastApp):
    def model(
        self,
    ) -> nn.Module:
        raise NotImplemented("Model function not implemented yet.") 
        return nn.Sequential(
        )

    def dataloaders(
        inputs:Path = fa.Param(help="The input file."), 
        batch_size:int = fa.Param(default=32, help="The batch size."),
    ):
        raise NotImplemented("Dataloaders function not implemented yet.") 