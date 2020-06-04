import transform as jt

# 1. Create a subclass of functions.Functions.
#    The function.Functions base class has logic
#    that introspects all of its methods and automatically
#    registers your custom functions in its function table.
class CustomFunctions(functions.Functions):

    # 2 and 3.  Create a function that starts with _func_
    # and decorate it with @signature which indicates its
    # expected types.
    # In this example, we're creating a jmespath function
    # called "unique_letters" that accepts a single argument
    # with an expected type "string".
    @functions.signature({'types': ['string']})
    def _func_unique_letters(self, s):
        # Given a string s, return a sorted
        # string of unique letters: 'ccbbadd' ->  'abcd'
        return ''.join(sorted(set(s)))

    # Here's another example.  This is creating
    # a jmespath function called "my_add" that expects
    # two arguments, both of which should be of type number.
    @functions.signature({'types': ['number']}, {'types': ['number']})
    def _func_my_add(self, x, y):
        return x + y

    def _to_number(self, s):
        return float(s)

# 4. Provide an instance of your subclass in a Options object.
options = jt.Options(custom_functions=CustomFunctions())

output_dict = jt.transform('testcase/input.json', 'testcase/template.json')

print(output_dict)
