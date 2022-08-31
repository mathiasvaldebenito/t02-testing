from . rule import *

class DataClassVisitor(NodeVisitor):
    def __init__(self):
        self.fun = 0

    def visit_FunctionDef(self, node: FunctionDef):
        if node.name != '__init__':
            self.fun += 1
            if len(node.body) == 1 and (isinstance(node.body[0], Assign) or isinstance(node.body[0], Return)):
                self.fun -= 1
        
    def total(self):
        return self.fun

class ClassVisitor(WarningNodeVisitor):

    def visit_ClassDef(self, node: ClassDef):
        visitor = DataClassVisitor()
        visitor.visit(node)
        if visitor.total() == 0:
            self.addWarning('DataClassWarning', node.lineno, 'method ' + node.name + ' is a Data Class') #atributos y accesores.
        NodeVisitor.generic_visit(self, node)          

class ClassRule(Rule):
    def analyze(self, ast):
        visitor = ClassVisitor()
        visitor.visit(ast)
        return visitor.warningsList()