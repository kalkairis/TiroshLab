class ExpressionMetaDataBase:
    def __init__(self, expression_matrix=None, cells_matrix=None, composing_items=[]):
        self.expression_matrix = expression_matrix
        self.cells_matrix = cells_matrix
        self.composing_items = composing_items
