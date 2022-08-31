from . rule import *

class VarVisitor(NodeVisitor):
    def __init__(self,vars):
        super().__init__()
        self.vars = vars

    def visit_Assign(self, node: Assign):
        if isinstance(node.targets[0], Name):
            self.vars[node.targets[0].id] = [False,node]
        if isinstance(node.value, Name):
            self.vars[node.value.id] = [True,node]
    
    def visit_Return(self, node: Return):
        if isinstance(node.value, Name):
            self.vars[node.value.id] = [True,node]
        
    def total(self):
        return self.vars


class FunctionVisitor(WarningNodeVisitor):
    def __init__(self):
        super().__init__()
        self.vars = {}

    def visit_FunctionDef(self, node: FunctionDef):
        #print(node.args.args[0].arg) 
        if node.args.args[0].arg != "self":
            self.vars[node.args.args[0].arg] = [False,node]
        visitor = VarVisitor(self.vars)
        visitor.visit(node)
        self.vars = visitor.total()
        

    def final(self):
        for var in self.vars:
            if not self.vars[var][0]:
                self.addWarning('VariableWarning', self.vars[var][1].lineno, 'this variable is not used!')


class VarNotUsed(Rule):
    def analyze(self, ast):
        visitor = FunctionVisitor()
        visitor.visit(ast)
        visitor.final()
        return visitor.warningsList()

#fun(a) arg
#y = 0 assign
#return 
