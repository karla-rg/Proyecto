from antlr.marzoListener import marzoListener
from antlr.marzoParser import marzoParser

import asm

class DataGenerator(marzoListener):
    def __init__(self):
        self.result = ''
        self.constants = 0

    def enterProgram(self, ctx: marzoParser.ProgramContext):
        self.result += asm.tpl_start_data

    def enterDeclaracion(self, ctx: marzoParser.DeclaracionContext):
        # No more variables in data segment in this version!
        # self.result += asm.tpl_var_decl.substitute(
        #     varname = ctx.getChild(1).getText()
        # )
        # ctx.code = ''
        ctx.code = ''

    def enterPrimaria_string(self, ctx: marzoParser.Primaria_stringContext):
        self.constants = self.constants + 1
        ctx.label = "const{}".format(self.constants)
        self.result += asm.tpl_string_const_decl.substitute(
            name = ctx.label, content = ctx.getText()
        )
