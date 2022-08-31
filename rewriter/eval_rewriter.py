from . rewriter import *

class LiteralEvalRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(LiteralEvalTransformer().visit(ast))
        return new_tree

class LiteralEvalTransformer(NodeTransformer):
    def visit_Call(self, node):
        transformedNode = NodeTransformer.generic_visit(self, node)
        if node.func.id == 'eval':
            return Call(func=Name(id='literal_eval', ctx=Load()),
                        args=transformedNode.args,
                        keywords=transformedNode.keywords)
        else:
            return transformedNode