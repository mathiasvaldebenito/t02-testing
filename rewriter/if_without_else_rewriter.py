from .rewriter import *

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