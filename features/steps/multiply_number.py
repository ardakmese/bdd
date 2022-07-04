from behave import given, when, then
from calculator import multiply

@given(u'Calculator app is run for multiplying')
def step_impl(context):
    print(u'Step: Given Calculator app is run')

@when(u'I multiply "{a}" and "{b}" using calculator')
def step_impl(context, a, b):
    print(u'Step: When I multiply "{}" and "{}" using calculator'. format(a, b))
    context.result = multiply(a, b)
    print(u'Stored result "{}" in context'. format(context.result))

@then(u'I get from multiplying "{out}"')
def step_impl(context, out):
    if (context.result == int(out)):
        print(u'Step: Then I get right result "{}", "{}"'.format(context.result, out))
        pass
    else :
        raise Exception("Invalid multiply is returned.")
