from . rewriter import *

class IfTrueTransformer(NodeTransformer):
    def visit_If(self, node):
        NodeTransformer.generic_visit(self, node)
        statements = node
        if isinstance(node.test, Constant):
            if node.test.value == True:
                # el body puede ser una lista de statement
                statements = node.body
        return statements


class IfTrueRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(IfTrueTransformer().visit(ast))
        return new_tree

class PlusPlusTransformer(NodeTransformer):

    def visit_Assign(self, node):
        NodeTransformer.generic_visit(self, node)
        statements = node
        if isinstance(statements.value, BinOp): #hay una operacion en el assign
            operation = statements.value
            target = statements.targets[0].id
            if isinstance(operation.op, Add):
                if isinstance(operation.left, Name) and isinstance(operation.right, Name):
                    if target == operation.left.id:
                        statements = AugAssign(target=operation.left, op=Add(), value=operation.right)
                    elif target == operation.right.id:
                        statements = AugAssign(target=operation.right, op=Add, value=operation.left)
                elif isinstance(operation.left, Name):
                    if target == operation.left.id:
                        statements = AugAssign(target=operation.left, op=Add(), value=operation.right)
                elif isinstance(operation.right, Name):
                    if target == operation.right.id:
                        statements = AugAssign(target=operation.right, op=Add(), value=operation.left)

        return statements
    

class PlusPlusRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(PlusPlusTransformer().visit(ast))
        return new_tree

class IfWithoutElseTransformer(NodeTransformer):
    def visit_If(self, node):
        NodeTransformer.generic_visit(self, node)
        statements = node
        if len(node.orelse):
            if isinstance(node.orelse[0], Pass):
                    statements.orelse = []
        return statements


class IfWithoutElseRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(IfWithoutElseTransformer().visit(ast))
        return new_tree 