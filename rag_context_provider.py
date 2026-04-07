# RAG Context Provider Implementation

class RagContextProvider:
    def __init__(self, context):
        self.context = context

    def get_context(self):
        return self.context

    def set_context(self, new_context):
        self.context = new_context

# Example usage:
# context_provider = RagContextProvider("initial context")
# print(context_provider.get_context())  # Output: initial context
# context_provider.set_context("updated context")
# print(context_provider.get_context())  # Output: updated context
