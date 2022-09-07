from . rule import *


class DummyVarVisitor(WarningNodeVisitor):
    def visit_Assign(self, node: Assign):
        if isinstance(node.targets[0], Name):
            if len(node.targets[0].id) == 1:
                self.addWarning('VariableWarning', node.lineno, 'this variable name is to short!')


class DummyVarRule(Rule):
    def analyze(self, ast):
        visitor = DummyVarVisitor()
        visitor.visit(ast)
        return visitor.warningsList()
